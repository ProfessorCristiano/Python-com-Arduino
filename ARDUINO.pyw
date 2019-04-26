# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 20:36:35 2019

@author: cristiano_001325
"""
'''Interessa isso aqui para o arduino'''
import serial                                                            

from tkinter import *
from tkinter import messagebox

 
window = Tk()
window.title("Programa para Ligar e Desligar")
window.geometry('400x250')
 
def clicked1():
    
    '''Interessa isso aqui para o arduino'''
    arduino = serial.Serial('COM3',9600)
    '''Interessa isso aqui para o arduino'''                       
    arduino.write(b"on\n")
    messagebox.showinfo('Acionado Ligar', 'A Luz está acesa')                                                
    try:
        '''nada'''
    except:
        '''nada'''
        messagebox.showinfo('Erro', 'Algum erro aconteceu')
    
    
    
def clicked2():
    
    '''Interessa isso aqui para o arduino'''
    arduino = serial.Serial('COM3',9600)
    '''Interessa isso aqui para o arduino'''                      
    arduino.write(b"off\n")
    messagebox.showinfo('Acionado Desligar', 'A Luz está apagada')                                               
    try:
        '''nada'''
    except:
        '''nada'''
        messagebox.showinfo('Erro', 'Algum erro aconteceu')
    

lb1 = Label(window,height=3, width=16, text='Ligar ou desligar ?',font=('Arial','12'))
lb1.grid(row=0)
 
btn1 = Button(window,height=3, width=16, text='Liga',bg='green',font=('Arial','16'), command=clicked1)
btn1.grid(column=0,row=1)

btn2 = Button(window,height=3, width=16,text='Desliga',bg='red',font=('Arial','16'), command=clicked2)
btn2.grid(column=2,row=1)



'''se fosse ler a resposta'''
'''arduino.read_until('\n')'''
'''vou tentar a resposta para desenhar um grafico'''

window.mainloop()