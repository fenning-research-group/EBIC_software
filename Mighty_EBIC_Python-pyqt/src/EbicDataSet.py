#TODO this doesn't seem to be in use Get rid of this file....
import array
"""
class EbicScanData():
	
	rawData = None
	xSize = 0
	ySize = 0
	sampleDepth = 0
	chCount = 0
	
	def __init__(self,xSize,ySize,sampleDepth,chCount):
		 self.rawData = array.array('h')
		 self.xSize = xSize
		 self.ySize = ySize
		 self.sampleDepth = sampleDepth
		 self.chCount = chCount
		
	def append(self, inArray):
		if( len(self.rawData) + len(inArray) > self.expected_data_size() ):
		     print 'this is more data than we expect. We have %d are receiving %d, and expect %d' \
		           % (len(self.rawData),len(inArray), self.expected_data_size() )		     
		self.rawData += inArray
		
	def expected_data_size(self):
		return (self.xSize * self.ySize * self.sampleDepth  * self.chCount)


if __name__ == "__main__":
	   'generic main'
	   #data = EbicScanData(16,16,16,16)
	   #data.append( array.array('h',(12,12,12,12)) )
	   #print data

"""
