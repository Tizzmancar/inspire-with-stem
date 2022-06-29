from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

i2c=I2C(0,sda=Pin(26), scl=Pin(27), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)

oled.text("hello world", 0, 0)
oled.show()