import math
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
servo_1.angle = 90
servo_2.angle = 90
time.sleep(1)
servo_3.angle = 90
servo_4.angle = 90
time.sleep(1)
servo_5.angle = 90
servo_6.angle = 90
time.sleep(1)


negative = False
origin = 90
a = 8
b = 8
x = int(input("choose x coordinate: "))
y = int(input("choose y coordinate: "))
z = int(input("choose z coordinate: "))
coordinates = (x, y, z)
if x < 0:
    negative = True
    x = abs(x)
d1 = ((x**2)+(z**2))**0.5
o = math.degrees(math.atan(z/x))
o1 = math.degrees(math.acos(((d1**2)-((a**2)+(b**2)))/(-2*a*b)))
o2 = math.degrees(math.acos(((b**2)-((a**2)+(d1**2)))/(-2*a*d1)))
if o1 + o >90:
    fo = o-o2
else: fo = o1+o

if negative == True:
    angle_servo = 90-fo
else:
    angle_servo = 90+fo
print(f"{d1}distance, o ={o}, o1={o1}, o2 = {o2}, fo={fo}, servo_angle = {angle_servo}")

if y < 0:
    base = 90 - math.atan(x/y)
else:
    base = 90 + math.atan(x/ y)


servo_1.angle = base
servo_2.angle = angle_servo
servo_3.angle = o1 

