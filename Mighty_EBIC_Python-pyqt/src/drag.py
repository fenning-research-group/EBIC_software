import numpy as np
import matplotlib.pyplot as plt

class DraggableRectangle:
    def __init__(self, rect):
        self.rect = rect
        self.press = None
        self.background = None
        self.lock = None


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


    def disconnect(self):
        'disconnect all the stored connection ids'
        self.rect.figure.canvas.mpl_disconnect(self.cidpress)
        self.rect.figure.canvas.mpl_disconnect(self.cidrelease)
        self.rect.figure.canvas.mpl_disconnect(self.cidmotion)


class ProfileLine:

    def __init__(self, canvas = None , ax = None ):
        self.startpoint = None
        self.endpoint = None
        self.canvas = canvas
        self.ax = ax

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
            self.dr1 = drag.DraggableRectangle(self.startpoint)
            self.dr1.connect()

        else:
            if self.endpoint !=None:
                self.endpoint.remove()
            self.endpoint =  self.ax.scatter(self.x, self.y, s = 60, c = color, marker=shape  )
            self.canvas.draw()
            self.dr2 = drag.DraggableRectangle(self.endpoint)
            self.dr2.connect() 
        #self.activeCh.canvas.mpl_disconnect(self.cidpress)

