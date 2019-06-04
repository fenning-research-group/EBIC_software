#!/usr/bin/env python
import sys, os, serial, threading, Queue, Tkinter, tkMessageBox, math, scipy, struct, h5py, numpy
from pylab import *
from scipy import mgrid
from time import strftime


def avg(l):
	a = 0;
	for i in l:
		a = a + i
	return a/len(l)

def flattenTo2d( inputDataSet):
	#reshape to an N,M instead of an N,M,1 array

	if(len(inputDataSet.shape) > 2 or inputDataSet.shape[2] == 1):
		tmp = numpy.zeros((inputDataSet.shape[0],inputDataSet.shape[1]), numpy.int32)
		for x in range(0,len(tmp)):
			for y in range(0,len(tmp[x])):	
				tmp[x][y] = avg(inputDataSet[x][y])
		print tmp.shape
		#print tmp
		return tmp


if __name__ == "__main__":
	if(len(sys.argv) > 1):
		print "Opening %s" % sys.argv[1]	
		f = h5py.File(sys.argv[1],'r')
	else: 
		print "opening default file"	
		f = h5py.File('ebictestdata2010-07-19_15-52-13.hdf5','r')

	
	dset1 = f["CH1"]
	#dset2 = f["Secondary"]

	EBIC = dset1[:,:,:,0]
	SE = dset1[:,:,:,1]
	#print EBIC.shape
	print dset1.shape


	EBIC = flattenTo2d(EBIC)
	SE = flattenTo2d(SE)

# Axis Range for Plot  (not data size, display size)
	xMax = 10
	xMin = 0
	yMax = 10
	yMin = 0

#Matplotlib poltting of stored hdf5 Files
#ToDo eaxmine datasets so files can be readback with out knowing their size 
 
	figure(1)
	imshow(EBIC, cmap=cm.gray, origin='upper', extent=[xMin, xMax, yMin, yMax])	title('EBIC ')
	xlabel('Position in microns')
	ylabel('Position in microns')
	axis('scaled')
	colorbar()
	#show()


	figure(2)
	imshow(SE, cmap=cm.gray, origin='upper', extent=[xMin, xMax, yMin, yMax])	title('Secondary Electron')
	xlabel('Position in microns')
	ylabel('Position in microns')
	axis('scaled')
	colorbar()
	show() # necessary to display the plots

print "Hello"

