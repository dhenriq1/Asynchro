import threading
from queue import Queue

print_lock = threading.Lock()

def threadTest(worker):
    # when this exits, the print_lock is released
    with print_lock:
        print(worker)

def threader():
  while True:
    # get the job from the front of the queue
    threadTest(q.get())
    q.task_done()

q = Queue()
for x in range(5):
    thread = threading.Thread(target = threader)
    # this ensures the thread will die when the main thread dies
    # can set t.daemon to False if you want it to keep running
    thread.daemon = True
    thread.start()

for job in range(10):
    q.put(job)
