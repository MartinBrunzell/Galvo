from labjack import ljm
import time
import numpy as np




class power_supply:
    def __init__(self,ID):
        self.ID = ID
        self.handle = ljm.openS("T7", "Any", "ANY")
        self.info = ljm.getHandleInfo(self.handle)

        self.WRITE = ljm.constants.WRITE
        self.READ = ljm.constants.READ
        self.FLOAT32 = ljm.constants.FLOAT32
        self.UINT16 = ljm.constants.UINT16
        self.UINT32 = ljm.constants.UINT32

    def set_output(self,v):

        if np.abs(v) < 10:
            dataType = self.FLOAT32
            ljm.eWriteAddress(self.handle, self.ID, dataType, v)

        else:
            print("Error: voltage limit exceded (you idiot)") 

    def scan_output(self,start_V, stop_V, N_steps,t_delay = 0):
        ## Scans the voltage from start_V to stop_V with N_steps ammount of steps
        #  power_supply - Instanced class of control functions for a power supply.
        #  t_delay      - sets the delay in time between each voltage step

        if np.abs(start_V) <= 10 and np.abs(stop_V) <= 10:
            voltages = np.linspace(start_V,stop_V,N_steps)
            for v in voltages:
                self.set_output(v)
                time.sleep(t_delay)
        else:
            print("ERROR: Voltage limit exceeded (±10V max)")      

    def repeat(self,V_start,V_stop,N_runs,N_steps,t_delay):
        for i in range(N_runs):
            self.scan_output(V_start,V_stop,N_steps,t_delay)
            self.scan_output(V_stop,V_start,N_steps,t_delay)

    def display_voltage(self):
        time.sleep(1) #TODO: fix
        return 0
    
    def display_current(self):
        time.sleep(1) #TODO: fix
        return 0

    def set_current(self,i):
        time.sleep(1) #TODO: fix
    def status(self):
        time.sleep(1) #TODO: fix

    def close(self):
        ljm.close(self.handle)    
    
        
class Time_Tagger:
    def __init__(self, ID):
        self.ID = ID
        self.handle = ljm.openS("T7", "Any", "ANY")
        self.info = ljm.getHandleInfo(self.handle)
        self.state = 0

        self.WRITE = ljm.constants.WRITE
        self.READ = ljm.constants.READ
        self.FLOAT32 = ljm.constants.FLOAT32
        self.UINT16 = ljm.constants.UINT16
        self.UINT32 = ljm.constants.UINT32


        self._set_state(self.state)

    def _set_state(self,state):
        self.state = state  # Output state = low (0 = low, 1 = high)
        ljm.eWriteName(self.handle, self.ID, state)

    def ping(self, time_delay = 0):
        self.set_high()
        time.sleep(time_delay)
        self.set_low()

    def set_high(self):
        self._set_state(1)

    def set_low(self):
        self._set_state(0)

    def get_state(self):
        return self.state

    def close(self):
        ljm.close(self.handle)


        
        
        
