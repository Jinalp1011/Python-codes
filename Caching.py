import time
from functools import  lru_cache

@lru_cache(maxsize=3)
def some_work(n):
    time.sleep(n) #some task takin n seconds
    return n

if __name__ == '__main__':
    print("now running some work")
    some_work(3)
    some_work(1)
    some_work(6)
    some_work(9)
    print("done....calling again")
    input()
    some_work(3)
    print("called again")


