import numpy



def make_pk(CCNT,samp,ch, TF_state = None):
    """
    Makes a packet of simulated data to restructure to test ordering of numpy.reshape()
    fills array with corresponding label for that channel 0-7 depending on the selected number of channels.

    Returns array in same order as ADC return data durring scan. 
    Channels, samples at that point, number of points in transfer.
    different transfer states determine structure

    """
    x = []

    #TODO: change CCNT to reflect partial pf pf = CCNT/smap
    #print "make pk TF_State", TF_state
    if (TF_state <= 1):
        x =[]
        for i in range(CCNT):
            for k in range(samp):
                for l in range(ch):
                    x.append(l)
    elif(TF_state == 2):
        x = []
        for k in range(samp):
            for l in range(ch):
                x.append(l)

    elif(TF_state == 3):
        x = []
        for i in range(CCNT):
            for l in range(ch):
                x.append(l)
    return x



def test_reshape(x,CCNT,samp,ch, TF_state = None, order = 'C'):
    y = None
    if(TF_state < 1):
        pF = CCNT/samp
        #print "pF", pF
        #print"TF state 0 or 1", TF_state
        y = numpy.reshape(x,(pF,samp,ch), order)

    elif(TF_state == 1):
        #print"TF state 0 or 1", TF_state
        pF = CCNT/samp
        y = numpy.reshape(x,(pF,samp,ch), order)



    elif(TF_state == 2):
        y = numpy.reshape(x,(samp,ch), order)


    elif(TF_state == 3):
        y = numpy.reshape(x,(CCNT,ch), order)


    return y







def test_all():
    x = 5

    y = 5

    c = 2


    for i in range(1,x):
        for x in range(1,y):
            for k in range(1,c):
                m = make_pk(x,y,c)
                test_reshape(m,x,y,c)

#x= 5
#y= 10
#c =8

#m = make_pk(x,y,c)
#test_reshape(m,x,y,c)


