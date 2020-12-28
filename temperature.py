"""
#returns CPU temperature for rasberry pi

from gpiozero import CPUTemperature

cpu = CPUTemperature()
print(cpu.temperature)

"""