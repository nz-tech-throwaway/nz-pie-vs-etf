# Description

This uses the block bootstrap method to sample historic index returns in "blocks", as annual returns tend to be dependent on previous years. 
100,000 random samples of 40 year periods are created from the S&P 500 annual return data from 1974 to 2025. Block sizes are 4 years, so rather than selecting 40 random years, block bootstrapping selects random 4-year chunks. For example, a block might be "2008, 2009, 2010, 2011".

Two approaches are compared: investing $100,000 into a New Zealand-domiciled PIE fund, and purchasing $100,000 shares of VOO (S&P 500 ETF provided by Vanguard).

A 0.25% fee is applied to the PIE fund, and a 0.03% fee is applied to the ETF.

This applies fees, FIF calculations, and taxes annually rather than monthly or three times a year. It also assumes the PIE fund is holding VOO and not the underlying assets directly. It does not apply any accountancy fees for calculating FIF yourself. Unfortunately, due to difficulty in getting good quality data, it uses currency exchange rates and index values for December of each year, rather than March. NZ tax is calculated for the NZ financial year, so this is inconsistent with reality.

This is also a single lump sum without subsequent contributions except reinvesting the returns.

This **does** account for currency fluctuations. However, this truncated the dataset down to only years since 1974, because New Zealand didn't float the NZD against the USD until then. This also results in a bias towards the PIE funds relative to a larger dataset, because there are a lower proportion of negative years since 1974 than since, say, 1890.

# Results

For 39% income tax bracket individuals:
```
Mean FDR or CV outcome (ETF)    :  $7,537,760.21
Mean FDR only outcome (PIE fund):  $7,875,846.58
CV method chosen 27.1% of the time
The PIE fund beats directly holding the ETF in 62109 samples out of 100000 (62.1%)
```

For 33% income tax bracket individuals:
```
Mean FDR or CV outcome (ETF)    :  $8,142,474.76
Mean FDR only outcome (PIE fund):  $7,842,175.81
CV method chosen 27.1% of the time
The PIE fund beats directly holding the ETF in 3994 samples out of 100000 (4.0%)
```
