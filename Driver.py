import numpy as np
import power_supply as ps
import time

class Driver:
    def __init__(self, power_x, power_y, max_voltage=10):
        self.power_x = power_x
        self.power_y = power_y
        self.max_voltage = max_voltage
        self.set_position(0,0)

    def display_position(self):
        # Displays the position in the console
        print("x = " ,self.power_x.display_voltage()," V")
        print("y = " ,self.power_y.display_voltage()," V")
        
    def set_current(self,ix,iy):
        # Sets the active 
        self.power_x.set_current(ix)
        self.power_y.set_current(iy)

    def set_position(self,x,y):
        self.power_x.set_output(x)
        self.power_y.set_output(y)
        self.display_position()

    def scan_rectangle(self,rectangle,dim,t_delay = 0):
        #rectangle = [x_max, y_max, x_min, y_min]
        #dim = [dim_x,dim_y]
        x_voltages = np.linspace(rectangle[0],rectangle[2],dim[0])
        y_voltages = np.linspace(rectangle[1],rectangle[3],dim[1])

        for y in y_voltages:
            x_voltages = np.flip(x_voltages)
            for x in x_voltages:
                self.set_position(x,y)
                time.sleep(t_delay)
    
    
