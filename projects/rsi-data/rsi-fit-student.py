import pandas as pd
import numpy as np
from scipy.stats import norm, chisquare, ttest_ind, ttest_1samp
import matplotlib.pyplot as plt

"""
Preamble: Load data from source CSV file
"""
### YOUR CODE HERE
# Loaded the csv as a panda dataframe
path = "../../data/drop-jump/all_participant_data_rsi.csv"
data = pd.read_csv(path)

"""
Question 1: Load the force plate and acceleration based RSI data for all participants. Map each data set (accel and FP)
to a normal distribution. Clearly report the distribution parameters (mu and std) and generate a graph to each curve's 
probability distribution function. Include appropriate labels, titles, and legends.
"""
print('-----Question 1-----')

### YOUR CODE HERE
# Loaded the force plate and acceleration based RSI data
force_plate = data["force_plate_rsi"]
accel = data["accelerometer_rsi"]

# Mapped each data set (accel and FP) to a normal distribution and generated their respective graphs
## START OF FORCE PLATE RSI GRAPH AND ANSWER ##

# Gathered the mean and standard deviation
plate_mu = force_plate.mean()
plate_std = force_plate.std()

# Reported the distribution parameters
print("The force plate distribution parameters are", plate_mu, "(mu) and", plate_std, "(standard deviation).")

# Creates density-based histogram graph
count, bins, ignored = plt.hist(force_plate, bins=20, density=True, label='Binned Force Plate Distribution',
                                edgecolor='k')

# Creates normal distribution curve based on the data
x = np.linspace(min(force_plate), max(force_plate), 100)
plt.plot(x, norm.pdf(x, loc=plate_mu, scale=plate_std,), label='Expected Force Plate Normal Distribution')

# Graph labels
plt.xlabel("Standard Deviation")
plt.ylabel("Probability Density")
plt.title("Force Plate Distribution")
plt.legend()
plt.show()


## START OF ACCELEROMETER RSI GRAPH AND ANSWER ##

# Gathered the mean and standard deviation
accel_mu = accel.mean()
accel_std = accel.std()

# Reported the distribution parameters
print("The accelerometer distribution parameters are", accel_mu, "(mu) and", accel_std, "(standard deviation).")

# Creates density-based histogram graph
count, bins, ignored = plt.hist(accel, bins=20, density=True, label='Binned Accelerometer Distribution',edgecolor='k')

# Creates normal distribution curve based on the data
x = np.linspace(min(accel), max(accel), 100)
plt.plot(x, norm.pdf(x, loc=accel_mu, scale=accel_std,), label='Expected Accelerometer Normal Distribution')

# Graph labels
plt.xlabel("Standard Deviation")
plt.ylabel("Probability Density")
plt.title("Accelerometer Distribution")
plt.legend()
plt.show()

"""
Question 2: Conduct a Chi2 Goodness of Fit Test for each dataset to test whether the data is a good fit
for the derived normal distribution. Clearly print out the p-value, chi2 stat, and an indication of whether it is 
a fit or not. Do this for both acceleration and force plate distributions. It is suggested to generate 9 bins between 
[0,2), add append -inf and +inf to both ends of the bins. An alpha = 0.05 is suitable for these tests.
"""
print('\n\n-----Question 2-----')

"""
Acceleration
"""
### YOUR CODE HERE

# Created 9 bins from 0 to 2, appended -inf and +inf, added them to a histogram
accel_bins = np.linspace(0, 2, 10)
accel_bins = np.r_[-np.inf, accel_bins, np.inf]
accel_counts, accel_edges = np.histogram(accel, bins=accel_bins, density=False)

# Expected values to test against
accel_expected_mu = 0.7
accel_expected_std = 0.3

# Generated the frequency of each bin
accel_expected_prob = np.diff(norm.cdf(accel_bins, loc=accel_expected_mu, scale=accel_expected_std))
accel_expected_counts = accel_expected_prob * len(accel)

# Chi2 Test
(accel_chi_stat, accel_p_value) = chisquare(f_obs=accel_counts, f_exp=accel_expected_counts, ddof=2)

# Reported Chi2 stat and p-value
print("The Chi2 stat for the accelerometer RSI data is", accel_chi_stat, "and the p-value is", accel_p_value)

# Alpha comparison if data is good or not to the expected values
alpha = 0.05
if accel_p_value < alpha:
    print("The accelerometer data doesn't match the expected data.\n")
else:
    print("The accelerometer data does match the expected data.\n")


"""
Force Plate
"""
### YOUR CODE HERE
# Created 9 bins from 0 to 2, appended -inf and +inf, added them to a histogram
plate_bins = np.linspace(0, 2, 10)
plate_bins = np.r_[-np.inf, plate_bins, np.inf]
plate_counts, plate_edges = np.histogram(force_plate, bins=plate_bins, density=False)

# Expected values to test against
plate_expected_mu = 0.7
plate_expected_std = 0.3

# Generated the frequency of each bin
plate_expected_prob = np.diff(norm.cdf(plate_bins, loc=plate_expected_mu, scale=plate_expected_std))
plate_expected_counts = plate_expected_prob * len(force_plate)

# Chi2 Test
(plate_chi_stat, plate_p_value) = chisquare(f_obs=plate_counts, f_exp=plate_expected_counts, ddof=2)

# Reported Chi2 stat and p-value
print("The Chi2 stat for the force plate RSI data is", plate_chi_stat, "and the p-value is", plate_p_value)

# Alpha comparison if data is good or not to the expected values
alpha = 0.05
if plate_p_value < alpha:
    print("The force plate data doesn't match the expected data.\n")
else:
    print("The force plate data does match the expected data.\n")

"""
Question 3: Perform a t-test to determine whether the RSI means for the acceleration and force plate data are equivalent 
or not. Clearly report the p-value for the t-test and make a clear determination as to whether they are equal or not.
An alpha = 0.05 is suitable for these tests.
"""
print('\n\n-----Question 3-----')

### YOUR CODE HERE
# Performed 2-sided t-test as it compares two samples
(RSI_stat, RSI_p_value) = ttest_1samp(force_plate, popmean=accel_mu, alternative='two-sided')

# Reported p-value of RSI from the t-test
print("The p-value for the t-test between the two sets of data is", RSI_p_value)

# Alpha comparison if data is good or not to the expected values
alpha = 0.05
if RSI_p_value < alpha:
    print("The force plate and acceleration RSI means are not equivalent.")
else:
    print("The force plate and acceleration RSI means are equivalent.")


"""
Question 4: Calculate the RSI Error for the dataset where error is expressed as the difference between the 
Force Plate RSI measurement and the Accelerometer RSI measurement. Fit this error distribution to a normal curve and 
plot a histogram of the data on the same plot showing the fitted normal curve. Include appropriate labels, titles, and 
legends. The default binning approach from matplot lib with 16 bins is sufficient.
"""

### YOUR CODE HERE
# RSI error being the difference of Accelerometer RSI subtracted from Force Plate RSI
RSI_error = force_plate - accel

# Created a weighted histogram of the RSI Error
count, bins, ignored = plt.hist(RSI_error, density=True, label='Binned RSI Error Distribution',edgecolor='k')

# Found mean and standard deviation
RSI_error_mu = RSI_error.mean()
RSI_error_std = RSI_error.std()

# Created a normal distribution curve based on the RSI Error
x = np.linspace(min(RSI_error), max(RSI_error), 100)
plt.plot(x, norm.pdf(x, loc=RSI_error_mu, scale=RSI_error_std), label='Expected RSI Error Normal Distribution')

# Graph labels
plt.xlabel("Standard Deviation")
plt.ylabel("Probability Density")
plt.title("RSI Error Distribution")
plt.legend()
plt.show()