import requests
import json

def sendSMS(contactno = "9764547781",message="Hey! What's Up"):

    url = "https://www.fast2sms.com/dev/bulk"

    payload = "sender_id=FSTSMS&message="+message+"&language=english&route=p&numbers="+contactno


    headers = {
        'authorization': "QhWn7BXlhmcgr9oDiFFD8Rg5r1boceIBXJLjcbM83rIOnUIv7pbt5Hpyp6NZ",
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",
    }
    response = requests.request("POST", url, data=payload, headers=headers)

    return json.loads(response.text)

s1 =sendSMS()
print(s1)
print(type (s1))