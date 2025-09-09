import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from tsbootstrap import MovingBlockBootstrap
from fif import count_cv_or_fdr, calculate_fif, calculate_fif_only_fdr

# Import S&P 500 annual returns/value dataset
myFile = pd.read_csv('snp500.csv', sep=',').values

# Variables (change these to match what you're interested in finding out)
total_years = 40
starting_investment = 100000
income_tax_rate = 0.39
pir = 0.28
pie_fund_fee = 0.0025
etf_fund_fee = 0.003

plot_outcome = False # Change to True to generate a plot of the results

# Instantiate the bootstrap object
n_bootstraps = 100000
block_length = 4
rng = 59
mbb = MovingBlockBootstrap(
    n_bootstraps=n_bootstraps, rng=rng, block_length=block_length
)

# Generate bootstrapped samples
return_indices = False
bootstrapped_samples = mbb.bootstrap(myFile, return_indices=return_indices)

# Collect bootstrap samples
X_bootstrapped = []
for data in bootstrapped_samples:
    # If we don't do this we get a sample length the same length as the total index dataset, e.g. 98 years of S&P 500.
    # We want to generate block bootstrap samples that are only total_years in length, but sampling blocks from 
    # the entire 98 years of index data.
    random_starting_index = np.random.randint(0, data.size/4 - total_years)
    X_bootstrapped.append(data[random_starting_index:random_starting_index+total_years])

X_bootstrapped = np.array(X_bootstrapped)


# Calculations
mean_pie_outcome = 0
mean_etf_outcome = 0
etf_results = []
pie_results = []
cv_method_chosen_count = 0
pie_beats_etf_count = 0

for sample in X_bootstrapped:
    
    etf_index_result = calculate_fif(sample, starting_investment, income_tax_rate, etf_fund_fee)
    etf_results.append(etf_index_result)
    mean_etf_outcome += etf_index_result[-1]

    pie_index_result = calculate_fif_only_fdr(sample, starting_investment, pir, pie_fund_fee)
    pie_results.append(pie_index_result)
    mean_pie_outcome += pie_index_result[-1]

    cv_method_chosen_count += count_cv_or_fdr(sample[:, 1])
    if (pie_index_result[-1] >= etf_index_result[-1]):
        pie_beats_etf_count += 1


print("Mean FDR or CV outcome (ETF)    : ", '${:,.2f}'.format(mean_etf_outcome / n_bootstraps))
print("Mean FDR only outcome (PIE fund): ", '${:,.2f}'.format(mean_pie_outcome / n_bootstraps))
print("CV method chosen {:.1%} of the time".format(cv_method_chosen_count / (n_bootstraps * total_years)))
print("The PIE fund beats directly holding the ETF in {} samples out of {} ({:.1%})".format(pie_beats_etf_count, n_bootstraps, pie_beats_etf_count/n_bootstraps))


# Plot the samples and original time series

if (plot_outcome == True):
    plt.figure()
    plt.plot(myFile[:,1], label="Original Time Series", color="black")

    for i in range(n_bootstraps):
        _ = plt.plot(etf_results[i],
                    ls="--",
                    color="blue")
        
    for i in range(n_bootstraps):
        _ = plt.plot(pie_results[i],
                    ls="--",
                    color="red")

    plt.xlabel("Time (Years)")
    plt.ylabel("Value")
    plt.show()
