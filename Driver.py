import numpy as np
import T7_power_supply as ps
import time

class Driver:
    def __init__(self, max_voltage=10):
        self.ID_x = 30002
        self.ID_y = 30000 # For our Labbjack T7
        self.channel_stop = "FIO3"
        self.channel_start = "FIO2"
 
        self.t7 = ps.T7()
        
        self.max_voltage = max_voltage
        self.set_position(0,0)

    def set_position(self,x,y):
        self.t7.set_output(self.ID_x,x)
        self.t7.set_output(self.ID_y,y)
        

    def scan_rectangle(self,rectangle,dim,t_delay = 0):
        #rectangle = [x_max, y_max, x_min, y_min]
        #dim = [dim_x,dim_y]
        x_voltages = np.linspace(rectangle[0],rectangle[2],dim[0])
        y_voltages = np.linspace(rectangle[1],rectangle[3],dim[1])

        for y in y_voltages:
            x_voltages = np.flip(x_voltages)
            for x in x_voltages:
                self.t7.ping(self.channel_stop)
                self.set_position(x,y)
                self.t7.ping(self.channel_start)

        self.t7.ping(self.channel_stop)

    


    def end(self):
        self.t7.close()


        
