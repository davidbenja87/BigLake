import os
import subprocess
import sys
import os
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

# os.environ['AZURE_CLIENT_ID'] = "734cb5f0-e2a5-4d10-aed4-2067bf6e7c4b"
# os.environ['AZURE_CLIENT_SECRET'] = "te5U]luA/sfOtj1cW@R6sksz/X8r[G9j"
# os.environ['AZURE_TENANT_ID'] = "c8fedfb4-d804-457b-9745-362581de2e4c"
# os.environ['KEY_VAULT_NAME'] = "mytestaccount"
credential = DefaultAzureCredential()
kvuri = "https://mytestaccount.vault.azure.net/"
client = SecretClient(vault_url=kvuri, credential=credential)
client.set_secret("test12", "pass12");
retrieved_secret = client.get_secret("test12")
print(retrieved_secret)
client.set_secret("test12", "pass14");