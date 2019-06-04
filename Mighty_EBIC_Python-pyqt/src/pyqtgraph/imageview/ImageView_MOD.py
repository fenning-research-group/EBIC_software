# -*- coding: utf-8 -*-
"""
ImageView.py -  Widget for basic image dispay and analysis
Copyright 2010  Luke Campagnola
Distributed under MIT/X11 license. See license.txt for more infomation.

Widget used for displaying 2D or 3D data. Features:
  - float or int (including 16-bit int) image display via ImageItem
  - zoom/pan via GraphicsView
  - black/white level controls
  - time slider for 3D data sets
  - ROI plotting
  - Image normalization through a variety of methods
"""
import os
import numpy as np

from ..Qt import QtCore, QtGui, USE_PYSIDE
if USE_PYSIDE:
    from .ImageViewTemplate_MOD_pyside import *
else:
    from .ImageViewTemplate_MOD_pyqt import *
    
from ..graphicsItems.ImageItem import *
from ..graphicsItems.LabelItem import *
from ..graphicsItems.TextItem import *
from ..graphicsItems.ROI import *
from ..graphicsItems.LinearRegionItem import *
from ..graphicsItems.InfiniteLine import *
from ..graphicsItems.ViewBox import *
from .. import ptime as ptime
from .. import debug as debug
from ..SignalProxy import SignalProxy
from .. import functions as fn
from math import *

from .. graphicsItems.ScaleBar import *

try:
    from bottleneck import nanmin, nanmax
except ImportError:
    from numpy import nanmin, nanmax

class CrossHairs():
    
    def __init__(self, vb, callback = None, Header = None, data = None, imScale = None):
        self.vb = vb
        self.callback = callback
        #self.scaleStep = 1/self.vb.scale()#scaleStep
        self.vLine = InfiniteLine(angle=90, movable=False, pen = 'g')
        self.hLine = InfiniteLine(angle=0, movable=False, pen = 'g')
        self.Display = False
        self.index = None
        self.label = TextItem()
        self.data = data
        self.set_imScale(imScale)
        self.units = ''

        if Header is not None:
            self.header= Header

    def set_units(self, units):        
        self.units = units

    def setData(self,data):
            self.data = data

    def show(self):
        self.Display = True
        self.vb.addItem(self.vLine, ignoreBounds=True)
        self.vb.addItem(self.hLine, ignoreBounds=True)
        #self.vb.addItem(self.label)
        self.vLine.setZValue(10)
        self.hLine.setZValue(10)

    def set_imScale(self, imScale):
        if imScale is None:
            self.imScale = 1.0
        else:
            self.imScale = imScale
        #print 'imScale',self.imScale,     

    def hide(self):
        self.Display = False
        self.vb.removeItem(self.vLine)
        self.vb.removeItem(self.hLine)
        #self.vb.removeItem(self.label)
        self.header.setText("")

    def moved(self,evt):
        pos = evt  ## using signal proxy turns original arguments into a tuple
        if self.vb.sceneBoundingRect().contains(pos) and self.Display == True :
            mousePoint = self.vb.mapSceneToView(pos)
            self.index = [int(mousePoint.x()), int(mousePoint.y())]
            #print self.index
            self.vLine.setPos(mousePoint.x())
            self.hLine.setPos(mousePoint.y())
            #prints out position of image data at that point and view range of vb
            try:
                x = int(mousePoint.x()/self.imScale)
                y = int(mousePoint.y()/self.imScale)
                #print  mousePoint.x(),mousePoint.y(), x, y
                temp_strX = fn.siFormat(mousePoint.x(), suffix = 'm')

                temp_strY = fn.siFormat(mousePoint.y(), suffix = 'm')

                if x >= 0 and y >= 0:
                    data = self.data[x,y]
                    data_str = fn.siFormat(data, suffix = self.units)
                    #self.header.setText("x=%0.6f  y=%0.6f   [%e]" % (mousePoint.x(),mousePoint.y() , data), color = [0,200,0,255])
                    self.header.setText(temp_strX + '  ' + temp_strY +'  ' + data_str, color = [0,200,0,255])

                else:
                    self.header.setText("")
            except:
                data = 0
                #self.label.setText("x=%0.1f, y1=%0.1f, y2=%0.1f" % (mousePoint.x(),mousePoint.y() , 0.2))
                self.header.setText("")


class PlotROI(ROI):
    def __init__(self, size):
        ROI.__init__(self, pos=[0,0], size=size, removable = True) #, scaleSnap=True, translateSnap=True)
        self.addScaleHandle([1, 1], [0, 0])
        self.addRotateHandle([0, 0], [0.5, 0.5])


class SelROI(ROI):
    def __init__(self, vb, evt1 = None, evt2 = None, img = None, data = None, imScale = None ):
        self.vb = vb
        self.evt1 = evt1
        self.evt2 = evt2
        self.img = img
        self.data = data
        self.p1 = self.vb.mapSceneToView(evt1.scenePos())
        self.p2 = self.vb.mapSceneToView(evt2.scenePos())
        origin, size = self.cal_origin()
        self.Po = None
        self.bounds = None


        self.roi = RectROI( pos= origin, size = size, removable = True) #, scaleSnap=True, translateSnap=True)
        self.roi.addScaleHandle([1, 1], [0, 0])
        #self.roi.addRotateHandle([0, 0], [0.5, 0.5])
        self.roi.addScaleHandle([0,0],[1,1])
        self.roi.sigRemoveRequested.connect(self.hide)
        
        if (self.img is not None) and (self.data is not None):
            self.roi.sigRegionChangeFinished.connect(self.updateBounds)
            print 'should be connected'

        self.show()
        self.updateBounds()

    def updateBounds(self):
        """
        Used for figuring out where indexing is coming from  img is the imageItem data is the ndArray  
        """
        #print self.roi.boundingRect(), 'bounding Rect'
        #print self.roi.parentBounds(), '\n'
        if (self.img.__class__ != None) and (self.data.__class__ != None):
            self.bounds, tr = self.roi.getArraySlice(self.data, self.img, returnSlice = False)#, 'arraySlice'
            #print self.bounds, ' ROI bounds'
            self.Po = np.asarray([self.bounds[0][0], self.bounds[1][0]])# these are used as scan offsets
            self.xdelta = self.bounds[0][1] - self.bounds[0][0]# Width
            self.ydelta = self.bounds[1][1] - self.bounds[1][0]# Height of scan
            print self.Po, self.xdelta, self.ydelta
            return  self.Po, self.xdelta, self.ydelta

    def get_Po(self):
        return self.Po
    
    def get_xdelta(self):
        return self.xdelta

    def get_ydelta(self):
        return self.ydelta


    def cal_origin(self):
        """
        Compute the origin and size using QrectF functions getting the bottom left corner to use as the origin

        """
        r = QtCore.QRectF(self.p1, self.p2)
        center = r.center()
        r = r.normalized()
        r.moveCenter(center)
        origin = [r.topLeft().x(), r.topLeft().y()]
        size = [r.width(),r.height()] 
        print r.width(), r.height(), origin, size
        
        return origin, size


    def show(self):
        self.vb.addItem(self.roi, ignoreBounds = True)
        self.roi.setZValue(10)

    def hide(self):
        self.vb.removeItem(self.roi)




class LineSeg():
    """ 
    Make This a contanier for all line segments and have methods for creating more line segment 
    objects that take the arguments of the viewbox and events 
    ########Not USED YET#####

    """
    def __init__(self, vb, evt1 = None, evt2 = None):
        self.vb = vb
        p1 = self.vb.mapSceneToView(evt1.scenePos())
        p2 = self.vb.mapSceneToView(evt2.scenePos())

        self.L = LineSegmentROI((p1,p2), pen = 'r', removable = True)
        self.L.sigRemoveRequested.connect(self.hide)

    def show(self):
        self.vb.addItem(self.L, ignoreBounds = True)
        self.L.setZValue(10)

    def hide(self):
        self.vb.removeItem(self.L)


class LineReg():
    """
    Kind of works not called yet...
    """
    #Angle was inverted fixed it is ROI.......
    def __init__(self, vb, evt1 = None, evt2 = None, callback = None, imScale = None):
        self.vb = vb
        self.callback = callback
        self.Display = False
        #p1 = evt1.pos()
        #p2 = evt2.pos()
        p1 = self.vb.mapSceneToView(evt1.scenePos())
        p2 = self.vb.mapSceneToView(evt2.scenePos())
        self.set_imScale(imScale)
        #print p1, p2
        width = 2*self.imScale #TODO need to scale with image for it to work
        self.L = LineROI(p1, p2, width,pen = 'g', removable = True)
        self.L.sigRemoveRequested.connect(self.hide)
        

        if self.callback is not None:
            #Use signal PRoxy herre
            self.proxy = SignalProxy(self.L.sigRegionChanged, rateLimit=60, slot=callback)

            #self.proxy =    self.L.sigRegionChanged.connect(callback)

    def set_imScale(self, imScale):
        if imScale is None:
            self.imScale = 1.0
        else:
            self.imScale = imScale

    def show(self):
        self.Display = True
        self.vb.addItem(self.L, ignoreBounds = True)
        self.L.setZValue(10)
        self.callback()

    def hide(self):
        self.Display = False
        self.vb.removeItem(self.L)


class CrossMark():
    """
    Kind of works not called yet...
    """
    #Angle was inverted fixed it is ROI.......
    def __init__(self, vb, evt1, parent = None, imScale = None):
        self.vb = vb
        self.parent = parent
        self.set_imScale(imScale)
        p1 = self.vb.mapSceneToView(evt1.scenePos())
        self.CrX = CrosshairROI(pos = p1, size =[2*self.imScale,2*self.imScale], removable = True, pen = 'g')

        self.CrX.sigRemoveRequested.connect(self.clean)

        self.show()


    def set_imScale(self, imScale):
        if imScale is None:
            self.imScale = 1.0
        else:
            self.imScale = imScale

    def show(self):
        self.vb.addItem(self.CrX, ignoreBounds = True)
        self.CrX.setZValue(10)

    def hide(self):
        self.vb.removeItem(self.CrX)

    def clean(self):
        self.hide()
        self.parent.Items.remove(self)

class CrossMarks():
    """
    container for keeping track of crosss mark items
    """ 
    def __init__(self):
        self.Items = []

    def addMarker(self, vb, evt1, imScale = None):
        self.Items.append(CrossMark(vb, evt1, parent = self, imScale = imScale))


class ImageView_MOD(QtGui.QWidget):
    """
    Widget used for display and analysis of image data.
    Implements many features:
    
    * Displays 2D and 3D image data. For 3D data, a z-axis
      slider is displayed allowing the user to select which frame is displayed.
    * Displays histogram of image data with movable region defining the dark/light levels
    * Editable gradient provides a color lookup table 
    * Frame slider may also be moved using left/right arrow keys as well as pgup, pgdn, home, and end.
    * Basic analysis features including:
    
        * ROI and embedded plot for measuring image values across frames
        * Image normalization / background subtraction 
    
    Basic Usage::
    
        imv = pg.ImageView()
        imv.show()
        imv.setImage(data)
        
    **Keyboard interaction**
    
       """
    #sigTimeChanged = QtCore.Signal(object, object)
    sigProcessingChanged = QtCore.Signal(object)
    
    def __init__(self, parent=None, name="ImageView", view=None, imageItem=None, toolState = None, imageunits = '', *args):
        """
        By default, this class creates an :class:`ImageItem <pyqtgraph.ImageItem>` to display image data
        and a :class:`ViewBox <pyqtgraph.ViewBox>` to contain the ImageItem. 
        
        ============= =========================================================
        **Arguments** 
        parent        (QWidget) Specifies the parent widget to which
                      this ImageView will belong. If None, then the ImageView
                      is created with no parent.
        name          (str) The name used to register both the internal ViewBox
                      and the PlotItem used to display ROI data. See the *name*
                      argument to :func:`ViewBox.__init__() 
                      <pyqtgraph.ViewBox.__init__>`.
        view          (ViewBox or PlotItem) If specified, this will be used
                      as the display area that contains the displayed image. 
                      Any :class:`ViewBox <pyqtgraph.ViewBox>`, 
                      :class:`PlotItem <pyqtgraph.PlotItem>`, or other 
                      compatible object is acceptable.
        imageItem     (ImageItem) If specified, this object will be used to
                      display the image. Must be an instance of ImageItem
                      or other compatible object.
        ============= =========================================================
        
        Note: to display axis ticks inside the ImageView, instantiate it 
        with a PlotItem instance as its view::
                
            pg.ImageView(view=pg.PlotItem())
        """
        QtGui.QWidget.__init__(self, parent, *args)
        self.levelMax = 4096
        self.levelMin = 0
        self.name = name
        self.image = None
        self.axes = {}
        self.imageDisp = None
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        print parent, 'parent item'
        self.scene = self.ui.graphicsView.scene()

        #TM added
        self.toolState = toolState
        self.Line = None
        self.selROI = None
        #self.Markers = [] #List of markers
        self.Markers = CrossMarks()
        #TM Xhair label stuff
        self.Header = TextItem(border = 'k', fill= 'k')
        self.imScale = None
        
        self.ignoreTimeLine = False
        
        if view is None:
            self.view = ViewBox()
        else:
            self.view = view
        self.ui.graphicsView.setCentralItem(self.view)
        self.ui.graphicsView.addItem(self.Header)
        #self.Label.setText("blahh")
        self.view.setAspectLocked(True)
        #self.view.invertY()
        
        if imageItem is None:
            self.imageItem = ImageItem()
        else:
            self.imageItem = imageItem
        self.view.addItem(self.imageItem)
        #self.currentIndex = 0
        
        self.ui.histogram.setImageItem(self.imageItem)

        #self.ui.histogram.axis.linkToView(self.view)#TM add to update Si units???
        
        self.menu = None
        
        self.ui.normGroup.hide()

        #self.roi = PlotROI(10)
        #self.roi.setZValue(20)
        #self.view.addItem(self.roi)
        #self.roi.hide()
        self.normRoi = PlotROI(10)
        self.normRoi.setPen('y')
        self.normRoi.setZValue(20)
        self.view.addItem(self.normRoi)
        self.normRoi.hide()
        #TODO: can pass this too ROI objects???
        self.roiCurve = self.ui.roiPlot.plot()

        #TM set units of plot to distance 
        self.ui.roiPlot.setLabel('bottom', units = 'm')

        self.ui.splitter.setSizes([self.height()-35, 35])
        self.ui.roiPlot.hideAxis('left')
        
        
        self.normRgn = LinearRegionItem()
        self.normRgn.setZValue(0)
        self.ui.roiPlot.addItem(self.normRgn)
        self.normRgn.hide()
            
        ## wrap functions from view box
        for fn in ['addItem', 'removeItem']:
            setattr(self, fn, getattr(self.view, fn))

        ## wrap functions from histogram
        for fn in ['setHistogramRange', 'autoHistogramRange', 'getLookupTable', 'getLevels']:
            setattr(self, fn, getattr(self.ui.histogram, fn))

        #TM added
        if self.toolState is not None:
            #print toolState
            #add statements connets tooltracker and signals and define mouse behavior....
            self.proxy = SignalProxy(self.view.scene().sigMouseMoved, rateLimit=60, slot=self.mouseMove)
            self.view.scene().sigMouseClicked.connect(self.mouseClicked) 
            #self.view.scene().sigMouseMoved.connect(self.mouseMove)
        #Init Xhair with header
        self.Xhair = CrossHairs(self.view, Header = self.Header)#initial Xhair 

        #Grab signal from main UI and connect it to local objects...
        QtCore.QObject.connect(self.toolState.mainUI.Vis, QtCore.SIGNAL("toggled(bool)"), self.set_Vis)


        #self.timeLine.sigPositionChanged.connect(self.timeLineChanged)
        self.ui.roiBtn.clicked.connect(self.roiClicked)
        #self.roi.sigRegionChanged.connect(self.roiChanged)
        #TODO: add signal for line ...
        
        #self.ui.normBtn.toggled.connect(self.normToggled)
        self.ui.menuBtn.clicked.connect(self.menuClicked)
        #self.ui.normDivideRadio.clicked.connect(self.normRadioChanged)
        
        self.normProxy = SignalProxy(self.normRgn.sigRegionChanged, slot=self.updateNorm)
        self.normRoi.sigRegionChangeFinished.connect(self.updateNorm)
        
        self.ui.roiPlot.registerPlot(self.name + '_ROI')
        self.view.register(self.name)
        
        
        self.roiClicked() ## initialize roi plot to correct shape / visibility
        


        self.ScaleBar = None

        self.setScaleBar()


    def setScaleBar(self, size = 1):
        if self.ScaleBar is not None:
            self.ScaleBar.clear()
        self.ScaleBar = ScaleBar(size, width = 7.5)# ten times smallest feature
        self.ScaleBar.setParentItem(self.view)
        self.ScaleBar.anchor((1, 1), (0.75, 1), offset=(0,-10))

    def set_imScale(self, imScale):
        if imScale is None:
            self.imScale = 1.0
        else:
            self.imScale = imScale
        self.setScaleBar(self.image.shape[0]*self.imScale)# always set the scale bar when this function is called    


    def setUnits(self, units):
        self.units = units
        self.ui.histogram.axis.setLabel(units = self.units)
        self.ui.roiPlot.setLabel('left', units = self.units)
        self.Xhair.set_units(self.units)

    def setImage(self, img, autoRange=True, autoLevels=True, levels=None, axes=None, pos=None, scale=None, transform=None, autoHistogramRange=True):
        """
        Set the image to be displayed in the widget.
        
        ================== =======================================================================
        **Arguments:**
        img                (numpy array) the image to be displayed.
        xvals              (numpy array) 1D array of z-axis values corresponding to the third axis
                           in a 3D image. For video, this array should contain the time of each frame.
        autoRange          (bool) whether to scale/pan the view to fit the image.
        autoLevels         (bool) whether to update the white/black levels to fit the image.
        levels             (min, max); the white and black level values to use.
        axes               Dictionary indicating the interpretation for each axis.
                           This is only needed to override the default guess. Format is::
                       
                               {'t':0, 'x':1, 'y':2, 'c':3};
        
        pos                Change the position of the displayed image
        scale              Change the scale of the displayed image
        transform          Set the transform of the displayed image. This option overrides *pos*
                           and *scale*.
        autoHistogramRange If True, the histogram y-range is automatically scaled to fit the
                           image data.
        ================== =======================================================================
        """
        profiler = debug.Profiler()
        
        if hasattr(img, 'implements') and img.implements('MetaArray'):
            img = img.asarray()
        
        if not isinstance(img, np.ndarray):
            required = ['dtype', 'max', 'min', 'ndim', 'shape', 'size']
            if not all([hasattr(img, attr) for attr in required]):
                raise TypeError("Image must be NumPy array or any object "
                                "that provides compatible attributes/methods:\n"
                                "  %s" % str(required))
        
        self.image = img
        self.imageDisp = None
        if scale is not None:
            #print scale[0]
            self.set_imScale(scale[0]) #reuse scale for imScale for other functions
        
        #profiler()
        
      

        self.currentIndex = 0
        self.updateImage(autoHistogramRange=autoHistogramRange)
        if levels is None and autoLevels:
            self.autoLevels()
        if levels is not None:  ## this does nothing since getProcessedImage sets these values again.
            self.setLevels(*levels)
            
        if self.ui.roiBtn.isChecked():
            self.roiChanged()

        #profiler()

        self.imageItem.resetTransform()
        if scale is not None:
            self.imageItem.scale(*scale)
        if pos is not None:
            self.imageItem.setPos(*pos)
        if transform is not None:
            self.imageItem.setTransform(transform)

        #profiler()

        if autoRange:
            self.autoRange()
        self.roiClicked()

        #profiler()
        
        #TODO fix scale bar
        #self.ScaleBar.updateBar()# show scale bar

    def clear(self):
        self.image = None
        self.imageItem.clear()
             
    def autoLevels(self):
        """Set the min/max intensity levels automatically to match the image data."""
        self.setLevels(self.levelMin, self.levelMax)

    def setLevels(self, min, max):
        """Set the min/max (bright and dark) levels."""
        self.ui.histogram.setLevels(min, max)

    def autoRange(self):
        """Auto scale and pan the view around the image such that the image fills the view."""
        image = self.getProcessedImage()
        self.view.autoRange()

    def getProcessedImage(self):
        """Returns the image data after it has been processed by any normalization options in use.
        This method also sets the attributes self.levelMin and self.levelMax 
        to indicate the range of data in the image."""
        if self.imageDisp is None:
            image = self.image
            self.imageDisp = image
            self.levelMin, self.levelMax = list(map(float, self.quickMinMax(self.imageDisp)))
            
        return self.imageDisp
        
        
    def close(self):
        """Closes the widget nicely, making sure to clear the graphics scene and release memory."""
        self.ui.roiPlot.close()
        self.ui.graphicsView.close()
        self.scene.clear()
        del self.image
        del self.imageDisp
        self.setParent(None)

 
    def normRadioChanged(self):
        self.imageDisp = None
        self.updateImage()
        self.autoLevels()
        self.roiChanged()
        self.sigProcessingChanged.emit(self)
    
    def updateNorm(self):
        if self.ui.normTimeRangeCheck.isChecked():
            self.normRgn.show()
        else:
            self.normRgn.hide()
        
        if self.ui.normROICheck.isChecked():
            self.normRoi.show()
        else:
            self.normRoi.hide()
        
        if not self.ui.normOffRadio.isChecked():
            self.imageDisp = None
            self.updateImage()
            self.autoLevels()
            self.roiChanged()
            self.sigProcessingChanged.emit(self)

    def normToggled(self, b):
        self.ui.normGroup.setVisible(b)
        self.normRoi.setVisible(b and self.ui.normROICheck.isChecked())
        self.normRgn.setVisible(b and self.ui.normTimeRangeCheck.isChecked())

    def roiClicked(self):
        #TM modify this function to work with Line ROI
        showRoiPlot = False
        if self.ui.roiBtn.isChecked():
            showRoiPlot = True
            #self.roi.show()
            #self.ui.roiPlot.show()
            self.ui.roiPlot.setMouseEnabled(True, True)
            self.ui.splitter.setSizes([self.height()*0.6, self.height()*0.4])
            self.roiCurve.show()
            self.roiChanged()
            self.ui.roiPlot.showAxis('left')
        else:
            #self.roi.hide()
            self.ui.roiPlot.setMouseEnabled(False, False)
            self.roiCurve.hide()
            self.ui.roiPlot.hideAxis('left')
            
        self.ui.roiPlot.setVisible(showRoiPlot)

    def roiChanged(self):
        if self.image is None:
            return
    
        if self.Line is None:
            return
            
        image = self.getProcessedImage()
        if image.ndim == 2:
            axes = (0, 1)
        elif image.ndim == 3:
            axes = (1, 2)
        else:
            return
        #data, coords = self.roi.getArrayRegion(image.view(np.ndarray), self.imageItem, axes, returnMappedCoords=True)
        # switch this too Line
        if self.Line.Display is True:
            data, coords = self.Line.L.getArrayRegion(image.view(np.ndarray), self.imageItem, axes, returnMappedCoords=True)

            if data is not None:
                while data.ndim > 1:
                    data = data.mean(axis=1)
                if image.ndim == 3:
                    self.roiCurve.setData(y=data, x=self.tVals)
                else:
                    while coords.ndim > 2:
                        coords = coords[:,:,0]
                    coords = coords - coords[:,0,np.newaxis]
                    xvals = (coords**2).sum(axis=0) ** 0.5
                    self.roiCurve.setData(y=data, x=xvals)

    def quickMinMax(self, data):
        """
        Estimate the min/max values of *data* by subsampling.
        """
        while data.size > 1e6:
            ax = np.argmax(data.shape)
            sl = [slice(None)] * data.ndim
            sl[ax] = slice(None, None, 2)
            data = data[sl]
        return nanmin(data), nanmax(data)



    def updateImage(self, autoHistogramRange=True):
        ## Redraw image on screen
        if self.image is None:
            return
            
        image = self.getProcessedImage()

        if self.Xhair.Display == True:
            self.Xhair.setData(image)
        
        if autoHistogramRange:
            self.ui.histogram.setHistogramRange(self.levelMin, self.levelMax)
            #self.ui.histogram.axis.updateAutoSIPrefix()#see if this cahnges values
            #self.ui.histogram.axis.setLabel(units = 'A')
            self.imageItem.updateImage(image)
            #self.ScaleBar.updateBar()# just added TM see if it will paint after update 
        else:
            self.ui.roiPlot.show()
            self.imageItem.updateImage(image)
            #self.ScaleBar.updateBar()
            
            

    def getView(self):
        """Return the ViewBox (or other compatible object) which displays the ImageItem"""
        return self.view
        
    def getImageItem(self):
        """Return the ImageItem for this ImageView."""
        return self.imageItem
        
    def getRoiPlot(self):
        """Return the ROI PlotWidget for this ImageView"""
        return self.ui.roiPlot
       
    def getHistogramWidget(self):
        """Return the HistogramLUTWidget for this ImageView"""
        return self.ui.histogram

    def export(self, fileName):
        """
        Export data from the ImageView to a file, or to a stack of files if
        the data is 3D. Saving an image stack will result in index numbers
        being added to the file name. Images are saved as they would appear
        onscreen, with levels and lookup table applied.
        """
        img = self.getProcessedImage()
        if self.hasTimeAxis():
            base, ext = os.path.splitext(fileName)
            fmt = "%%s%%0%dd%%s" % int(np.log10(img.shape[0])+1)
            for i in range(img.shape[0]):
                self.imageItem.setImage(img[i], autoLevels=False)
                self.imageItem.save(fmt % (base, i, ext))
            self.updateImage()
        else:
            self.imageItem.save(fileName)
            
    def exportClicked(self):
        fileName = QtGui.QFileDialog.getSaveFileName()
        if fileName == '':
            return
        self.export(fileName)
        
    def buildMenu(self):
        self.menu = QtGui.QMenu()
        self.normAction = QtGui.QAction("Normalization", self.menu)
        self.normAction.setCheckable(True)
        self.normAction.toggled.connect(self.normToggled)
        self.menu.addAction(self.normAction)
        self.exportAction = QtGui.QAction("Export", self.menu)
        self.exportAction.triggered.connect(self.exportClicked)
        self.menu.addAction(self.exportAction)
        
    def menuClicked(self):
        if self.menu is None:
            self.buildMenu()
        self.menu.popup(QtGui.QCursor.pos())
    
    def mouseClicked(self, evt):
        """
        Define Behavior of Tool interaction with ROI and plots    
        """
        if evt.button() == QtCore.Qt.LeftButton:
            #print evt.pos(), evt.scenePos(), self.view.mapSceneToView(evt.scenePos())

            if self.toolState.lineState == True:
                #print "yesss Lines"
                self.toolState.set_ClickState(evt)
                #check to see if we create a line
                if self.toolState.ClickState == 2:
                    #TM this will changes once we can handle multiple lines well
                    if self.Line != None:
                        self.Line.hide()
                    self.Line = LineReg(self.view, evt1 = self.toolState.firstClickEvt, evt2 = self.toolState.secondClickEvt, 
                    callback = self.roiChanged, imScale = self.imScale)
                    self.toolState.clearClick()
                    self.view.rbScaleBox.hide()
                    self.Line.show()

            elif self.toolState.rectROIState == True:
                #print "Rectsss"
                self.toolState.set_ClickState(evt)
                #self.toolState.firstClickPos = evt.pos()
                if (self.toolState.ClickState == 2):
                    if (self.selROI != None):
                        self.selROI.hide()
                    self.selROI = SelROI(self.view, evt1 = self.toolState.firstClickEvt, evt2 = self.toolState.secondClickEvt, 
                    data = self.image, img = self.imageItem, imScale = self.imScale)   # create selROI 
                    self.toolState.clearClick()
                    self.view.rbScaleBox.hide()

            elif self.toolState.roiCrossState == True:  
                #print "roiCRossss"    
                #self.toolState.set_ClickState()
                #self.Markers.append(CrossMark(self.view, evt))
                self.Markers.addMarker(self.view, evt, imScale = self.imScale) #TODO add imScale here too

    def mouseMove(self, evt):
        """
        activate tooltracker
        """
        evt = evt[0]
        if self.toolState.ClickState == 1:
            self.view.updateScaleBox(self.toolState.firstClickEvt.pos(), evt)


        #Stuff for Xhair to show or not
        if self.toolState.viewXhair == True:
            if self.Xhair.Display == False:
                self.Xhair.show()
                self.Xhair.setData(self.image)
            self.Xhair.set_imScale(self.imScale) # make sure Xhair has imScale
            self.Xhair.moved(evt)
        elif self.toolState.viewXhair == False:
            if self.Xhair.Display == True:
                self.Xhair.hide()

    def set_Vis(self):

        if self.toolState.mainUI.Vis.isChecked() == True:
            self.ShowObjects()
        if self.toolState.mainUI.Vis.isChecked() == False:
            self.HideObjects()

    def HideObjects(self):
        if self.Line is not None:
            self.Line.hide()
        if self.selROI is not None:    
            self.selROI.hide()
        if self.Markers.Items.__len__() > 0:
            for temp in self.Markers.Items:
                #temp = self.Markers[i]
                temp.hide()
        
    def ShowObjects(self):
        if self.Line is not None:
            self.Line.show()
        if self.selROI is not None:    
            self.selROI.show()
        if self.Markers.Items.__len__() > 0:
            for temp in self.Markers.Items:
                temp.show()
         



    #TODO create function for creating and adding view and removeing them handle multiple lines
