from stockfish import Stockfish
import time
stockfish = Stockfish()
stockfish.set_depth(20)
stockfish.update_engine_parameters({"Hash": 8196, "Threads": 8})

stockfish.set_position(["b2b3", "d7d5", "d2d4", "b8c6", "c1b2", "c8g4", "h2h3", "g4h5"])

start = time.time()
data = []
for i in range(10000):
    stockfish.get_best_move_time(1)

end = time.time()

print(end - start)

start = time.time()
for i in range(10000):
    stockfish.get_best_move_time(2)

end = time.time()

print(end - start)


