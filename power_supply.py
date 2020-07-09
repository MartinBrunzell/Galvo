import DP832 as DP
import numpy as np
import time

class power_supply:
    def __init__(self,ID):
        self.myrigol = DP.DP832(ID)
        self.ID = ID

    def set_output(self,v):
        ## Enables the output of negative voltages.
        ## Made to work for the Rigol DP832 using two channels.
        #  v            - Desired output (-10 to 10 V).
        #  power_supply - Instanced class of control functions for a power supply.
        if np.abs(v) <= 10:
            if v < 0:
                self.myrigol.set_voltage(2,v)
                self.myrigol.set_voltage(1,0)
            elif v >= 0:
                self.myrigol.set_voltage(2,0)
                self.myrigol.set_voltage(1,v)
        else:
            print("ERROR: Voltage limit exceeded (±10V max)")
        

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
        return self.myrigol.measure_voltage(1)-self.myrigol.measure_voltage(2)
    
    def display_current(self):
        return self.myrigol.measure_current(1) ## TODO: test it with equip.

    def set_current(self,i):
        self.myrigol.set_current(1,i)
        self.myrigol.set_current(2,i)

    def status(self):
        return self.myrigol.status

    
        
