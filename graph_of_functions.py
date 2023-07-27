import math
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 168, 1)

y = [x_item ** 1.5 for x_item in x]

# Plot the chart
plt.plot(x, y)
plt.xlabel("number of accesses")
plt.ylabel("score")
plt.title("Graph of Functions")
plt.grid(True)
plt.show()