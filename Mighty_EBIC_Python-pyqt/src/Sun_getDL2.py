import numpy as np
import scipy
import numpy.ma
import sys
sys.path.append('/home/mightydev2/Mighty_EBIC_Python/src/')
import os.path
import scanobject
import matplotlib.pyplot as plt
from scipy import stats


directory=  os.getcwd()


Scan = scanobject.scanObjectUtils.load_scanobject("../data/7_14_SP10kvionMx11.scan")
pro = Scan.profiles[0]

EB = pro.profileData[:,:,1]

print EB.shape

print EB.max()

EB= EB/EB.max()
X = pro.Xposition[127:149]
Xp = pro.Xposition[162:222]
Xp2 = pro.Xposition[222:300]
EB_lp = np.log(EB[162:222,0])
EB_l = np.log(EB[127:149,0])
EB_lp2 = np.log(EB[222:300,0])

slope_p, intercept_p, r_value_p, p_value_p, std_err_p = stats.linregress(Xp, EB_lp)
predict_yp = intercept_p + slope_p * Xp

slope_p2, intercept_p2, r_value_p2, p_value_p2, std_err_p2 = stats.linregress(Xp2, EB_lp2)
predict_yp2 = intercept_p2 + slope_p2 * Xp2


slope_n, intercept_n, r_value_n, p_value_n, std_err_n = stats.linregress(X, EB_l)
predict_y = intercept_n + slope_n * X

F = np.exp((X-X[-1])/(1/slope_n))
LF = (np.log(F))


#print "1/slope n", "{:.2f}".format(np.abs(1/slope_n)), "1/slope_p", "{:.2f}".format(np.abs(1/slope_p))

print slope_n, slope_p

print pro.Xposition.shape
#set to white background ...
plt.axes(axisbg='w')
plt.rc('axes', fc = 'w')
LEB=np.abs(np.log(EB[:,0]))

plt.plot(pro.Xposition, LEB, 'b.', markersize = 3, )

#plt.plot(pro.Xposition, np.log(EB[:,0]), 'b', )
#plt.plot(Xp,predict_yp,'r--', linewidth = 2.5, label = "Lp"+" {:.2f}".format(np.abs(1/slope_p)),)

#plt.plot(Xp2,predict_yp2,'m--', linewidth = 2.5, label = "Lp*"+" {:.2f}".format(np.abs(1/slope_p2)),)

#plt.plot(X,predict_y,'g--', linewidth = 2.5, label = "Ln"+" {:.2f}".format(np.abs(1/slope_n)),)
#plt.plot(X,LF,'c', linewidth = 2.5,)# label = "Ln"+" {:.2f}".format(1/slope_n),)
#plt.xlim(0,20)
plt.xlabel("Microns")
plt.ylabel("Log of EBIC profile")
#plt.legend(loc = 1)
plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
plt.savefig("10kvDLSunx11_lglg.pdf", format = 'pdf') # can also save as a tif see docstring
plt.show()

"""

#plot EBIC image

plt.plot(pro.Xposition, pro.profileData[:,:,1], 'b.', markersize = 3)
plt.ticklabel_format(style = 'sci', scilimits = (0,0), axis = 'y')
plt.ylabel("EBIC Current")
plt.xlabel("Microns")
plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
#plt.xlim(0,20)
plt.savefig("10kvEBprofileSunx11.pdf", format = 'pdf') # can also save as a tif see docstring
plt.show()


    # get the array from the channel
EB = Scan.DisplayArray[:,:,1]    
    #Mask zeros values
EB_nZ= numpy.ma.masked_equal(EB, 0.0)
plt.imshow(EB_nZ, extent = Scan.extent, origin = 'lower',\
    cmap = 'gist_yarg_r', vmax = 2.3*EB_nZ.max(), vmin = EB_nZ.min() )
#plt.tight_layout()
plt.plot([pro.startpoint[0], pro.endpoint[0]], [pro.startpoint[1], pro.endpoint[1]])
plt.tight_layout()
plt.colorbar(format = '%.2e')
plt.savefig("10kvEBSunPx11.pdf", format = 'pdf', dpi = 600) # can also save as a tif see docstring
plt.show()

SE = Scan.DisplayArray[:,:,0]    
plt.imshow(SE, extent = Scan.extent, origin = 'lower',cmap = 'gist_yarg_r')
plt.plot([pro.startpoint[0], pro.endpoint[0]], [pro.startpoint[1], pro.endpoint[1]])
plt.tight_layout()
plt.savefig("10kvSESunPx11.pdf", format = 'pdf', dpi = 600) # can also save as a tif see docstring
plt.show()
"""
