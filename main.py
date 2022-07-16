from stockfish import Stockfish
stockfish = Stockfish()
stockfish.set_depth(30)
stockfish.update_engine_parameters({"Hash": 8196, "Threads": 8})
#Wall-facer
#stockfish.set_position(["b2b3", "d7d5", "d2d4", "b8c6"])
#stockfish.set_position(["b2b3", "e7e5"])
#stockfish.set_position(["b2b3", "e7e5", "e2e4", "g8f6", "b1c3", "f8c5"])
#stockfish.set_position(["b2b3", "e7e5","c1b2", "b8c6", "e2e3", "g8f6", "f1b5", "f8d6", "b1a3",
 #                       "c6a5", "b5e2", "a7a6", "g1f3", "d8e7","a3b1", "e8g8", "d2d3"])
#stockfish.set_position(["b2b3", "c7c6", "c1b2", "d7d5"])
stockfish.set_position(["b2b4", "e7e5", "c1b2", "f8b4", "b2e5", "f7f6", "e5c3", "b4c3", "b1c3", "b8c6"])
data = []
for i in range(500):
    data.append(stockfish.get_best_move_time(10))

print(data)

def count_elements(seq) -> dict:
    hist = {}
    for i in seq:
        hist[i] = hist.get(i, 0) + 1
    return hist

counted = count_elements(data)
print(counted)
