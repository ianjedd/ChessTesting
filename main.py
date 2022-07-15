from stockfish import Stockfish
stockfish = Stockfish()
stockfish.set_depth(40)
stockfish.update_engine_parameters({"Hash": 4096, "Threads": 6})
#Wall-facer
#stockfish.set_position(["b2b3", "d7d5", "d2d4", "b8c6"])
stockfish.set_position(["b2b3", "e7e5"])
data = []
while True:
    print(stockfish.get_best_move_time(1))
