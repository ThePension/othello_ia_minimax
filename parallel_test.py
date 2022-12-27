from othello_no_gui import OthelloNoGUI
import multiprocessing as mp
from time import sleep

if __name__ == "__main__":
    pool = mp.Pool(mp.cpu_count())
    
    results = [pool.apply(OthelloNoGUI()._new_game) for i in range(10)]
    
    print(results)