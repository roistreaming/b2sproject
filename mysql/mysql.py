import mysql.connector
import json
   
def sql_connect(sql_server,sql_database,sql_user,sql_password):
    """"Creates a connection to MySql"""
    cnx = mysql.connector.connect(user=sql_user, password=sql_password,
                               host=sql_server,database=sql_database)
    return cnx
def sql_enrich(json_msg,cnx):
    """Accepts a JSON message and returns enriched JSON with values from MYSQL"""
    msg_dict = json.loads(json_msg)
    sku = msg_dict['sku']
    cursor = cnx.cursor()
    query =  ("""SELECT * FROM product WHERE sku = %(sku_no)s""")
    cursor.execute(query,{'sku_no':sku})
    result = cursor.fetchall()
    description = result[0][1]
    msg_dict['description'] = description
    stock_qty = result[0][2]
    msg_dict['stock_qty'] = stock_qty
    enriched_json = json.dumps(msg_dict)
    cursor.close()    
   
    return enriched_json
### Unit Test
### Want to leave connection open while messages are processed
# cnx = sql_connect('10.26.194.22','b2s','b2suser','ROI2022cb')
# my_msg = '{"datetime": "2022-12-09 10:14:05.856308", "orderid": 11111, "storeid": 22222, "registerid": 33333, "cashierid": 44444, "customerid": 55555, "sku": 750, "qty": 1, "price": 0.99}'
# print(sql_enrich(my_msg,cnx))
