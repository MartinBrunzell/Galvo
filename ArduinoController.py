import time
import serial

class ArduinoController:
  def __init__(self,port="COM3"):
    self.ardu= serial.Serial('COM3',115200, timeout=.1)  
    time.sleep(2)
    
  def write(self,pin):
      #print("sent")
      self.ardu.write(pin.encode())


