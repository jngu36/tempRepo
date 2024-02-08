import time

def timer(func):
    start_time = time.time()

    end_time = time.time()
    return "Time:"+ round(end_time - start_time, 1) + "s"

def doSomething(n):
    for x in range(1,n):
        print(x)

#==========================================

func = doSomething
timer(500)