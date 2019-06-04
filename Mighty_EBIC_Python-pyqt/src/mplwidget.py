#!/usr/bin/env python
import Mfigure

# Python Qt4 bindings for GUI objects
from PyQt4 import QtGui
import mplwidget

# import the Qt4Agg FigureCanvas object, that binds Figure to
# Qt4Agg backend. It also inherits from QWidget
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas

#name change of libraries in matplotlib TODO figure whatthis is exactly
try:
    from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar
except ImportError:    
    from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar

# Matplotlib Figure object
from matplotlib.figure import Figure

class MplCanvas(FigureCanvas):
    """Class to represent the FigureCanvas widget"""
    def __init__(self):
        # setup Matplotlib Figure and Axis
        self.fig = Figure(facecolor = '0.2', edgecolor = 'black')
        self.plotters = []
        self.subplots = []

        # added to support multiple subplots and axes and be able to keep track of everything
        # not  done yet but this is the idea TM
        #self.subplots.append(SubPlot())
        #self.subplots[-1].axes.append(self.fig.add_subplot(111, autoscale_on=False)) 
        
        #replaced :self.ax = self.fig.add_subplot(111, autoscale_on=False), with:
        #self.ax = self.subplots[0].axes[0]
        #fits old format to new one so we don't break everything at once ,TM
        self.oneSubPlot()
        # initialization of the canvas
        FigureCanvas.__init__(self, self.fig)
        # we define the widget as expandable
        FigureCanvas.setSizePolicy(self,
                                   QtGui.QSizePolicy.Expanding,
                                   QtGui.QSizePolicy.Expanding)
        # notify the system of updated policy
        FigureCanvas.updateGeometry(self)



    def add_Ax(self, ax = None, axes = None):
        if ax == None:
            self.ax2 = self.ax.twinx()
        elif ax != None and axes != None:
            axes.append(ax.twinx())
            self.ax2 = axes[-1]

        self.ax2.set_navigate(False)
        #self.ax2.set_picker(False)
        self.draw() 


    #TODO: make function that can specify how many subplots they are row and columns
    # where is the best palce to do this?

    def twoSubplots(self):
        
        self.fig.clear()
        #self.plotters is not really need anymore since it is now contained in 
        self.plotters = []
        self.subplots = []
        self.subplots.append(SubPlot())
        self.subplots[-1].axes.append(self.fig.add_subplot(211, autoscale_on=False))
        self.ax = self.subplots[0].axes[0]
        self.ax.clear()

        self.subplots.append(SubPlot())
        self.subplots[-1].axes.append(self.fig.add_subplot(212, sharex = self.ax))
        self.ax_2 = self.subplots[-1].axes[0]
        self.ax_2.clear()

#        self.ax = self.fig.add_subplot(211)
#        self.ax_2 = self.fig.add_subplot(212, sharex = self.ax)# shares the same x access so data lines up right!

    def oneSubPlot(self):
        """
        should be used for every new plot should call this to clear out the subplots for loaded file
        """
        self.fig.clear()
        #self.fig.subplots_adjust(right = 0.95 , left = 0.05)
        #self.plotters = []
        #self.ax = self.fig.add_subplot(111, autoscale_on=False)
        #self.ax.clear()

        self.subplots = []
        self.subplots.append(SubPlot())
        self.subplots[-1].axes.append(self.fig.add_subplot(111, autoscale_on=False))
        
        #replaced :self.ax = self.fig.add_subplot(111, autoscale_on=False), with:
        self.ax = self.subplots[0].axes[0]
        self.ax.clear()
        self.ax.tick_params(axis='both', colors = 'black', direction ='out', top = 'off', right = 'off')
        self.ax.tick_params(axis='x', colors = 'white')
        

    def add_plotter(self,ax = None, axBox = None, subplot = None):
        #self.plotters.append(Mfigure.Plotter(ax = ax, axBox = axBox, canvas = self))
        if subplot != None:
            subplot.plotters.append(Mfigure.Plotter(ax = ax, axBox = axBox, canvas = self))

    def append_subplot(self):
        self.subplots.append(SubPlot())

    def remove_subplot(self, index):
        self.subplots.pop(index)

    def load_figure(self, figure = None):
        if figure != None :
            self.fig = figure
            FigureCanvas.__init__(self, self.fig)
            # we define the widget as expandable
            FigureCanvas.setSizePolicy(self,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
            # notify the system of updated policy
            FigureCanvas.updateGeometry(self)
 
    

class MplWidget(QtGui.QWidget):
    """Widget defined in Qt Designer"""
    def __init__(self, parent = None):
        # initialization of Qt MainWindow widget
        QtGui.QWidget.__init__(self, parent)
        # set the canvas to the Matplotlib widget
        self.canvas = MplCanvas()
        self.nav=NavigationToolbar(self.canvas, parent)
        # create a vertical box layout
        self.vbl = QtGui.QVBoxLayout()
        # add mpl widget to the vertical box
        self.vbl.addWidget(self.canvas)
        self.vbl.addWidget(self.nav)
        # set the layout to the vertical box
        self.setLayout(self.vbl)

class MplHIST(QtGui.QWidget):
    """Widget defined in Qt Designer"""
    def __init__(self, parent = None):
        # initialization of Qt MainWindow widget
        QtGui.QWidget.__init__(self, parent)
        # set the canvas to the Matplotlib widget
        self.canvas = MplCanvas()
        # create a vertical box layout
        self.vbl = QtGui.QVBoxLayout()
        # add mpl widget to the vertical box
        self.vbl.addWidget(self.canvas)
        # set the layout to the vertical box
        self.setLayout(self.vbl)


class Cursor:
    def __init__(self, ax, canvas):
        self.canvas = canvas
        self.ax = ax
        self.lx = ax.axhline(color='k')  # the horiz line
        self.ly = ax.axvline(color='k')  # the vert line

        # text location in axes coords
        self.txt = ax.text( 0.7, 0.9, '', transform=ax.transAxes)

    def mouse_move(self, event):
        if not event.inaxes: return

        x, y = event.xdata, event.ydata
        # update the line positions
        self.lx.set_ydata(y )
        self.ly.set_xdata(x )

        self.txt.set_text( 'x=%1.2f, y=%1.2f'%(x,y) )
        self.canvas.draw()

class SubPlot:
    def __init__(self):
        self.axes = []
        self.plotters = []
