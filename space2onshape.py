#!/usr/bin/python3

import sys,spacenav,atexit,time
from pynput.keyboard import Key, Controller

def rotateX(kb,velocity):
    if velocity < 0:
        kb.press(Key.ctrl)
        kb.press(Key.up)
        kb.release(Key.up)
        kb.release(Key.ctrl)
    else:
        kb.press(Key.ctrl)
        kb.press(Key.down)
        kb.release(Key.down)
        kb.release(Key.ctrl)

def rotateZ(kb,velocity):
    if velocity < 0:
        kb.press(Key.ctrl)
        kb.press(Key.left)
        kb.release(Key.left)
        kb.release(Key.ctrl)
    else:
        kb.press(Key.ctrl)
        kb.press(Key.right)
        kb.release(Key.right)
        kb.release(Key.ctrl)

def moveX(kb,velocity):
    if velocity < 0:
        kb.press(Key.ctrl)
        kb.press(Key.shift)
        kb.press(Key.left)
        kb.release(Key.left)
        kb.release(Key.shift)
        kb.release(Key.ctrl)
    else:
        kb.press(Key.ctrl)
        kb.press(Key.shift)
        kb.press(Key.right)
        kb.release(Key.right)
        kb.release(Key.shift)
        kb.release(Key.ctrl)

def moveZ(kb,velocity):
    if velocity < 0:
        kb.press(Key.ctrl)
        kb.press(Key.shift)
        kb.press(Key.down)
        kb.release(Key.down)
        kb.release(Key.shift)
        kb.release(Key.ctrl)
    else:
        kb.press(Key.ctrl)
        kb.press(Key.shift)
        kb.press(Key.up)
        kb.release(Key.up)
        kb.release(Key.shift)
        kb.release(Key.ctrl)


try:
    # open the connection
    spacenav.open()
    # register the close function if no exception was raised
    atexit.register(spacenav.close)
except spacenav.ConnectionError:
    # give some user advice if the connection failed
    print("No connection to the SpaceNav driver. Is spacenavd running?")
    exit(1)

# check if the connection was established
if spacenav.is_connected:
	
    kb = Controller()

    while True:
        # 10ms pooling
        time.sleep(0.001)
        try:
            event = spacenav.poll()
            if event != None :
                if event.type == spacenav.EVENT_TYPE_MOTION:
    
                    if event.rx != 0:
                        rotateX(kb,event.rx)
                        #print (str(event.rx))
    
                    if event.rz != 0:
                        rotateZ(kb,event.rz)
                        #print (str(event.rz))

                    if event.x != 0:
                        moveX(kb,event.x)
                        #print (str(event.x))
    
                    if event.z != 0:
                        moveZ(kb,event.z)
                        #print (str(event.z))
        except KeyboardInterrupt:
            sys.exit(0)
else:
   print("No connection to the SpaceNav driver. Is spacenavd running?")
   exit(1)
