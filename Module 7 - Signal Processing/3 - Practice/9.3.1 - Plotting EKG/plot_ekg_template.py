import matplotlib.pyplot as plt
import numpy as np

# import the CSV file using numpy
path = '../../../data/ekg/mitdb_201.csv'

# load data in matrix from CSV file; skip first two rows

### Your code here ###
ekg_arr = np.asarray(np.loadtxt(path, delimiter = ',', skiprows = 2))

# save each vector as own variable

### Your code here ###
window_len = 10
time = ekg_arr[:,0]
V1 = ekg_arr[:,2]
diff_V1 = np.diff(V1)
square_V1 = np.square(diff_V1)
ave_V1 = np.convolve(square_V1, np.ones(window_len), mode = 'same')/window_len

# use matplot lib to generate a single plot
### Your code here ###

plt.plot(time, V1)
plt.xlim(0,10)
#plt.ylim(0, 0.016)
plt.xlabel("Time (s)")
plt.ylabel("V1 Lead (mV)")
plt.title("First 10 Seconds of a Heartbeat Using a V1 Lead from EKG Data")
plt.show()