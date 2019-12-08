 
from intuitlib.client import AuthClient
from intuitlib.enums import Scopes
# from quickbooks import Oauth2SessionManager
redirect_uri = "https://developer.intuit.com/v2/OAuth2Playground/RedirectUrl"

client_id = "ABGA9WMqhlrmpP39UxG5Q3H2227bLiXsIWVTeoq0UnQVW2B8fw"
client_secret = "risgBjg1RqjqK8AVDHnYmbwnY46vG0K45v6kG3FH"
Environment ="“sandbox”"

# Instantiate client
auth_client = AuthClient(
    client_id,
    client_secret,
    redirect_uri,
    Environment # “sandbox” or “production”
    
)

scopes = [
    Scopes.ACCOUNTING,
]

#  Get authorization URL
auth_url = auth_client.get_authorization_url(scopes)
print(auth_url)
# auth_cent.get_bearer_token(auth_code=auth_code,realm_id=realm_id)
# auth_client.get_bearer_token(auth_code, realm_id=realm_id)
