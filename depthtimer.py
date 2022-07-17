from stockfish import Stockfish
import string
import random
import time

stockfish = Stockfish()
stockfish.update_engine_parameters({"Hash": 8196, "Threads": 8})

for i in range(1,41):
    stockfish.set_depth(i)
    start = time.time()
    stockfish.get_best_move()
    end = time.time()
    print (str(i) + ": " + str(end - start))
