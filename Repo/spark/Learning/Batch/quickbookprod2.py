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
from quickbooks.objects.vendor import Vendor
import json
from pandas.io.json import json_normalize


client_id = "ABFLFrNJRfC5BVkJdV2DNEulWor6S5huvA0cEegUDbQMJiMSTD"
client_secret = "zhW1LwwClmtxNTx9aEO6j4CQ379yrL6neSfyZQs0"
redirect_uri = "https://developer.intuit.com/v2/OAuth2Playground/RedirectUrl"
# redirect_uri = "https://oauth.platform.intuit.com/oauth2/v1/tokens/bearer"
environment= 'production'
# redirect_uri = "https://sandbox-quickbooks.api.intuit.com/v3"
REFRESH_TOKEN = "AB11584110237eLUnuCKSJoBTLs7QoytCPc5gy8tWviCCM5XLM"
# auth_code = 'AB11575546999KtMpCmrJsOi14bGhy4LBZXSg63L2mRcJkkExt'

realm_id = "1239606780"



auth_client = AuthClient( client_id, client_secret, redirect_uri, environment )
auth_client.refresh(refresh_token=REFRESH_TOKEN)
print(auth_client.refresh_token)

# client = QuickBooks(
#         auth_client=auth_client,
#         refresh_token= REFRESH_TOKEN ,
#         # access_token="eyJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiZGlyIn0..dViz7d81j4DwVeWl0vpq_g._2eI-xNTM2uwAHygGLxRFmv0GHD5t8-5SZC1zv1PX-rfG038n1kathFBG9JEfWmzq0zzwoAT23hXIF_GVmiImldWJMwNAeD_PGVRdzdG6P3_6Sux_4QMkIXP3DZv0YBkzqTidO7Z9vz6Znw8bgjupwLASvXNxYcKnaj8w0E99r4I1MjvDC6N_7YB9g75gPPTJWeVwJPkGfcRr27olteezcPcU27lFTmwDHjPGfvhRkZFuDFNkumon4OCYNiDDU5zWUMDxK0maWA4TXJSH0DzsOXdCPv8UjoGBGpJsVuW6zU5iFUVCpG7Z3_ewel5P_CHVsp1Bo6btN18kqEAqa3lhNp8FX-Ma839uWNg_PehM-QWe4xJe52cApcm-fYMumRVv7KbjAaUzPMddLj5V4a6DLyhUBMI1OxhJ02VY0xi9NuSfIHwt5Lrz8_FmQF8Hw18o9Or0M8JNEO6qCxAPFZ40KPCb8cgWRXVSDQganzl331qgs9wQPi9kZy9uCA1po-7y5PyA3c4PiktMyY-svgh1vrJ12U1ovYMW0QekVelGtAxpBQl18eQByRkZNQoHw0I0GyobQsZTcLPZrUPCmANqa8JgbZarxO6pe2T8i0VwLyVjvGpAb3g1X9jTbwMyX-90DMzl_ltcIlE3s59gJ6Cw-fP4tBqwWYtR1k5cnznPoMZ9WF5cqXlBP7nQFcz0qr2n_9VILf5u55owml3Ulr3JPQd95OIwSehjhKnR2sFyeSg-aK_iZPfKVjx5mK7UwdZgqtfrBwIUHDTDIFtG9Hq4OkCJ_l-2WhebACYOY-AG5_VavJ1xyGVDDZBLh8WRx3CNXVPkI65bqlFAsaSp4RgSeXAYhZxXK4nCTJ9k-re5VzhoUqQ-wFiYhnf6iKCq61L.bYF_YHwBwZtD9YsPrmLBAA",
#         company_id='1239606780'
#     )    

# account = Account.all(qb=client)
# print(account)
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