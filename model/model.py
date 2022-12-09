import json

example_string = '{"datetime": "2022-12-09 09:17:32.525727", "orderid": 1, "storeid": 35, "registerid": 6, "cashierid": 1, "customerid": 464, "sku": 6137, "qty": 2, "price": 80.8, "stock_qty": 0}'

def is_suspicious(s):
    example_json = json.loads(s)
    purchase_qty = example_json['qty']
    stock_qty = example_json['stock_qty']
    suspicious = 0
    
    if purchase_qty > stock_qty:
        suspicious = 1
    else:
        suspicious = 0

    # print(example_json['qty'])
    # print(example_json['stock_qty'])
    # print(suspicious)

    example_json['suspicious'] = suspicious

    output = json.dump(example_json)

    return output


if __name__ == "__main__":
    is_suspicious(example_string)
