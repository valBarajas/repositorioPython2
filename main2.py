"""
Date:        09/30/2022
Authors:     vale barajas
File:        2022-4.py
Brief:       Description file
Version:     0.1
Changes By:  none
Fixes:       nonea
"""
import Functions
a=1
b=2

if __name__=='__main__':
    #declaracion de varibles
    no1 = 1
    no2 = 2
    no3 = 3
    no4 = 1
    #llamdo de funciones que se importan de otro archivo  he impresion
    print(f'resultado de sumar  {no1:d} y { no2:d} es: ', Functions.suma(no1,no2))
    print(f'resultado de sumar  {no3:d} y {no3:d} es: ', Functions.suma(no3, no4))
    print(f'resultado de restar  {no1:d} y { no2:d} es: ', Functions.resta(no1,no2))
    print(f'resultado de restar  {no3:d} y {no3:d} es: ',  Functions.resta(no3, no4))
    print(f'resultado de multiplicar  {no1:d} y {no2:d} es: ', Functions.multiplicar(no1, no2))
    print(f'resultado de multiplicar  {no3:d} y {no3:d} es: ', Functions.multiplicar(no3, no4))
    print(f'resultado de dividir  {no1:d} y {no2:d} es: ', Functions.dividir(no1, no2))
    print(f'resultado de dividir  {no3:d} y {no3:d} es: ', Functions.dividir(no3, no4))


