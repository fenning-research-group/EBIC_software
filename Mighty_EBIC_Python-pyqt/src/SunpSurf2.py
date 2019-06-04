import scanobject
import Mfigure
import scipy.ndimage as nd
import numpy


from mayavi.mlab import *

Scan = scanobject.scanObjectUtils.load_scanobject("../data/SunP/7_14_SP10kvcleavedx1.scan")
EB = Scan.DisplayArray[:,:,1]
SE = Scan.DisplayArray[:,:,0]
EB = numpy.fliplr(EB)

SE = numpy.fliplr(SE)
Gaus = nd.gaussian_filter(EB,1, order = 0)
G_se = nd.gaussian_filter(SE,2, order = 0) 
surf(Gaus*-1e9, warp_scale ='auto', colormap = "YlOrRd", vmin =0 , vmax = 3 )
surf(G_se, warp_scale ='auto', colormap = "gist_gray")#, vmin =0.1 , vmax = 100 )

