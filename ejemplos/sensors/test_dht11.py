import dht
import machine
import time

d = dht.DHT11(machine.Pin(4))

while 1:
    try:
        print("medicion ",d.measure())
        time.sleep(1)
        print("temperatura ",d.temperature())
        time.sleep(1)
        print("humedad ",d.humidity())
        time.sleep(1)
    except:
        break
