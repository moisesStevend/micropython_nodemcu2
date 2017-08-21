# This file is executed on every boot (including wake-boot from deepsleep)
import esp
import gc
import webrepl

def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('jicamarca', 'radioobservatory')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())

esp.osdebug(None)
gc.collect()
do_connect()
webrepl.start()
