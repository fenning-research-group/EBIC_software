import sys, time
import threading
import pylab

import sys
import os
CWD = os.getcwd()
sys.path.append(CWD +'/proto_Code')
sys.path.append(CWD)
import os.path


from src import pyqtgraph as pg
#from qt import *
import pyQtWindow
import numpy
#import pyqtView
from PyQt4 import QtCore, QtGui

class ScanUpdate(QtCore.QThread):

    def __init__(self,parent, mpl, img, displayArray, channel, scanFlag, extent ):
        QtCore.QThread.__init__(self,parent)
        #threading.Thread.__init__(self)
        self.mpl = mpl
        self.parent = parent
        #self.IView = IView
        self.extent = extent
        self.displayArray = displayArray
        self.channel = channel
        self.counter = 0
        self.scanFlag = scanFlag
        self.img = img


                
    def run(self):
        self.mpl.canvas.ax.clear()

        while self.displayArray[0] is None:
            time.sleep(0.2)
            pass

        self.emit(QtCore.SIGNAL("setup_mpl()"))
         
        while 1:
            self.msleep(500)
            #time.sleep(0.5)

            if self.scanFlag[0] is True:
                print "scan Flag true"
                break


            #new  for Pyqtgraph
            self.emit(QtCore.SIGNAL("update_img()"))

            self.emit(QtCore.SIGNAL("update_mpl()"))

            self.counter = self.counter +1
            

        #Wait then update on last time to make sure everything is plotted        

        self.msleep(200)
        self.emit(QtCore.SIGNAL("update_img()"))

        #update mpl
        self.emit(QtCore.SIGNAL("update_mpl()"))


class ProgressBarUpdate(QtCore.QThread):
    """
    Update the progress bar and nothing else, Uses Qthread to send signal

    """

    def __init__(self,parent,scanFlag):
        QtCore.QThread.__init__(self,parent)
        self.parent = parent
        self.scanFlag = scanFlag

    #timer and update stuff
    def run(self):

        while 1:
            #emit update signal every 500 msecs
            self.msleep(500)
            self.emit(QtCore.SIGNAL("update()"))#updates progress bar

            if self.scanFlag[0] == True: #stop updating when scan finishes
                print "Progress done"
                break
        self.msleep(200)
        self.terminate()


class TransUpdate(threading.Thread):
    #TODO Make a Qthread instead send signals to parent 

    def __init__(self, mpl, scanFlag, Transport = None):
        self.mpl = mpl
        self.scanFlag = scanFlag
        self.transport = Transport
        threading.Thread.__init__(self)

    def run(self):
        while self.scanFlag[0] != True:
            while len(self.transport.dataIstd) == 0:
                time.sleep(0.2)
            time.sleep(1)
            self.mpl.canvas.ax.clear()
            self.mpl.canvas.ax.errorbar(self.transport.sentVoltage, self.transport.dataI,  yerr = self.transport.dataIstd)
            self.mpl.canvas.draw()
        
