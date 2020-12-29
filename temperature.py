 
#returns CPU temperature for rasberry pi

from gpiozero import CPUTemperature
"""
cpu = CPUTemperature()
print(cpu.temperature)

"""
def getTemperature(): 
    cpu = CPUTemperature()
    print(cpu.temperature)
    return cpu.temperature

 