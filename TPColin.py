from machine import Pin, ADC, PWM  #importing PIN,ADC and PWM
import time #importing time   
import utime 

xAxis = ADC(Pin(27))
yAxis = ADC(Pin(26))
# Defining motor pins

#OUT1  and OUT2
In1=Pin(6,Pin.OUT)  #IN1`
In2=Pin(7,Pin.OUT)  #IN2
EN_A=PWM(Pin(8))




#OUT3  and OUT4
In3=Pin(4,Pin.OUT)  #IN3
In4=Pin(3,Pin.OUT)  #IN4
EN_B=PWM(Pin(2))

  
# Defining frequency for enable pins
EN_A.freq(1500)
EN_B.freq(1500)


# Forward
def move_forward():
    In1.high()
    In2.low()
    In3.low()
    In4.high()
    
# Backward
def move_backward():
    In1.low()
    In2.high()
    In3.high()
    In4.low()
    
   
#Stop
def stop():
    In1.low()
    In2.low()
    In3.low()
    In4.low()

while True:
    time.sleep(0.1)
    
    yValue = yAxis.read_u16()
    xValue = xAxis.read_u16()
    print(yValue)
    print(xValue)
    
    if yValue >= 32000 and yValue <= 34000 or xValue >= 32000 and xValue <= 34000:

        stop()
        

    
    
    if yValue >=