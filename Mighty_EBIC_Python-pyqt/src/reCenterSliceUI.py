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
import EbicCommandManager
import time
import EbicPythonCommandsAuto
import EbicDataManager
import WriteToHdf5
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

from reCenterSlice import Ui_Dialog

class ReCenterSliceUI(QDialog, Ui_Dialog):

    def __init__(self, parent = None, scan = None, callback = None):
        Ui_Dialog.__init__(self)
        QDialog.__init__(self)
        #super(Ui_profiler, self).__init__()
        # I don't know why this doesn't work for dialogs but found answer here:
        #http://www.nanoengineer-1.net/mediawiki/index.php?title=Qt_4_mysteries#Pyuic4_hiccups
        self.setupUi(self) 
        self.activeSlice = None
        self.activeCh = 0
        self.scan = scan
        self.callback = callback
        self.ParentName.setText(self.scan.name)
        self.update_view_Ch_index()
        self.update_ref_Ch_index()

        self.refCH = 0
        self.margin = 20
        self.axis = 1


        #self.delay= float(str(self.Delay.text()))

        #slots
        QObject.connect(self.addSlice, SIGNAL("clicked()"), self.temp_slice_append_to_scan)
        QObject.connect(self.viewCH_comboBox, SIGNAL("currentIndexChanged(int)"), self.update_activeCH)
        QObject.connect(self.set_margin, SIGNAL("valueChanged(int)"), self.update_Margin)
        QObject.connect(self.referenceCH, SIGNAL("currentIndexChanged(int)"), self.update_ReferenceCH)
        QObject.connect(self.sobelAxis, SIGNAL("valueChanged(int)"), self.update_Axis)


        self.set_tempSlice()


    def update_view_Ch_index(self):
        for i in range(0,self.scan.channelCount):
            self.viewCH_comboBox.addItem(str(i))

    def update_ref_Ch_index(self):
        for i in range(0,self.scan.channelCount):
            self.referenceCH.addItem(str(i))



    def show_image(self):
        self.widget.canvas.ax.clear()
        self.widget.canvas.ax.imshow(self.tempSlice.DisplayArray[:,:,self.activeCh])
        self.widget.canvas.ax.yaxis.set_tick_params(direction='out')#, length=6, width=2, colors='k')
        self.widget.canvas.ax.xaxis.set_visible(False)
        print 'did it work????'    
        self.widget.canvas.draw()

    def set_tempSlice(self):
        """
        gets called anytime anything changes in field name, margin, reference channel etc...
        """
        self.tempSlice = scanobject.reCenterSlice(self.scan, name = str(self.SliceName.text()) )
        self.tempSlice.reCenter(bounds = None, SEChannel = self.refCH, margin = self.margin, sobelAxis = self.axis)
        self.show_image()


    def temp_slice_append_to_scan(self):
        self.tempSlice.name = str(self.SliceName.text()) 
        self.scan.slices.append(self.tempSlice)
        if self.callback != None:
            self.callback()
        
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

