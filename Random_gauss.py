#!/usr/bin/env python
import matplotlib.pyplot as plt
import random
import numpy as np
from scipy.stats import norm

gauss = list()

for i in range(0, 1000):
 gauss.append(random.gauss(-2, 1))

y = norm.pdf(gauss,-2,1)
print(gauss)
plt.plot(gauss,y)
plt.show()

