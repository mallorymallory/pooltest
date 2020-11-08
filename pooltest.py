import multiprocessing
import time


def fuck(name, name2, name3, other, manObj):
    print(name)
    if name3 == 3:
        time.sleep(2)
    mano = manObj[other[0]]
    mano[other[1]] = (name*name2*name3)
    manObj[other[0]] = mano
    return name* name2 * name3

def error(huh):
    print('huh', huh)
    
def success(huh):
    print('uwu', huh)
        
if __name__ == '__main__':
    
    man = multiprocessing.Manager()
    mlist = man.list([])
    
    A = []
    for x in range(3):
        listies = {'0':[1,2,3], '1':[4,5,6], '2':[7,8,9]}
        #listies = [[1,2,3], [4,5,6], [7,8,9], [10,11,12], [13, 14, 15]]
        mlist.insert(x, [None]*len(listies))
        if type(listies) == list:
            for y in range(len(listies)):
                listies[y].extend([[x, y], mlist])
        elif type(listies) == dict:
            for y in range(len(listies)):
                listies[str(y)].extend([[x, y], mlist])
            
        a = multiprocessing.Pool(4)
        b = a.starmap_async(fuck, iterable=list(listies.values()), error_callback=error, callback=success)
        A.insert(x, [a, b])
        
        
        if len(A) == 0:
            pass
        else:
            for y in range(len(A)):
                if type(A[y][1]) != list:
                    if A[y][1].ready():
                        print('ready')
                        A[y][1] = A[y][1].get()
                    else:
                        pass
        time.sleep(1)
        
        print(A)
        print(mlist)
        print('-'*200)
    
    