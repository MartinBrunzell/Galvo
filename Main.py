import numpy as np
import T7_power_supply as ps
import Driver
import time

"""
motor_y_ID = 'USB0::0x1AB1::0x0E11::DP8C201000734::INSTR'
motor_x_ID = 'USB0::0x1AB1::0x0E11::DP8C201000755::INSTR'
time_tagger_ID
"""

motor_y_ID = 30000
motor_x_ID = 30002
time_tagger_ID = "FIO2"



galvo = Driver.Driver()



#galvo.set_position(1,1)
#galvo.display_position()
#galvo.set_current(1,1)

#while True:
#   galvo.t7.ping_FIO("FIO2")
#galvo.t7.ping_DAC(1000,0.5)
    
galvo.scan_rectangle([2,1,-2,-1],[20,20])

"""
start = time.time()




stop = time.time()

print("elapsed time = ", stop-start)
print("time/pixel = ", (stop-start)/(100*100))
print("PPS = ", ((stop-start)/(20*20))**-1)
"""

galvo.set_position(0,0)

#galvo.end()


