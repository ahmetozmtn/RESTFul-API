import requests

def get_request(url):
    return requests.get(url)

def post_request(url,json = None):
    return requests.post(url,json=json)

def put_request(url,params=None,json = None):
    return requests.put(url,json=json)

def delete_request(url):
    return requests.delete(url)