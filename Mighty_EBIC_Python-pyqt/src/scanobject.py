import numpy
import pickle
import EbicDataManager
import sys
import os
import math
import scipy
import scipy.ndimage
from time import strftime
import Mfigure


class Scan():


    def __init__(self, bounds = ((-0x7fff,-0x7fff),( 0x7fff, 0x7fff)), 
                cal = None, SEMstate = None, controllerState = None, scanstate = None, name = None, Notes = None):
        self.created = strftime("%Y-%m-%d_%H-%M-%S") 
        self.name = name
        self.cal = cal  # store calibration info for microscope with the scan
        self.bounds = bounds  #imaging bounds of the scan (actual values sent to DACs)
        self.rotation = []
        # these are the location for storeing child profiles,slices, and figures
        self.figures = None        
        self.profiles = []
        self.slices = []
        self.notes = Notes
        # for displaying figures
        self.viewmin = []   # lower limit of colorscale
        self.viewmax = []   # upper limits of colorscale
        self.cmap = ['','','','','',''] # cmap for each channels is stored here

        # these will maintian the state of the controller
        self.SEMstate = self.load_SEM_state(SEMstate)
        self.controllerState = self.load_controller_state(controllerState)
        self.scanstate = self.load_scan_state(scanstate)
 

    def load_scan_state(self, scanState = None):
        if scanState != None :
            #extra copy of scanState is left unmodified to refer to latter.
            self.scanState = scanState
            self.stepH = scanState.stepH 
            self.stepV = scanState.stepV
            self.pointsH = scanState.pointsH
            self.pointsV = scanState.pointsV
            self.offsets = scanState.offsets
            self.channelMask = scanState.channelMask 
            self.scanMag = scanState.mag 
            self.units = scanState.units
            self.labels = scanState.labels
            self.gain = scanState.gain
            self.delay = scanState.delay
            self.samples = scanState.samplesPerPoint
            self.channels = self.set_channel_scale()
            self.channelCount = EbicDataManager.DataManagerUtils.maskToChannelCount(self.channelMask)
            self.set_position_scale()
            self.rawDataArray = Scan.makeNDataArray(self.pointsH, self.pointsV, self.samples, self.channelCount)
            self.DataArray = None
            self.DisplayArray = Scan.makeDisplayArray(self.pointsH, self.pointsV, self.channelCount)    # created by sdm stored here

        return scanState

    @staticmethod
    def setup_scan_state(stepH = None, stepV = None, pointsH = None, pointsV = None, spread = None, offsets = None
                            , channelMask = None, units = None, labels = None, gain = None, delay = None, samples = None
                            , mag = None, cal = None, bounds = None):
        """
        grabs the data given from the qt_designer and puts it into a ScanConfig object. 
        It handles any conversion for the data to be stored in the appropriate form
        """
        delayFine, delayCoarse = Scan.setDelay(delay)
        hMin, hMax, vMin, vMax = Scan.scan_bounds(bounds, offsets, spread)
        units, labels, gain = Scan.compact_channel_info(channelMask,units = units,labels = labels, gain = gain)

        scanState = EbicDataManager.ScanConfig(stepH, stepV, hMin, vMin, pointsH, pointsV, samples, channelMask, delayFine, delayCoarse
                                                , mag, units, gain, labels, delay, offsets) 

        return scanState  


    def load_controller_state(self, controllerState = None):       
        if controllerState != None :
            self.Aux1 = controllerState['Aux1']
            self.Aux2 = controllerState['Aux2']
        return controllerState
            

    def load_SEM_state(self, SEMstate = None):
        if SEMstate != None:
            self.beam = SEMstate['beam']
            self.accel = SEMstate['accel'] 
        return SEMstate 


    def scale_channels(self):
        """
        scale the data with the appropriate units
        """
        self.DataArray = numpy.multiply(self.rawDataArray,self.channels)
	print "channels" , self.channels
        self.DisplayArray = numpy.average(self.DataArray, axis = 2)


    def set_channel_scale(self):
        """
        sets the matrix that will multiple the dataarray to scale the values to actual quantitaive values 
        """
        self.ADC_voltage_step = 20.0/(0x40000)  #changed for 18bit ADC
        self.channels = self.ADC_voltage_step/self.gain
        return self.channels


    def set_position_scale(self):
        """
        sets the position scale for x and y  
        if calibration is not given it sets the extent equal to the shape
        and the scanScales to 1.0   
        """
        if self.cal != None:

            self.vMagScale = self.cal['vMagScale']
            self.hMagScale = self.cal['hMagScale']

            self.scanScaleH = self.scale(self.hMagScale, self.scanMag)
            self.scanScaleV = self.scale(self.vMagScale, self.scanMag)

            self.deltaH = (self.stepH*self.pointsH)*self.scanScaleH  
            self.deltaV = (self.stepV*self.pointsV)*self.scanScaleV
            self.left = self.scanState.displayOffsets[0]*self.scanScaleH
            self.bottom = self.scanState.displayOffsets[1]*self.scanScaleV
            
        else :
            self.deltaH = self.pointsH
            self.deltaV = self.pointsV
            self.scanScaleH = 1.0
            self.scanScaleV = 1.0
            self.left = 0
            self.bottom = 0

        self.extent =(0, self.deltaH, 0, self.deltaV)
        self.displayExtent = (self.left, self.deltaH + self.left, self.bottom, self.bottom + self.deltaV)         
       

    @staticmethod
    def scale(magscale, scanMag):
        """
        returns the scaler to convert units from DAC values to position
        """
        scale = magscale/scanMag   # units = (distance in microns)/(single DAC step 305uV)
        return scale

    @staticmethod
    def step_from_distance(stepDistance = 1, scale = 1):
        """
        takes the defined step size in distance and returns the step size that corresponds to a DAC value
        """
        step = int(stepDistance/scale)
        if step == 0:        
            step = 1 # return minimum DAC step value
        return step


    @staticmethod 
    def scale_extent(extent, scale):
        extent = scanObjectUtils.scale_size(extent, scale)
        return extent
        

    @staticmethod
    def scan_points(extent = 1, step = 1):
        """
        stepsize is given in same units as extent (i.e. distance)
        scales the stepsize to integers and scales the extent
        returns number of points in the scan, step, and spread in that direction
        """
        points = int(extent/step)
        spread = points*step  # actual maximum value sent to DACs 

        return points, spread



 
    @staticmethod
    def scan_bounds(limits, offset, spread):
        """
        computes the startpoint for x and y given default limits of scan area and defined offsets
        """

        vMin = int(limits[1] + offset[1] ) 
        vMax = int(limits[1] + offset[1] + spread[1])  
        hMin = int(limits[0] + offset[0])
        hMax = int(limits[0] + offset[0] + spread[0])

        if vMin < -0x7fff:
            vMin = -0x7fff
        if vMax > 0x7fff:
            vMax = 0x7fff
        if hMin < -0x7fff:
            vMin = -0x7fff
        if hMax > 0x7fff:
            hMin = 0x7fff

        return hMin, hMax, vMin, vMax

    @staticmethod
    def makeNDataArray(lenX, lenY, numsamples, channel):
        storedArray = numpy.zeros([lenY, lenX, numsamples, channel], numpy.int32)
        return storedArray

    @staticmethod
    def makeDisplayArray(lenX, lenY, channel):
        displayArray = numpy.zeros([lenY, lenX, channel], numpy.float)
        return displayArray 


    @staticmethod
    def setDelay(delayseconds):
        """
        sets delay using two shorts (fine and coarse) works in micro controller clock cylces.  
        delay is between new position and sample times
        """
        delayStep= 10e-9 #10ns# #1/50e6 # delay in clock cycles default
        delay= numpy.uint32(delayseconds/delayStep)
        delayFine = numpy.uint16(delay & 0xFFFF) # lsb short
        delayCoarse = numpy.uint16(delay >> 16) # Msb  short   
        print "delayFine", delayFine, "delayCoarse", delayCoarse, "delay", delay 
	return delay, delayCoarse   #TODO: fix this ugly hack, sets delay to delay fine, TM     


    @staticmethod
    def compact_channel_info(channelMask, units = None, gain = None, labels = None ):
        """
        takes array of channels and units and compact them into an array with no empty positions
        ex: channel mask 0b000111 will produce an array len 3
            channel mask 0b010001 wil produce an array len 2
        this is so the gain channel will be in the proper length to perfrom matrix multiplication to scale values of the array
        """
        count = 0
        c_units = []
        c_labels = []
        c_gain = []
        for n in range(6):
            if((channelMask & (1 << n)) != False):            
                c_units.append(str(units[n]))
                c_labels.append(str(labels[n]))
                c_gain.append(float(str(gain[n])))     
        c_gain = numpy.array(c_gain, dtype = 'float')        
        return c_units, c_labels, c_gain


    
#    def add_profile(self, startpoint, endpoint):
#        self.profiles.append(Profile(startpoint,endpoint,self)) 
         
    @staticmethod
    def add_profile(startpoint, endpoint, Scan):
        Scan.profiles.append(Profile(startpoint = startpoint,endpoint = endpoint ,Scan = Scan)) 



class Profile():

    def __init__(self, name = None, startpoint = None,  endpoint = None, Scan = None):
        self.name = str(name)
        self.startpoint = startpoint
        self.endpoint = endpoint
        self.extract_profile(Scan)
        self.gain = Scan.gain
        self.units = Scan.units
        self.angle = None      
        
    def extract_profile(self, Scan):
        if Scan == None:
            print ('data is None')
            return
        else :
            rotate = Rotation(self.startpoint, self.endpoint, Scan)
            self.angle = rotate.angle
            self.positionScaleH = rotate.scaleH
            self.positionScaleV = rotate.scaleV
            print "rotate.p0, rotate.p1" ,rotate.p0, rotate.p1
            print "rotate Date", rotate.rData.shape
            print "angle", self.angle
            if rotate.p0[0] < rotate.p1[0]:
                start = rotate.p0[0]
                end = rotate.p1[0] 
            else :
                start = rotate.p1[0]
                end = rotate.p0[0]                 
            self.profileData = rotate.rData[rotate.p0[1],start:end,:,:]
            print"profile data shape", self.profileData.shape
            self.profileDataAvg = numpy.average(self.profileData, axis = 1) #averages sample for each channel
            self.Xposition = (numpy.arange(self.profileDataAvg.shape[0]) + start )*self.positionScaleH 



class Transport():

    def __init__(self, samples = 50, channelMask = 1, delay = 0.5, Start = 0, End = 2
                    , step = 0.2 , points = 50, gain = 1, gate = None, units = None, labels = None, name = None ):
        self.name = name
        self.samples = samples 
        self.created = strftime("%Y-%m-%d_%H-%M-%S")
        self.delay = delay
        self.vstep = 20.0/0xffff
        self.gain = gain
        self.gate = gate
        self.start = Start/self.vstep        
        self.channelMask = channelMask
        self.points = points
        self.pointsUp = int(abs(End/step)) + 1
        self.step = int(step/self.vstep)
        self.end = self.step*(self.pointsUp -1) 
        self.pointsDown = self.pointsUp - 1
        self.dataIRaw = []
        self.dataI = []
        self.sentVoltage = [] 
        self.dataIstd = []
        self.soakTime = []


class Rotation():
    def __init__(self, startpoint = None, endpoint = None, scan = None):
        self.scaleH = scan.stepH*scan.scanScaleH 
        self.scaleV = scan.stepV*scan.scanScaleV
        startpoint = [startpoint[0]/self.scaleV, startpoint[1]/self.scaleH]
        endpoint = [endpoint[0]/self.scaleV, endpoint[1]/self.scaleH]
        print "startpoint", startpoint, "endpoint", endpoint

        #self.p0, p1 are unscaled points
        self.rData, self.angle, self.p0, self.p1 = scanObjectUtils.rotate_image_points(startpoint, endpoint, scan.DataArray)
        self.rDisplayData = numpy.average(self.rData, 2)
        print "r0", self.p0, "r1", self.p1
        self.r0 = [self.p0[0]*self.scaleH,self.p0[1]*self.scaleV]
        self.r1 = [self.p1[0]*self.scaleH,self.p1[1]*self.scaleV]
        self.p0 = self.p0.round()
        self.p1 = self.p1.round()


        left = self.rData.shape[1]*self.scaleH 
        top = self.rData.shape[0]*self.scaleV
        self.extent= (0, left, 0, top)
        print "angle ",  self.angle
     


#put Slice types here:
#slices can be any manipulation of original data that show the parent, subset of original data,
#arugments used to produce the slice etc. they can stand on their own or be stored with the parent.
class reCenterSlice():
    """
    A reCentered slice takes a subset of data from parent and uses it to recenter data along a central access
    using a sobel filter(finds gradient and picks center point this will typicaly
    use to Secondary electron as the input signal) along a determined axis and reshifts each line to fit.
    """
    def __init__(self, scan =None , kind = 'recentered', name = None):
        self.profiles = []
        self.offset = None
        self.scan = scan  #I assume this is just a pointer to the scan and not actually copying it
        self.name = name
        self.kind = kind
        self.extent = None
        self.figures = None
        self.DisplayArray = None
        self.sourceExtent= None
        self.point = 1
        


    def reCenter(self, RefCH = 0, margin = 11, sobelAxis = 1, Gaus_distance = 2):
        self.margin = margin
        self.RefCH = RefCH
        self.sobelAxis = sobelAxis
        self.Gaus_distance = Gaus_distance

        """
        takes the display array and the identified source of secondary channel
        performs gaussian filter to remove noise before finding the gradient to identify the center 

        """

        self.getBounds()
        self.sliceData = self.scan.DisplayArray[self.y : self.dy, self.x : self.dx, :]

        #uses sobel filter along axis of interest to find center of feature to reconstruct
        self.Gaus = scipy.ndimage.gaussian_filter(self.sliceData[:,:,self.RefCH],self.Gaus_distance)
        self.sx = scipy.ndimage.sobel(self.Gaus, axis = self.sobelAxis, mode = 'reflect')
        self.C = (self.sx.argmax(axis = self.sobelAxis) + self.sx.argmin(axis = self.sobelAxis))/2

        # determines what the likely radius of the feature is and defines an offset from the center to grab data from either side
        self.distance = (self.sx.argmin(axis = 1) - self.sx.argmax(axis =1))
        self.radius = int(self.distance.mean()/2)
        self.offset = self.radius + self.margin

        Y = numpy.arange(self.C.shape[0])
        Dx = 2*(self.offset)
        Dy = self.sx.shape[0]


        self.DisplayArray = numpy.zeros((Dy,Dx,self.sliceData.shape[-1]))
        self.GausDisplayArray = numpy.zeros((Dy,Dx,self.sliceData.shape[-1]))
        


#TODO decide is this functionality is helpful: shows the results of sobel filter and plots the center for reference
        #pylab.plot(C,Y)
        #pylab.imshow(sx, cmap ='gray')
        #pylab.show()



        #for each row grab data on either side of the center 
        for i in range(self.sx.shape[0]):
            In1 = self.C[i] - self.offset
            In2 = self.C[i] + self.offset
            #print str(In1) +' , ' + str(In2) 
            if In2 <= self.sliceData.shape[self.sobelAxis] and In1 >= 0:
                self.DisplayArray[i,0:(Dx),:] = self.sliceData[i,In1:In2,:]

        self.sliceExtent()
        self.set_GausDisplayArray(point = self.point)


    def set_GausDisplayArray(self, point = 1):
        for i in range(self.DisplayArray.shape[-1]):
            self.GausDisplayArray[:,:,i] = scipy.ndimage.gaussian_filter(self.DisplayArray[:,:,i], point)



    def sliceExtent(self):
        """
        Recalculates the extent of the slice based on the points extracted from scan
        future versions of scan data type should include the resolution in um or nanometers so it is easier to extract
        """
        print "stepH and step V"
        print self.scan.stepH, self.scan.stepV

        print "scanScale"
        print self.scan.scanScaleH, self.scan.scanScaleV
        
        self.deltaH = self.scan.stepH*self.scan.scanScaleH*self.DisplayArray.shape[1]
        self.deltaV = self.scan.stepV*self.scan.scanScaleV*self.DisplayArray.shape[0]

        self.extent =(0, self.deltaH, 0, self.deltaV)
        print self.extent


    def addSlice(self):
        self.scan.slices.append(self)

    
    def getBounds(self):
        """
        gets a defined slice from the data from the sourceExtent i.e."ax.viewLim.extents"

        """
        self.scaleH = self.scan.stepH*self.scan.scanScaleH 
        self.scaleV = self.scan.stepV*self.scan.scanScaleV

        #defines which points to grab from the original data
        self.x = int(round(self.sourceExtent[0]/self.scaleH))
        self.dx = int(round(self.sourceExtent[2]/self.scaleH))
        self.y = int(round(self.sourceExtent[1]/self.scaleV))
        self.dy = int(round(self.sourceExtent[3]/self.scaleV))

        print self.x, self.dx, self.y, self.dy





class scanObjectUtils:

    @staticmethod
    def getMaxMin(inputArray, axisIndex, center, threshold, channel):
        """
        takes either a min or  max value which ever is greater in magnitude
        and is within a certain threshold of the center

        returns the value and position of the selected values and
        the max value, position of max, minvalue and its position  
        """
        axisindex = axisIndex
        posMax = numpy.argmax(inputArray[:,:,channel],axis = axisindex)
        posMin = numpy.argmin(inputArray[:,:,channel],axis = axisindex)
        valMax = numpy.amax(inputArray[:,:,channel],axis = axisindex)
        valMin = numpy.amin(inputArray[:,:,channel],axis = axisindex)
        traceValue=[]
        tracePosition=[]

        for n in range(0,len(posMax)):
            if (abs(valMin[n]) >= abs(valMax[n])) and (abs(center - posMin[n]) < threshold):
                traceValue.append(valMin[n])
                tracePosition.append(posMin[n])
            elif (abs(valMax[n]) >= abs(valMin[n])) and (abs(center - posMax[n]) < threshold):  
                traceValue.append(valMax[n])
                tracePosition.append(posMax[n])
            else:
                traceValue.append(inputArray[center][n][0])
                tracePosition.append(center)

        return traceValue, tracePosition, valMax, posMax, valMin, posMin


   

    @staticmethod
    def scale_size(inPut = None, scale = None):
        """
        takes the scale and an input gives you a value as an int for DACs
        """
        if inPut.__class__ == numpy.ndarray:
            outPut = (inPut/scale).astype(int)
        else :  
            outPut = int(inPut/scale) #output is given as DAC values
        return outPut 



    @staticmethod
    def pickle_scanobject(scanobject, filename):
        """
        pickles an object with the filename given and writes it as abinary file
        """
        pickle.dump(scanobject,open(str(filename), 'wb'), protocol = 1)

    
    @staticmethod
    def load_scanobject(filename):
        """
        loads a pickled ojects from the given filename
        """
        Scan = pickle.load(open(str(filename), 'rb'))
        return Scan

    @staticmethod
    def rotateImage(startOffset, endOffset, data):
        x0 = startOffset[0]
        y0 = startOffset[1]
        x1 = endOffset[0]
        y1 = endOffset[1]
        dx= x1-x0     #TODO: fix this so it can rotate in all quadrants 
        dy= y1-y0
        angle = numpy.angle(numpy.complex(dx,dy), deg = True)
	print angle
        #angle = (math.atan(dy/dx) * 180 / math.pi)   #This isn't correct use arctan2 or numpy.angle
        rdata = scipy.ndimage.interpolation.rotate(data,angle) #rotate array
        
        return rdata, angle

    @staticmethod
    def swap_scan_axes(scan):
        scan.DataArray = scan.DataArray.swapaxes(0,1)
        scan.DisplayArray = scan.DisplayArray.swapaxes(0,1)
        scan.rawDataArray = scan.rawDataArray.swapaxes(0,1)
        scan.extent = (0,scan.extent[3], 0, scan.extent[1])
        return scan

    @staticmethod
    def flip_scan_lr(scan):
        scan.DataArray = numpy.fliplr(scan.DataArray)
        scan.DisplayArray = numpy.fliplr(scan.DisplayArray)
        scan.rawDataArray = numpy.fliplr(scan.rawDataArray)
        return scan

    @staticmethod
    def flip_scan_ud(scan):
        scan.DataArray = numpy.flipud(scan.DataArray)
        scan.DisplayArray = numpy.flipud(scan.DisplayArray)
        scan.rawDataArray = numpy.flipud(scan.rawDataArray)
        return scan




    @staticmethod
    def rotate_point(point, angle):
        angle = angle*math.pi/180
        c = numpy.cos(angle)
        s = numpy.sin(angle)
        x = point[0]
        y = point[1]
        xprime = x*c + y*s
        yprime = -x*s + y*c 
        
        return [xprime,yprime]

    
    @staticmethod
    def rotate_image_points(startOffset, endOffset, data):
        rdata, angle = scanObjectUtils.rotateImage(startOffset, endOffset, data)
        xoffset = (data.shape[1] -1)/2.0 
        yoffset = (data.shape[0]-1)/2.0
        print "xoffset",xoffset,"yoffset",yoffset
        p0 = [startOffset[0]- xoffset, startOffset[1]- yoffset]
        p1 = [endOffset[0]- xoffset, endOffset[1]- yoffset]
        print "p0", p0, "p1", p1
        rxOff = (rdata.shape[0]-1)/2.0 
        ryOff = (rdata.shape[1]-1)/2.0
        print "rxoff", rxOff, "ryOff", ryOff 
        rstart = scanObjectUtils.rotate_point(p0, angle)
        rend = scanObjectUtils.rotate_point(p1, angle)
        print "rstart", rstart, "rend", rend
        r0 = numpy.array([rstart[0]+ ryOff, rstart[1]+ rxOff])
        r1 = numpy.array([rend[0]+ ryOff, rend[1]+ rxOff])

        return rdata, angle, r0, r1


    @staticmethod
    def dwellTime(OS = 0, CH = 1, samples = 1, delay = 1):
        """
        Calculates the dwell time of each pixel based on Channels, samples, delay and oversampling.

        OS stands for Oversampling range 0,2,4,8,16,32, and 64 doubling each time.
        CH is the number of channels activated, range from 1 to 8.  
        samples is the number of samples that are measured at each pixel and averaged.
        The delay is inputed as an integer and increases in multiples of 10 ns 
        this is a variable delay that allows for the signal to reach a steady state before it is measured.

        Time constants are based on PRU code that drives for AD5764 DAC and AD7608 ADC
        All constants are in nanoseconds.Returns dwell time in us
        """
        #ADC Time constants
        WAIT = 4000 #default conversion rate
        OS_scalar = 4500 #Oversampling scalar per OS multiple 0,2,4,8,16,32,64 
        CH_scalar = 1365 #Scalar for each channel we need to clock out
        samples_scalar = 20 #

        #DAC time constants
        DAC_var = 10 #variable delay muliplipier in ns

        #ADC sampling Overhead
        sample_Overhead = 110 # 

        #DAC write Overhead
        LOADDAC_OV= 5345 # overhead 
        DACUP_OV = 200

        #Calculate how long it takes to do a ADC read with 
        #if OS is greater than 2 we need to use different scalar
        if OS >= 2:
                WAIT = OS_scalar*OS
        # for each conversion amount of time it takes clock out each channel
        CH_T = CH_scalar*CH

        #total ADC READ based on CH and OS
        ADCREAD = 120 + CH_T + WAIT

        #total number of conversions at a pixel    
        LOOP3 = sample_Overhead + samples_scalar*samples + ADCREAD*samples
                

        #time for each DAC update
        DACUPDATE = LOADDAC_OV + DAC_var*delay +DACUP_OV


        Dwell_us = (LOOP3 + DACUPDATE)/1000.0 #convert to us

        return Dwell_us


    @staticmethod
    def scanTime(Dwell = 0, pF=1 , pS=1):
        """
        Takes the dwell time and scan size to calculate scan time in seconds
        Dwell is inputed in us calulated from dwellTime()
        pF stands for the number of pixels in the fast scan dimension
        pS stands for the number of pixels in the slow scan dimension

        All constants are in ns

        returns scanTime in seconds
        """
        if pF is None:
           return 
        if pS is None:
           return 
        LOOP2_OV = 40
        LOOP1_OV = 40
        SETUP = 1025 #Overhead to set up scan 

        LOOP2 = (Dwell*1000+LOOP2_OV)*pF + 5 #in nanoseconds

        LOOP1 = (LOOP2+LOOP1_OV)*pS

        ScanTime_ns = SETUP + LOOP1 # scantime in nanoseconds


        ScanTime_s = ScanTime_ns/1.0e9

        #print divmod(ScanTime_s, 60)
        #print ScanTime_s

        return ScanTime_s

    
