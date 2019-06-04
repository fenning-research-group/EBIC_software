import scanobject
import Mfigure
import scipy.ndimage as nd


from mayavi.mlab import *

Scan = scanobject.scanObjectUtils.load_scanobject("../data/BNL_Si_PV/2ndpieceAsi5kvtilt45_x2.scan")
EB = Scan.DisplayArray[:,:,1]
Gaus = nd.gaussian_filter(EB,3, order = 0)

surf(Gaus*-1e6, warp_scale ='auto', colormap = "YlOrRd", vmin = 3, vmax = 5.33 )
