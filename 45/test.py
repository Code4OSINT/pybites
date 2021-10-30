from collections import deque


def my_queue(n=5):
    

mq = my_queue()
for i in range(10):
    mq.append(i)
    print((i, list(mq)))
