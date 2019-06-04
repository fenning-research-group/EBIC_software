import scanobject
import Mfigure


from mayavi.mlab import *

Scan = scanobject.scanObjectUtils.load_scanobject("../data/BNL_Si_PV/2ndpieceAsi5kvtilt45_x2.scan")
EB = Scan.DisplayArray[:,:,1]
surf(EB*1e6, warp_scale ='auto')
