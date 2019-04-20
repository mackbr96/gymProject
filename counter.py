import keyboard
import re

shot_pressed = 0
was_pressed = False


import signal
import sys
import time
import threading

filedata = ""

def signal_handler(signal, frame):
    with open('/home/ben/django-locallibrary-tutorial/catalog/templates/index.html', 'w') as file:
        file.write(filedata)

    sys.exit(0)

while True:
    
    if keyboard.is_pressed('s'):
        if not was_pressed:
            shot_pressed += 1
            print("shot_pressed %d times"%shot_pressed)
            was_pressed = True
    elif keyboard.is_pressed('a'):
        if not was_pressed:
            shot_pressed -= 1
            print("shot_pressed %d times"%shot_pressed)
            was_pressed = True
    
    else:
        was_pressed = False

    with open('/home/ben/django-locallibrary-tutorial/catalog/templates/index.html', 'r') as file :
        signal.signal(signal.SIGINT, signal_handler)
        p = re.compile("(numberOfPeople\">)(.*)(<)")
        filedata = file.read()
        i = shot_pressed
        file.close()

      # Replace the target string
    #filedata = filedata.replace(p, '>70<')
    s = "numberOfPeople\">" + str(i) + "<"
    filedata = re.sub(p,s, filedata)
      # Write the file out again
    with open('/home/ben/django-locallibrary-tutorial/catalog/templates/index.html', 'w') as file:
            signal.signal(signal.SIGINT, signal_handler)
            file.write(filedata)
            file.close()
    


