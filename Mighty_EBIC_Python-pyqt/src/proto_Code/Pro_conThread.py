import Queue
import threading


class Edm(threading.Thread):

    def __init__(self,):

        threading.Thread.__init__(self)


    def run(self):
        print "poo \n"
      
      
      
E = Edm()
E.run() 
