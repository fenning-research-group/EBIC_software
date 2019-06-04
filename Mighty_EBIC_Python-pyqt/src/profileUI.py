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

from profileDialog import Ui_profiler

class ProfileUI(QDialog, Ui_profiler):

    def __init__(self, parent = None, scan = None, callback = None):
        Ui_profiler.__init__(self)
        QDialog.__init__(self)
        #super(Ui_profiler, self).__init__()
        # I don't know why this doesn't work for dialogs but found answer here:
        #http://www.nanoengineer-1.net/mediawiki/index.php?title=Qt_4_mysteries#Pyuic4_hiccups
        self.setupUi(self) 
        self.activeprofile = None
        self.activeCh = 0
        self.scan = scan
        self.callback = callback
        self.ParentName.setText(self.scan.name)

        #slots
        QObject.connect(self.addprofile, SIGNAL("clicked()"), self.temp_profile_append_to_scan)
        QObject.connect(self.viewCH_comboBox, SIGNAL("currentIndexChanged(int)"), self.update_activeCH)

        #initializing combobox
        self.update_view_Ch_index()

    def update_view_Ch_index(self):
        for i in range(0,self.scan.channelCount):
            self.viewCH_comboBox.addItem(str(i))

    def plot_profile(self):
        self.widget.canvas.ax.plot(self.temp_profile.Xposition, self.temp_profile.profileDataAvg[:,self.activeCh])
        self.widget.canvas.ax.grid()
        self.widget.canvas.draw()

    def set_tempprofile(self, temp_profile):
        self.temp_profile = temp_profile


    def temp_profile_append_to_scan(self):
        self.temp_profile.name = str(self.ProfileName.text()) 
        self.scan.profiles.append(self.temp_profile)
        if self.callback != None:
            self.callback()
        
    def update_activeCH(self, value):
        self.activeCh = value
        self.widget.canvas.ax.clear()
        self.plot_profile()

