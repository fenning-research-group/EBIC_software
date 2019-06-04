import EbicDataManager
#import WriteToHdf5
import numpy
import sys, threading , Queue , time

import socket
import CCNT_test
from CCNT_test_unit import *

IP = "10.0.1.8"
PORT = 5009

#q = Queue.Queue()


buf_size = 4096
dt = numpy.dtype('uint32')

class socket_to_queue(threading.Thread):

    def __init__(self,q, scanFlag = None):

        threading.Thread.__init__(self)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
        self.sock.settimeout(0.5) #tried timeout will continue until data is done
        self.sock.bind(("",PORT))
        self.q = q
        self.count = 0
	self.scanFlag = scanFlag

    def run(self):
        print "Started recieve Q and Socket \n"

        while True:
            try:
                data = (self.sock.recv(buf_size))
                self.count = self.count + 1
            except socket.error as msg:
                self.sock.close()
		if self.scanFlag is not None:
	            self.scanFlag[0] = True	
                print "error", msg
                break
            
            if not data: 
                print "no data"
                self.sock.close()
                break
            self.q.put(data)

        self.sock.close()
        print"Recieve Socket Closed \n"
	return#self.join()


class Edm(threading.Thread):

    def __init__(self, displayArray = None, scanFlag = None, progress = None, scanData = None\
                    , scanConfig = None, scanObject = None, Transport = None, Aux1 = None, \
                    Aux2 = None, OS = None, sockQ = None, q = None):
        self.scanData = scanData
        self.progress = progress
        self.scanConfig = scanConfig
        self.displayArray = displayArray
        self.scanFlag = scanFlag
        self.scanObject = scanObject
        self.transport = Transport
        self.Aux1 = Aux1
        self.Aux2 = Aux2
        self.OS = OS
        self.sockQ = sockQ
        self.q = q
        if  self.scanObject is not None:
            self.sdm = EbicDataManager.ScanDataManager(self.scanConfig, self.scanObject, OS = self.OS) 
        threading.Thread.__init__(self)


    def run(self):
        if  self.scanObject is not None:
            #self.setupAndStartScan()
            self.displayArray[0] = self.sdm.displayArray                
            self.scanProgress_NEW() # changed for new version of Mighty EBIC


        if self.transport != None:
            self.takeIV()
        if self.Aux1 != None:
            self.setAux1()
        if self.Aux2 != None:
            self.setAux2()      


	#self.join()
	return  
                

    def setupAndStartScan(self):
        #self.sdm = EbicDataManager.ScanDataManager(self.scanConfig, self.scanObject, OS = self.OS) 
        return
    

    #TODO: find the right place for this to live ok for now
    def setAux1(self):
        vstep = 20.0/0xffff
        self.Aux1 = self.Aux1/vstep
        vRamp = 255

    def setAux2(self):
        vstep = 20.0/0xffff
        self.Aux2 = self.Aux2/vstep


    def takeIV(self):
        #constants
        vRamp = 255
        delayAux1Fine = 0
        delayAux1Coarse = 1
        samplesPerPoint = self.transport.samples
        delayFine = 100
        delayCoarse = 0
        sendVoltageValue = self.transport.start
        Up = True
        print "step size = ", self.transport.step
        for k in range(0, self.transport.pointsUp + self.transport.pointsDown):
            self.ebicCommands.setAux1(sendVoltageValue,vRamp, delayAux1Fine, delayAux1Coarse)
            startTime = time.time()
            time.sleep(self.transport.delay)
            sampleAverage = [] 
            for n in range(0,self.transport.points):
                data = self.samplePoint(samplesPerPoint,self.transport.channelMask, delayFine, delayCoarse)
                time.sleep(0.066)
                self.transport.dataIRaw.append(data.dataArray)
                scaledData = data.dataArray*self.transport.vstep/self.transport.gain
                sampleAverage.append(numpy.average(scaledData))
            self.transport.soakTime.append(time.time() - startTime)
            self.transport.dataI.append(numpy.average(sampleAverage))
            self.transport.dataIstd.append(numpy.std(sampleAverage))
            self.transport.sentVoltage.append(sendVoltageValue*self.transport.vstep)
            if sendVoltageValue >= self.transport.end :
                Up = False
            if Up == True:
                sendVoltageValue += self.transport.step
            else:
                sendVoltageValue -= self.transport.step
            self.transport.soakTime.append(time.time() - startTime)
        self.scanFlag[0] = True
        return



    def samplePoint(self, samplesPerPoint, channelMask, delayFine, delayCoarse):
        ADCconfig = EbicDataManager.SampleConfig(samplesPerPoint,channelMask, delayFine, delayCoarse)
        dataPoint = EbicDataManager.SampleADCsManager(ADCconfig)
        self.edm.setupCommandCallback(self.ebicCommands.SAMPLEADCFROMMASK, dataPoint.restructureToArray)
        self.ebicCommands.sampleADCfromMask(*(ADCconfig.sampleTuple()))
        return dataPoint



    #NEW for putting data from ethernet into
    def scanProgress_NEW(self):
        #TODO: add in values for these parameters
        datacount = self.sdm.test_scanSize()
        print datacount
        #count = 0

        while self.sockQ.is_alive() and (self.scanFlag[0] is False):
            try:
                data = self.q.get()
                 
                header = numpy.frombuffer(data, dtype = dt, count = 1, offset = 4)
            #Grab data from buff keep sign shift remaing data back print values
                X = numpy.frombuffer(data, dtype = dt, count = datacount, offset = 16)
            #typecast to keep sign
                Copy = numpy.int32(X << 14)
            #shift data back to proper space
            #now we have signed 18bit data represented as signed int32
                Z = Copy >> 14   #get data back to its place but keep the sign
            #data is always zero indexed


                if header <= self.sdm.TF :

            
                    xindex , sub_xindex, yindex, samp_index, sub_samp_index = CCNT_test.TF_index(self.sdm.TF, \
                    self.sdm.TF_state, pF = self.sdm.pF, pS = self.sdm.pS, samp = self.sdm.samp,\
                    CCNT= self.sdm.CCNT, header = header, resizeDim = self.sdm.resizeDim)

                    sub_data_array = sim_data.test_reshape(Z, self.sdm.CCNT, self.sdm.samp, self.sdm.CH, \
                    TF_state = self.sdm.TF_state)


            # put data in dataArray
                    put_inP(self.sdm.dataArray,sub_data_array, xindex, sub_xindex, yindex, samp_index, \
                    sub_samp_index, self.sdm.TF_state, self.sdm.resizeDim)

                    temp = numpy.multiply(sub_data_array, self.scanObject.channels)#scales just the data coming back for the display    


            #put data in displayArray and average
                    put_in_Display(self.sdm.displayArray,numpy.average(temp, axis = 1), xindex, sub_xindex,\
                    yindex, samp_index, sub_samp_index, self.sdm.TF_state, self.sdm.resizeDim)


                    self.displayArray[0] = self.sdm.displayArray# numpy.multiply(self.sdm.displayArray, self.scanObject.channels)#modified scaleing
                    self.progress[0] = 100*((1.0*header)/self.sdm.TF)
                if header == self.sdm.TF:
                    print "done"
                    break
            except:
                print "No data \n"
                 
        self.sockQ.sock.close()
        self.scanData[0] = self.sdm.dataArray
        self.scanObject.rawDataArray = self.sdm.dataArray
        self.scanObject.scale_channels()
        self.scanFlag[0] = True
	print "scanFlag True"
       
	return 








# vim: set ts=4:sw=4
