from labjack import ljm
import time
import numpy as np




class T7:
    def __init__(self):
        self.handle = ljm.openS("T7", "Any", "ANY")
        self.info = ljm.getHandleInfo(self.handle)

        self.WRITE = ljm.constants.WRITE
        self.READ = ljm.constants.READ
        self.FLOAT32 = ljm.constants.FLOAT32
        self.UINT16 = ljm.constants.UINT16
        self.UINT32 = ljm.constants.UINT32

    def set_output(self, ID,v):

        if np.abs(v) < 10:
            dataType = self.FLOAT32
            ljm.eWriteAddress(self.handle, ID, dataType, v)

        else:
            print("Error: voltage limit exceded (you idiot)")


    def ping(self,channel,time_delay=0):
        
        ljm.eWriteName(self.handle, channel, 1)
        time.sleep(time_delay) #Might slow down the program
        ljm.eWriteName(self.handle, channel, 0)
        

    def close(self):
        ljm.close(self.handle)

      
 
