#including the required libraries
from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)    #setting the gpio mode to board

GPIO.setup(8,GPIO.OUT)      #initialising the blue led.
GPIO.setup(10,GPIO.OUT)     #initialising the green led.
GPIO.setup(12,GPIO.OUT)     #initialising the red led.

win=Tk()        #opening the window
win.title("Morsecode")      #setting window title
myFont=tkinter.font.Font(family='Helvetica',size=13,weight="bold")

#dot function to blink blue led as per the morsecode
def dot():
    GPIO.output(8,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(8,GPIO.LOW)
    time.sleep(1)

#dash function to blink green led as per the morsecode    
def dash():
    GPIO.output(10,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(10,GPIO.LOW)
    time.sleep(1)

#defining the morsecode of all the alphabets
MORSE= { 'A':'.-', 'B':'-...','C':'-.-.','D':'-..', 'E':'.','F':'..-.',
         'G':'--.', 'H':'....','I':'..','J':'.---', 'K':'-.-','L':'.-..',
         'M':'--', 'N':'-.','O':'---','P':'.--.', 'Q':'--.-','R':'.-.',
         'S':'...', 'T':'-','U':'..-','V':'...-', 'W':'.--','X':'-..-',
         'Y':'-.--', 'Z':'--..'}

#convert funtion to convert the alphabets entered into morsecode (dot and dash)
def convert():
    input=user_input.get()      #taking the user input
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
    #blinking red led after blinking of morsecode
    GPIO.output(12,GPIO.HIGH)
    time.sleep(2)
    GPIO.output(12,GPIO.LOW)
    
#creating a user input box            
user_input=Entry(win,font=myFont,width=24,bg='white')
user_input.grid(row=0,column=0)

#creaing a button for the convert command
button=Button(win,text='convert',font=myFont,command=convert,bg='grey',height=1,width=10)
button.grid(row=1,column=0)
