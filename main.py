from stockfish import Stockfish
stockfish = Stockfish()
stockfish.set_depth(30)
stockfish.update_engine_parameters({"Hash": 8196, "Threads": 8})
#Wall-facer
#stockfish.set_position(["b2b3", "d7d5", "d2d4", "b8c6"])
#stockfish.set_position(["b2b3", "e7e5"])
#stockfish.set_position(["b2b3", "e7e5", "e2e4", "g8f6", "b1c3", "f8c5"])
stockfish.set_position(["b2b3", "e7e5", "c1b2", "b8c6"])
data = []
for i in range(100):
    data.append(stockfish.get_best_move_time(3))

print(data)

def count_elements(seq) -> dict:
    hist = {}
    for i in seq:
        hist[i] = hist.get(i, 0) + 1
    return hist

counted = count_elements(data)
print(counted)
