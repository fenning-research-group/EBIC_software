import pickle

#Results of a sample calibration from PNNL visit kept here for as a note TODO: remove!
#        self.testmag=14000
#        self.testStepSize=127
#        self.rangeOfPoints = 2**16.0
#        self.hMagScale=(self.rangeOfPoints/(self.testStepSize*54.))*self.testmag # (max points/(number of points in 1 micron at resolution))* test Mag  
#        self.vMagScale=(self.rangeOfPoints/(self.testStepSize*74.6))*self.testmag
#        self.aspectRatio= self.vMagScale/ self.hMagScale


def setCalibration(testmag = 1000  , testStepSizeH = 127 , 
                    testStepSizeV = 127, knownDistanceH = 1, knownDistanceV = 1, 
                    pointsH = 100, pointsV = 100 , hMax = 32767, hMin = -32767, vMax = 32767, vMin = -32767 ):

    rangeOfPoints = 0xffff

    #knownDistance should be in microns
    #units are in (distance*mag)/(16 DAC range)  
    hMagScale=(testmag*float(knownDistanceH))/(testStepSizeH*pointsH)
    vMagScale=(testmag*float(knownDistanceV))/(testStepSizeV*pointsV) 

    aspectRatio= vMagScale/hMagScale
    cal = dict([('testmag',testmag),( 'testStepSizeH', testStepSizeH),( 'testStepSizeV', testStepSizeV),( 'knownDistanceH', knownDistanceH),
                 ('knownDistanceV', knownDistanceV), ('pointsH', pointsH), ('pointsV', pointsV), ('aspectRatio', aspectRatio), 
                 ('hMagScale', hMagScale), ('vMagScale', vMagScale), ('hMax', hMax), ('hMin',hMin), ('vMax', vMax) ,('vMin', vMin) ])        


    f = open('calibration.mcal', 'wb')
    pickle.dump(cal,f)
    f.close()

    return cal


def getCalibration():

    f = open('calibration.mcal', 'rb')
    cal = pickle.load(f)
    f.close()

    return cal


#TODO: add in other function to handle other profile configurations, possibly a library of different microscopes and basic configs
#def microscopeConfiguration():

    
