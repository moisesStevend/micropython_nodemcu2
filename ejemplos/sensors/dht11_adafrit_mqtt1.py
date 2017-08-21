#
# Micropython ESP8266 code to Publish temperature sensor data to an Adafruit IO Feed using the MQTT protocol
# Also publishes statistics on the number of free bytes on the micropython Heap
#
# Hardware used:
# - Adafruit Huzzah ESP8266 running micropython version esp8266-20160909-v1.8.4.bin
# - Adafruit MCP9808 temperature breakout board
# - USB to serial converter
#

# prerequisites:
# - Adafruit account
# - registered to use Adafruit IO

#
# References and Kudos
#
# Big thanks to Tony DiCola from Adafruit for excellent tutorials on:
#   Ampy tutorial:  valuable tool to efficiently develop python code on ESP8266 hardware:
#     https://learn.adafruit.com/micropython-basics-load-files-and-run-code
#   i2c on micropython hardware tutorial:
#     https://learn.adafruit.com/micropython-hardware-i2c-devices
#
import dht
import network
import time
import machine
import gc
import time
from umqtt.simple import MQTTClient


myMqttClient = "moises_stevend"  # can be anything unique
adafruitIoUrl = "io.adafruit.com"
adafruitUsername = "moisesStevend"  # can be found at "My Account" at adafruit.com
adafruitAioKey = "dd652bfbb7c94422b873d59f136b11de"  # can be found by clicking on "VIEW AIO KEYS" when viewing an Adafruit IO Feed
c = MQTTClient(myMqttClient, adafruitIoUrl, 0, adafruitUsername, adafruitAioKey)
c.connect()

d = dht.DHT11(machine.Pin(4))


while True:
    try:
        d.measure()
        temperatura = d.temperature()
        print(temperatura)
        c.publish("moisesStevend/f/DemoFeed", str(temperatura))  # publish temperature to adafruit IO feed
        #c.publish("MikeTeachman/feeds/feed-micropythonFreeHeap", str(gc.mem_free()))  #publish num free bytes on the Heap
        time.sleep(1)  # number of seconds between each Publish

        d.measure()
        humedad = d.humidity()
        print(humedad)
        c.publish("moisesStevend/f/humedityFeed", str(humedad))
        time.sleep(1)
    except:
        break

c.disconnect()
