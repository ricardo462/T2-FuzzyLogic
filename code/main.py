from model.DSS     import DSS
from model.Premise import Premise
from model.Rule    import Rule


efectividad = [12, 17, 25, 25]
altura = [170, 195, 220, 220]
sprint = [0, 0, 10, 15]

Basket_maker  = Premise(efectividad)
Tall          = Premise(altura)
Sprinter      = Premise(sprint)

R1 = Rule((Basket_maker, Tall),      0.80)
R2 = Rule((Basket_maker, Sprinter),  0.95)
R3 = Rule((Tall,         Sprinter),  0.75)

dss = DSS((R1, R2, R3))

print('Bienvenidx al sistema de asistencia de preselección de jugadores de Basketball')

while True:
    name = input('Ingrese el nombre del jugador/a:')
    
    basket = int(input('Ingrese el número de canastas'))
    while basket >25 or basket < 0 or type(basket) != int:
        basket = int(input('Ingrese un número de canastas válido (0 <= int <= 25)'))

    
    height = float(input('Ingrese su altura (cm)'))
    while height < 0:
        height = int(input('Ingrese una altura válida (0 <= float)'))

    time = float(input('Ingrese el tiempo de sprint (s)'))
    while time < 0:
        time = float(input('Ingrese un tiempo válido (0 <= int)'))

    puntaje = dss(basket, height, time)
    print(f'El usuario {name} tiene un puntaje de: {puntaje}')



    continue_ = input('¿Desea continuar? [y/n]')
    if continue_ == 'n':
        break
