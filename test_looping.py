import time
import datetime
import random
n=0

maksimal = range(10)

for i in maksimal:
    n+=2
    print(n)
    time.sleep(1)

    print(random.randrange(30, 50))