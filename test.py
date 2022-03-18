#speed test between list and numpy array

import numpy as np
import time

n = 1000000
listed = list(range(n)) # creating a list from 0 to 1000000
nplist = np.array(listed) # creating a numpy array from 0 to 1000000

t1 = time.time() # t1 is start time of list time
for i in listed:
    k= i
t2 = time.time()
print('time of the list (second) =>', round((t2-t1), 5))
for x in nplist:
    k = x
t3 = time.time()
print('time of the numpy array (second) =>',round((t3-t2),5))
