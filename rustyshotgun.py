from stockfish import Stockfish
import time
stockfish = Stockfish()
stockfish.set_depth(20)
stockfish.update_engine_parameters({"Hash": 8196, "Threads": 8})

stockfish.set_position(["b2b3", "d7d5", "d2d4", "b8c6", "c1b2", "c8g4", "h2h3", "g4h5"])

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

go(1,0.05)
go(250, 0.15)
go(20,20)
go(40,40)
go(1,1500)
go(1,10000)
go(1,30000)
go(1,60000)
go(1,120000)
go(1,300000)