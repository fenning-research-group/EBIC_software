#!/usr/bin/env python
from __future__ import with_statement

import numpy
import scipy
import scipy.ndimage
import h5py
import Mfigure
import math
import pylab
import lineProfile
#import EbicCommandManager
import time
#import EbicPythonCommandsAuto
import EbicDataManager
#import WriteToHdf5
import scanUpdate, edm
import thread, Queue
import config
import scanobject

#import sys
import numpy
#from pylab import *
from scipy import mgrid
from time import strftime




#import plotActions
#import regionOfInterest

# used to parse files more easily
#from __future__ import with_statement

# Numpy module
import numpy as np


# for command-line arguments
import sys

# Qt4 bindings for core Qt functionalities (non-GUI)
from PyQt4.QtCore import*
# Python Qt4 bindings for GUI objects
from PyQt4.QtGui import*

# import the MainWindow widget from the converted .ui files
from qtdesigner import Ui_MplMainWindow

from reCenterSlice import Ui_ReCenter_Slice

class ReCenterSliceUI(QMainWindow,Ui_ReCenter_Slice):

    def __init__(self, parent = None, scan = None, callback = None, mainUI = None):
        Ui_ReCenter_Slice.__init__(self)
        QMainWindow.__init__(self)
        #super(Ui_profiler, self).__init__()
        # I don't know why this doesn't work for dialogs but found answer here:
        #http://www.nanoengineer-1.net/mediawiki/index.php?title=Qt_4_mysteries#Pyuic4_hiccups
        self.setupUi(self) 
        self.activeSlice = None
        self.mainUI = mainUI
        self.activeCh = 0
        self.scan = scan
        self.callback = callback
        self.ParentName.setText(self.scan.name)
        self.ColorMap.addItems(pylab.cm._cmapnames)
        self.cmap = pylab.cm.afmhot
        self.cmapindex = 0
        self.update_view_Ch_index()
        self.update_ref_Ch_index()
        self.point = 1


        self.refCH = 0
        self.margin = 10
        self.axis = 1
        self.Gaus = 2


        #self.delay= float(str(self.Delay.text()))

        #slots
        QObject.connect(self.addSlice, SIGNAL("clicked()"), self.temp_slice_append_to_scan)
        QObject.connect(self.viewCH_comboBox, SIGNAL("currentIndexChanged(int)"), self.update_activeCH)
        QObject.connect(self.set_margin, SIGNAL("valueChanged(int)"), self.update_Margin)
        QObject.connect(self.referenceCH, SIGNAL("currentIndexChanged(int)"), self.update_ReferenceCH)
        QObject.connect(self.sobelAxis, SIGNAL("valueChanged(int)"), self.update_Axis)
        QObject.connect(self.saveSlice, SIGNAL("clicked()"), self.save_slice)
        QObject.connect(self.ColorMap, SIGNAL("currentIndexChanged(int)"), self.change_cmap)
        QObject.connect(self.rColorMap, SIGNAL("stateChanged(int)"), self.set_reverse_cmap)
        QObject.connect(self.colorbar, SIGNAL("stateChanged(int)"), self.set_colorbar)
        QObject.connect(self.filterBox, SIGNAL("valueChanged(int)"), self.set_filter_point)
        QObject.connect(self.Filter, SIGNAL("stateChanged(int)"), self.set_filter)


        self.set_tempSlice()


    def update_view_Ch_index(self):
        for i in range(0,self.scan.channelCount):
            self.viewCH_comboBox.addItem(str(i))

    def update_ref_Ch_index(self):
        for i in range(0,self.scan.channelCount):
            self.referenceCH.addItem(str(i))

    def getboundsFromMain(self):
        """
        gets the bounds of the scan from main    
        """
        if self.mainUI != None:
            self.tempSlice.sourceExtent =  self.mainUI.scanTracker.figTracker.activeCh.canvas.ax.viewLim.extents
            print "bounds from main:", self.tempSlice.sourceExtent


    def change_cmap(self, value):
        self.cmapindex = value
        self.cmap = pylab.cm._cmapnames[self.cmapindex]
        if self.rColorMap.isChecked() == True:
            self.cmap =pylab.cm._cmapnames[value]+'_r'
        self.show_image()

    def set_reverse_cmap(self, value):
        self.change_cmap(self.cmapindex)

    def set_colorbar(self, value):
        self.change_cmap(self.cmapindex)

    def set_filter(self,value):
        self.change_cmap(self.cmapindex)

    def set_filter_point(self, value):
        self.point = int(value)
        self.set_tempSlice()
        


    def show_image(self):
        self.widget.canvas.oneSubPlot()
        self.data = self.tempSlice.DisplayArray[:,:,self.activeCh]

        if self.Filter.isChecked() == True:
            self.data = self.tempSlice.GausDisplayArray[:,:,self.activeCh]

        self.im = self.widget.canvas.ax.imshow(self.data ,extent = self.tempSlice.extent, cmap = self.cmap , origin = "lower")
        self.widget.canvas.ax.yaxis.set_tick_params(direction='out')#, length=6, width=2, colors='k')
        self.widget.canvas.ax.xaxis.set_visible(False)
        if self.colorbar.isChecked() == True:
            self.cbar = self.widget.canvas.fig.colorbar(self.im, ax = self.widget.canvas.ax , orientation = 'vertical')
    
            self.cbar.ax.yaxis.set_tick_params(direction = 'out')
        print 'did it work????'    
        self.widget.canvas.draw()


    def set_tempSlice(self):
        """
        gets called anytime anything changes in field name, margin, reference channel etc...
        """
        self.tempSlice = scanobject.reCenterSlice(self.scan, name = str(self.SliceName.text()) )
        self.tempSlice.point = self.point
        self.getboundsFromMain()
        self.tempSlice.reCenter(RefCH = self.refCH, margin = self.margin, sobelAxis = self.axis, Gaus_distance = self.Gaus)
        self.show_image()


    def temp_slice_append_to_scan(self):
        self.tempSlice.name = str(self.SliceName.text()) 
        self.scan.slices.append(self.tempSlice)
        if self.callback != None:
            self.callback()
  
    def save_slice(self):
        """
        saves the slice
        """
        scanobject.scanObjectUtils.pickle_scanobject(self.tempSlice , '../data/' + self.tempSlice.name + ',' + self.tempSlice.scan.name[1:] + '.slc')


    def update_activeCH(self, value):
        self.activeCh = value
        self.show_image()

    def update_ReferenceCH(self, value):
        self.refCH = value
        self.set_tempSlice()

    def update_Margin(self, value):
        self.margin = value
        self.set_tempSlice()

    def update_Axis(self, value):
        self.axis = value
        self.set_tempSlice()


    def update_Gaus_filter(self ,value):
        self.Gaus = value
        self.set_tempSlice()






