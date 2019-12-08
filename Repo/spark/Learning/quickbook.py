# import requests
# from requests.auth import AuthBase

# class TokenAuth(AuthBase):
#     """Implements a custom authentication scheme."""

#     def __init__(self, token):
#         self.token = token

#     def __call__(self, r):
#         """Attach an API token to a custom auth header."""
#         r.headers['X-TokenAuth'] = '{self.token}'  # Python 3.6+
#         return r


# test =requests.get('https://quickbooks.api.intuit.com/v3/company/1387182235', auth=TokenAuth('AB11583602761ziz5MK8EwSkjEvAlyY3qFEBsaGvDUl9aSFJ6B'))
# print(test.text)

import requests

# myToken = 'AB11583602761ziz5MK8EwSkjEvAlyY3qFEBsaGvDUl9aSFJ6B'
myUrl = 'https://quickbooks.api.intuit.com/v3/company/1387182235/reports/CustomerSalesDetail?start_date=2017-01-01&amp;end_date=2020-12-31&amp;minorversion=40'
# head = {'Authorization': 'token {}'.format(myToken)}
# response = requests.get(myUrl, headers=head)
# print(response.text)

from requests.auth import HTTPBasicAuth
res = requests.get(myUrl, auth=HTTPBasicAuth('ABfrsk5gdjpRUQBNu6w040WCrlaTE8jZrp9HbY4tMueJbEUWSD', 'kLFoTFkiSKKfyjXHjPDfpjrjFOmLlbuWfMsqLpMM'))
print(res)