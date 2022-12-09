import json
import requests
example_string = '{"datetime": "2022-12-09 09:17:32.525727", "orderid": 1, "storeid": 35, "registerid": 6, "cashierid": 1, "customerid": 464, "sku": 6137, "qty": 2, "price": 80.8, "stock_qty": 0}'

res = requests.post('http://localhost:8080/model',json=example_string)