import requests   #importing the requests library to send html requests
url = "https://www.fast2sms.com/dev/bulk"  #Using the fast2sms url
#Create a account in fast2sms with your phone number and copy the headers creditinals
#Now change the payload to the way you want to send the message.

payload = "sender_id=FSTSMS&message=Hey%20Athul&language=english&route=p&numbers=9866989137"
headers = {
    'authorization': "q1vSrCUh2nGIAWcasdyeTuKBZ8jmbgkMLoN5pf69J0wP7Xi4ztKb86rVPnhaqBEcuYtG0UXDoZ2p1gw4",
    'Content-Type': "application/x-www-form-urlencoded",
    'Cache-Control': "no-cache",
    
} #authorization credentials

response = requests.request("POST", url, data=payload, headers=headers)
#Sending the response to to the url.
print(response.text)
