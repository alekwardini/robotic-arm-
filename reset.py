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


servo_1 = servo.Servo(pca.channels[0], min_pulse=500, max_pulse=2500)
servo_2 = servo.Servo(pca.channels[1], min_pulse=500, max_pulse=2500)
servo_3 = servo.Servo(pca.channels[2], min_pulse=500, max_pulse=2500)
servo_4 = servo.Servo(pca.channels[3], min_pulse=500, max_pulse=2500)
servo_5 = servo.Servo(pca.channels[4], min_pulse=500, max_pulse=2500)
servo_6 = servo.Servo(pca.channels[5], min_pulse=500, max_pulse=2500)

time.sleep(3)
def reset():
	servo_1.angle = 90
	time.sleep(1)
	servo_2.angle = 90
	time.sleep(1)
	servo_3.angle = 90
	time.sleep(1)
	servo_4.angle = 90
	time.sleep(1)
	servo_5.angle = 90
reset()
print("done")

pca.deinit()
