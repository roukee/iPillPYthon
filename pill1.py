from Tkinter import *
import tkFont
import urllib
import time
import schedule
from time import strftime
import os;

win = Tk()

#win.attributes("-fullscreen", True)  # substitute `Tk` for whatever your `Tk()` object is called

myFont = tkFont.Font(family = 'Calibri Light', size = 36)
myFont2 = tkFont.Font(family = 'Calibri Light', size = 12)
bgcolor = '#%02x%02x%02x' % (128, 128, 128)

def test1():
	print("Test 1")
	textLabel.config(text='Naechste Einnahme: Jetzt', foreground='#%02x%02x%02x' % (0, 128, 0))
	os.system("sudo python time.py")
def test2():
	print("Test 2")
	textLabel.config(text='Naechste Einnahme: Jetzt', foreground='Gold')
def test3():
	print("Test 3")
	textLabel.config(text='Naechste Einnahme: Jetzt', foreground='darkred')
def test4():
	print("Test 4")
	textLabel.config(text='Naechste Einnahme: Jetzt', foreground='DarkRed')
        return urllib.urlopen('http://baitmain.de/ipill')

def eject():
	print("Eject button pressed")
        
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

test1Button = Button(win, text = "Test 1", font = myFont2, command = test1, height =1, width =5, relief=FLAT, background='grey'  )
test1Button.pack(padx=5, pady=10, side=LEFT, anchor=S)

test2Button = Button(win, text = "Test 2", font = myFont2, command = test2, height =1, width =5, relief=FLAT, background='grey'  )
test2Button.pack(padx=5, pady=10, side=LEFT, anchor=S)

test3Button = Button(win, text = "Test 3", font = myFont2, command = test3, height =1, width =5, relief=FLAT, background='grey'  )
test3Button.pack(padx=5, pady=10, side=LEFT, anchor=S)

test4Button = Button(win, text = "Test 4", font = myFont2, command = test4, height =1, width =5, relief=FLAT, background='grey' )
test4Button.pack(padx=5, pady=10, side=LEFT, anchor=S)

mainloop()