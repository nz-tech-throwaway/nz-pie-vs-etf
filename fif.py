import numpy as np

def cv_method_taxable_income(opening_value, closing_value):
    return max(0, closing_value - opening_value)

def fdr_method_taxable_income(opening_value):
    return opening_value * 0.05

def choose_fif_taxable_income(annual_return, initial_investment_value):
    if annual_return >= 5:
        return fdr_method_taxable_income(initial_investment_value)
    else:
        return cv_method_taxable_income(initial_investment_value, initial_investment_value * (annual_return / 100))

def cv_or_fdr(annual_return):
    if annual_return >= 5:
        return 'fdr'
    else:
        return 'cv'
    
def count_cv_or_fdr(market_index: np.ndarray):
    cv_count = 0
    for annual_return in market_index:
        if(cv_or_fdr(annual_return) == 'cv'):
            cv_count += 1
    return cv_count

def calculate_fif(market_index: np.ndarray, initial_investment, tax_rate, fund_fee):
    total_investment = initial_investment
    value_over_time = []
    for annual_return in market_index:
        total_investment = total_investment +(total_investment * (annual_return[1] / 100)) - (choose_fif_taxable_income(annual_return[1], total_investment) * tax_rate) - (total_investment * fund_fee)
        value_over_time.append(total_investment)
        
    return value_over_time

def calculate_fif_only_fdr(market_index: np.ndarray, initial_investment, tax_rate, fund_fee):
    total_investment = initial_investment
    value_over_time = []
    for annual_return in market_index:
        total_investment = total_investment + (total_investment * (annual_return[1] / 100)) - (fdr_method_taxable_income(total_investment) * tax_rate) - (total_investment * fund_fee)
        value_over_time.append(total_investment)
        
    return value_over_time
