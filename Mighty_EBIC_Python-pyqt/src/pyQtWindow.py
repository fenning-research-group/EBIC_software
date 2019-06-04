# -*- coding: utf-8 -*-
"""
This example demonstrates the creation of a plot with a customized
AxisItem and ViewBox. 
"""

import sys
import os
CWD = os.getcwd()
PWD = os.pardir
sys.path.append(CWD +'/proto_Code')
sys.path.append(PWD)

import os.path


#import initExample ## Add path to library (just for examples; you do not need this)
import src.pyqtgraph as pg
#import pyqtgraph as pg
from src.pyqtgraph.Qt import QtCore, QtGui
import numpy as np
import time


class CustomViewBox(pg.ViewBox):
    def __init__(self, *args, **kwds):
        pg.ViewBox.__init__(self, *args, **kwds)
        self.setMouseMode(self.RectMode)
        self.enableAutoRange()
        
    ## reimplement right-click to zoom out
    def mouseClickEvent(self, ev):
        if ev.button() == QtCore.Qt.RightButton:
            self.autoRange()
            
    def mouseDragEvent(self, ev):
        if ev.button() == QtCore.Qt.RightButton:
            ev.ignore()
        else:
            pg.ViewBox.mouseDragEvent(self, ev)



class CrossHairs():
    
    def __init__(self, vb, scaleStep):
        self.vb = vb
        self.scaleStep = 1/self.vb.scale()#scaleStep
        self.vLine = pg.InfiniteLine(angle=90, movable=False, pen = 'g')
        self.hLine = pg.InfiniteLine(angle=0, movable=False, pen = 'g')
        self.Display = False
        self.proxy = pg.SignalProxy(self.vb.scene().sigMouseMoved, rateLimit=60, slot=self.mouseMoved)
        #self.pro = pg.SignalProxy(self.vb.scene().sigMouseClicked, rateLimit=60, slot=self.mouseClicked)
        #self.vb.scene().sigMouseClicked.connect(self.mouseClicked)
        self.index = None

        #self.show()

    #def __getitem__(self):
    #    return

    def show(self):
        self.Display = True
        self.vb.addItem(self.vLine, ignoreBounds=True)
        self.vb.addItem(self.hLine, ignoreBounds=True)
        self.vLine.setZValue(10)
        self.hLine.setZValue(10)
        

    def hide(self):
        self.Display = False
        self.vb.removeItem(self.vLine)
        self.vb.removeItem(self.hLine)
        
        #self.proxy = pg.SignalProxy(self.vb.scene().sigMouseMoved, rateLimit=60, slot=self.mouseMoved)
    def mouseMoved(self,evt):
        pos = evt[0]  ## using signal proxy turns original arguments into a tuple
        if self.vb.sceneBoundingRect().contains(pos) and self.Display == True :
            mousePoint = self.vb.mapSceneToView(pos)
            self.index = [int(mousePoint.x()), int(mousePoint.y())]
            self.vLine.setPos(mousePoint.x())
            self.hLine.setPos(mousePoint.y())
            #prints out position of image data at that point and view range of vb
            print int(self.scaleStep*mousePoint.x()), int(self.scaleStep*mousePoint.y())

    def mouseClicked(self, evt):        
        #print evt.pos(), evt.scenePos(), self.vb.mapSceneToView(evt.scenePos())
        return

class LineSeg():
    def __init__(self, vb, scale):
        self.vb = vb
        self.scale  = self.vb.scale()
        self.L = pg.LineSegmentROI([[110*scale,5*scale],[5*scale,5*scale]], pen = 'r')

    def show(self):
        self.vb.addItem(self.L, ignoreBounds = True)
        self.L.setZValue(10)

    def hide(self):
        self.vb.removeItem(self.L)


class ROI_Rec():
    def __init__(self, vb, scale):
        self.vb = vb
        self.scale = self.vb.scale()
        self.roi = pg.ROI([20*scale, 20*scale], [40*scale, 40*scale])#removable = True)
        self.roi.addScaleHandle([0.5, 1], [0.5, 0.5])
        self.roi.addScaleHandle([0, 0.5], [0.5, 0.5])

    def show(self):    
        self.vb.addItem(self.roi)
        self.roi.setZValue(10)

    def hide(self):
        self.vb.removeItem(self.roi)
