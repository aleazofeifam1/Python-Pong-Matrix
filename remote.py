from flask import Flask
from flask import jsonify, request, json
import  requests

app = Flask(__name__)
count = 1
gameDashboard = [
    {
        'sessionID' : count,
        'cliente1' : None,
        'cliente2' : None,
        'ganadorPartida1' : None,
        'ganadorPartida2' : None,
        'ganadorPartida3' : None,
        'ganadorDelSet' : None
    }]

gameMoves = [
    {
        'moveID' : count,
        'cliente1Moved' : None,
        'cliente2Moved' : None,
    }]

matchMoves = [
    {
        'matchID' : count,
        'cliente1' : None,
        'cliente2' : None,
    }]

playMoves = [{
        'playID' : count,
        'movimientoEnX0_j1' : None,
        'movimientoEnY0_j1' : None,
        'movimientoEnX1_j1' : None,
        'movimientoEnY1_j1' : None,
        'movimientoEnX2_j1' : None,
        'movimientoEnY2_j1' : None,
        'movimientoEnX3_j1' : None,
        'movimientoEnY3_j1' : None,
        'movimientoP1_j1' : None,
        'movimientoP2_j1' : None,
        'movimientoEnX0_j2': None,
        'movimientoEnY0_j2': None,
        'movimientoEnX1_j2' : None,
        'movimientoEnY1_j2' : None,
        'movimientoEnX2_j2' : None,
        'movimientoEnY2_j2' : None,
        'movimientoEnX3_j2' : None,
        'movimientoEnY3_j2' : None,
        'movimientoP1_j2' : None,
        'movimientoP2_j2' : None,
        'perdedor' : None
    }]
turno = 'cliente1'



@app.route('/game/checksession/matches', methods=['POST', 'GET', 'PUT'])
def matches():
    if request.method == 'GET':
        return jsonify(matchMoves)

    else:
        def cicloDecision():
            if matchMoves[len(matchMoves) - 1]['cliente1'] == None:
                matchMoves[len(matchMoves) - 1]['cliente1'] = 'listo'
                return jsonify(matchMoves)
            elif matchMoves[len(matchMoves) - 1]['cliente2'] == None:
                matchMoves[len(matchMoves) - 1]['cliente2'] = 'listo'
                return jsonify(matchMoves)
            else:
                matchMoves.append({
                    'matchID' : count +1,
                    'cliente1' : None,
                    'cliente2' : None,
                })
                return cicloDecision()
        cicloDecision()
        return jsonify(matchMoves)



@app.route('/game/checksession', methods=['POST', 'GET', 'PUT'])
def game():
    if request.method == 'GET':
        return jsonify(gameDashboard)

    else:
        def cicloDecision():
            if gameDashboard[len(gameDashboard) - 1]['cliente1'] == None:
                gameDashboard[len(gameDashboard) - 1]['cliente1'] = 'listo'
                return jsonify(gameDashboard)
            elif gameDashboard[len(gameDashboard) - 1]['cliente2'] == None:
                gameDashboard[len(gameDashboard) - 1]['cliente2'] = 'listo'
                return jsonify(gameDashboard)
            else:
                gameDashboard.append({
                    'sessionID': len(gameDashboard) + 1,
                    'cliente1': None,
                    'cliente2': None,
                    'ganadorPartida1': None,
                    'ganadorPartida2': None,
                    'ganadorPartida3': None,
                    'ganadorDelSet': None
                })
                return cicloDecision()
        cicloDecision()
        return jsonify(gameDashboard)

@app.route('/game/checksession/move/', methods=['POST', 'GET'])
def move() :
    print('LLEGUE AL MOVIMIENTO')
    if request.method == 'POST' :
        responseFromClient = request.get_json(force=True)
        print(responseFromClient)
        turno = responseFromClient[0]['usuario']
        print("TURNO "+ turno)
        def cicloMovimiento() :
            if gameMoves[len(gameMoves) - 1]['cliente1Moved'] == None:
                gameMoves[len(gameMoves) - 1]['cliente1Moved'] = "si"
                playMoves[len(playMoves) - 1]['movimientoEnX0_j1'] = responseFromClient[0]['movimientoEnX0']
                playMoves[len(playMoves) - 1]['movimientoEnY0_j1'] = responseFromClient[0]['movimientoEnY0']
                playMoves[len(playMoves) - 1]['movimientoEnX1_j1'] = responseFromClient[0]['movimientoEnX1']
                playMoves[len(playMoves) - 1]['movimientoEnY1_j1'] = responseFromClient[0]['movimientoEnY1']
                playMoves[len(playMoves) - 1]['movimientoEnX2_j1'] = responseFromClient[0]['movimientoEnX2']
                playMoves[len(playMoves) - 1]['movimientoEnY2_j1'] = responseFromClient[0]['movimientoEnY2']
                playMoves[len(playMoves) - 1]['movimientoEnX3_j1'] = responseFromClient[0]['movimientoEnX3']
                playMoves[len(playMoves) - 1]['movimientoEnY3_j1'] = responseFromClient[0]['movimientoEnY3']
                playMoves[len(playMoves) - 1]['movimientoP1_j1'] = responseFromClient[0]['movimientoP1']
                playMoves[len(playMoves) - 1]['movimientoP2_j1'] = responseFromClient[0]['movimientoP2']

                #guarda la partida de la sesion
                if gameDashboard[len(gameDashboard) - 1]['ganadorPartida1'] == None:
                    gameDashboard[len(gameDashboard) - 1]['ganadorPartida1'] = responseFromClient[0]['ganadorPartida']
                elif gameDashboard[len(gameDashboard) - 1]['ganadorPartida2'] == None:
                    gameDashboard[len(gameDashboard) - 1]['ganadorPartida2'] = responseFromClient[0]['ganadorPartida']
                elif gameDashboard[len(gameDashboard) - 1]['ganadorPartida3'] == None:
                    gameDashboard[len(gameDashboard) - 1]['ganadorPartida3'] = responseFromClient[0]['ganadorPartida']

                print(playMoves[len(playMoves) - 1])
                return playMoves
            elif gameMoves[len(gameMoves) - 1]['cliente2Moved'] == None:
                gameMoves[len(gameMoves) - 1]['cliente2Moved'] = "si"
                playMoves[len(playMoves) - 1]['movimientoEnX0_j2'] = responseFromClient[0]['movimientoEnX0']
                playMoves[len(playMoves) - 1]['movimientoEnY0_j2'] = responseFromClient[0]['movimientoEnY0']
                playMoves[len(playMoves) - 1]['movimientoEnX1_j2'] = responseFromClient[0]['movimientoEnX1']
                playMoves[len(playMoves) - 1]['movimientoEnY1_j2'] = responseFromClient[0]['movimientoEnY1']
                playMoves[len(playMoves) - 1]['movimientoEnX2_j2'] = responseFromClient[0]['movimientoEnX2']
                playMoves[len(playMoves) - 1]['movimientoEnY2_j2'] = responseFromClient[0]['movimientoEnY2']
                playMoves[len(playMoves) - 1]['movimientoEnX3_j2'] = responseFromClient[0]['movimientoEnX3']
                playMoves[len(playMoves) - 1]['movimientoEnY3_j2'] = responseFromClient[0]['movimientoEnY3']
                playMoves[len(playMoves) - 1]['movimientoP1_j2'] = responseFromClient[0]['movimientoP1']
                playMoves[len(playMoves) - 1]['movimientoP2_j2'] = responseFromClient[0]['movimientoP2']

                if gameDashboard[len(gameDashboard) - 1]['ganadorPartida1'] == None:
                    gameDashboard[len(gameDashboard) - 1]['ganadorPartida1'] = responseFromClient[0]['ganadorPartida']
                elif gameDashboard[len(gameDashboard) - 1]['ganadorPartida2'] == None:
                    gameDashboard[len(gameDashboard) - 1]['ganadorPartida2'] = responseFromClient[0]['ganadorPartida']
                elif gameDashboard[len(gameDashboard) - 1]['ganadorPartida3'] == None:
                    gameDashboard[len(gameDashboard) - 1]['ganadorPartida3'] = responseFromClient[0]['ganadorPartida']

                print(playMoves[len(playMoves) - 1])
                return playMoves
            else:
                gameMoves.append({
                    'moveID' : len(gameMoves)+ 1,
                    'cliente1Moved' : None,
                    'cliente2Moved' : None,
                })
                return cicloMovimiento()
        cicloMovimiento()

    else :
        #if gameMoves[len(gameMoves) - 1]['cliente2Moved'] == None:
            #gameMoves[len(gameMoves) - 1]['cliente2Moved'] = "si"
        return jsonify(playMoves)


@app.route('/game/checksession/turno/<sessionID>', methods=['GET'])
def turno(sessionID) :
    if request.method == 'GET':
        print(sessionID)
        if gameMoves[len(gameMoves)-1]['cliente1Moved'] == None :
            return  'cliente1'
        elif gameMoves[len(gameMoves)-1]['cliente2Moved'] == None :
            return 'cliente2'
        else :
            return 'cliente1'

@app.route('/game/checkgame/', methods=['GET'])
def checkgame() :
    return jsonify(gameDashboard)



if __name__ == '__main__':
    app.run()
