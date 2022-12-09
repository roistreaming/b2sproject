import time

example_string = '{"datetime": "2022-12-09 09:17:32.525727", "orderid": 1, "storeid": 35, "registerid": 6, "cashierid": 1, "customerid": 464, "sku": 6137, "qty": 2, "price": 80.8, "stock_qty": 0, "is_suspicious":0}'

def create_file(s):
    timestr = time.strftime("%Y%m%d%H%M%S")
    text_file = open(timestr+".txt", "w")
    n = text_file.write(example_string)
    text_file.close()

if __name__ == "__main__":
    create_file(example_string)
