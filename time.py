# using Tkinter's Optionmenu() as a combobox
import Tkinter as tk
from Tkinter import *
import tkFont
import time
from time import strftime
import os

def apply():
     time = var1.get() + ":" + var2.get()
     os.system("sudo date -s" + time)
     print time
     quit()

def cancel():
  quit()


root = tk.Tk()
# use width x height + x_offset + y_offset (no spaces!)
root.geometry("%dx%d+%d+%d" % (330, 80, 200, 150))
root.title("Change local time")

myFont = tkFont.Font(family = 'Calibri Light', size = 12, weight = 'normal')

var1 = tk.StringVar(root)
var2 = tk.StringVar(root)
# initial value
var1.set('12')
var2.set('00')

choices1 = ['00', '01', '02', '03', '04','05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']
choices2 = ['00', '01', '02', '03', '04','05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59']
choices3 = ['AM', 'PM']

clock = Label(root, height=1, width=20, text = "Current time: " + strftime("%H:%M"), font=myFont)
clock.pack(side = TOP, anchor=W, pady=5)

hour = tk.OptionMenu(root, var1, *choices1)
hour.pack(side='left', padx=15, pady=10)

minute = tk.OptionMenu(root, var2, *choices2)
minute.pack(side='left', padx=10, pady=10)

applyButton = tk.Button(root, text="Apply", command=apply)
applyButton.pack(side='left', padx=5, pady=10)

cancelButton = tk.Button(root, text="Cancel", command=cancel)
cancelButton.pack(side='left', padx=5, pady=10)

root.mainloop()