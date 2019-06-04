import numpy
import scipy
import pylab

angle = 0 #in degrees
rad = numpy.radians(angle)
r =  5 #resolution of scan
Pfast = 100
Pslow = 300

dx = r*numpy.cos(rad)
dy = r*numpy.sin(rad)


Sx = 0
Sy = 0

X = []
Y = []

fastVector =[dx,dy]
slowVector =[dx,-dy]


pAxFast =20
pAxSlow =10

for c in range(pAxSlow):
        Fx = Sx
        Fy = Sy
        for i in range(pAxFast):
                X.append(Fx)
                Y.append(Fy)
                Fx = Fx + dx
                Fy = Fy + dy

        Sx = Sx + dx
        Sy = Sy - dy

pylab.plot(X ,Y, "bo")
pylab.show()


