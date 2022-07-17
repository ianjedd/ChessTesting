from stockfish import Stockfish
import string
import random
stockfish = Stockfish()
stockfish.set_depth(20)
stockfish.update_engine_parameters({"Hash": 8196, "Threads": 8})

game = []

i = 0
filename = "fights/" + ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10)) + ".txt"
#print(filename)
datastream = open(filename, 'w')
initGame = []
for x in initGame:
    stockfish.make_moves_from_current_position([x])


while True:

    game.append(stockfish.get_best_move_time(10000));

    print(game[i])
    stockfish.make_moves_from_current_position([game[i]])
    print(stockfish.get_evaluation())


    game.append(stockfish.get_best_move_time(1))
    i += 1

    print(game[i])



    stockfish.make_moves_from_current_position([game[i]])
    print(stockfish.get_evaluation())
    #print(str(i) + "::")
    #print(stockfish.get_board_visual())

    i += 1
    print(i)
#    if i > 60:
#        break

moveCounter = 0

gameString = ""
for x in initGame:
    if (moveCounter % 2 == 0):
        gameString += str(int((moveCounter/2) + 1) ) + ". "
    gameString += x + " "
    moveCounter +=1

for x in game:
    if (moveCounter % 2 == 0):
        gameString += str(int((moveCounter/2) + 1) ) + ". "
    gameString += x + " "
    moveCounter += 1
datastream.write(gameString)
datastream.close()

#print(stockfish.get_board_visual())