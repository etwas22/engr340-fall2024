import matplotlib.pyplot as plt
import numpy as np

"""
Step 0: Select which database you wish to use.
"""

# database name
database_name = 'mitdb_201'

# path to ekg folder
path_to_folder = "../../../data/ekg/"

# select a signal file to run
signal_filepath = path_to_folder + database_name + ".csv"

"""
Step #1: load data in matrix from CSV file; skip first two rows. Call the data signal.
"""

signal = 0
## YOUR CODE HERE ##
signal = np.loadtxt(signal_filepath, delimiter = ',', skiprows = 2)
window_len = 12
#time = signal[:,0]
lead = signal[:,2]


"""
Step 2: (OPTIONAL) pass data through LOW PASS FILTER (fs=250Hz, fc=15, N=6). These may not be correctly in radians
"""

## YOUR CODE HERE ##

"""
Step 3: Pass data through weighted differentiator
"""

## YOUR CODE HERE ##
diff = np.diff(lead)

"""
Step 4: Square the results of the previous step
"""
 ## YOUR CODE HERE ##
square = np.square(diff)

"""
Step 5: Pass a moving filter over your data
"""

## YOUR CODE HERE
ave = np.convolve(square, np.ones(window_len), mode = 'same')

# make a plot of the results. Can change the plot() parameter below to show different intermediate signals
plt.title('Moving Signal for ' + database_name)
plt.plot(ave)
plt.xlim(0, 5000)
plt.ylim(0, 0.2)
plt.ylabel("Lead (mV)")
plt.xlabel("Index")
plt.show()