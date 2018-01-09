## Overview
This microservice provides company stability scoring based on its financial results. As input it gets information about profits, taxes, costs, etc and as output service provides value from 0 up to 100 (0 - most unstable and 100 - most stable).

General idea of this scoring was got from CompanyWatch HScore but implementation is completely independent. Base of this scoring model is open source gradient boosting library XGBoost.

Technology tags: Python, Pandas, Flask, Pickle, XGBoost

## Example of usage
#### Server
```
v:~/ml/python/hscore/ml-score$ python3 service.py 
 * Running on http://127.0.0.1:3000/ (Press CTRL+C to quit)
```

#### Client
```python
import requests, json
url = 'http://127.0.0.1:3000/api'
params =      {  'sales': 732489.79666,
                 'operating_profit': 15820.70435,
                 'interest_income_and_other': 97.12503,
                 'interest_expense': -1696.09344,
                 'tax': -3.56581,
                 'cash_and_equivalents': 2951.27727,
                 'accounts_receivable': 17335.54630,
                 'other_current_receivables': 116476.57912,
                 'inventory': 85034.15932,
                 'intangible_assets': 4238.80328,
                 'fixed_assets': 23485.19226,
                 'other_non_current_assets': 29.83469,
                 'short_term_debt': 0.00000,
                 'accounts_payable': 93434.85948,
                 'other_current_liabilities': 71309.01155,
                 'long_term_debt': 0.00000,
                 'other_long_term_liabilities': 45626.06055,
                 'total_shareholders_equity': 39181.46066
               } 
data = json.dumps(params)
r = requests.post(url, data)
print(r.json())
#{'results': 48}
```
