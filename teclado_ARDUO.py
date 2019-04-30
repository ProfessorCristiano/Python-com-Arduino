# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 20:35:34 2019

@author: cristiano_001325
"""

from tkinter import *
import serial                                                            
sarduino = serial.Serial('COM5', 9600)
result=""
 
window = Tk()
window.title("Teclado")
#window.geometry('240x215')

def click1():
    bt1.configure(text= " dó ")
    lb.configure(text= " dó ")
    sarduino.write(b"C\n")
def click2():
    bt2.configure(text= " ré ")
    lb.configure(text= " ré ")
    sarduino.write(b"D\n")
def click3():
    bt3.configure(text= " mí ")
    lb.configure(text= " mí ")
    sarduino.write(b"E\n")
def click4():
    bt4.configure(text= " fá ")
    lb.configure(text= " fá ")
    sarduino.write(b"F\n")
def click5():
    bt5.configure(text= " sol ")
    lb.configure(text= " sol ")
    sarduino.write(b"G\n")
def click6():
    bt6.configure(text= " lá ")
    lb.configure(text= " lá ")
    sarduino.write(b"A\n")
def click7():
    bt7.configure(text= " sí ")
    lb.configure(text= " sí ")
    sarduino.write(b"B\n")

    
bt1 = Button(window, text=" 1 ", width=6, height=6, command=click1)
bt1.grid(column=0, row=0)
bt2 = Button(window, text="  2 ", width=6, height=6, command=click2)
bt2.grid(column=1, row=0)
bt3 = Button(window, text=" 3 ", width=6, height=6,command=click3)
bt3.grid(column=2, row=0)
bt4 = Button(window, text="  4 ", width=6, height=6,command=click4)
bt4.grid(column=3, row=0)
bt5 = Button(window, text=" 5 ", width=6, height=6,command=click5)
bt5.grid(column=4, row=0)
bt6 = Button(window, text="  6 ", width=6, height=6,command=click6)
bt6.grid(column=5, row=0)
bt7 = Button(window, text=" 7 ", width=6, height=6,command=click7)
bt7.grid(column=6, row=0)
lb=Label(window, text=result)
lb.grid(column=0,row=1)

#result = sarduino.readline()
#result = result.decode("utf-8")
#print("Resultado:", result[:(len(result)-2)], "\n")
#sarduino.close()

window.mainloop()



