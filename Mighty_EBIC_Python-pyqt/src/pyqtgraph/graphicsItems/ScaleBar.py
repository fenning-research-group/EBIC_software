from ..Qt import QtGui, QtCore
from .GraphicsObject import *
from .GraphicsWidgetAnchor import *
from .TextItem import TextItem
import numpy as np
from .. import functions as fn
from .. import getConfigOption
from ..Point import Point

__all__ = ['ScaleBar']

class ScaleBar(GraphicsObject, GraphicsWidgetAnchor):
    """
    Displays a rectangular bar to indicate the relative scale of objects on the view.
    """
    def __init__(self, size, width=5, brush= 'w', pen='k', suffix='m', offset=None):
        GraphicsObject.__init__(self)
        GraphicsWidgetAnchor.__init__(self)
        self.setFlag(self.ItemHasNoContents)
        self.setAcceptedMouseButtons(QtCore.Qt.NoButton)
        
        if brush is None:
            brush = getConfigOption('foreground')
        self.brush = fn.mkBrush(brush)
        self.pen = fn.mkPen(pen)
        self._width = width
        self.size = size# not the best coding practice
        self.set_Size(size)
        if offset == None:
            offset = (0,0)
        self.offset = offset
        
        self.bar = QtGui.QGraphicsRectItem()
        self.bar.setPen(self.pen)
        self.bar.setBrush(self.brush)
        self.bar.setParentItem(self)
        
        self.text = TextItem(text=fn.siFormat(self.size, suffix=suffix), anchor=(0.5,1), color = 'w', fill = None)
        self.text.setParentItem(self)


    def parentChanged(self):
        view = self.parentItem()
        if view is None:
            return
        #view.sigRangeChanged.connect(self.updateBar)
        #view.sigRangeChangedManually.connect(self.updateBar)
        #view.sigResized.connect(self.updateBar) # TM No effect
        view.sigStateChanged.connect(self.updateBar)
        #print 'Update Bar'
        #self.updateBar()
        
        
    def updateBar(self):
        view = self.parentItem()
        if view is None:
            return
        #    
        p1 = view.mapFromViewToItem(self, QtCore.QPointF(0,0))
        p2 = view.mapFromViewToItem(self, QtCore.QPointF(self.size,0))
        w = (p2-p1).x()

        #view.checkSceneChange()# see if it repainted since last time
        #w =100
        #TM
        #print w, p1, p2, self.size
        self.bar.setRect(QtCore.QRectF(-w, 0, w, self._width))
        self.text.setPos(-w/2., 0)


    def boundingRect(self):
        return QtCore.QRectF()

    def setParentItem(self, p):
        ret = GraphicsObject.setParentItem(self, p)
        if self.offset is not None:
            offset = Point(self.offset)
            anchorx = 1 if offset[0] <= 0 else 0
            anchory = 1 if offset[1] <= 0 else 0
            anchor = (anchorx, anchory)
            self.anchor(itemPos=anchor, parentPos=anchor, offset=offset)

        #TM self.updateBar()    
        return ret

    def clear(self):
        view = self.parentItem() 
        view.removeItem(self.bar)
        view.removeItem(self.text)


    def set_Size(self,distance, scale = None, percent=25):
        """
        returns the size of the scale bar to be approximately a fixed percentage of the view that is closest to 
        1,5,10,20,25,50,75,100
        """
        temp = 1
        fraction = percent/100.0
        if scale is None:
            (scalar, prefix) =fn.siScale(distance)

            temp = distance*scalar#int(np.log10(distance/100))
            #print temp
            scale = 1/scalar

        size = temp*fraction#(distance/scale)*fraction
        seq= [500,200,100,75,50,25,20,15,10,5,4,3,2,1]
        ssize = size
        for i in seq:
            result, rem = divmod(size,i)
            #print i,  result, rem
            if result > 0:
                ssize = i
                break
        self.size = ssize*scale
        return ssize, scale
