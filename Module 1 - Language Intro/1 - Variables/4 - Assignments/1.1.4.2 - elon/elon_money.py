"""
This problem requires you to calculate compounding interest and final value of a  US treasury deposit based upon
current interest rates (that will be provided). Your analysis should return the final value of the investment
after a 10-year and 20-year period. The final values should be stored in the variables "ten_year_final"
and "twenty_year_final", respectively. Perform all your calculations in this file. Do not perform the calculations by hand
and simply write in the final result.

Prompt: On October 27th, 2022, Elon Musk purchased Twitter for $44B in total, with reportedly $33B of his own money. Since
that time, it appears this investment has not worked out. If Elon has instead bought $44B of US Treasury Bonds, how much
would his investment be worth in 10-year and 20-year bonds? Assume the 10-year bonds pay 3.96%,
the 20-year bonds pay 4.32%, with each compounding annually.
"""

### all your code below ###

# Constant variables
Principal = 33000000000   # Initial amount of money

# Variables to use for 10-year period
N_10 = 10         # Number of years
R_10 = 3.96       # Interest rate

# 10 year calculation
ten_year = Principal * ((1 + (R_10/100)) ** N_10)
print(ten_year)

# Variables to use for 20-year period
N_20 = 20         # Number of years
R_20 = 4.32       # Interest rate

# 20 year calculation
twenty_year = Principal * (pow(1 + (R_20/100), N_20))
print(twenty_year)


# final answer for 10-year
ten_year_final = 48660509081.78675

# final answer for 20-year
twenty_year_final = 76889229275.98897