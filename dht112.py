import time
import board
import adafruit_dht
import RPi.GPIO as GPIO
#Initial the dht device, with data pin connected to:

def getTemperatureStr():
    GPIO.cleanup()
    dhtDevice = adafruit_dht.DHT11(board.D17)
   
    tempStr=""

    try:
        # Print the values to the serial port
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity
        
        tempStr="Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(temperature_f, temperature_c, humidity)

        print("Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(temperature_f, temperature_c, humidity))
    except RuntimeError as error:     
        print(error.args[0])
        tempStr=error.args[0]
        time.sleep(2.0)
    
    return tempStr

if __name__=="__main__":
    getTemperatureStr()
