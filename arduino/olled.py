from machine import Pin,ADC, Pin, I2C
import ssd1306
import time
from time import sleep
from dht import DHT11, InvalidChecksum
 

# using default address 0x3C
i2c = I2C(1,sda=Pin(26), scl=Pin(27))
display = ssd1306.SSD1306_I2C(128, 64, i2c)

sensor = DHT11(Pin(16, Pin.OUT, Pin.PULL_DOWN))
 
while True:
    t = sensor.temperature
    h= sensor.humidity
    print("Temperature: {}°C   Humidity: {:.0f}% ".format(t, h))
    time.sleep(2)
    display.text('Temp:{}'.format(t) , 5, 8, 1)
    display.text('Hum:{}'.format(h), 15, 25, 1)
    #display.text('Light: {}'.format(value), 20, 0, 1)
    display.show()
    time.sleep(3)