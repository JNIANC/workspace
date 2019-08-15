import time
import _thread


def  print_time(ThreadNme,delay):
    count = 0;
    while count < 5:
        time.sleep(delay);
        count +=1;
        print("{} : {}".format(ThreadNme,time.ctime(time.time())));

try:
    _thread.start_new_thread(print_time,("thread-1",2));
    _thread.start_new_thread(print_time,("thread-2",4));
except:
    print("error");

while 1:
    # 让线程有足够的时间完成
    pass

