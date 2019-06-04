class config():

    def __init__(self):

        self.hMagScale=(2**16.0/(127*54.))*14000 # (max points/(number of points in 1 micron at resolution))* test Mag  
        self.vMagScale=(2**16.0/(127*74.6))*14000
        self.aspect= self.vMagScale/ self.hMagScale

