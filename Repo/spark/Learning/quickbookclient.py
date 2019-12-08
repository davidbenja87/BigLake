from intuitlib.client import AuthClient
from quickbooks import QuickBooks
from quickbooks.objects.customer import Customer
from quickbooks.objects.account import Account
import json

CLIENT_ID = "ABGA9WMqhlrmpP39UxG5Q3H2227bLiXsIWVTeoq0UnQVW2B8fw"
CLIENT_SECRET = "risgBjg1RqjqK8AVDHnYmbwnY46vG0K45v6kG3FH"
# REDIRECT_URI = "https://developer.intuit.com/v2/OAuth2Playground/RedirectUrl"
REDIRECT_URI = "https://sandbox-quickbooks.api.intuit.com/v3"
REFRESH_TOKEN = "AB11584091105kCAQoexKsxQzQ6XGgrhDRMUl2TX5cPoowTTXa"
auth_client = AuthClient(
        client_id= CLIENT_ID,
        client_secret=CLIENT_SECRET,
        environment= 'sandbox',
        redirect_uri= REDIRECT_URI,
    )


client = QuickBooks(
        auth_client=auth_client,
        refresh_token= REFRESH_TOKEN ,
        company_id='4620816365025351930'
    )    

account = Account.count(qb=client)   
# print(account) 
# res = json.loads(account)
# for r in account:
#     print(r)
print(account)

# account = Account.get(1, qb=client)
# account = Account.all(1, qb=client)
# json_data = account.to_json()
# print(json_data)

# customers = Customer.query("SELECT * FROM Customer WHERE Active = True", qb=client)
# print(customers)
# print(client.company_id)
