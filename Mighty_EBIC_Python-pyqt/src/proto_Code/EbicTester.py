import EbicCommandManager
import time
import EbicPythonCommandsAuto
import EbicDataManager
import WriteToHdf5
import sys
import numpy

from pylab import *
from scipy import mgrid
from time import strftime
from progressbar import ProgressBar, Percentage, Bar, ETA, FileTransferSpeed, RotatingMarker, ReverseBar, SimpleProgress
 
#          |commandID|PayloadSize (head plus payload size)|data in shorts|Tail FFFF



wait = False

def ETdefaultCallback():
    wait = False

#def __main__():
waitTime = 1

EbicCommands = EbicPythonCommandsAuto.EbicCommands

edm = EbicCommandManager.EbicDeviceManager()
#edm.serialCallback = ETdefaultCallback


ebicCommands = EbicCommands(edm)
writeToFile = WriteToHdf5.writeHdf5
ion()

# TODO LIST:
# Create an instance of the EbicCommands class
# Register an approriate callback to handle the incoming data
# Of course, we should have an instance of EbicDeviceManager already
# We can create an instance of the EbicDataManager class to handle incoming
# and register its member functions as above mentioned callbacks
# That leaves us needing to do something like:
# Create stuff
# register callbacks
# do a goddamn scan
# goodnight


def setupAndStartScan(edm, ebicCommands, scanConfig):
	sdm = EbicDataManager.ScanDataManager(scanConfig)
	edm.setupCommandCallback(ebicCommands.SCANCONTROLLER_SETUP,sdm.storeDataInArray)
	ebicCommands.scanController_setup(*(scanConfig.setupTuple())) # expand the tuple to get all 8 args	
	
	return sdm


def scanProgress(sdm, im):
	startTime = time.time()
	pbar = ProgressBar(widgets=[Percentage(), Bar()], maxval = sdm.valuesExpected).start()

	while not sdm1.filled(): #(time.time() - startTime < 6): # and not sdm1.filled():
		time.sleep(1)
		pbar.update(min(sdm.valuesFilled,sdm.valuesExpected))
		im.set_array(sdm.displayArray[:,:,0])
		im.autoscale()
		draw()
		pass	

	pbar.finish()
	totalTime = time.time()- startTime
	return totalTime

def samplePoint(edm, ebicCommands, samplesPerPoint, channelMask, delayFine, delayCoarse):
	ADCconfig = EbicDataManager.SampleConfig(samplesPerPoint,channelMask, delayFine, delayCoarse)
	dataPoint = EbicDataManager.SampleADCsManager(ADCconfig)
	edm.setupCommandCallback(ebicCommands.SAMPLEADCFROMMASK, dataPoint.restructureToArray)
	
	ebicCommands.sampleADCfromMask(*(ADCconfig.sampleTuple()))
	return dataPoint


def takeIV(edm, ebicCommands, samplesPerPoint, channelMask, delayFine, delayCoarse, Start, End, Vstep, points):
	pointsUp = (End-Start)/Vstep +1
	pointsDown = pointsUp-1
	offsetAux1 = -138
	sendVoltageValue = Start + offsetAux1
	vRamp = 255
	delayAux1Fine = 0
	delayAux1Coarse = 1
	dataIRaw=[]
	dataI=[]
	sentVoltage=[] 
	sampleAverage = []

	Up = True

	for k in range(0, pointsUp + pointsDown):

		ebicCommands.setAux1(sendVoltageValue,vRamp, delayAux1Fine, delayAux1Coarse)
		time.sleep(1)
		
		for n in range(0,points):
			sampleAverage=[]
			data = samplePoint(edm, ebicCommands, samplesPerPoint,channelMask, delayFine, delayCoarse)
			time.sleep(0.033)
			dataIRaw.append(data.dataArray)
			sampleAverage.append(numpy.average(data.dataArray))
			
		
		#dataI.append(numpy.average(data.dataArray))
		print sampleAverage
		dataI.append(numpy.average(sampleAverage))
		sentVoltage.append(sendVoltageValue - offsetAux1)

		if Up == True:
			sendVoltageValue += Vstep
		else:
			sendVoltageValue -= Vstep

		if (sendVoltageValue - offsetAux1) >= End :
			Up = False

	return dataI, sentVoltage, dataIRaw




def plotImageChannels(sdm):
	dataShape = sdm.displayArray.shape
	
	for k in range(0, (dataShape[2])):	
		FigTitle = 'Channel: %d' %(k+1)
		figure(k+1)
		imshow(sdm1.displayArray[:,:,k], cmap=cm.gray, origin='upper')
		title(FigTitle)
		xlabel('Points')
		ylabel('Points')
		axis('scaled')
		colorbar()
	draw()
	#show()

if edm.ebicDevice.isReadyToRun():
	print "ready to run"
	edm.startReaders()


	
    #ScanConfig(stepSize, xOffset, yOffset, lenX, lenY, samplesPerPoint, channelMask, delayFine, delayCoarse)
	scanConfig = EbicDataManager.ScanConfig(255,255,-32767,-32767,255,255,1,1,0,1)#TODO config

	sdm1 = setupAndStartScan(edm, ebicCommands, scanConfig)
	
	im = imshow(sdm1.displayArray[:,:,0], cmap=cm.gray, origin='upper') 
	TotalTime = scanProgress(sdm1, im)	

	print "Got %d; expected %d" %(sdm1.valuesFilled, sdm1.valuesExpected)
	print "here"

	print "total time to scan: %f" %(TotalTime)
	writeToFile(sdm1.dataArray, "ScanData")
	

	plotImageChannels(sdm1)
	show()
	
	#sample = samplePoint(edm, ebicCommands, 5,3, 1,0)
	
	#time.sleep(1)

	#iData, vSent = takeIV(edm, ebicCommands, 100,1,0,1,0,330,33)

	time.sleep(1)
	#print sample.dataArray
	#print iData
	print "Snotties !!!! \n"
	#print vSent

	
	#figure(3)
	#plot(vSent,iData)
	#draw()
	#show()

	#time.sleep(5)
	edm.keepRunning = False
	edm.stopReaders()




# vim: set ts=4:sw=4
