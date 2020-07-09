import numpy as np
import power_supply as ps
import Driver
import time

motor_y_ID = 'USB0::0x1AB1::0x0E11::DP8C201000734::INSTR'
motor_x_ID = 'USB0::0x1AB1::0x0E11::DP8C201000755::INSTR'

motor_x = ps.power_supply(motor_x_ID)
motor_y = ps.power_supply(motor_y_ID)



galvo = Driver.Driver(motor_x,motor_y)

# Tests
#galvo.is_connected()
galvo.display_position()

#galvo.set_position(1,1)
#galvo.display_position()
galvo.set_current(1,1)
start = time.time()

galvo.scan_rectangle([2,1,-2,-1],[10,10])

stop = time.time()

print("elapsed time = ", stop-start)
print("time/pixel = ", (stop-start)/(20*20))


