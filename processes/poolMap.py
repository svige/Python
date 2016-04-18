#coding: utf-8
import time
from multiprocessing import Pool

def f(i):
    time.sleep(1)
    return "test" + str(i)
    

def poolMap():
    pool = Pool()
    myList = [1,2,3,4,5]
    print myList
    #"map用来实现多线程"
    ret = pool.map(f,myList)
    for r in ret:print r
    pool.close()
    pool.join()

if __name__ == "__main__":
    '''
    Pool线程池的用法,
    '''
    poolMap()
    
