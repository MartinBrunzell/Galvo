import numpy as np
import T7_power_supply as ps
import time

class Driver:
    def __init__(self, max_voltage=10):
        """
        Initiates a Labjack-T7 object as a power supply
        """

        #The ID,s of the outports of the T7 labjack, hardcoded for our purposes
        self.ID_x = 30002
        self.ID_y = 30000 
        #self.channel_stop = "FIO3"
        #self.channel_start = "FIO2"
        self.channel_stop = 1000 #DAC0
        self.channel_start = 1002 #DAC1
        self.x = 0
        self.y = 0

        self.t7 = ps.T7()
        
        self.max_voltage = max_voltage
        self.set_position(0,0)

    def set_position(self,x,y):
        #sets the output of the different motors
        self.t7.set_output(self.ID_x,x)
        self.t7.set_output(self.ID_y,y)
        self.x = x
        self.y = y
        

    def get_position(self):
        print("The X voltage is ", self.x, "Volts")
        print("The Y voltage is ", self.y, "Volts")
        

    def scan_rectangle(self,rectangle,dim,t_delay = 0):
        #rectangle = [x_max, y_max, x_min, y_min]
        #dim = [dim_x,dim_y]
        x_voltages = np.linspace(rectangle[0],rectangle[2],dim[0])
        y_voltages = np.linspace(rectangle[1],rectangle[3],dim[1])

        for y in y_voltages:
            x_voltages = np.flip(x_voltages)
            for x in x_voltages:
                self.t7.ping_DAC(self.channel_stop,0.5) #Sends a signal that mirrors are moving
                self.set_position(x,y)
                self.t7.ping_DAC(self.channel_start,0.5) #Sends a signal that the mirrors have stopped

        self.t7.ping_DAC(self.channel_stop,0.5)

    

    def end(self):
        self.t7.close() #Closes the connection with the labjack


        
