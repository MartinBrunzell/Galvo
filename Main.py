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

motor_x = ps.power_supply(motor_x_ID)
motor_y = ps.power_supply(motor_y_ID)



galvo = Driver.Driver(motor_x,motor_y, time_tagger_ID)

# Tests
#galvo.is_connected()
#galvo.display_position()

#galvo.set_position(1,1)
#galvo.display_position()
#galvo.set_current(1,1)
start = time.time()
#for i in range(0,50):
galvo.scan_rectangle([2,1,-2,-1],[20,20])


stop = time.time()

print("elapsed time = ", stop-start)
print("time/pixel = ", (stop-start)/(100*100))
print("PPS = ", ((stop-start)/(20*20))**-1)

galvo.end()


