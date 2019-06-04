# -*- coding: utf-8 -*-
from __future__ import division
import sys
from os import path
sys.path.append('/home/mightyebic/Mighty_EBIC_Python/src/proto_Code/')
import numpy as np
import decimal, re
import ctypes
import struct


#SI_PREFIXES = asUnicode('yzafpnµm kMGTPEZY')
SI_PREFIXES_ASCII = 'yzafpnum kMGTPEZY'


def get_Size(distance, scale = None, percent=25):
    """
    returns the size of the scale bar to be approximately a fixed percentage of the view that is closest to 
    1,5,10,20,25,50,75,100
    """
    fraction = percent/100.0
    if scale is None:
        (scalar, prefix) =siScale(distance)

        temp = distance*scalar#int(np.log10(distance/100))
        print temp
        #if abs(temp) > 6 and temp < 0:
        #if distance/10**(temp) > 1000
        #else :
        #scale = 10**temp
        #print scale    
        scale = 1/scalar

    size = temp*fraction#(distance/scale)*fraction
    seq= [500,200,100,75,50,25,20,15,10,5,4,3,2,1]
    ssize = size
    for i in seq:
        result, rem = divmod(size,i)
        print i,  result, rem
        if result > 0:
            ssize = i
            break
        
    return ssize, scale

def siScale(x, minVal=1e-25, allowUnicode=False):
    """
    Return the recommended scale factor and SI prefix string for x.
    
    Example::
    
        siScale(0.0001)   # returns (1e6, 'μ')
        # This indicates that the number 0.0001 is best represented as 0.0001 * 1e6 = 100 μUnits
    """
    
    if isinstance(x, decimal.Decimal):
        x = float(x)
        
    try:
        if np.isnan(x) or np.isinf(x):
            return(1, '')
    except:
        print(x, type(x))
        raise
    if abs(x) < minVal:
        m = 0
        x = 0
    else:
        m = int(np.clip(np.floor(np.log(abs(x))/np.log(1000)), -9.0, 9.0))
    
    if m == 0:
        pref = ''
    elif m < -8 or m > 8:
        pref = 'e%d' % (m*3)
    else:
        if allowUnicode:
            pref = SI_PREFIXES[m+8]
        else:
            pref = SI_PREFIXES_ASCII[m+8]
    p = .001**m
    
    return (p, pref)    
