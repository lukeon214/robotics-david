import pigpio
import time
pi = pigpio.pi()
pi.set_PWM_frequency(20,200)

def map(x:float,in_min:float,in_max:float,out_min:float,out_max:float)-> float:
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def setAngle(angle:float):
    pi.set_servo_pulsewidth(20,map(angle,-90,90,1000,1900))
        
while 1:
    for i in range(-90,90):
    
        setAngle(float(i))
        time.sleep(0.01)

    for i in range(-90,90)[::-1]:
    
        setAngle(float(i))
        time.sleep(0.01)