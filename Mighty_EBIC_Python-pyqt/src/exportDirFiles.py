#!/usr/bin/env python
from __future__ import with_statement
import sys
import os
CWD = os.getcwd()
PWD = os.pardir
sys.path.append(CWD +'/proto_Code')
sys.path.append(CWD)
sys.path.append(PWD)

import os.path
import scanobject
from Mexport import Exporter

IP = "10.0.1.8"
PORT = 9930


def export_scan2(scan,expDataPath):
    # scan = self.scanTracker.activeScan
    chArr=[0,1];
    for ch_index in chArr:
        display_scan = scan.DisplayArray[:,:,ch_index]
        export = Exporter()
        header = export.make_header(scan, ch_index)
        name = expDataPath + scan.name + 'scan_ch' + str(ch_index)
        export.export_csv(name = name, header = header, data = display_scan)
        header = ''
        name = ''


# To export files in a given directory
outputDirs="/Volumes/GoogleDrive/My Drive/EBIC/ucla_xc/dataRaw/cho/20190602_cho26"
rawDataPath = "/Volumes/GoogleDrive/My Drive/EBIC/ucla_xc/dataExported/cho/20190603"
files = os.listdir(outputDirs);
counter = 1;
for ebicfile in files:
    fileExt = '.scan'
    if fileExt in ebicfile:
        filePath = outputDirs + '/' + ebicfile
        scanFile = scanobject.scanObjectUtils.load_scanobject(filePath)
        tempname = filePath[filePath.rfind('/'):]
        scanFile.name = tempname
        counter = counter + 1;
        export_scan2(scanFile,rawDataPath)
        # print('finish exporting '+ ebicfile)
print('counter is',counter)
