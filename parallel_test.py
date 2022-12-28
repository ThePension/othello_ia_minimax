import threading
from othello_no_gui import OthelloNoGUI
import multiprocessing as mp

def play_game():
    return OthelloNoGUI()._new_game()

if __name__ == "__main__":
    pool = mp.Pool(mp.cpu_count())
    
    results = [result for result in pool.starmap(play_game, [() for i in range(16)]) if result is not None]
    
    pool.close()
    
    # Get the percentage of wins for each player
    black_wins = 0
    white_wins = 0
    for result in results:
        if result == 'B':
            black_wins += 1
        elif result == 'W':
            white_wins += 1
            
    print(f"Black wins: {black_wins / len(results) * 100} %")
    print(f"White wins: {white_wins / len(results) * 100} %")