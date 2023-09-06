import functools
import random
import sys

pool = ( list('A23456789JQK') + [ '10' ] ) * 4 + [ 'black_joker', 'red_joker']

def comprison(one, two):
    order = list('3456789') + [ '10' ] + list('JQKA2') + [ 'black_joker', 'red_joker']
    if( order.index(one) == order.index(two) ):
        return 0
    return [1, -1][ order.index(one) < order.index(two) ]

def choose():
    result = []
    for i in range(17):
        get = random.randrange(0, 54)
        while( not pool[get] ):
            get = random.randrange(0, 54)
        result.append( pool[get] )
        pool[get] = None
    return result

def save(get, file=''):
    if(file):
        fout = open(file, 'w+')
    else:
        fout = sys.stdout
    
    print(' '.join( sorted(get, key=functools.cmp_to_key(comprison) ) ), file=fout)

    if(file):
        fout.close()


save(choose())
save(choose())
save(choose())

while(True):
    try:
        pool.index(None)
    except:
        break
    else:
        pool.remove(None)


save(pool)