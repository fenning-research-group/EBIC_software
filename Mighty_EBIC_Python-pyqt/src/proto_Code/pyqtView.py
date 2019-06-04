import numpy as np
import sys
import os
os.chdir("..")
CWD = os.getcwd()
PWD = os.pardir
sys.path.append(CWD +'/proto_Code')
sys.path.append(PWD)

import os.path



from src.pyqtgraph.Qt import QtGui, QtCore
import src.pyqtgraph as pg

app = QtGui.QApplication([])
mw = QtGui.QMainWindow()
mw.setWindowTitle('pyqtgraph example: ViewBox')
mw.show()
mw.resize(800, 600)

gv = pg.GraphicsView()
mw.setCentralWidget(gv)
l = QtGui.QGraphicsGridLayout()
l.setHorizontalSpacing(0)
l.setVerticalSpacing(0)


scale =1


class CustomViewBox(pg.ViewBox):
    def __init__(self, *args, **kwds):
        pg.ViewBox.__init__(self, *args, **kwds)
        self.setMouseMode(self.RectMode)

        
    ## reimplement right-click to zoom out
    def mouseClickEvent(self, ev):
        if ev.button() == QtCore.Qt.RightButton:
            self.autoRange()
            #print 'k'
            
    def mouseDragEvent(self, ev):
        if ev.button() == QtCore.Qt.RightButton:
            ev.ignore()
        else:
            pg.ViewBox.mouseDragEvent(self, ev)




class CrossHairs():
    
    def __init__(self, vb, scaleStep):
        self.vb = vb
        self.scaleStep = scaleStep
        self.vLine = pg.InfiniteLine(angle=90, movable=False, pen = 'g')
        self.hLine = pg.InfiniteLine(angle=0, movable=False, pen = 'g')
        self.Display = False

    #def __getitem__(self
    #    return

    def show(self):
        self.Display = True
        self.vb.addItem(self.vLine, ignoreBounds=True)
        self.vb.addItem(self.hLine, ignoreBounds=True)
        self.vLine.setZValue(10)
        self.hLine.setZValue(10)
        
        self.proxy = pg.SignalProxy(self.vb.scene().sigMouseMoved, rateLimit=60, slot=self.mouseMoved)


    def mouseMoved(self,evt):
        pos = evt[0]  ## using signal proxy turns original arguments into a tuple
        if self.vb.sceneBoundingRect().contains(pos) and self.Display == True :
            mousePoint = self.vb.mapSceneToView(pos)
            #index = int(mousePoint.x())
            self.vLine.setPos(mousePoint.x())
            self.hLine.setPos(mousePoint.y())
            #prints out position of image data at that point and view range of vb
            print int(self.scaleStep*mousePoint.x()), int(self.scaleStep*mousePoint.y())# data[int(self.scaleStep*mousePoint.x()),int(self.scaleStep*mousePoint.y())] 
            #print self.vb.viewRange()





#vb = CustomViewBox(lockAspect=True, invertY = False, invertX = False)
vb = pg.ViewBox(lockAspect=True) #TM scale bar behaves differently with this enablaed updates if dragged

l.addItem(vb, 1, 1)
gv.centralWidget.setLayout(l)


#SB.size = 20*scale

L = pg.LineSegmentROI([[100*scale,0*scale],[5*scale,5*scale]], pen = 'r')

#cross hair
#vLine = pg.InfiniteLine(angle=90, movable=False, pen = 'g')
#hLine = pg.InfiniteLine(angle=0, movable=False, pen = 'g')
img = pg.ImageItem()

roi = pg.ROI([50*scale, 50*scale], [10*scale, 10*scale])
roi.addScaleHandle([0.5, 1], [0.5, 0.5])
roi.addScaleHandle([0, 0.5], [0.5, 0.5])
vb.addItem(roi)
roi.setZValue(10)

vb.addItem(img)
#vb.addItem(vLine, ignoreBounds=True)
#vb.addItem(hLine, ignoreBounds=True)
vb.addItem(L, ignoreBounds = True)

Xhair = CrossHairs(vb, 1.0/scale)


Xhair.show()



# Generate image data
data = np.random.normal(size=(100, 100))
data[20:80, 20:80] += 2.
data = pg.gaussianFilter(data, (3, 3))
data += np.random.normal(size=(100, 100)) * 0.1
img.setImage(data)
img.scale(scale,scale)
#hist.setLevels(data.min(), data.max())


#scaleStep = 1.0/scale



     


SB = pg.ScaleBar(size = 10*scale, pen = 'w', offset = [-200,-10])
SB.setParentItem(vb)


#vb.addItem(scale)
#scale.anchor((1,1),(1,1), offset =(-40,-20),)




## Start Qt event loop unless running in interactive mode.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
