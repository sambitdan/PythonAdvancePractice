
import requests
import json
def api_call(url : str, api_key : str =None):
    import requests
    # headers={
    #     "X-API-Key" : api_key
    # }
    response=requests.get(url)
    return {"data" : response.json()}
