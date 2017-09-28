from random import random
list = []

bound = 1000000

for i in range(10000):
    list.append(str(int(random()*bound)))

print(' '.join(list))

print('\n'.join([' '.join(sorted([str(int(random()*bound)),str(int(random()*bound))])) for i in range(1000)]))


