from __future__ import absolute_import

from requests import HTTPError
import json

from intuitlib.client import AuthClient
from intuitlib.migration import migrate
from intuitlib.enums import Scopes
from intuitlib.exceptions import AuthClientError

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseServerError
from django.conf import settings
from django.core import serializers


client_id = "ABGA9WMqhlrmpP39UxG5Q3H2227bLiXsIWVTeoq0UnQVW2B8fw"
client_secret = "risgBjg1RqjqK8AVDHnYmbwnY46vG0K45v6kG3FH"
redirect_uri = "https://developer.intuit.com/v2/OAuth2Playground/RedirectUrl"
# redirect_uri = "https://oauth.platform.intuit.com/oauth2/v1/tokens/bearer"
environment= 'sandbox'

def index(request):
    return render(request, 'index.html')

def oauth():
    auth_client = AuthClient(
        client_id, 
        client_secret, 
        redirect_uri, 
        environment,
    )

    url = auth_client.get_authorization_url([Scopes.ACCOUNTING])
    # request.session['state'] = auth_client.state_token
    return redirect(url)

oauth()