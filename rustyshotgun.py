from stockfish import Stockfish
import time
stockfish = Stockfish()
stockfish.set_depth(20)
stockfish.update_engine_parameters({"Hash": 8196, "Threads": 8})

stockfish.set_position(["e2e4", "d7d5", "e4d5", "d8d5", "b1c3", "d5d8", "d2d4"])

def getData(n, timeToSolve):
    start = time.time()
    data = []
    for i in range(n):
        data.append(stockfish.get_best_move_time(timeToSolve))

    end = time.time()
    print("n:" + str(n) + " time:" + str(timeToSolve) + " Fished in " + str(end - start) + " seconds")

    return data



def count_elements(seq) -> dict:
    hist = {}
    for i in seq:
        hist[i] = hist.get(i, 0) + 1
    return hist

def go(n, t):
    data = getData(n, t)
    counted = count_elements(data)
    print(counted)

go(1,1)
go(500, 3)
go(20,20)
go(40,40)
go(1,1500)
go(1,10000)
go(1,30000)
go(1,60000)
go(1,120000)
go(1,300000)