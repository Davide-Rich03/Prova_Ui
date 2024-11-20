import streamlit as st


def somma(l1:float, l2:float):
    return l1+l2

def diff(l1:float, l2:float):
    return l1-l2

def molt(l1:float, l2:float):
    return l1*l2

def div(l1:float, l2:float):
    return l1/l2


while True:

    print('Benvenuti nel programma calcolatrice')
    print('====================================')
    print('Operazioni disponibili')
    print('1) Somma')
    print('2) Moltiplicazione')
    print('3) Divisione')
    print('4) Sottrazione')
    print('------------------------------------')
    print('0) Esci')

    scelta= input('inserire una scelta valida: ')
    if scelta == 0:
        break
    if scelta not in [1,2,3,4]:
        print ('Scelta non valida')
        continue
    a= input('Primo operando: ')
    b= input('Secondo operando: ')
    if scelta == 1:
        print('la somma è ', somma(a,b))
    elif scelta == 2:
        print('la moltiplicazione è ', molt(a,b))
    elif scelta == 3:
        print('la divisione è ', div(a,b))
    elif scelta == 4:
        print('la sottrazione è ', diff(a,b))

print ('\nGrazie  alla prossima')