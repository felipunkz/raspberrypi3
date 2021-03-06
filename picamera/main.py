from picamera import PiCamera
from gpiozero import Button, RGBLED
from datetime import date
from datetime import datetime
import time

camera = PiCamera()
boton = Button(14, False)
flash = RGBLED(red=21, green=20, blue=19)
colores = [(0.5, 1, 1), (1, 0.5, 1), (1, 1, 0.5)]

def genera_flash():
    for color in colores:
        flash.color = color
        time.sleep(1)

def apaga_rgb():
    flash.color = (1, 1, 1)

def enciende_rgb():
    flash.color = (0.75, 0.75, 0.75)

def toma_foto():
    genera_flash()
    hora = datetime.now()
    hora_string = hora.strftime('%d%m%Y%H%M%S')
    enciende_rgb()
    camera.capture('/home/pi/Desktop/image{}.jpg'.format(hora_string))
    time.sleep(1)



if __name__ == '__main__':
    
    while True:
        apaga_rgb()
        if boton.is_pressed:
            toma_foto()
        