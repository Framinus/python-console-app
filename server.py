import json
from requests import *
from hellosign_sdk import HSClient

client = HSClient(api_key='API_KEY')

# send a non-embedded signature request
def signatureRequest ():

    files = ["NDA.pdf"]
    signers = [
        {"name": "James", "email_address": "james@example.com"}
    ]

    response = client.send_signature_request(
        test_mode=True,
        files=files,
        file_urls=None,
        title="Python Signature Request",
        message="Please sign!",
        signing_redirect_url=None,
        signers=signers
    )

    print(response);


# Raw requests section.

# get files for request.
def getFilesRawRequest ():
    API_KEY = 'YOUR_API_KEY'
    SIGNATURE_REQUEST_ID = 'YOUR_SIGNATURE_REQUEST_ID'
    URL = 'https://'+API_KEY+':@api.hellosign.com/v3/signature_request/files/'+SIGNATURE_REQUEST_ID
    PARAMS = {'get_url': True}
    r = get(url = URL, params = PARAMS)
    print(r.url)
    data = r.json()
    print(data);

# list signature requests
def listSignatureRequestsRawRequest (account_id, page, page_limit):
    API_KEY = 'YOUR_API_KEY'
    URL = 'https://'+API_KEY+':@api.hellosign.com/v3/signature_request/list?account_id='+account_id
    r = get(url = URL)
    data = r.json()
    print(data);

def updateAppRawRequest (client_id, callback_url):
    API_KEY = 'YOUR_API_KEY'
    URL = 'https://'+API_KEY+':@api.hellosign.com/v3/api_app/'+client_id
    DATA = {'callback_url': callback_url}
    r = post(URL, data = DATA)
    data = r.json()
    print(data);

updateAppRawRequest('CLIENT_ID', 'https://api-support-node-webapp.herokuapp.com/callback');

# >>> r = requests.post('https://httpbin.org/post', data = {'key':'value'})
