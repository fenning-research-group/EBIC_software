#classes to export files to csv and other formats
import numpy
import scanobject
from scanobject import*

class Exporter:



    #TODO: make smarter and just be able to pass an object and have it export that data
    #with headings for each channel    
    def __init__(self):
        return

    def export_csv(self, name = None, header = None, data = None):
        newfile = name + '.csv'
        f = open(newfile, 'w')
        if header != None:
            f.write(header)
        if data is not None:
            if data.__class__  == list:
                for i in range(len(data)):
                    numpy.savetxt(f,data[i], delimiter = ',', fmt= '%1.4e')
                    f.write('\n')
            else : 
                numpy.savetxt(f,data, delimiter = ',', fmt= '%1.4e')
        f.close()

    def make_header(self, scanObject, index = None):
        if scanObject.__class__ == scanobject.Scan :
            labels = 'label: ' + scanObject.labels[index] + '\t'
            units = 'units: ' + scanObject.units[index] + '\t'
            name = 'scan name:' + scanObject.name + '\t'
            gain = 'gain: ' + str(scanObject.gain[index]) + '\t'
            extent = 'extent: ' + str(scanObject.extent) +'(units in microns)' + '\t'
            Ch = 'channel: '+ str(index) + '\t'
            created = 'created:' + scanObject.created + '\t'
            header = name + Ch + created + labels + units + gain + extent + '\n'
            return header
        elif scanObject.__class__ == scanobject.Profile :
            startpoint = 'startpoint: ' + str(scanObject.startpoint) + '\t'
            endpoint = 'endpoint:' + str(scanObject.endpoint) + '\t'
            units = 'units: ' + scanObject.units[index] + '\t'
            name = 'scan name:' + scanObject.name + '\t'
            gain = 'gain: ' + str(scanObject.gain[index]) + '\t'
            #created = 'created:' + scanObject.created + '\t'
            header = name + units + gain + startpoint + endpoint + '\n'
            return header
        elif scanObject.__class__ == scanobject.Transport:
            created = 'created' + str(scanObject.created) + '\t'
            delay = 'delay'  + str(scanObject.delay) + '\t'
            gain = 'gain'  + str(scanObject.gain)  + '\t'
            header = created + delay + gain + '\n'
            return header
        else:
            print 'ohno no header'
        
        
