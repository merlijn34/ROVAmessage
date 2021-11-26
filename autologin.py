import requests

# enter the url to login to
url = "";

# create a session
session = requests.session()

# enter credentials
payload = {
    'password': '',
    'Login': '',
    'forward': '' # url/x to forward to
}
# visit url and enter payload
response = session.post(url, data=payload)
# get responsecode
print(response.status_code)