#TODO: this seems like it is no longer in use????

import numpy

def getMaxMin(inputArray, axisIndex, center, threshold, channel):
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


