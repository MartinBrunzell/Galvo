import DP832 as DP
import numpy as np
import time
import power_supply as ps


def set_output(v, power_supply):
    ## Enables the output of negative voltages.
    ## Made to work for the Rigol DP832 using two channels.
    #  v            - Desired output (-10 to 10 V).
    #  power_supply - Instanced class of control functions for a power supply.
    if np.abs(v) <= 10:
        if v < 0:
            power_supply.set_voltage(2, v)
            power_supply.set_voltage(1, 0)
        elif v >= 0:
            power_supply.set_voltage(2, 0)
            power_supply.set_voltage(1, v)
    else:
        print("ERROR: Voltage limit exceeded (±10V max)")


def scan_output(start_V, stop_V, N_steps, power_supply, t_delay=0):
    ## Scans the voltage from start_V to stop_V with N_steps ammount of steps
    #  power_supply - Instanced class of control functions for a power supply.
    #  t_delay      - sets the delay in time between each voltage step

    if np.abs(start_V) <= 10 and np.abs(stop_V) <= 10:
        voltages = np.linspace(start_V, stop_V, N_steps)
        for v in voltages:
            set_output(v, power_supply)
            time.sleep(t_delay)
    else:
        print("ERROR: Voltage limit exceeded (±10V max)")


def repeat(power_supply, N_runs, t_delay):
    for i in range(N_runs):
        scan_output(-1, 1, 100, power_supply, t_delay)
        scan_output(1, -1, 100, power_supply, t_delay)


def main():
    motor_x_name = 'USB0::0x1AB1::0x0E11::DP8C201000734::INSTR'
    motor_y_name = "USB0::0x1AB1::0x0E11::DP8C201000755::INSTR"
    myrigol = DP.DP832(motor_x_name)
    x_voltages = np.linspace(-10, 10, 21)
    print(myrigol.status)
    if myrigol.status == 'Connected':
        # scan_output(10,-10,21,myrigol,1)
        myrigol.set_current(1, 1)
        myrigol.set_current(2, 1)
        repeat(myrigol, 5, 0)
        # set_output(0,myrigol)

        # myrigol.toggle_output(0, 1)
        # for x_voltage in x_voltages:
        # myrigol.set_voltage(1, x_voltage)
        # myrigol.set_voltage(2, 10-x_voltage)
        # set_output(x_voltage,myrigol)
        # time.sleep(1)

        # print(myrigol.measure_current(1))
"""

motor_x = ps.power_supply("motor_x")

motor_x.set_output(2)
"""


if __name__ == '__main__':
    main()
