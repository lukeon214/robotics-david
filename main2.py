import pigpio
pi = pigpio.pi()


def map(x:float,in_min:float,in_max:float,out_min:float,out_max:float)-> float:
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

pi.set_servo_pulsewidth(20,map(float(input()),-90,90,1000,1900))