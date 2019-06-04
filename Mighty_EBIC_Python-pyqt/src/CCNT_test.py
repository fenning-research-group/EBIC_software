
pF = 3000
CH = 8
samp = 2

def set_CCNT(pF = 3000,pS = 3000, CH = 8, samp =1):
    """
    CCNT_test tries to best fit packet size into 1020 samples of 32 bits plus 4 ints of header per packet.
    number of channels is limited to 8 samples are limited as well. BCNT is always number of channels. 
    ACNT is always 4 for one int.  

    Determines the Transfer State and total number of transfers that will be made.

    resizes pF or samp taken to fit better into transfer 4096 bytes or 1020 int - 4 int for header
    
    Transfer states:

    TF_state == pS_CCNT:
    TF = pS*(pF/CCNT) , CCNT is 1 for this case

    TF_state == pS_pF_resized_CCNT:
    TF = pS*(pF/CCNT) CCNT is greater than 1 but more than 1 point is in a transfer

    TF_state == pS_pF_CCNT:
    TF = pS*pF #CCNT = CH*samp , each point(x,y) is a transfer

    TF_state == pS_pF_samp_CCNT:
    TF = pS*pF*(samp/CCNT)  


    Returns: (TF, TF_state, pF, pS, samp, CCNT)

    """

    assert CH <= 8
    assert samp >= 1

    TF_state = None #variable used for identifying state of transfer total
    TF = None # number of transfer in scan

    # Transfer States
    pS_CCNT = 0             # CCNT buffer size is   CH*samp*pF
    pS_pF_resized_CCNT = 1                         #CH*samp*pF_resized
    pS_pF_CCNT = 2                                 #CH*samp 
    pS_pF_samp_CCNT = 3                            #CH

    resizeDim = None  # dimension to pass to the indexing to store data into an array


    # no need to resize everything fits nicely
    if(CH*pF*samp <= 1020):
        CCNT = pF*samp #don't need CH included because that is in BCNT!!
        TF_state = pS_CCNT
        resizeDim = (pF,samp,CH) #shape of matrix for reshaping


    # number of points greater than 1020 see if we can make it fit better
    # round down number of points
    elif (pF > 1020/(CH*samp)):

        for i in range(2,100):


            #trying to break pF into smaller points so it maximizes CCNT to fill up 1020 data points
            sub_pF = (pF/i)
            #print "sub_pF", sub_pF


            # try and fit CCNT packet size(CH*samp) into 1020 nicely
            if((sub_pF*(CH*samp) <= 1020) and ( sub_pF > 0)):
                print "i" , i

                #print "CCNT", CCNT

                pF = (pF/sub_pF)*sub_pF # make pF a multiple of subPF
                
                CCNT = samp*sub_pF



                TF_state = pS_pF_resized_CCNT
                # trying CCNT/samp to account shape with samples greater than 1
                resizeDim = (sub_pF,samp, CH) #shape of matrix to put things into
                print "pF", pF, "TF_state", TF_state, "CCNT", CCNT, "resizeDim", resizeDim, "\n"
                break  
            
            #see if we can set CCNT to the number of samples             
            if (i > 98 or sub_pF == 0):   #CCNT less than zero stop!!

                if (CH * samp < 1020):
                    CCNT = samp
                    TF_state = pS_pF_CCNT
                    resizeDim = (samp,CH)
                    break

                # resize samples to fit in multiples of CCNT
                else:
                    TF_state = pS_pF_samp_CCNT 
                    for k in range(1,1000):
                        sub_samp = int(samp/k)
                        #CCNT = int(1020/(CH*k))
                        if (sub_samp*CH <= 1020):

                            CCNT = sub_samp
                            samp = (samp/sub_samp)*sub_samp

                            resizeDim = (CCNT, CH) #shape of the matrix to size things
                            print "samp", samp, "CCNT", CCNT, "k", k 
                            break              
                        if (sub_samp == 0):
                            CCNT = 1
                            resizeDim = (CCNT, CH) #shape of the matrix to resize things for each transfer
                            break
                    # shouldn't be used all that often probably a better way to break this up

                print "Ch and Sample" , CH, samp
                pF = pF   #Don't round pF
                print "CCNT", CCNT
                print "pF", pF
                print "i" , i

                break    



                    
            
    #Calculate number of Transfers based on state
    print " TF State", TF_state
    if(TF_state == pS_CCNT):
        TF = pS #CCNT = pF*samp

    elif(TF_state == pS_pF_resized_CCNT):
        TF = pS*(pF/resizeDim[0]) #CCNT greater than 1 but more than 1 point is in a transfer

    elif(TF_state == pS_pF_CCNT):
        TF = pS*pF #CCNT = CH*samp each point(x,y) is a transfer

    elif(TF_state == pS_pF_samp_CCNT):
        TF = pS*pF*(samp/CCNT)  
        # each sample is transfer, using cases means we can define a more elegant solution for this
        #right now it breaks up the number of samples to fit in CCNT transfer

    assert TF !=None
    assert TF < 2**32
    print "TF", TF

    return (TF, TF_state, pF, pS, samp, CCNT, resizeDim)


def TF_index(TF=None, TF_state=None, pF=None, pS=None, samp= None, CCNT=None, header = None, resizeDim = None):
    """
    Determines the Transfer index for x, y, samp, and CH based on the Transfer State TF


    Returns:

    """


    yindex = None
    xindex = None
    sub_xindex = None

    samp_index = None
    sub_samp_index = None
    

    #Need a switch to define xindex and yindexing method

    if(TF_state < 1):
        yindex_dem = 1
        xindex_dem = 1

        yindex = (header - 1)/yindex_dem
        #print" TF state 0, yindex", yindex, "\n"
        #xindex = (header - yindex*yindex_dem -1)

        #sub_xindex = xindex*resizeDim[0]


    
    if(TF_state == 1):
        #print "TF state 1"
        yindex_dem = pF/resizeDim[0]
        xindex_dem = 1

        yindex = int((header - 1)/yindex_dem)

        xindex = (header - yindex*yindex_dem -1)
        sub_xindex = xindex*resizeDim[0]

    elif(TF_state == 2):
        yindex_dem = pF
        xindex_dem = 1

        yindex = int((header - 1)/yindex_dem)

        xindex =(header - yindex*yindex_dem -1)

    
    elif(TF_state == 3):
        yindex_dem = ((pF*samp)/CCNT)
        xindex_dem = (samp/CCNT)

        yindex = int((header - 1)/yindex_dem)

        xindex = int((header - yindex*yindex_dem -1)/xindex_dem)

        samp_index = header - yindex*yindex_dem - xindex*xindex_dem - 1
        sub_samp_index = samp_index*resizeDim[-2]

    #print "xindex", xindex,"sub_xindex", sub_xindex, "yindex", yindex, "samp_index", samp_index, "sub_samp_index", sub_samp_index 


    return xindex , sub_xindex, yindex, samp_index, sub_samp_index

"""


        sub_data_array = numpy.reshape(Z, ((CCNT/samp),CH,samp), order = 'C')

        print "data", count , " len", len(data), "xindex" , xindex, "yindex", yindex ,
             "data shape", sub_data_array.shape, "header" , header[0], "Z", Z[1]

        #print sub_data_array
        sub_xindex = xindex*sub_data_array.shape[0]
        print sub_xindex 
        storedArray[sub_xindex[0] : sub_xindex[0] + sub_data_array.shape[0], yindex[0], :,:] = sub_data_array

"""
