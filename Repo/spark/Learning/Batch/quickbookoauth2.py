from intuitlib.client import AuthClient
from intuitlib.migration import migrate
from intuitlib.enums import Scopes
from intuitlib.exceptions import AuthClientError
from requests import HTTPError
import requests

from intuitlib.client import AuthClient
from quickbooks import QuickBooks
from quickbooks.objects.customer import Customer
from quickbooks.objects.account import Account
from quickbooks.objects.tax import TxnTaxDetail
from quickbooks.objects import *

import json
from pandas.io.json import json_normalize


client_id = "ABGA9WMqhlrmpP39UxG5Q3H2227bLiXsIWVTeoq0UnQVW2B8fw"
client_secret = "risgBjg1RqjqK8AVDHnYmbwnY46vG0K45v6kG3FH"
redirect_uri = "https://developer.intuit.com/v2/OAuth2Playground/RedirectUrl"
# redirect_uri = "https://oauth.platform.intuit.com/oauth2/v1/tokens/bearer"
environment= 'sandbox'
# redirect_uri = "https://sandbox-quickbooks.api.intuit.com/v3"
# REFRESH_TOKEN = "AB11584276657dGSTYbj1MlF5tUqCz2arzhTUZcDHzW01W0QD9"
REFRESH_TOKEN = 'AB1158436670497omUaXlA28cHBaiENiW4K3AdFFtEAzSHJEsm'

realm_id = "4620816365025351930"

scopes = [
    Scopes.ACCOUNTING,
]



auth_client = AuthClient( client_id, client_secret, redirect_uri, environment )
auth_client.refresh(refresh_token=REFRESH_TOKEN)
ACCESS_TOKEN = auth_client.access_token
# print(auth_client.access_token)
# print(auth_client.auth_endpoint)
# print(auth_client.refresh_token)
# # auth_client.au
client = QuickBooks(
        auth_client=auth_client,
        refresh_token= REFRESH_TOKEN ,
        access_token=auth_client.access_token,
        company_id='4620816365025351930'
    )    


account = CompanyCurrency.count(qb=client)

print(account)

# auth_client.response_type

# // Get authorization URL
# auth_url = auth_client.get_authorization_url(scopes)
# print(auth_url)
# res = requests.get(auth_url)
# print(res.)


# request.session['state'] = auth_client.state_token
# print(auth_url)

# auth_client.get_bearer_token(auth_code = auth_client.state_token, realm_id=realm_id)
# print(auth_client.access_token)
# print(auth_client.refresh_token)
# print(res)
# print(auth_client)