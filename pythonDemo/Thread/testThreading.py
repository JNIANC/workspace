import threading

# 创建锁
import time

threadLock = threading.Lock();
# 创建线程列表
threadList = [];

class myThread(threading.Thread):
    def __init__(self,threadId,name,counter):
        threading.Thread.__init__(self);
        self.threadId = threadId;
        self.ame = name;
        self.counter = counter;

    def run(self):
        print("start thread: "+ self.name);
        # 获取锁，同步线程
        threadLock.acquire();
        print_time(self.name,self.counter,3);
        # 释放锁，开启线程
        threadLock.release();
        print("thread Exit: "+ self.name);

def print_time(threadName,delay,counter):
    while counter:
        time.sleep(delay);
        print("{} : {}".format(threadName,time.ctime(time.time())))
        counter -=1;

# 创建线程
thread1 = myThread(1001,"thread-1",1);
thread2 = myThread(1002,"thread-2",2);

# 开启线程
thread1.start()
thread2.start()

# 添加线程列表
threadList.append(thread1)
threadList.append(thread2)

# 等待所有线程完成
for t in threadList:
   t.join()
print("exiting main_threading")