# Here I am going to try looking at binomial distributions

import numpy as np
import matplotlib.pyplot as plt

def choose(n, j):
    """ n choose j is how binomial coefficients are called in English
        which is n items, pick j
        In Russian, we call it C(n,m)
    """
    n += 1
    p = 1
    for i,j in zip(range(j+1, n), range(1, n - j)):
        p = p * i / j
    return p

# test
n = 3
a = []
for i in range(0, n+1):
    a.append(choose(n,i))

print(a)

plt.plot(range(0, n+1), a)
plt.show()

