import numpy as np
import matplotlib.pyplot as plt

trials = 100000
flashMargin = 0
speeds = np.random.uniform(5, 16, trials)
times = 100 / speeds
margins = 10 - times
flashWins = np.sum(speeds > 10)

n, bins, patches = plt.hist(speeds, density=True)
plt.vlines(np.mean(speeds), 0, 1.1*max(n), colors='r')
plt.xlabel("speed (m/s)")
plt.savefig("speeds.png")
plt.clf()
n, bins, patches = plt.hist(times, density=True)
plt.vlines(np.mean(times), 0, 1.1*max(n), colors='r')
plt.xlabel("time (s)")
plt.savefig("times.png")
plt.clf()
n, bins, patches = plt.hist(margins, density=True)
plt.vlines(np.mean(margins), 0, 1.1*max(n), colors='r')
plt.xlabel("margin (s)")
plt.savefig("margins.png")

print("Flash's winning percentage: {}".format(flashWins/trials))
print("Flash's average margin: {}".format(np.mean(margins)))
