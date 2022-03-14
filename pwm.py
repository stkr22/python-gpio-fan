import lgpio
import time
import psutil

# Configuration
FAN = 18 # pin used to drive PWM fan
FREQ = 10000

h = lgpio.gpiochip_open(0)

try:
    running_speed = -1
    while True:
        sensors = psutil.sensors_temperatures()['cpu_thermal']
        if sensors[0].current <= 45 and running_speed != 0:
            print("Below 45, turning off.")
            running_speed = 0
            lgpio.tx_pwm(h, FAN, FREQ, running_speed)
        elif sensors[0].current > 45 and sensors[0].current < 55 and running_speed != 25:
            print("Above 45, increasing to 25.")
            running_speed = 25
            lgpio.tx_pwm(h, FAN, FREQ, running_speed)
        elif sensors[0].current >= 55 and sensors[0].current < 65 and running_speed != 50:
            print("Above 55, increasing to 50.")
            running_speed = 50
            lgpio.tx_pwm(h, FAN, FREQ, running_speed)
        elif sensors[0].current >= 65 and sensors[0].current < 70 and running_speed != 75:
            print("Above 65, increasing to 75.")
            running_speed = 75
            lgpio.tx_pwm(h, FAN, FREQ, running_speed)
        elif sensors[0].current > 70 and running_speed != 75:
            print("Above 70, increasing to 100.")
            running_speed = 100
            lgpio.tx_pwm(h, FAN, FREQ, running_speed)
        time.sleep(10)

except KeyboardInterrupt:
    # Turn the fan to medium speed
    lgpio.tx_pwm(h, FAN, FREQ, 50)
    lgpio.gpiochip_close(h)
