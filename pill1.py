from Tkinter import *
import tkFont
import urllib
from time import strftime
import time
from Adafruit_PWM_Servo_Driver import PWM
import os;

win = Tk()
pwm = PWM(0x40)

#win.attributes("-fullscreen", True)  # substitute `Tk` for whatever your `Tk()` object is called

myFont = tkFont.Font(family = 'Calibri Light', size = 36)
myFont2 = tkFont.Font(family = 'Calibri Light', size = 12)
bgcolor = '#%02x%02x%02x' % (128, 128, 128)

win.attributes("-fullscreen", True)

def test1():
	print("Jetzt, gruen")
	textLabel.config(text='Naechste Einnahme: Jetzt', foreground='#%02x%02x%02x' % (0, 128, 0))
        ejectButton.config(state='active')
def test2():
	print("Jetzt, gelb")
	textLabel.config(text='Naechste Einnahme: Jetzt', foreground='Gold')
def test3():
	print("Jetzt, rot")
	textLabel.config(text='Naechste Einnahme: Jetzt', foreground='darkred')
def test4():
	print("Jetzt, verpasst")
	textLabel.config(text='Naechste Einnahme: Jetzt', foreground='DarkRed')
	os.system("sudo python sms.py")
        return urllib.urlopen('http://baitmain.de/ipill')
def test5():
        print("Zeit geaendert")
        os.system("sudo python time.py")
def eject():
	print("Eject button pressed")
	ejectButton.config(state='disabled')
	textLabel.config(text='Naechste Einnahme: 8 Uhr', foreground='green')
	pwm.setPWM(0, 0, 150)
        time.sleep(1)
        pwm.setPWM(0, 0, 500)      
def update_clock():
        clock.configure(text=strftime("%H:%M"))
        win.after(30000, update_clock)
        
win.after(3000, update_clock)

#os.system('date -s "2 OCT 2010 18:00:00"')

win.configure(bg=bgcolor)
win.title("SmartPill")
win.geometry('800x480')

clock = Label(win, height=1, width=10, text = strftime("%H:%M"), font = myFont2, background= bgcolor, foreground='White', relief=FLAT)
clock.pack(side = TOP, anchor=E, ipady=10)

Spacer = Label(win, height=1, width=2, text = "", font = myFont, background= bgcolor)
Spacer.pack(side = TOP, ipady=0)

textLabel = Label(win, height=2, width=30, text = "Naechste Einnahme: 18 Uhr", font = myFont, background= bgcolor, foreground='#%02x%02x%02x' % (0, 128, 0), relief=FLAT)
textLabel.pack(side = TOP)

ejectButton = Button(win, text = "Tabletten ausgeben", font = myFont, command = eject, height =1 , width = 20,anchor=N, foreground='white', background='#%02x%02x%02x' % (0, 120, 215), activebackground='grey', disabledforeground='grey', relief=FLAT)
ejectButton.pack(side = TOP)
ejectButton.config(state='disabled')

test1Button = Button(win, text = "Gruen", font = myFont2, command = test1, height =1, width =5, relief=FLAT, background='grey'  )
test1Button.pack(padx=5, pady=10, side=LEFT, anchor=S)

test2Button = Button(win, text = "Gelb", font = myFont2, command = test2, height =1, width =5, relief=FLAT, background='grey'  )
test2Button.pack(padx=5, pady=10, side=LEFT, anchor=S)

test3Button = Button(win, text = "Rot", font = myFont2, command = test3, height =1, width =5, relief=FLAT, background='grey'  )
test3Button.pack(padx=5, pady=10, side=LEFT, anchor=S)

test4Button = Button(win, text = "Verpasst", font = myFont2, command = test4, height =1, width =5, relief=FLAT, background='grey' )
test4Button.pack(padx=5, pady=10, side=LEFT, anchor=S)

test5Button = Button(win, text = "Zeit", font = myFont2, command = test5, height =1, width =5, relief=FLAT, background='grey' )
test5Button.pack(padx=5, pady=10, side=LEFT, anchor=S)

test6Button = Button(win, text = "Beenden", font = myFont2, command = exit, height =1, width =5, relief=FLAT, background='grey' )
test6Button.pack(padx=5, pady=10, side=LEFT, anchor=S)

mainloop()
