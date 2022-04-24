import numpy as np
import matplotlib.pyplot as plt

trials = 10
gemsNeeded = np.zeros(trials)
for i in range(trials):
    level = 1
    gemsNeeded[i] += 1
    while level < 5:
        rng = np.random.rand()
        if rng < (1-level*0.2):
            level += 1
        gemsNeeded[i] += 1

avg = np.mean(gemsNeeded)
print(avg)

plt.hist(gemsNeeded, density=True)
plt.vlines(np.mean(avg, 0, np.amax(gemsNeeded), colors='r')
plt.xlabel("gems needed")
plt.save
