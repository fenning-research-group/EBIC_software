import sys, time
from threading import *
#from qt import *

class TextThread(Thread):

    def __init__(self, name):
        Thread.__init__(self,)        
        self.counter=0
        self.name=name

        #apply(Thread.__init__, (self, ) + args)

    def run(self):
        while self.counter < 200:
            print self.name, self.counter
            self.counter = self.counter + 1
            time.sleep(1)

