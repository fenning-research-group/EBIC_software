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


scale =1e-6


class CustomViewBox(pg.ViewBox):
    def __init__(self, *args, **kwds):
        pg.ViewBox.__init__(self, *args, **kwds)
        self.setMouseMode(self.RectMode)
        
    ## reimplement right-click to zoom out
    def mouseClickEvent(self, ev):
        if ev.button() == QtCore.Qt.RightButton:
            self.autoRange()
            
    def mouseDragEvent(self, ev):
        if ev.button() == QtCore.Qt.RightButton:
            ev.ignore()
        else:
            pg.ViewBox.mouseDragEvent(self, ev)








vb = CustomViewBox(lockAspect=True, invertY = False, invertX = False)

L = pg.LineSegmentROI([[110*scale,5*scale],[5*scale,5*scale]], pen = 'r')

#cross hair
vLine = pg.InfiniteLine(angle=90, movable=False, pen = 'g')
hLine = pg.InfiniteLine(angle=0, movable=False, pen = 'g')
img = pg.ImageItem()

roi = pg.ROI([8*scale, 14*scale], [6*scale, 5*scale])
roi.addScaleHandle([0.5, 1], [0.5, 0.5])
roi.addScaleHandle([0, 0.5], [0.5, 0.5])
vb.addItem(roi)
roi.setZValue(10)

vb.addItem(img)
vb.addItem(vLine, ignoreBounds=True)
vb.addItem(hLine, ignoreBounds=True)
vb.addItem(L, ignoreBounds = True)

# Generate image data
data = np.random.normal(size=(100, 100))
data[20:80, 20:80] += 2.
data = pg.gaussianFilter(data, (3, 3))
data += np.random.normal(size=(100, 100)) * 0.1
img.setImage(data)
img.scale(scale,scale)
#hist.setLevels(data.min(), data.max())


scaleStep = 1.0/scale



     

l.addItem(vb, 1, 1)
gv.centralWidget.setLayout(l)


scale = pg.ScaleBar(size = 20*scale, pen = 'w' )#offset = (-20,-20))
scale.setParentItem(vb)
scale.anchor((1,1),(1,1), offset =(-500,-20))


def mouseMoved(evt):
    pos = evt[0]  ## using signal proxy turns original arguments into a tuple
    if vb.sceneBoundingRect().contains(pos):
        mousePoint = vb.mapSceneToView(pos)
        index = int(mousePoint.x())
        vLine.setPos(mousePoint.x())
        hLine.setPos(mousePoint.y())
        #prints out position of image data at that point and view range of vb
        print int(scaleStep*mousePoint.x()), int(scaleStep*mousePoint.y()),data[int(scaleStep*mousePoint.x()),int(scaleStep*mousePoint.y())], vb.viewRange()


proxy = pg.SignalProxy(vb.scene().sigMouseMoved, rateLimit=60, slot=mouseMoved)
#p1.scene().sigMouseMoved.connect(mouseMoved)
## Start Qt event loop unless running in interactive mode.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
