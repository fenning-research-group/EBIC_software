import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import Mfigure
import pylab
import numpy




class DraggableRectangle:
    def __init__(self, rect, callback = None):
        self.rect = rect
        self.press = None
        self.background = None
        self.lock = None
        self.callback = callback


    def connect(self):
        'connect to all the events we need'
        self.cidpress = self.rect.figure.canvas.mpl_connect(
            'button_press_event', self.on_press)
        self.cidrelease = self.rect.figure.canvas.mpl_connect(
            'button_release_event', self.on_release)
        self.cidmotion = self.rect.figure.canvas.mpl_connect(
            'motion_notify_event', self.on_motion)

    def on_press(self, event):
        'on button press we will see if the mouse is over us and store some data'
        if event.inaxes != self.rect.axes: return

        contains, attrd = self.rect.contains(event)
        if not contains: return
        #print 'event contains', self.rect.get_array
        offset = self.rect.get_offsets()
        #y0 = self.rect.get_offsets[1] 
        self.press = offset, event.xdata, event.ydata

        self.lock = True

        # draw everything but the selected rectangle and store the pixel buffer
        canvas = self.rect.figure.canvas
        axes = self.rect.axes
        self.rect.set_animated(True)
        canvas.draw()
        self.background = canvas.copy_from_bbox(self.rect.axes.bbox)

        # now redraw just the rectangle
        axes.draw_artist(self.rect)

        # and blit just the redrawn area
        canvas.blit(axes.bbox)


    def on_motion(self, event):
        'on motion we will move the rect if the mouse is over us'
        if self.lock is not True:
            return
        if event.inaxes != self.rect.axes: return

#        'on motion we will move the rect if the mouse is over us'
#        if self.press is None: return
#        if event.inaxes != self.rect.axes: return
        offset, xpress, ypress = self.press
        dx = event.xdata - xpress
        dy = event.ydata - ypress
        x0 = offset[0][0]
        y0 = offset[0][1]
        self.rect.set_offsets([(x0+dx),(y0+dy)])

        canvas = self.rect.figure.canvas
        axes = self.rect.axes
        # restore the background region
        canvas.restore_region(self.background)

        # redraw just the current rectangle
        axes.draw_artist(self.rect)

        # blit just the redrawn area
        canvas.blit(axes.bbox)


    def on_release(self, event):
#        'on release we reset the press data'
#        self.press = None

        'on release we reset the press data'
        if self.lock is not True:
            return

        self.press = None
        self.lock = None

        # turn off the rect animation property and reset the background
        self.rect.set_animated(False)
        self.background = None

        # redraw the full figure
        self.rect.figure.canvas.draw()
        self.callback()


    def disconnect(self):
        'disconnect all the stored connection ids'
        self.rect.figure.canvas.mpl_disconnect(self.cidpress)
        self.rect.figure.canvas.mpl_disconnect(self.cidrelease)
        self.rect.figure.canvas.mpl_disconnect(self.cidmotion)





class ProfileLine:

    def __init__(self, canvas = None , ax = None , callback = None):
        self.startpoint = None
        self.endpoint = None
        self.line = None
        self.canvas = canvas
        self.ax = ax
        self.callback = callback
        self.set_Point1()


    def set_Point1(self):
        self.point = True
        self.cidpress = self.canvas.mpl_connect('button_press_event', self.drawPoint)

    def set_Point2(self):
        self.point = False  # switch to set to end point TODO: make more intuitative/correct
        self.cidpress = self.canvas.mpl_connect('button_press_event', self.drawPoint)


    def drawPoint(self, event):
        if self.point == True:
           color = 'b'
           shape = 's'
        else:
            color = 'r'
            shape = 'o'
        self.x= event.xdata 
        self.y= event.ydata
        print self.x , self.y
        self.canvas.mpl_disconnect(self.cidpress)
        if self.point == True:
            if self.startpoint != None:
                self.startpoint.remove()
            self.startpoint = self.ax.scatter(self.x, self.y, s = 60, c = color, marker=shape  )
            self.canvas.draw()
            self.dr1 = DraggableRectangle(self.startpoint, self.drawLine)
            self.dr1.connect()
            self.set_Point2()

        else:
            if self.endpoint !=None:
                self.endpoint.remove()
            self.endpoint =  self.ax.scatter(self.x, self.y, s = 60, c = color, marker=shape  )
            self.canvas.draw()
            self.dr2 = DraggableRectangle(self.endpoint, self.drawLine)
            self.dr2.connect()
            self.drawLine() 


    
    def drawLine(self):
        if  self.startpoint and self.endpoint != None:
            self.startOffset = self.startpoint.get_offsets()[0]
            self.endOffset =  self.endpoint.get_offsets()[0]

            self.xPoints = [self.startOffset[0], self.endOffset[0]]
            self.yPoints = [self.startOffset[1], self.endOffset[1]]
            if self.line != None:
                self.line.remove()
                    
            self.line, = self.ax.plot(self.xPoints,self.yPoints, alpha = 0.4, color = 'green')
            self.canvas.draw()
            self.callback()

        elif self.startpoint != None:
             self.set_Point2()
        
        else:

            return
  

class FigureBox:
    def __init__(self):
        self.subplots = []
        self.add_subplot()
    
    def add_subplot(self):
        self.subplots.append(Mfigure.SubPlots())


class SubPlots:
    def __init__(self):
        self.axes = []
        self.add_axes()

    def add_axes(self):
        self.axes.append(Mfigure.AxesBox())
        #add in position as well? 111, 211 etc. for reploting

class AxesBox:
    def __init__(self):
        """
        axes box stores the data needed to replot everything that is in a figure,  needs to be updated when the ax is changed
        """
        self.title = None
        self.xlabel = None
        self.ylabel = None
        # for replotting will plot in order it is stored in list
        # It will look at the type of object to determine how to plot it
        self.axesObjects = []


class ImageBox:
    def __init__(self, data = None, cmap = pylab.cm.Greys, extent = None, origin = "lower", alpha = 1.0, clim = None, name = 'Image', bins = 49 ):
        """
        stores information for reploting these if we close the scan or application and can be reloaded
        """
        self.cmap = cmap
        self.data = data
        self.extent = extent
        self.origin = origin
        self.alpha = alpha
        self.clim = clim 
        self.name = name
        self.bins = bins
        self.create_histogram(self.bins)
        
    def create_histogram(self, bins):
        self.binx, self.binHist = numpy.histogram(self.data, bins)
        self.binHistTrunk = self.binHist[0:bins] #gets rid of last value so it will plot          

class LineBox:
    def __init__(self, Xdata = None, Ydata = None, alpha = 1.0,  color = 'b', label = None, ls = '-', lw = 2, name = 'line'):
        self.Xdata = Xdata
        self.Ydata = Ydata
        self.alpha = alpha
        self.color = color
        self.label = label
        self.ls = ls
        self.lw = lw
        self.name = name

class ScatterBox:
    def __init__(self, x, y, size = 60, color = 'b', marker = 'o', alpha = 1.0, name = 'scatterPlot'):
        self.x = x
        self.y = y
        self.size = size
        self.c = color
        self.marker = marker
        self.alpha = alpha
        self.name = name

class ErrorPlot:
    def __init__(self, x ,y,  yerr=None, xerr=None,ecolor=None, elinewidth=None, name = 'error'):
        self.x = x
        self.y = y
        self.xerr = xerr
        self.yerr = yerr
        self.ecolor = ecolor
        self.elinewidth = elinewidth
        self.name = name


class Plotter:
    def __init__(self, ax = None, axBox = None, canvas = None):
        self.ax = ax
        self.axBox = axBox
        self.canvas = canvas
        self.activeplots = []
        if self.axBox != None:
            self.replot()

    def replot(self):
        if self.axBox != None:
            #self.ax.clear()
            for i in range(len(self.axBox.axesObjects)):
                var =  None
                temp = self.axBox.axesObjects[i]
                if temp.__class__ == Mfigure.ImageBox:
                    self.show_image(temp)
                elif temp.__class__ == Mfigure.ScatterBox:
                    self.scatter_plot(temp)
                elif temp.__class__ == Mfigure.ErrorPlot:
                    self.show_errorbar(temp)
                elif temp.__class__ == Mfigure.LineBox:
                    self.show_line(temp)
                print "len activeplots", len(self.activeplots)               
 
    def scatter_plot(self, ScatterB = None):
        scat = self.ax.scatter(ScatterB.x , ScatterB.y, alpha = ScatterB.alpha, c = ScatterB.c, marker = ScatterB.marker)
        self.canvas.draw()
        self.activeplots.append(scat)
        return scat

    def show_image(self, Im = None):
        image = self.ax.imshow(Im.data, extent = Im.extent, cmap = Im.cmap, alpha = Im.alpha, origin = Im.origin, clim = Im.clim)
        self.canvas.draw()
        self.activeplots.append(image)
        return image



    def show_line(self, Line = None):
        line, = self.ax.plot(Line.Xdata, Line.Ydata, alpha = Line.alpha, color = Line.color, label = Line.label, ls = Line.ls, lw = Line.lw)
        self.canvas.draw()
        self.activeplots.append(line)
        return line

    def show_errorbar(self, Eplot = None):
        er, xer, yer = self.ax.errorbar(Eplot.x, Eplot.y, yerr = Eplot.yerr, xerr = Eplot.xerr, ecolor = Eplot.ecolor, elinewidth = Eplot.elinewidth)
        self.canvas.draw()
        return er, xer, yer


    def remove_and_update(self, axobject):
        """
        takes the ax object, images, plot removes them and redraws
        """
        if axobject.__class__ == matplotlib.image.AxesImage:
            self.ax.images.remove(axobject)
        else:
            axobject.remove()
        #find the index of the axobject and remove it from activeplots
        tempindex = self.activeplots.index(axobject)
        print len(self.activeplots)
        print 'tempindex', tempindex
        self.activeplots.pop(tempindex)
        #remove coressponding object from axesObjects
        self.axBox.axesObjects.pop(tempindex)
        print str(self.canvas.__class__())
        self.canvas.draw()
        
    #TODO: add in function to add this. self.activeCh.canvas.fig.colorbar(image, ax = self.activeCh.canvas.ax , orientation = 'vertical')  

    def add_colorbar(self,image):

        self.canvas.fig.colorbar(image, ax = self.ax , orientation = 'vertical')
        self.canvas.draw()   

