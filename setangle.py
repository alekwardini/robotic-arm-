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



def set_all(x):
	time.sleep(3)
	servo_1.angle = x
	time.sleep(0.5)
	servo_2.angle = x
	time.sleep(0.5)
	servo_3.angle = x
	time.sleep(0.5)
	servo_4.angle = x
	time.sleep(0.5)
	servo_5.angle = x
	time.sleep(0.5)
	servo_6.angle = x
	time.sleep(0.5)
	print(f"all servo motors set to {x} degrees")
def set_angle():
    while True:
        x = input("which servo would you like to use: ")
        y = int(input("what is the angle? "))
        time.sleep(3)
        if x == "1":
            servo_1.angle = y
        elif x == "2":
            servo_2.angle = y
        elif x == "3":
            servo_3.angle = y
        elif x == "4":
            servo_4.angle = y
        elif x == "5":
            servo_5.angle = y
        elif x == "6":
            servo_6.angle = y
        if input("continue? (y/n)") == "n":
            break
def close_claw():
    servo_6.angle = 170
def open_claw():
    servo_6.angle = 80
while True:
    ans = input("choose function: set_all(setting all servos to an angle)\nset_angle(set a servo to a specific angle)\nclose_claw\nopen_claw)")
    if ans == "set_all": set_all(int(input("choose angle to set all servos to: ")))
    elif ans == "set_angle": set_angle()
    elif ans == "open_claw": open_claw()
    elif ans == "close_claw": close_claw()
    if input("continue? (y/n): ") == "n":
        break

pca.deinit()
