import DP832 as DP
import numpy as np
import time

class Motor(power_supply)
    def __init__(self, power_supply):
        self.power_supply = power_supply


    def set_output(self, v):
    ## Enables the output of negative voltages.
    ## Made to work for the Rigol DP832 using two channels.
    #  v            - Desired output (-10 to 10 V).
    #  power_supply - Instanced class of control functions for a power supply.
    if np.abs(v) <= 10:
        if v < 0:
            self.power_supply.set_voltage(2,v)
            self.power_supply.set_voltage(1,0)
        elif v >= 0:
            self.power_supply.set_voltage(2,0)
            self.power_supply.set_voltage(1,v)
    else:
        print("ERROR: Voltage limit exceeded (±10V max)")


    
    def scan_output(self, start_V, stop_V, N_steps, t_delay = 0):
        ## Scans the voltage from start_V to stop_V with N_steps ammount of steps
        #  power_supply - Instanced class of control functions for a power supply.
        #  t_delay      - sets the delay in time between each voltage step

        if np.abs(start_V) <= 10 and np.abs(stop_V) <= 10:
            voltages = np.linspace(start_V,stop_V,N_steps)
            for v in voltages:
                self.set_output(v, self.power_supply)
                time.sleep(t_delay)
        else:
            print("ERROR: Voltage limit exceeded (±10V max)")


def trace_curve(MotorX, MotorY):

    vx = 10
    vy = 4

    N_steps_y = 20
    N_steps_x = 51

    for v in range(-vy,vy,(2*vy/N_steps_y)):
        MotorX.scan_output(-vx,vx,N_steps_x)
        
    
    
    

def set_output(v,power_supply):
    ## Enables the output of negative voltages.
    ## Made to work for the Rigol DP832 using two channels.
    #  v            - Desired output (-10 to 10 V).
    #  power_supply - Instanced class of control functions for a power supply.
    if np.abs(v) <= 10:
        if v < 0:
            power_supply.set_voltage(2,v)
            power_supply.set_voltage(1,0)
        elif v >= 0:
            power_supply.set_voltage(2,0)
            power_supply.set_voltage(1,v)
    else:
        print("ERROR: Voltage limit exceeded (±10V max)")
        

def scan_output(start_V, stop_V, N_steps,power_supply,t_delay = 0):
    ## Scans the voltage from start_V to stop_V with N_steps ammount of steps
    #  power_supply - Instanced class of control functions for a power supply.
    #  t_delay      - sets the delay in time between each voltage step

    if np.abs(start_V) <= 10 and np.abs(stop_V) <= 10:
        voltages = np.linspace(start_V,stop_V,N_steps)
        for v in voltages:
            set_output(v, power_supply)
            time.sleep(t_delay)
    else:
        print("ERROR: Voltage limit exceeded (±10V max)")

def repeat(power_supply,N_runs):
    for i in range(N_runs):
        scan_output(-10,10,21,power_supply,1)
        scan_output(10,-10,21,power_supply,1)

    
myrigol = DP.DP832()
x_voltages = np.linspace(-10,10,21)
print(myrigol.status)
if myrigol.status == 'Connected':
    #scan_output(10,-10,21,myrigol,1)
    repeat(myrigol,1)


    
    #myrigol.toggle_output(0, 1)
    #for x_voltage in x_voltages:
        #myrigol.set_voltage(1, x_voltage)
        #myrigol.set_voltage(2, 10-x_voltage)
        #set_output(x_voltage,myrigol)
        #time.sleep(1)

    #print(myrigol.measure_current(1))




    
