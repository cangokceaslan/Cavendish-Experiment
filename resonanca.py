import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statistics as st
data = pd.read_csv('damped.txt', sep=" ", header=None,delimiter="\t")
datapointx = []
datapointy = []
countAll = 0
for a in range(data[1].size):
    if a > 4000:
        datapointx.append(data[0][a])
        datapointy.append(data[1][a])
        countAll += data[1][a]
mean = countAll / (data[1].size - 4000)
standard_deviation = st.stdev(datapointy)
plt.plot(datapointx, datapointy)
plt.legend("Resonance")
def fitterSine(t):
    w=0.03300
    A=((0.6566 - 0.33)/2)
    theta= w*t
    sin = A * np.sin(theta-60.5)
    return sin 
fity = []
timer = []
for i in range(2000,3224):
    timer.append(i)
    fity.append(fitterSine(i)+0.20)
plt.plot(timer,fity)
plt.title("Sinus fit on resonance")
plt.xlabel("time")
plt.ylabel("voltage")
plt.legend("Sine")
plt.show()
