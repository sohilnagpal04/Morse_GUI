from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(8,GPIO.OUT)
GPIO.setup(10,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)

win=Tk()
win.title("Morsecode")
myFont=tkinter.font.Font(family='Helvetica',size=13,weight="bold")

def dot():
    GPIO.output(8,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(8,GPIO.LOW)
    time.sleep(1)
    
def dash():
    GPIO.output(10,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(10,GPIO.LOW)
    time.sleep(1)
    
MORSE= { 'A':'.-', 'B':'-...','C':'-.-.','D':'-..', 'E':'.','F':'..-.',
         'G':'--.', 'H':'....','I':'..','J':'.---', 'K':'-.-','L':'.-..',
         'M':'--', 'N':'-.','O':'---','P':'.--.', 'Q':'--.-','R':'.-.',
         'S':'...', 'T':'-','U':'..-','V':'...-', 'W':'.--','X':'-..-',
         'Y':'-.--', 'Z':'--..'}

def convert():
    input=user_input.get()
    print("Hello " + input)
    for letter in input:
        for symbol in MORSE[letter.upper()]:
            if symbol=='.':
                dot()
            elif symbol=='-':
                dash()
            else:
                time.sleep(0.5)
    print("Morsecode Blinked Successfully!")
    GPIO.output(12,GPIO.HIGH)
    time.sleep(2)
    GPIO.output(12,GPIO.LOW)
    
            
user_input=Entry(win,font=myFont,width=24,bg='white')
user_input.grid(row=0,column=0)

button=Button(win,text='convert',font=myFont,command=convert,bg='grey',height=1,width=10)
button.grid(row=1,column=0)
