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
window.geometry('600x450')

def leitura():
    try:
        temperatura=arduino.read()
    except:
        '''nada'''
        messagebox.showinfo('Sem Conexão', 'Não foi possível fazer a leitura do Arduino.')

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

leitura()

lbnada = Label(window,height=3, width=16, text=' ',font=('Arial','12'))
lbnada.grid(column=0, row=2)
lb2 = Label(window,height=3, width=16, text='Temperatura',font=('Arial','12'))
lb2.grid(column=0, row=3)
lb3 = Label(window,height=3, width=16, text='°C',bg='green',font=('Arial','12'))
lb3.grid(column=2, row=3)

'''se fosse ler a resposta'''
'''arduino.read_until('\n')'''
'''vou tentar a resposta para desenhar um grafico'''

window.mainloop()
