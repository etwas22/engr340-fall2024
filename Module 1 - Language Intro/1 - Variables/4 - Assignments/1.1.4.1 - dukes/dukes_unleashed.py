"""
For investments over $1M it can be typically assumed that they will return 5% forever.
Using the [2022 - 2023 JMU Cost of Attendance](https://www.jmu.edu/financialaid/learn/cost-of-attendance-undergrad.shtml),
calculate how much a rich alumnus would have to give to pay for one full year (all costs) for an in-state student
and an out-of-state student. Store your final answer in the variables: "in_state_gift" and "out_state_gift".

Note: this problem does not require the "compounding interest" formula from the previous problem.

"""

### Your code here ###
# For easy reference, in-state cost is $32,248 and out-of-state cost is $49,482
rate = 5
in_state = 30792
out_of_state = 47882
year = 1

# Finding donation amount of in-state
in_donate = in_state / ((rate / 100) * year)
print(in_donate)

# Finding donation amount of out-of-state
out_donate = out_of_state / ((rate / 100) * year)
print(out_donate)


in_state_gift = 615840.00

out_state_gift = 957640.00