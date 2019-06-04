
import socket
import time
import struct
import numpy
import pylab
import sys
import CCNT_test
from CCNT_test_unit import *
import Queue
import threading

# address of the BeagleBone DMX
IP = "10.0.1.8"
PORT = 5009


buf_size = 4096
#data =[]

# can just us numpy.int16 to take care of 2's complement
#easily scan in every direction
dt = numpy.dtype('uint32')

#my attempt at using a queue
q = Queue.Queue()

TF_I = CCNT_test.TF_index

#pF = 2047#0x800
#pS = 2047#0x800
#sF = pS
#samp = 100
#CH = 1


samp =numpy.int16(100)
CH = numpy.int16(1)
Count= numpy.int16(400)










#TF, TF_state, pF, pS, samp, CCNT, resizeDim = CCNT_test.set_CCNT(pF = pF,pS = pS, CH = CH , samp = samp)
CCNT = CH*samp

resizeDim = (samp,CH)
count = 0

storedArray = numpy.zeros([Count, samp, CH], numpy.int32)
print "storedArray", storedArray.shape

header_max = Count#TF
print header_max


def test_scanSize():
    temp = 1
    for i in resizeDim:
        temp = i*temp

    #assert TF*temp == pF*pS*samp*CH
    return temp

def constructPayload():
    #bit shift
    OS_0 = 2
    OS_1 = 3
    OS_2 = 5

    #extract bits
    OS0 = 0b001
    OS1 = 0b010
    OS2 = 0b100
    OSI = 3


    if OSI > 0:
        OS_value = int(numpy.log2(OSI))
    else:
        OS_value = OSI
    print "OS_valuen", bin(OS_value)

    nStep = numpy.int16(-50)
    pStep =  numpy.int16(50)
    Count= numpy.int16(400)
    Start= numpy.int32(0)
    Stop = numpy.int16(0)
    Min = numpy.int16(0)
    Max = numpy.int16(200)
    STEP = numpy.int16(50)
    samp =numpy.int16(100)
    CH = numpy.int16(1)
    DVAR = numpy.uint32(1000)
    OS = numpy.uint16(2)


    OS =  ((OS_value & OS2) >> 2) << OS_2 | ((OS_value & OS1) >> 1) << OS_1 | (OS_value & OS0) << OS_0 
    print "OS", OS
    XFER = CH << 16 | ((CH*4) -1) << 8
    
    print "XFER",XFER
    # make sure pF is integer multiple of CCNT

    print "CCNT",CCNT
    #print "pF",pF

    #header_max = pF/CCNT * sF 
    #print header_max

  

    res = "%8x" %0xa011
    res += "%8x"%nStep	
    res += "%8x"%pStep
    res += "%8x"%Count
    res += "%8x"%Start
    res += "%8x"%Stop
    res += "%8x"%Min
    res += "%8x"%Max
    res += "%8x"%STEP
    res += "%8x"%samp
    res += "%8x"%CH
    res += "%8x"%DVAR
    res += "%8x"%OS
    res += "%8x"%XFER
    res += "%8x"%CCNT
    

    return res


def loop():
  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
  sock.connect((IP, 9930))

  #while True:
  payload = constructPayload()
  print payload
  sock.send(payload)
  sock.close()



def RX_loop():
    #time.sleep(1)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
    sock.bind(("",PORT))
    datacount = CH*samp
    print datacount
    count = 0
    #loop()


    while True:
    
        data = sock.recv(buf_size)

        #TODO: do I need a buffer and handle puting into the array else where sperate thread??
        
        header = numpy.frombuffer(data, dtype = dt, count = 1, offset = 4)
        if header[0] > header_max:
            break


        #Grab data from buff keep sign shift remaing data back print values
        X = numpy.frombuffer(data, dtype = dt, count = datacount, offset = 16)
        #typecast to keep sign
        Copy = numpy.int32(X << 14)
        #shift data back to proper space
        #now we have signed 18bit data represented as signed int32
        Z = Copy >> 14   #15 to get data back to its place but keep the sign
        #data is always zero indexed




        #xindex , sub_xindex, yindex, samp_index, sub_samp_index = TF_I(TF, TF_state, pF = pF, pS = pS, samp = samp, CCNT= CCNT, header = header, resizeDim = resizeDim)

        

        #sub_data_array = sim_data.test_reshape(Z,CCNT, samp,CH, TF_state = TF_state)

        

def dump_loop(dump,datacount):
    #time.sleep(1)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
    sock.settimeout(3) #tried timeout will continue until data is done
    sock.bind(("",PORT))
    #datacount = test_scanSize()
    print "data count",datacount
    count = 0
    #loop()
   
    #dump = []
    Hmax = 0

    while True:
        try:
            data = (sock.recv(buf_size))
            count = count + 1
        except socket.error as msg:
            sock.close()
            print "error", msg
            break
            
        if not data: 
            print "no data"
            break
        dump.append(data)
        q.put(data)
        header = numpy.frombuffer(data, dtype = dt, count = 1, offset = 4)
        if header[0] == header_max:
            print "header max", header[0]
            break
        if header[0] > header_max:
            Hmax = Hmax + 1 #print"header max greater than"
            break
            print "data length", len(dump)    

    print "length of dump",len(dump)
    print "queue maxsize", q.qsize()
    sock.close()

    #sortToImage(dump,datacount)
    return Hmax, count




def sortToImage(dump, datacount):
    """
    if header is in range put it into the image else go to the next one

    """
    #print dump
    header_dump =[]
    Hmax = 0
    for i in range(len(dump)):
        try:
            data = dump.pop(-1)
            header = numpy.frombuffer(data, dtype = dt, count = 1, offset = 4)
            ping = numpy.frombuffer(data, dtype = dt, count = 1, offset = 8)
            pong = numpy.frombuffer(data, dtype = dt, count = 1, offset = 12)
        except:
            header_dump.append(data)
                
        if header[0] <= header_max:

            #print "header", header, '\n'
        #Grab data from buff keep sign shift remaing data back print values
            X = numpy.frombuffer(data, dtype = dt, count = datacount, offset = 16)
        #typecast to keep sign
            Copy = numpy.int32(X << 14)
        #shift data back to proper space
        #now we have signed 18bit data represented as signed int32

            Z = Copy >> 14   #15 to get data back to its place but keep the sign

            #xindex , sub_xindex, yindex, samp_index, sub_samp_index = TF_I(TF, TF_state, pF = pF, pS = pS, samp = samp, CCNT= CCNT, header = header, resizeDim = resizeDim)

            
        

            #sub_data_array = sim_data.test_reshape(Z,CCNT, samp,CH, TF_state = TF_state)

            #print header, ping, pong, xindex, sub_xindex, yindex, Z.max(), Z.min(),"\n",Z, '\n'


            #put_inP(storedArray,sub_data_array, xindex, sub_xindex, yindex, samp_index, sub_samp_index, TF_state, resizeDim)
        else:
            Hmax = Hmax + 1
            
    print "Hmax", Hmax
    for k in range(CH):

        print storedArray[:,:,:,k].mean()
        pylab.imshow(numpy.average(storedArray[:,:,:,k], axis = 2))

        #pylab.imshow(storedArray[:,:,0,k])
        pylab.colorbar()
        pylab.show()

        #pylab.imshow(storedArray[:,:,1,k])
        #pylab.colorbar()
        #pylab.show()




def get_data_from_q(q, datacount):
    """
    if header is in range put it into the image else go to the next one

    """
    #print dump
    header_dump =[]
    Hmax = 0
    while True:
        try:
            data = q.get()
            header = numpy.frombuffer(data, dtype = dt, count = 1, offset = 4)
            ping = numpy.frombuffer(data, dtype = dt, count = 1, offset = 8)
            pong = numpy.frombuffer(data, dtype = dt, count = 1, offset = 12)
        except:
            header_dump.append(data)
                
        if header[0] <= header_max:

            #print "header", header, '\n'
        #Grab data from buff keep sign shift remaing data back print values
            X = numpy.frombuffer(data, dtype = dt, count = datacount, offset = 16)
        #typecast to keep sign
            Copy = numpy.int32(X << 14)
        #shift data back to proper space
        #now we have signed 18bit data represented as signed int32

            Z = Copy >> 14   #15 to get data back to its place but keep the sign

            #xindex , sub_xindex, yindex, samp_index, sub_samp_index = TF_I(TF, TF_state, pF = pF, pS = pS, samp = samp, CCNT= CCNT, header = header, resizeDim = resizeDim)

            
            #sub_data_array = numpy.reshape(Z, resizeDim, order = 'C')
        

           # sub_data_array = sim_data.test_reshape(Z,CCNT, samp,CH, TF_state = TF_state)

            print header, ping, pong, Z.max(), Z.min(),"\n"#,Z, '\n'


            #put_inP(storedArray,sub_data_array, xindex, sub_xindex, yindex, samp_index, sub_samp_index, TF_state, resizeDim)
        else:
            Hmax = Hmax + 1

        if header[0] == header_max:
            break
            







if __name__ == "__main__":

    loop()
    #RX_loop()
    dump = []
    #Hmax, count = dump_loop(dump)
    datacount = CH*samp#test_scanSize()
    Producer = threading.Thread(target = dump_loop, args = (dump,datacount))

    Consumer = threading.Thread(target = get_data_from_q, args =(q, datacount))
    Consumer.start()
    Producer.start()

    while Producer.is_alive():
        time.sleep(1) 
             
    #sortToImage(dump, datacount)    

    print "final length of dump",len(dump)
    #print "headers max", Hmax, "count total", count
    

