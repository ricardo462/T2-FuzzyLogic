import numpy as np
import matplotlib.pyplot as plt

efectividad = [12, 17, 25, 25]
altura = [170, 195, 220, 220]
sprint = [0, 0, 10, 15]
y = [0, 1, 1, 0]

plt.figure(figsize = (10, 5))
plt.plot(efectividad, y)
plt.show()