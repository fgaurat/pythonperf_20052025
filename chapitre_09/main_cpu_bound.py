import time
import threading
import multiprocessing
def count():
    x = 0
    for _ in range(50_000_000):
        x+=1


def run_sequentielle():
    start = time.time()
    count()
    count()
    end = time.time()
    print(f"run_sequentielle {end-start:.3f}s")

def run_threading():
    start = time.time()
    t1 = threading.Thread(target=count)
    t2 = threading.Thread(target=count)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    
    end = time.time()
    print(f"run_threading {end-start:.3f}s")

def run_multiprocessing():
    start = time.time()
    p1 = multiprocessing.Process(target=count)
    p2 = multiprocessing.Process(target=count)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    
    end = time.time()
    print(f"run_multiprocessing {end-start:.3f}s")

def main():
    run_sequentielle()
    run_threading()
    run_multiprocessing()

if __name__ == '__main__':
    main()