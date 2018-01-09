import pickle
import pandas as pd
from collections import OrderedDict

class Predictor:
    def __init__(self):
        file_object = open('big_model', 'rb')
        self.model = pickle.load(file_object)

    def predict(self, params):
        od = OrderedDict()
        od['sales'] = [params['sales']]
        od['operating_profit'] = [params['operating_profit']]
        od['interest_income_and_other'] = [params['interest_income_and_other']]
        od['interest_expense'] = [params['interest_expense']]
        od['tax'] = [params['tax']]
        od['cash_and_equivalents'] = [params['cash_and_equivalents']]
        od['accounts_receivable'] = [params['accounts_receivable']]
        od['other_current_receivables'] = [params['other_current_receivables']]
        od['inventory'] = [params['inventory']]
        od['intangible_assets'] = [params['intangible_assets']]
        od['fixed_assets'] = [params['fixed_assets']]
        od['other_non_current_assets'] = [params['other_non_current_assets']]
        od['short_term_debt'] = [params['short_term_debt']]
        od['accounts_payable'] = [params['accounts_payable']]
        od['other_current_liabilities'] = [params['other_current_liabilities']]
        od['long_term_debt'] = [params['long_term_debt']]
        od['other_long_term_liabilities'] = [params['other_long_term_liabilities']]
        od['total_shareholders_equity'] = [params['total_shareholders_equity']]
        
        df = pd.DataFrame.from_dict(od)
        
        result = self.model.predict(df)
        
        return int(result[0])
