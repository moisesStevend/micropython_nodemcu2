import machine
import time
# GPIO2  built_led nodemcu originales
# GPIO16 led del encapsulado de grabacion
# GPIO0 button pul_up fflash

p2=machine.Pin(2, machine.Pin.OUT)
#pin = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)
'''
p2.on()
p2.off()
p2.value() #sin argumentos devuelve valor only
p2.value(0)
p2.value(1)
'''
print("inicio")

while True:
    try:
        p2.value(not p2.value())
        print("value: ",p2.value())
        time.sleep(0.2)
    except:
        print("error, p2: 0")
        p2.value(0)
        break
