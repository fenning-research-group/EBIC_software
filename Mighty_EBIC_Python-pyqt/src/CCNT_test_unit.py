import CCNT_test
import numpy
import sys
import os
CWD = os.getcwd()
sys.path.append(CWD +'/proto_Code')
import os.path
import sim_data
import pylab



def test_scanSize(TF, pF, pS, samp, CH, resizeDim):
    """
    Returns the size of the data packets in ints.
    asserts that the datasize is equal to the expected value of transfers

    """
    temp = 1
    for i in resizeDim:
        temp = i*temp

    assert TF*temp == pF*pS*samp*CH
    return temp

def put_inP(storedArray, inputarray, xindex = None , sub_xindex = None, yindex = None, samp_index = None, sub_samp_index= None, TF_state = None, resizeDim = None ):
    """
    Depending on the transfer state put data into array given index for X, Y, samples and CH

    """

    if(TF_state == 0):

        storedArray[:, yindex[0] , :,:] = inputarray
    
    if(TF_state == 1):

        storedArray[sub_xindex : sub_xindex + resizeDim[0], yindex, :,:] = inputarray

    elif(TF_state == 2):

        storedArray[xindex, yindex, :,:] = inputarray
        
    elif(TF_state == 3):

        storedArray[xindex, yindex,sub_samp_index : sub_samp_index + resizeDim[-2], :] = inputarray


def put_in_Display(storedArray, inputarray, xindex = None , sub_xindex = None, yindex = None, samp_index = None, sub_samp_index= None, TF_state = None, resizeDim = None ):
    """
    Depending on the transfer state put data into array given index for X, Y, samples and CH

    """

    if(TF_state == 0):

        storedArray[:, yindex[0] ,:] = inputarray
    
    if(TF_state == 1):

        storedArray[sub_xindex : sub_xindex + resizeDim[0], yindex,:] = inputarray

    elif(TF_state == 2):

        storedArray[xindex, yindex,:] = inputarray
        
    elif(TF_state == 3):

        storedArray[xindex, yindex, :] = inputarray




#TODO come up with a test pattern for each state


mk = sim_data.make_pk

TF_I = CCNT_test.TF_index


def runTest():
    #Test Parameters

    pF = 100
    pS = 10
    samp = 2
    CH = 2



    #Determine the state of the transfer and if anything needs to get resized
    TF, TF_state, pF, pS, samp, CCNT, resizeDim = CCNT_test.set_CCNT(pF = pF,pS = pS, CH = CH , samp = samp)


#make array to put the data in
    storedArray = numpy.zeros([pF, pS, samp, CH], numpy.int32)
    print "storedARRay", storedArray.shape
    print "resizeDIM", resizeDim
    print "CCNT", CCNT



    for i in range(TF):
        #Make test packet
        test_packet = mk(CCNT,samp,CH, TF_state = TF_state)

        #check scan size
        test_scanSize(TF, pF, pS, samp, CH, resizeDim)

        #reshape data into an array
        test_data = sim_data.test_reshape(test_packet,CCNT, samp,CH, TF_state = TF_state)

    #Get indexes
        xindex , sub_xindex, yindex, samp_index, sub_samp_index = TF_I(TF, TF_state, pF = pF, pS = pS, samp = samp, CCNT= CCNT, header = (i+1), resizeDim = resizeDim)



        #store data in array
        put_inP(storedArray, ((test_data + 1) *yindex), xindex , sub_xindex, yindex, samp_index, sub_samp_index, TF_state)
    for k in range(CH):

        print storedArray[:,:,:,k].mean()
        pylab.imshow(storedArray[:,:,0,k])
        pylab.colorbar()
        pylab.show()


        print "YUSS"

if __name__ == "__main__":

    runTest()
        

