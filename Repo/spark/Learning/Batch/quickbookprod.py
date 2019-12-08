from intuitlib.client import AuthClient
from quickbooks import QuickBooks
from quickbooks.objects.customer import Customer
from quickbooks.objects.account import Account
from quickbooks.objects.tax import TxnTaxDetail
from quickbooks.objects.vendor import Vendor
import json
from pandas.io.json import json_normalize


CLIENT_ID = "ABFLFrNJRfC5BVkJdV2DNEulWor6S5huvA0cEegUDbQMJiMSTD"
CLIENT_SECRET = "zhW1LwwClmtxNTx9aEO6j4CQ379yrL6neSfyZQs0"
REDIRECT_URI = "https://developer.intuit.com/v2/OAuth2Playground/RedirectUrl"
# REDIRECT_URI = "https://sandbox-quickbooks.api.intuit.com/v3"
REFRESH_TOKEN = "AB11584110237eLUnuCKSJoBTLs7QoytCPc5gy8tWviCCM5XLM"



# api_url = "https://quickbooks.api.intuit.com/v3"
# company_id = "4620816365025351930"

auth_client = AuthClient(
        client_id= CLIENT_ID,
        client_secret=CLIENT_SECRET,
        environment= 'production',
        redirect_uri= REDIRECT_URI,
    )

auth_client.refresh(refresh_token=REFRESH_TOKEN)
ACCESS_TOKEN = auth_client.access_token
print(ACCESS_TOKEN)


# client = QuickBooks(
#         auth_client=auth_client,
#         refresh_token= REFRESH_TOKEN ,
#         access_token=ACCESS_TOKEN,
#         company_id='1239606780'
#     )    

# # client.get_authorize_url()

# # def querycutomized(cls, select, qb=None):
# #     """
# #     :param select: QBO SQL query select statement
# #     :param qb:
# #     :return: Returns list
# #     """
# #     if not qb:
# #         qb = QuickBooks()
# #     json_data = qb.query(select)
# #     return json_data   

# # def getentity(obj, entity : str, qb = None, offset : int = 1, limit : int = 1000):
# #     obj = querycutomized(obj,"select * from " + entity + "  STARTPOSITION " + str(offset) + " MAXRESULTS "+ str(limit), qb = qb)
# #     obj = obj["QueryResponse"][entity]
# #     df = json_normalize(obj)
# #     return df


# # working code
# #################################################################################################################
# # vendor = Vendor.querycutomize("select * from Vendor  STARTPOSITION 1 MAXRESULTS 250", qb=client)
# # vendor = vendor["QueryResponse"]["Vendor"]
# # df = json_normalize(vendor)
# # df.to_csv("C:\\Users\\sugumarb\\BDAP\\quicbooks\\vendor.csv")


# ##################################################################################################################

# # account = Account()
# # df = getentity(account, "Account", qb = client, offset = 3, limit=5)
# # print(df)

# # df.to_csv("C:\\Users\\sugumarb\\BDAP\\quicbooks\\account.csv")
# # print(acc)

# account = Account.all(qb=client)
# print(account)






# print(df)
# for i in account["QueryResponse"]["Account"]:
#     print(i)
# print(account["QueryResponse"]["Account"])
# for i in account:
#     print(i)
# print(account)
# for i in account:
#     print(i)
# print(account)
# print(account) 
# res = json.loads(account)
# for r in account:
#     print(r)
# print(account)

# account = Account.get(1, qb=client)
# account = Account.all(1, qb=client)
# json_data = account.to_json()
# print(json_data)

# customers = Customer.query("SELECT * FROM Customer WHERE Active = True", qb=client)
# print(customers)
# print(client.company_id)
# Customer.count("Active IN (True, False)" , qb=client)
