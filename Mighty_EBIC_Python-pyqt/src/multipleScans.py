import sys
import os
import scanobject
import MightyInit as mighty

def initializeEBICInstance(ebicInstance):
    # Initiallizing the Mighty class for EBIC scan instance
    units=['V','A','','','','']
    labels=['SE','EBIC','','','','']
    gains=['1','1e9','','','','']
    chmask=0b000011    # 6 channels binary format and has two channel turned on for SE and EBIC

    ebicInstance.takeChannelUnits(units)
    ebicInstance.takeChannelGain(gains)
    ebicInstance.takeChannelLabels(labels)
    ebicInstance.setMask(chmask)
    return ebicInstance

def assignUserInput(ebicInstance,numsmp,mag,delayTime,osIndex,dx): 
    ebicInstance.setDx(dx)
    ebicInstance.setMag(mag)
    ebicInstance.setSamplesPerPoint(numsmp)
    ebicInstance.setDelay(delayTime)
    ebicInstance.update_OS(osIndex)
    ebicInstance.update_Dwell()
    return ebicInstance

# User input
numsmp=2           # number of samples in Mighty interface
mag=4000           # magnification value in the SEM setting
delayTime=30*1e-6  # delay time in sec
osIndex=1          # Index of Oversampling list, os=[0,2,4,8,16,32,64]
dx=0.02            # dx defines the step size
numScan=2	   # number of repeat scans

# Initialized the ebic instance
ebicInstance = mighty.DesignerMainWindow()
ebicInstance = initializeEBICInstance(ebicInstance)

# Assign user input to ebic instance
ebicInstance=assignUserInput(ebicInstance,numsmp,mag,delayTime,osIndex,dx)

# Start repeated scans
for i in range(numScan):
    print('start scanning')
    # ebicInstance.startScan()
    print('done scanning')
    scanName=['test'+str(i)]
    # ebicInstance.saveScanObject(scanName)
    print('save scan')