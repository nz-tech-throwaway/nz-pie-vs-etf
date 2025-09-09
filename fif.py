import numpy as np

def cv_method_taxable_income(opening_value, closing_value):
    return max(0, closing_value - opening_value)

def fdr_method_taxable_income(opening_value):
    return opening_value * 0.05

def choose_fif_taxable_income(opening_value, closing_value):
    annual_return = ((closing_value - opening_value) / opening_value)
    if annual_return >= 0.05:
        return fdr_method_taxable_income(opening_value)
    else:
        return cv_method_taxable_income(opening_value, closing_value)

def cv_or_fdr(annual_return):
    if annual_return >= 5:
        return 'fdr'
    else:
        return 'cv'
    
def count_cv_or_fdr(synthetic_market_data: np.ndarray):
    cv_count = 0
    for annual_return in synthetic_market_data:
        if(cv_or_fdr(annual_return) == 'cv'):
            cv_count += 1
    return cv_count

def calculate_fif(synthetic_market_data: np.ndarray, initial_investment_nzd, tax_rate, fund_fee):
    total_investment_usd = initial_investment_nzd * synthetic_market_data[0][2]
    value_over_time_nzd = []
    for current_year in synthetic_market_data:
        current_year_returns_usd = total_investment_usd * (current_year[1] / 100)
        current_year_value_before_tax_and_fees = total_investment_usd + current_year_returns_usd
        total_investment_usd = (current_year_value_before_tax_and_fees - (choose_fif_taxable_income(total_investment_usd, current_year_value_before_tax_and_fees) * tax_rate)) - (current_year_value_before_tax_and_fees * fund_fee)
        value_over_time_nzd.append(total_investment_usd / current_year[3])
        
    return value_over_time_nzd

def calculate_fif_only_fdr(synthetic_market_data: np.ndarray, initial_investment_nzd, tax_rate, fund_fee):
    total_investment_usd = initial_investment_nzd * synthetic_market_data[0][2]
    value_over_time_nzd = []
    for current_year in synthetic_market_data:
        current_year_returns_usd = total_investment_usd * (current_year[1] / 100)
        current_year_value_before_tax_and_fees = total_investment_usd + current_year_returns_usd
        total_investment_usd = current_year_value_before_tax_and_fees - (fdr_method_taxable_income(total_investment_usd) * tax_rate) - (current_year_value_before_tax_and_fees * fund_fee)
        value_over_time_nzd.append(total_investment_usd / current_year[3])
        
    return value_over_time_nzd
