import time
import busio
from board import SCL, SDA
from adafruit_pca9685 import PCA9685
from adafruit_motor import servo

# Create the I2C connection channel
i2c = busio.I2C(SCL, SDA)

# Pass that channel to the PCA9685 driver
pca = PCA9685(i2c)

pca.frequency = 50

my_servo = servo.Servo(pca.channels[0], min_pulse=500, max_pulse=2500)


print("initializing")
time.sleep(5)
print("starting")

my_servo.angle = 0
print("angle = 0")

time.sleep(2)

my_servo.angle = 90
print("angle = 90")

time.sleep(2)

my_servo.angle = 180
print("angle = 180")

time.sleep(2)
print("done")

pca.deinit()
