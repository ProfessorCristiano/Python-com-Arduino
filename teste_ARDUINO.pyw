# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 20:36:35 2019

@author: cristiano_001325
"""
'''Interessa isso aqui para o arduino'''
import serial                                                            
arduino = serial.Serial('COM3', 9600)

opcao=int(input("1 para ligar\n2 paradesligar\n"))

if(opcao==1):
    arduino.write(b"on\n")
if(opcao==2):
    arduino.write(b"off\n")
result = arduino.readline()
result = result.decode("utf-8")

print("Resultado:", result[:(len(result)-2)], "\n")

arduino.close()



'''pagina 76 do pdf'''
'''se fosse ler a resposta'''
'''arduino.read_until('\n')'''
'''vou tentar a resposta para desenhar um grafico'''

