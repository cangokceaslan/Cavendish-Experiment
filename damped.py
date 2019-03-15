import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statistics as st
data = pd.read_csv('damped.txt', sep=" ", header=None,delimiter="\t")
datapointx = []
datapointy = []
countAll = 0
for a in range(data[1].size):
    if a > 3000:
        datapointx.append(data[0][a])
        datapointy.append(data[1][a])
        countAll += data[1][a]
mean = countAll / (data[1].size - 3000)
standard_deviation = st.stdev(datapointy)
plt.plot(datapointx, datapointy)
plt.legend("Resonance")
plt.xlabel("time")
plt.ylabel("voltage")
plt.legend("Sine")
plt.show()
