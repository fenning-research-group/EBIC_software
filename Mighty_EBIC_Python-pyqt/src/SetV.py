
import socket
import time
import struct
import numpy
import sys

# address of the BeagleBone DMX
IP = "10.0.1.8"
PORT = 5009



def constructPayload(V1 = 15000, V2 = -15000, CTRL = 0b11):

    V1 = numpy.int16(V1)
    V2 =  numpy.int16(V2)
    CTRL= numpy.int16(CTRL)
    
    res = "%8x" %0x10f1
    res += "%8x"%V1	
    res += "%8x"%V2
    res += "%8x"%CTRL
    
    return res


def SendV(V1 =20000, V2=-20000, CTRL = 0b11):
  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
  sock.connect((IP, 9930))

  payload = constructPayload(V1, V2, CTRL)
  print payload
  sock.send(payload)
  sock.close()


if __name__ == "__main__":

    SendV()
