import numpy
import pylab

def getProfile(File):

    dataProfile = File['profiles']

    wire = dataProfile[0,0,:]
    base = dataProfile[-1,0,:]

    startx = File['profileposition'][0,0,0]
    endx = File['profileposition'][0,1,0]

    Vstep= 20/2**16.0  # voltage of adc
    Gain = 10**9.0
    scale = Vstep/Gain

    return wire, base, startx, endx, scale

def getSlice(File):
     sliceData = File['sliceData']
     displayData = numpy.average(sliceData, 2)   
     return displayData  

      
def loadFile(loadName):
    File = numpy.load(str(loadName))

    return File 

def displayAll(profile, image, channel,title, startx, endx):
    fig = pylab.figure()
    ax = fig.add_subplot(111)

    ax.imshow(image[:,startx:endx,channel], cmap= pylab.cm.BrBG, origin='lower')
    
    ax2 = ax.twinx() 

    ax2.plot(profile[startx:endx])
    #ax.set_title(title) 
    ax2.grid()
    pylab.show()

def displayTwo(profile, image, channel,title, startx, endx, base, wire):
    fig = pylab.figure()
    ax = fig.add_subplot(211)
    
    right = endx-startx
    left = 0
    #top = image.shape[0]
    #bottom = 0
    ax.imshow(image[:,startx:endx,channel],cmap= pylab.cm.BrBG, origin='lower')
    ax.set_xbound(left, right)
 
    ax2 = ax.twinx() 

    ax2.plot(profile[startx:endx], color='g')
    ax2.set_xbound(left, right)

    ax.set_title(title) 
    ax2.grid()

    ax3 = fig.add_subplot(212)
    
    ax3.plot(wire[startx:endx], color ='b')
    ax3.plot(base[startx:endx], color='r')

    unscaledProfile = wire-base
    ax3.plot(unscaledProfile[startx:endx], color='g')

    ax3.set_xbound(left, right)

    ax3.grid()
 
    pylab.show()




def run(loadName, channel):

    File = loadFile(loadName)
    
    wire, base ,startx, endx, scale = getProfile(File)

    profile = (wire-base)*scale
    
    image = getSlice(File)
     
    displayAll(profile, image, channel, loadName, startx, endx)
    
    #displayTwo(profile, image, channel, loadName, startx, endx, base, wire)



