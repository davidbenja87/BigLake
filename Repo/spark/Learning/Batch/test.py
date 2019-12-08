from intuitlib.client import AuthClient
from intuitlib.migration import migrate
from intuitlib.enums import Scopes
from intuitlib.exceptions import AuthClientError
from requests import HTTPError
import requests
import os
from intuitlib.client import AuthClient
from quickbooks import QuickBooks
from quickbooks.objects.customer import Customer
from quickbooks.objects.account import Account
from quickbooks.objects.tax import TxnTaxDetail
from quickbooks.objects.vendor import Vendor
import json
from pandas.io.json import json_normalize
from django.shortcuts import render, redirect

# os.environ['DJANGO_SETTINGS_MODULE'] = "nirla.settings"

client_id = "ABGA9WMqhlrmpP39UxG5Q3H2227bLiXsIWVTeoq0UnQVW2B8fw"
client_secret = "risgBjg1RqjqK8AVDHnYmbwnY46vG0K45v6kG3FH"
redirect_uri = "https://developer.intuit.com/v2/OAuth2Playground/RedirectUrl"
# redirect_uri = "https://oauth.platform.intuit.com/oauth2/v1/tokens/bearer"
environment= 'sandbox'
# redirect_uri = "https://sandbox-quickbooks.api.intuit.com/v3"
# REFRESH_TOKEN = "AB11584276657dGSTYbj1MlF5tUqCz2arzhTUZcDHzW01W0QD9"


realm_id = "4620816365025351930"
from intuitlib.client import AuthClient
from intuitlib.enums import Scopes


auth_client = AuthClient(
    client_id,
    client_secret,
    redirect_uri,
    environment, # “sandbox” or “production”
)


scopes = [
    Scopes.ACCOUNTING,
]


ENVIRONMENT_VARIABLE = "DJANGO_SETTINGS_MODULE"
os.environ.get(ENVIRONMENT_VARIABLE)

