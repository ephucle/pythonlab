#!/usr/bin/env python3
import time
from gpiozero import CPUTemperature
from myfunc import call
for i in range(100):
	print("temperature check from vcgencmd")
	call('/home/pi/check_temp.sh')
	
	cpu = CPUTemperature()
	print("temperature, check from module gpiozero",cpu.temperature)
	time.sleep(5)
	print("-"*10)



