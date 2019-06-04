import sys, os, math, scipy, h5py, numpy
from time import strftime



def writeHdf5(BulkdataArray, savename):

	CH1 = BulkdataArray
	#print CH1.shape
	#Then save to hdf5
	filename = strftime("%Y-%m-%d_%H-%M-%S")
	Z = savename + filename +'.hdf5'
	f = h5py.File(Z, 'w')
	dset1 = f.create_dataset('CH1', data=CH1)

	f.close()
	print "Data saved to" + Z
	#return BulkdataArray.shape

	#shutil.copy2(src, dst)
