"""
import os
print (os.uname())

osInfo = os.uname()

print(osInfo[1])

if osInfo[1]=='raspberrypi':
    print("os is raspberrypi")
else:
    print("N/A:")
"""
#cat /proc/device-tree/model

import platform
print(platform.node())
print(platform.platform())
platformInfo = platform.platform()

def getOperatingSystemVersion():
    if platformInfo.find("Linux") ==-1:
        print("Other") 
        return("Other")  
    else:
        print("linux version")
        return("linux")  
"""
if __name__== '__main__':
    getOperatingSystemVersion()

"""
    
         