import numpy
import CCNT_test

class ScanConfig:
    def __init__(self, stepSizeH = None ,stepSizeV = None, hOffset = None, vOffset = None, pointsH = None, pointsV = None
                    ,samplesPerPoint = None, channelMask = None, delayFine = None, delayCoarse = None, mag = None
                    , units = None, gain = None, labels = None, delaySeconds = None, displayOffsets = None, OSI = None):
        """
        create a ScanConfig object to store data to be sent to the microcontroller, also stores other scaninfo about inputs and their
        properties
        """
        self.stepH = stepSizeH
        self.stepV = stepSizeV
        self.hOffset = hOffset
        self.vOffset = vOffset
        self.pointsH = pointsH
        self.pointsV = pointsV
        self.samplesPerPoint = samplesPerPoint 
        self.channelMask = channelMask 
        self.delayFine = delayFine
        self.delayCoarse = delayCoarse
        self.mag = mag
        self.units = units
        self.gain = gain
        self.labels = labels
        self.delay = delaySeconds
        self.offsets = [hOffset,vOffset] #TODO: make this make more sense
        self.displayOffsets = displayOffsets
        self.OSI = OSI

    def setupTuple(self):
        return (self.stepH, self.stepV, self.hOffset, self.vOffset, self.pointsH
                ,self.pointsV, self.samplesPerPoint, self.channelMask, self.delayFine, self.delayCoarse)


class SampleConfig:
    def __init__(self, samplesPerPoint, channelMask, delayFine, delayCoarse):
        self.samplesPerPoint = samplesPerPoint
        self.channelMask = channelMask
        self.delayFine = delayFine
        self.delayCoarse = delayCoarse

    def sampleTuple(self):
        return(self.samplesPerPoint, self.channelMask, self.delayFine, self.delayCoarse)



class SampleADCsManager:

    def __init__(self,SampleConfig):
        self.samplesPerPoint = SampleConfig.samplesPerPoint
        self.channelMask = SampleConfig.channelMask
        self.delayFine = SampleConfig.delayFine
        self.delayCoarse = SampleConfig.delayCoarse
        self.valuesFilled = 0
        self.channelCount = DataManagerUtils.maskToChannelCount(self.channelMask)
        self.valuesExpected = self.samplesPerPoint * self.channelCount
        self.dataArray = self.makeNDataArray(self.samplesPerPoint ,self.channelCount)
        self.upDateFunc = None  
    
    def makeNDataArray(self, numsamples, channel):
        storedArray = numpy.zeros([numsamples, channel], numpy.int16)
        return storedArray

    def restructureToArray(self, index, commandData):
        dataOffset = 2
        self.dataArray = DataManagerUtils.packetToArray(self.samplesPerPoint, self.channelCount, dataOffset, commandData)
        
        


class ScanDataManager: 

    def __init__(self, scanConfig = None, scanObject = None, OS = None): 
        #self.scanConfig = scanConfig.scanConfig # good idea? OL, yes TM
        self.stepSizeX = scanConfig.stepV
        self.stepSizeY = scanConfig.stepH
        self.xOffset = scanConfig.vOffset
        self.yOffset = scanConfig.hOffset
        self.lenX = scanConfig.pointsV
        self.lenY = scanConfig.pointsH
        self.samplesPerPoint = scanConfig.samplesPerPoint 
        self.channelMask = scanConfig.channelMask
        self.delayFine = numpy.uint32(scanConfig.delayFine)# changed to uint32 for delay see if this works
        self.delayCoarse = numpy.uint16(scanConfig.delayCoarse)
        self.channelCount = DataManagerUtils.maskToChannelCount(self.channelMask)
        self.OSI = OS
        #self.res = None
        self.stopScanCommand()

        self.constructPayload()
        if scanObject is None :

            self.dataArray = numpy.zeros([self.pF, self.pS, self.samp, self.channelCount], numpy.int32)
            print "dataArray" , self.dataArray.shape
            self.displayArray = numpy.zeros([self.pF, self.pS, self.channelCount], numpy.float)
            print "Display Array", self.displayArray.shape
        else :

            self.dataArray = numpy.zeros([self.pF, self.pS, self.samp, self.channelCount], numpy.int32)
            print "dataArray" , self.dataArray.shape
            self.displayArray = numpy.zeros([self.pF, self.pS, self.channelCount], numpy.float)
            print "Display Array", self.displayArray.shape

            #Janky buts seems nessecary 
            scanObject.rawDataArray = self.dataArray
            scanObject.DisplayArray = self.displayArray
            #self.dataArray = scanObject.rawDataArray
            #self.displayArray = scanObject.DisplayArray
        #self.valuesFilled = 0
        #self.valuesExpected = self.lenX * self.lenY * (self.samplesPerPoint * self.channelCount)
        #self.dumpArray=[] 

    #TODO: remove most of these as we won't need them with new way of doing things

    def filled(self):
        return (self.valuesFilled >= self.valuesExpected)

    def getIndex(self, position, stepSize, positionOffset):
        indexValue = (position - positionOffset)/stepSize
        return indexValue
    

    #TODO: swapped numsamples and channel, should use keywords instead
    def makeNDataArray(self, lenX, lenY, channel, numsamples):
        storedArray = numpy.zeros([lenX, lenY, channel, numsamples], numpy.int32)
        return storedArray

    def makeDisplayArray(self, lenX, lenY, channel):
        displayArray = numpy.zeros([lenX, lenY, channel], numpy.float)
        return displayArray 

    #TODO: need to replace this function with new one     
    def storeDataInArray(self, index, commandData):
        xindex, yindex, data = self.restructureToArray(index, commandData)
        self.dataArray[yindex,xindex] = data 
        self.displayArray[yindex,xindex] = numpy.average(data, axis = 0)
        #print data
        self.valuesFilled += self.samplesPerPoint * self.channelCount
        if self.upDateFunc != None:
           self.upDateFunc(self)

    def test_scanSize(self):
        temp = 1
        for i in self.resizeDim:
            temp = i*temp

        assert self.TF*temp == self.pF*self.pS*self.samp*self.CH
        return temp


    #TODO: clean up taken from example, USE this in new GUi design, less constraints in complexity
    def constructPayload(self):
	
        #bit shift
        OS_0 = 2
        OS_1 = 3
        OS_2 = 5

        #extract bits
        OS0 = 0b001
        OS1 = 0b010
        OS2 = 0b100
        #self.OSI = 8


        if self.OSI > 0:
            OS_value = int(numpy.log2(self.OSI))
        else:
            OS_value = self.OSI
        #print "OS_value", OS_value

        self.Sx = numpy.int16(self.xOffset)
        self.Sy = numpy.int16(self.yOffset)
        self.sdx = numpy.int16(0x0000)
        self.sdy = numpy.int16(self.stepSizeY)
        self.dx = numpy.int16(self.stepSizeX)
        self.dy = numpy.int16(0x0000)
        self.pF = self.lenX
        self.pS = self.lenY
        self.samp = self.samplesPerPoint
        self.CH = self.channelCount
        self.DVAR = self.delayFine
        self.OS =  ((OS_value & OS2) >> 2) << OS_2 | ((OS_value & OS1) >> 1) << OS_1 | (OS_value & OS0) << OS_0 
        #print "OS", self.OS
        self.XFER = self.CH << 16 | ((self.CH*4) -1) << 8
   
   
   
        #this replaces what follows:
        self.TF, self.TF_state, self.pF, self.pS, self.samp, self.CCNT, self.resizeDim = CCNT_test.set_CCNT(pF = self.pF,pS = self.pS, CH = self.CH , samp = self.samp)
        
        #Make sure scan doesn't go outside bounds of what the DAC can take as an input
        assert abs(self.Sx + self.sdx*self.pS) <= abs(0x8000) 

        assert abs(self.Sx + self.dx*self.pF) <= abs(0x8000) 

        assert abs(self.Sy + self.sdy*self.pS) <= abs(0x8000) 

        assert abs(self.Sy + self.dy*self.pF) <= abs(0x8000) 


    
        # format Command
        res = "%8x" %0xa0aa        #
        res += "%8x" %self.Sx	
        res += "%8x"%self.Sy
        res += "%8x"%self.sdx
        res += "%8x"%self.sdy
        res += "%8x"%self.dx
        res += "%8x"%self.dy
        res += "%8x"%self.pF
        res += "%8x"%self.pS
        res += "%8x"%self.samp
        res += "%8x"%self.CH
        res += "%8x"%self.DVAR
        res += "%8x"%self.OS
        res += "%8x"%self.XFER
        res += "%8x"%self.CCNT
        self.res = res
    

        return self.res


    def stopScanCommand(self):

        #define STOP_SCAN  0xf0ff
        cmd = "%8x" %0xf0ff
        self.stopCommand = cmd


    #takes commanddata and returns position index for x and y and 2d numpy array with channel and sample for 
    def restructureToArray(self, index, commandData):
        dataOffset = 6 
        numChan = DataManagerUtils.maskToChannelCount(commandData[0])
        numSamples = DataManagerUtils.getNumSamples(commandData[1])
        Xpos = DataManagerUtils.twoBytestoShort(2,commandData)
        #print "Xpos: %d" % Xpos
        xIndex = self.getIndex(Xpos, self.stepSizeX, self.xOffset)
        #print "xIndex: %d" % xIndex
        Ypos = DataManagerUtils.twoBytestoShort(4, commandData)
        #print "Ypos: %d" % Ypos
        yIndex = self.getIndex(Ypos, self.stepSizeY, self.yOffset) 
        #print "yIndex: %d " % yIndex
        newArray = DataManagerUtils.packetToArray(numSamples, numChan, dataOffset, commandData)     
        return xIndex, yIndex, newArray


    def upDateFunc(self,sdm):
        return

    def put_in_array(self, index, commandData):
        self.dumpArray.append([commandData, index])
        self.valuesFilled += self.samplesPerPoint * self.channelCount


class DataManagerUtils:
    @staticmethod
    def packetToArray(numSamples, numChan, dataOffset, commandData):
        newArray = numpy.zeros([numSamples,numChan],numpy.int16)
        for k in range(0,numSamples):
            depthOffset = k*numChan*2 
            for l in range(0,numChan):
                #print "klc: %d, %d, %d" % (k,l, len(commandData)) #TM for debuging
                # -- assemble each unit16 from 2 unit8's   
                tmp = (numpy.uint16(commandData[dataOffset + depthOffset + (l*2)]) << 8)
                tmp += numpy.uint16(commandData[dataOffset + depthOffset +((l*2)+1)])
                newArray[k,l] = numpy.int16(tmp)
        return newArray

    @staticmethod
    def maskToChannelCount(channelMask):
        count = 0
        for n in range(8):
            if((channelMask & (1 << n)) != False):     
                count += 1
        return count

    # takes two bytes as structured from microcontroller and put them into a short
    @staticmethod
    def twoBytestoShort(offset, Data):
        tmp = numpy.uint16(Data[offset])
        tmp += (numpy.uint16(Data[offset +1]) << 8)
        return numpy.int16(tmp)

    @staticmethod
    def getNumSamples(sampleByte):
        return(sampleByte)



class DumptoMemory:

    def __init__(self, scanConfig):
        self.stepSizeX = scanConfig.stepSizeX
        self.stepSizeY = scanConfig.stepSizeY
        self.xOffset = scanConfig.xOffset
        self.yOffset = scanConfig.yOffset
        self.lenX = scanConfig.lenX
        self.lenY = scanConfig.lenY
        self.samplesPerPoint = scanConfig.samplesPerPoint 
        self.channelMask = scanConfig.channelMask
        self.delayFine = numpy.uint16(scanConfig.delayFine)
        self.delayCoarse = numpy.uint16(scanConfig.delayCoarse)
        self.channelCount = 1#DataManagerUtils.maskToChannelCount(self.channelMask)
        self.dataArray = self.makeNDataArray(self.lenX, self.lenY, self.samplesPerPoint, self.channelCount)
        self.displayArray = numpy.zeros([self.lenX, self.lenY, self.channelCount], numpy.float) 
        self.valuesFilled = 0
        self.valuesExpected = self.lenX * self.lenY * (self.samplesPerPoint * self.channelCount) 
        self.memdump=[]
    
    def storeDataInArray(self, index, commandData):
        self.valuesFilled += self.samplesPerPoint * self.channelCount
        self.memdump.append(commandData)
        

    def filled(self):
        return (self.valuesFilled >= self.valuesExpected)

    def makeNDataArray(self, lenX, lenY, numsamples, channel):
        storedArray = numpy.zeros([lenX, lenY, numsamples, channel], numpy.int16)
        return storedArray

