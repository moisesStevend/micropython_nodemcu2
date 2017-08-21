from machine import  Timer
import time
#global  tim
tim = Timer(-1)

def fun_call():
    try:
        print("hola")
    except:
        print("close timer")
        tim.deinit()

tim = Timer(-1)   #timer disponible, los demas timer son para pwm, adc, etc
#tim.init(period=1000, mode=Timer.PERIODIC, callback=lambda t:print("calback"))
tim.init(period=1000, mode=Timer.PERIODIC, callback=lambda t:fun_call())

while True:
    try:
        time.sleep(0.1)
    #except KeyboardInterrupt:
    except:
        print("fin")
        break

tim.deinit()
