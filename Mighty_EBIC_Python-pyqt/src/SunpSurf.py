import scanobject
import Mfigure
import scipy.ndimage as nd
import numpy


from mayavi.mlab import *

Scan = scanobject.scanObjectUtils.load_scanobject("../data/SunP/7_14_SP10kvionMx8.scan")
EB = Scan.DisplayArray[:,:,1]
EB = numpy.fliplr(EB)
Gaus = nd.gaussian_filter(EB,1, order = 0)

surf(Gaus*-1e9, warp_scale ='auto', colormap = "YlOrRd", vmin =0.1 , vmax = 100 )
#surf(EB*-1e9, warp_scale ='auto', colormap = "YlOrRd", vmin =0.1 , vmax = 100 )

