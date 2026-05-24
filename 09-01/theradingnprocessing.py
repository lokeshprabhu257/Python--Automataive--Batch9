import threading
import multiprocessing
import time

def count_numbers(n):
    result = 0
    for i in range(n):
        result += i
    return result

if __name__ == '_main_':
    print("Speed Test (100K count)")
    print("="*30)
    
    # 1. NORMAL
    print("\n1 Normal")
    start = time.time()
    r1 = count_numbers(100000)  # 100K!
    r2 = count_numbers(100000)
    normal_time = time.time() - start
    print(f"Time: {normal_time:.3f}s")
    
    # 2. THREADING  
    print("\n2 Threading")
    t1 = threading.Thread(target=count_numbers, args=(100000,))
    t2 = threading.Thread(target=count_numbers, args=(100000,))
    start = time.time()
    t1.start(); t2.start()
    t1.join(); t2.join()
    thread_time = time.time() - start
    print(f"Time: {thread_time:.3f}s")
    
    # 3. PROCESSING
    print("\n3 Processing")
    p1 = multiprocessing.Process(target=count_numbers, args=(100000,))
    p2 = multiprocessing.Process(target=count_numbers, args=(100000,))
    start = time.time()
    p1.start(); p2.start()
    p1.join(); p2.join()
    proc_time = time.time() - start
    print(f"Time: {proc_time:.3f}s")
    
    print(f"\n  {normal_time/proc_time:.1f}x faster!")