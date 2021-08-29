
import random

def CreateTable(carts_num): #se crea una lista con los posibles numeros y luego se revuelve para agregarse al tablero

    table = []
    temp = []
    
    for i in range(carts_num*2):
        temp.append( i%carts_num + 1)

    random.shuffle(temp)

    table.append(temp[:carts_num])
    table.append(temp[carts_num:])

    return table

def PrintTable(table, carts_num, turn, coori, coorj, past_coor):

    print('---------------------------------------------------------')
    print(f'\nturn {turn}:\n')

    for i in range(2):
        for j in range(carts_num):

            if coorj-1 == j and coori-1 == i: # si la coordenada es correcta
                print(' ',table[i][j], end="   ")

            elif past_coor[0]-1 == i and past_coor[1]-1 == j: # si la coordenada pasada es correcta
                print(' ',table[i][j], end="   ")

            elif table[i][j] == ' ': # si ya fue adivinado
                print('     ', end=" ")

            else:                       # si aun no ha sido adivinado
                print(f"({i+1},{j+1})", end=" ")

            if j == carts_num-1:
                print('\n')
                
    print('---------------------------------------------------------')

def ChangeTurn(lap, turn): # se cambia el turn o se aumenta la "lap" de la jugada

    if lap == 0:
            lap+=1
    
    elif lap == 1:
        lap = 0

        if turn == 0:
            turn = 1
        
        elif turn == 1: 
            turn = 0
    
    return lap, turn

def SeeEqual(coor, past_coor, table, turn, points, players):

    if table[coor[0]-1][coor[1]-1] == table[past_coor[0]-1][past_coor[1]-1]:
        points[turn] += 1
    
        print(f"{players[turn]} Gana punto!!")

        table[coor[0]-1][coor[1]-1] = ' '
        table[past_coor[0]-1][past_coor[1]-1] = ' '

    return table, points

def Winner(points, players, carts_num): # se comprueba si algun jugador gano

    if points[0] + points[1] == carts_num:

        print(f"\n{players[0]} obtuvo {points[0]}, {players[1]} obtuvo {points[1]}")

        if points[0] < points[1]:

            print(f"\nGANO EL JUGADOR {players[1]}!!!!")

        else:

            print(f"GANO EL JUGADOR {players[0]}!!!!")
        
        return 1
    
    return 0
        


ready_to_play = 0

#corroborar que se ingresa un numero de cartas valido 
while ready_to_play != 1:

    jugador1 = input('ingrese nombre del jugador 1: ')
    jugador2 = input('ingrese nombre del jugador 2: ')

    players = [jugador1, jugador2]

    carts_num = input("Ingrese numero de cartas: ")

    try:
        carts_num = int(carts_num)

        if carts_num <= 0:
                print('numero de cratas no valido')
    
        else: 
            ready_to_play = 1

    except:
        print("numero de cartas no valido")

table = CreateTable(carts_num) # se crea el tablero

# se inicializan variables para imprimir el tablero
end_game = 0
coorj = -1
coori = -1
past_coor = [-1, -1]
turn = 0
lap = 0
points = [0,0]

PrintTable(table, carts_num, players[turn], coori, coorj, past_coor)

while end_game == 0:

    if lap == 0:
        past_coor = input(f'{players[turn]}, ingresa coordenadas i,j : ')
    
    elif lap == 1:
        coor = input(f'{players[turn]}, Ingrese coordenadas i,j : ')

    try:
        # se comprueba que las coordenadas dean validas
        if lap == 0:
            past_coor = past_coor.split(',')
            past_coor[0] = int(past_coor[0])
            past_coor[1] = int(past_coor[1])

            coori = past_coor[0]
            coorj = past_coor[1]
            table[past_coor[0]-1][past_coor[1]-1] # se corrobora que sean coordenadas dentro del tablero
            
        
        elif lap == 1:
            coor = coor.split(',')
            coor[0] = int(coor[0])
            coor[1] = int(coor[1])

            coori = coor[0]
            coorj = coor[1]

            table[coori-1][coorj-1] # se corrobora que sean coordenadas dentro del tablero
        
        # si son validas, se imprime el tablero
        PrintTable(table, carts_num, players[turn], coori, coorj, past_coor)

        if lap == 1: # se comprueba si adivina un par
            table, points = SeeEqual(coor, past_coor, table, turn, points, players)

            if Winner(points, players, carts_num): # si la funcion retorna 1, el juego finaliza
                break

        lap, turn = ChangeTurn(lap, turn) # cambia de turno si es necesario
    
    
    except:
        print('coordenadas no validas, pierdes turno')
        lap, turn = ChangeTurn(1, turn)

