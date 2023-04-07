import numpy as np
import random

with open('sample.txt', 'w') as my_file:
    for i in range(1,51):
        num = random.randint(1,10)
        my_file.write(str(num)+'\n')



