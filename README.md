# Description

This uses the block bootstrap method to sample historic index returns in "blocks", as annual returns tend to be dependent on previous years. 
100,000 random samples of 40 year periods are created from the S&P 500 annual return data from 1928 to 2025. Block sizes are 4 years, so rather than selecting 40 random years, block bootstrapping selects random 4-year chunks. For example, a block might be "2008, 2009, 2010, 2011".

Two approaches are compared: investing $100,000 into a New Zealand-domiciled PIE fund, and purchasing $100,000 shares of VOO (S&P 500 ETF provided by Vanguard).

A 0.25% fee is applied to the PIE fund, and a 0.03% fee is applied to the ETF.

This does not currently account for currency fluctuations, and applies fees, FIF calculations, and taxes annually rather than monthly or three times a year. It also assumes the PIE fund is holding VOO and not the underlying assets directly. It does not apply any accountancy fees for calculating FIF yourself. 

This is also a single lump sum without subsequent contributions except reinvesting the returns.

# Results

```
Mean FDR or CV outcome (ETF)    :  $1,443,384.77
Mean FDR only outcome (PIE fund):  $1,207,808.48
CV method chosen 16.06567% of the time
The PIE fund beats directly holding the ETF in 0 samples out of 100000 (0.0%)
```

Even when comparing the top tax bracket of 39% with the top PIR of 28%, the PIE fund always loses out in the long term, because it is unable to use the Comparative Value (CV) method of calculating FIF tax in years where returns are <5%.
