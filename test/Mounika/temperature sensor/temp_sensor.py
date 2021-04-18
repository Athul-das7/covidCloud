# test code for getting data from mlx90614 ir thermal sensor
# import the package "Adafruit Blinka"
# import the package "adafruit-circuitpython-mlx90614"
# need to enable i2c on the pi https://pimylifeup.com/raspberry-pi-i2c/
# Reboot after enabling i2C
# here sensor will be connected to 3.3V, GND and the i2C pins 3(SDA) and 5(SCL)

import board
import busio as io
# The busio module contains an interface for using hardware-driven I2C communication from your board
import adafruit_mlx90614

from time import sleep

i2c = io.I2C(board.SCL, board.SDA, frequency=100000)   # to create an interface to access the I2C bus
mlx = adafruit_mlx90614.MLX90614(i2c)    # to create an instance of the I2C bus connected to the sensor

ambientTemp = "{:.2f}".format(mlx.ambient_temperature)
targetTemp = "{:.2f}".format(mlx.object_temperature)

sleep(1)

print("Ambient Temperature:", ambientTemp, "°C")
print("Target Temperature:", targetTemp, "°C")


#   ensure the device is available on the i2c bus:   in rapberry pi ->  sudo i2cdetect -y 1
