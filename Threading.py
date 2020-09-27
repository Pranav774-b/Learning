# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 16:01:02 2020

@author: PranavM
"""

import threading
from queue import Queue
import time

print_lock = threading.Lock()

def exampleJob(worker):
    time.sleep(0.5) # pretend to do some work.
    
    with print_lock:
        print(threading.current_thread().name, worker)
    
# The threader thread pulls an worker from the queue and processes it
def threader():
    while True:
        worker=q.get()
        exampleJob(worker)
        q.task_done()
        

q=Queue()

#how many threads are allowed for 
for x in range(10):
    t=threading.Thread(target=threader)
    t.daemon = True #This will die when the main thread dies
    
    t.start() #This will start the threading 

start = time.time()

#20 jobs assigned 
for worker in range(20): 
    q.put(worker)
    
q.join()

# with 10 workers and 20 tasks, with each task being .5 seconds, then the completed job
# is ~1 second using threading. Normally 20 tasks with .5 seconds each would take 10 seconds.

print('Entire Job took:',time.time()-start)

