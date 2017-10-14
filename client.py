from random import randint
import requests, math, time
import logging
import sys


print("===========================")
print("==== MENU PING - PONG  ====")
print("====[1] Empezar juego  ====")
print("====[2] Reglas         ====")
print("====[3] Salir          ====")
print("===========================")
numeroDeEleccion = input("\n= Ingrese numero escogido: =\n")

print("The time got from the server is %s" % tm.decode('ascii'))

def mostarReglas():
    print('Estas son las reglas')

# definir el tablero
y, x = 7, 5
matrix = [[' ' for x in range(x)] for y in range(y)]
posicionYBola = 3
posicionXBola = 1
movimientoEnX1 = 1
movimientoEnX2 = 1
movimientoEnY1 = 3
movimientoEnY2 = 3
turno = 'nadie'
ganadorPartida = None
for x in range(0, 5):
    matrix[0][x] = "-"
    matrix[6][x] = "-"

def limpiarMatriz():
    y, x = 7, 5
    matrix = [[' ' for x in range(x)] for y in range(y)]
    for x in range(0, 5):
        matrix[0][x] = "-"
        matrix[6][x] = "-"
    return matrix

def inicioDeJuego():
    global matrix
    limpiarMatriz()
    matrix[3][0] = "1"
    matrix[3][4] = "1"
    matrix[3][1] = "O"

def imprimirTablero():
    print(matrix[0][0] + "  " + matrix[0][1] + "  " + matrix[0][2] + "  " + matrix[0][3] + "  " + matrix[0][4])
    print(matrix[1][0] + "  " + matrix[1][1] + "  " + matrix[1][2] + "  " + matrix[1][3] + "  " + matrix[1][4])
    print(matrix[2][0] + "  " + matrix[2][1] + "  " + matrix[2][2] + "  " + matrix[2][3] + "  " + matrix[2][4])
    print(matrix[3][0] + "  " + matrix[3][1] + "  " + matrix[3][2] + "  " + matrix[3][3] + "  " + matrix[3][4])
    print(matrix[4][0] + "  " + matrix[4][1] + "  " + matrix[4][2] + "  " + matrix[4][3] + "  " + matrix[4][4])
    print(matrix[5][0] + "  " + matrix[5][1] + "  " + matrix[5][2] + "  " + matrix[5][3] + "  " + matrix[5][4])
    print(matrix[6][0] + "  " + matrix[6][1] + "  " + matrix[6][2] + "  " + matrix[6][3] + "  " + matrix[6][4] + "\n")

def movimientoDeLaBolaPrimerJugador(x,y):
    global movimientoEnX1, movimientoEnX2, movimientoEnY1, movimientoEnY2
    numeroAleatorio = randint(1, 3)
    print(numeroAleatorio)
    # lineal siempre
    movimientoEnX1 = x + 1
    movimientoEnX2 = x + 2
    movimientoEnX3 = x + 3
    movimientoEnY1 = y
    movimientoEnY2 = y
    movimientoEnY3 = y

    #limites en x 0 y 5
    #limites en y 0 y 6

    #para arriba
    if (((numeroAleatorio == 2) and (y != 1)) or (numeroAleatorio == 3 and (y == 5))):
        movimientoEnY1 = y - 1
        #si hay alemnos un espacio mas al borde
        if y != 2 :
            #suba otro mas
            movimientoEnY2 = y - 2
            #si el ultimo golpe pega en el borde
            if y == 3:
                #el eje y no se mueve
                movimientoEnY3 = movimientoEnY2
            else:
                movimientoEnY3 = y - 3
        #si pega con el borde
        else :
            #baje uno
            movimientoEnY2 = y
            movimientoEnY3 = y
        print("movimiento para arriba")

    #para abajo
    elif ((numeroAleatorio == 3 and (y != 5))or (((numeroAleatorio == 2) and (y == 1)))):
        movimientoEnY1 = y + 1
        # si hay almenos un espacio mas al borde
        if y != 4:
            # suba otro mas
            movimientoEnY2 = y + 2
            # si el ultimo golpe pega en el borde
            if y == 3:
                # el eje y no se mueve
                movimientoEnY3 = movimientoEnY2
            else:
                movimientoEnY3 = y + 3
        # si pega con el borde
        else:
            # baje uno
            movimientoEnY2 = y
            movimientoEnY3 = y
        print("movimiento para abajo")
        print(movimientoEnY1)
    return  movimientoEnX1, movimientoEnY1,movimientoEnX2, movimientoEnY2, movimientoEnX3, movimientoEnY3

def movimientoDeLaBolaSegundoJugador(x,y):
    global movimientoEnX1, movimientoEnX2, movimientoEnY1, movimientoEnY2, posicionXBola, posicionYBola
    numeroAleatorio = randint(1, 3)
    print(numeroAleatorio)
    # lineal siempre
    movimientoEnX1 = x - 1
    movimientoEnX2 = x - 2
    movimientoEnX3 = x - 3
    movimientoEnY1 = y
    movimientoEnY2 = y
    movimientoEnY3 = y
    #limites en x 0 y 5
    #limites en y 0 y 6

    #para arriba
    if (((numeroAleatorio == 2) and (y != 1)) or (numeroAleatorio == 3 and (y == 5))):
        movimientoEnY1 = y - 1
        if y != 2 :
            movimientoEnY2 = y - 2
        else :
            movimientoEnY2 = y + 1
        print("movimiento para arriba")

    #para abajo
    elif ((numeroAleatorio == 3 and (y != 5))or (((numeroAleatorio == 2) and (y == 1)))):
        movimientoEnY1 = y + 1
        movimientoEnY2 = y + 2
        movimientoEnY3 = y + 3
        print("movimiento para abajo")
        print(movimientoEnY1)
    return  movimientoEnX1, movimientoEnY1,movimientoEnX2, movimientoEnY2, movimientoEnX3, movimientoEnY3

def calcularMovimientoDePaleta(p1, p2,x3, y2):
    numeroAleatorio = randint(1, 4)
    print("NUMERO RANDOM ES "+str(numeroAleatorio))
    #paleta 1 baja
    if numeroAleatorio == 1:
        if ((p1 < 5) and  (p1 >= 1)):
            p1 = p1 + 1
    #paleta 2 baja
    elif numeroAleatorio == 2:
        if ((p2 < 5) and  (p2 >= 1)):
            p2 = p2 + 1
    # paleta 1 sube
    elif numeroAleatorio == 3:
        if ((p1 <= 5) and (p1 > 1)):
            p1 = p1 - 1
    # paleta 2 sube
    elif numeroAleatorio == 4:
        if ((p2 <= 5) and (p2 > 1)):
            p2 = p2 - 1




    return  p1,p2

def calcularMovimientoDeBola(x0, y0, x1,y1,x2,y2,x3,y3, p1, p2):
    global posicionXBola, posicionYBola, matrix, ganadorPartida
    numeroAleatorio = randint(1, 2)
    delay = 0
    if numeroAleatorio == 1:
        delay = 1
    matrix = limpiarMatriz()
    matrix[p1][0] = "1"
    matrix[p2][4] = "1"
    matrix[y0][x0] = "O"
    time.sleep(2)
    imprimirTablero()
    #matrix[p1][0] = " "
    #matrix[p2][4] = " "
    matrix = limpiarMatriz()
    p1, p2 = calcularMovimientoDePaleta(p1, p2,x3, y2)
    #matrix[y0][x0] = " "
    matrix[y1][x1] = "O"
    matrix[p1][0] = "1"
    matrix[p2][4] = "1"
    time.sleep(1)
    imprimirTablero()
    #matrix[p1][0] = " "
    #matrix[p2][4] = " "
    matrix = limpiarMatriz()
    p1, p2 = calcularMovimientoDePaleta(p1, p2,x3, y2)
    #matrix[y1][x1] = " "
    matrix[y2][x2] = "O"
    matrix[p1][0] = "1"
    matrix[p2][4] = "1"
    time.sleep(2)
    imprimirTablero()
   # matrix[y2][x2] = " "
   # matrix[y2][4] = " "
   # matrix[y2][0] = " "


    #if turno del jugador 1
    if(x3 == 0) :
        #si no le da a la paleta
        if(matrix[y2][x3] != "1" ) :
            ganadorPartida = 'cliente2'
            matrix[y2][x2] = " "
            matrix[y3][x3] = "O"
            #matrix[y2][0] = "1"
            #matrix[y3][4] = "1"
            time.sleep(2)
            imprimirTablero()
            inicioDeJuego()
    #if turno del jugador 2
    else :
        # si no le da a la paleta
        if (matrix[y2][x3] != "1"):
            ganadorPartida = 'cliente1'
            matrix[y2][x2] = " "
            matrix[y3][x3] = "O"
            # matrix[y2][0] = "1"
            # matrix[y3][4] = "1"
            time.sleep(2)
            imprimirTablero()
            inicioDeJuego()

    return ganadorPartida

def juegoDeJugador1():
    print('poner lo que hace jugador1')

def empezarJuego():
    global posicionXBola, posicionYBola, ganadorPartida
    #dictToSend = {'question':'what is the answer?'}
    #response = requests.post('http://localhost:5000/game/checksession', json=dictToSend)
    responseGet = requests.get('http://localhost:5000/game/checksession')
    print('response from server to get:', responseGet.text)

    responsePost = requests.post('http://localhost:5000/game/checksession')
    sessionID = responsePost.json()[-1]['sessionID']
    cliente1 = None
    cliente2 = None
    while (cliente1 == None or cliente2 == None):
        time.sleep(2)
        print("Waiting for the other player...")
        getParaEmpezar = requests.get('http://localhost:5000/game/checksession')
        cliente1 = getParaEmpezar.json()[-1]['cliente1']
        cliente2 = getParaEmpezar.json()[-1]['cliente2']
    print('response from server to post:', responsePost.text)
    p1,p2 = 3,3
    if responsePost.json()[-1]['cliente2'] != 'listo' :
        global turno
        print("Sos el jugador #1")
        partidas = 0
        inicioDeJuego()
        while partidas < 3:
            x0, y0 = posicionXBola, posicionYBola
            #when gameOn = true

            while True :
                x1,y1,x2,y2,x3,y3 = movimientoDeLaBolaPrimerJugador(x0, y0)
                ganadorPartida = calcularMovimientoDeBola(x0,y0,x1,y1,x2,y2,x3,y3, p1, p2)
                movimientosCliente1 = [{'movimientoEnX0':x0, 'movimientoEnY0':y0,
                                        'movimientoEnX1':x1, 'movimientoEnY1':y1,
                                        'movimientoEnX2': x2, 'movimientoEnY2':y2,
                                        'movimientoEnX3': x3, 'movimientoEnY3': y3,
                                        'movimientoP1': p1, 'movimientoP2': p2,
                                        'usuario' : 'cliente1',
                                        'ganadorPartida' : ganadorPartida}]
                requests.post('http://localhost:5000/game/checksession/move/' , json=movimientosCliente1)
                if ganadorPartida != None:
                    partidas = partidas + 1
                    print("GANE SOY EL JUGADOR 1")
                    requests.post('http://localhost:5000/game/checksession/matches/')
                    ganadorPartida = None
                    turno = None
                    while (turno == None):
                        time.sleep(2)
                        print("Waiting for the second player...")
                        getMatch = requests.get('http://localhost:5000/game/checksession/matches/')
                        print(getMatch)
                        turno = getMatch.json()[-1]['cliente2']

                    time.sleep(3)
                    break
                turno = "cliente2"
                while (turno == 'cliente2') :
                    time.sleep(2)
                    print("Waiting for the second player...")
                    getTurno = requests.get('http://localhost:5000/game/checksession/turno/' + str(sessionID))
                    turno = getTurno.text


                responseGet = requests.get('http://localhost:5000/game/checksession/move/')

                print('response from server to get:', responseGet.json()[-1]['movimientoP1_j2'])
                calcularMovimientoDeBola(int(responseGet.json()[-1]['movimientoEnX0_j2']),
                                         int(responseGet.json()[-1]['movimientoEnY0_j2']),
                                         int(responseGet.json()[-1]['movimientoEnX1_j2']),
                                         int(responseGet.json()[-1]['movimientoEnY1_j2']),
                                         int(responseGet.json()[-1]['movimientoEnX2_j2']),
                                         int(responseGet.json()[-1]['movimientoEnY2_j2']),
                                         int(responseGet.json()[-1]['movimientoEnX3_j2']),
                                         int(responseGet.json()[-1]['movimientoEnY3_j2']),
                                         int(responseGet.json()[-1]['movimientoP1_j2']),
                                         int(responseGet.json()[-1]['movimientoP2_j2']))
                x0 = int(responseGet.json()[-1]['movimientoEnX2_j2'])
                y0 = int(responseGet.json()[-1]['movimientoEnY2_j2'])
                p1 = int(responseGet.json()[-1]['movimientoP1_j2'])
                p2 = int(responseGet.json()[-1]['movimientoP2_j2'])
                time.sleep(1)


    elif responsePost.json()[-1]['cliente2'] == 'listo' :
        print("Sos el jugador #2")
        partidas = 0
        while partidas < 3:
            #loop inicial
            turno = "cliente1"
            while (turno == 'cliente1'):
                time.sleep(2)
                print("Waiting for the first player...")
                getTurno = requests.get('http://localhost:5000/game/checksession/turno/' + str(sessionID))
                turno = getTurno.text
                print(turno)
             #while gameOn = true X3 Y3 !!!!!!!!!!!!!1
            while True :

                responseGet = requests.get('http://localhost:5000/game/checksession/move/')
                print('response from server to get:', responseGet.json()[-1]['movimientoEnX1_j1'])
                calcularMovimientoDeBola(int(responseGet.json()[-1]['movimientoEnX0_j1']),
                                         int(responseGet.json()[-1]['movimientoEnY0_j1']),
                                         int(responseGet.json()[-1]['movimientoEnX1_j1']),
                                         int(responseGet.json()[-1]['movimientoEnY1_j1']),
                                         int(responseGet.json()[-1]['movimientoEnX2_j1']),
                                         int(responseGet.json()[-1]['movimientoEnY2_j1']),
                                         int(responseGet.json()[-1]['movimientoEnX3_j1']),
                                         int(responseGet.json()[-1]['movimientoEnY3_j1']),
                                         int(responseGet.json()[-1]['movimientoP1_j1']),
                                         int(responseGet.json()[-1]['movimientoP2_j1']))
                time.sleep(1)
                x0, y0 = int(responseGet.json()[-1]['movimientoEnX2_j1']), int(responseGet.json()[-1]['movimientoEnY2_j1'])
                p1, p2 = int(responseGet.json()[-1]['movimientoP1_j1']), int(responseGet.json()[-1]['movimientoP2_j1'])

                x1, y1, x2, y2,x3,y3 = movimientoDeLaBolaSegundoJugador(int(responseGet.json()[-1][ 'movimientoEnX2_j1']),
                                                    int(responseGet.json()[-1][ 'movimientoEnY2_j1']))
                ganadorPartida = calcularMovimientoDeBola(x0,y0,x1,y1,x2,y2, x3, y3,p1,p2)
                movimientosCliente2 = [{'movimientoEnX0':x0, 'movimientoEnY0':y0,
                                        'movimientoEnX1':x1, 'movimientoEnY1':y1,
                                        'movimientoEnX2': x2, 'movimientoEnY2':y2,
                                        'movimientoEnX3': x3, 'movimientoEnY3': y3,
                                        'movimientoP1': p1, 'movimientoP2': p2,
                                        'usuario' : 'cliente1',
                                        'ganadorPartida' : ganadorPartida}]
                requests.post('http://localhost:5000/game/checksession/move/', json=movimientosCliente2)
                if ganadorPartida != None:
                    partidas = partidas + 1
                    print("GANE SOY EL JUGADOR 2")
                    ganadorPartida = None
                    time.sleep(3)
                    break
                turno = "cliente1"
                while (turno == 'cliente1'):
                    time.sleep(2)
                    print("Waiting for the second player...")
                    getTurno = requests.get('http://localhost:5000/game/checksession/turno/' + str(sessionID))
                    turno = getTurno.text
                    print("Turno de: " + turno)


if numeroDeEleccion == '1':
    empezarJuego()

elif numeroDeEleccion == '2' :
    mostarReglas()

elif numeroDeEleccion == '3':


    exit()
