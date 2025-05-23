import threading


lock = threading.Lock()

def thread1():
    l =[]
    for i in range(30):
        l.append(i)
    
    with lock:
        for i in l:
            print("thread1",i)

def thread2():
    l =[]
    for i in range(30):
        l.append(i)    
    
    with lock:    
        for i in l:
            print("thread2",i)


def main():
    th1 = threading.Thread(target=thread1)
    th2 = threading.Thread(target=thread2)

    th1.start()
    th2.start()
    

    th1.join()
    th2.join()
    
    print("fin")

if __name__ == '__main__':
    main()