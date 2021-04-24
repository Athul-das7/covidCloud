import requests   #importing the requests library to send html requests
import json

url = "https://www.fast2sms.com/dev/bulk"  #Using the fast2sms url
#Create a account in fast2sms with your phone number and copy the headers creditinals
#Now change the payload to the way you want to send the message.

#payload = "sender_id=FSTSMS&message=Hey%20Athul&language=english&route=p&numbers=9866989137"

# create a dictionary
my_data = {
    # Your default Sender ID
    'sender_id': 'FSTSMS',

    # Put your message here!
    'message': '''The student {} is having temperature above {} degree farenheit.
                Please come to the gate immediately''',

    'language': 'english',
    'route': 'p',

    # You can send sms to multiple numbers
    # separated by comma.
    'numbers': '9866989137',
}

headers = {
    'authorization': "q1vSrCUh2nGIAWcasdyeTuKBZ8jmbgkMLoN5pf69J0wP7Xi4ztKb86rVPnhaqBEcuYtG0UXDoZ2p1gw4",
    'Content-Type': "application/x-www-form-urlencoded",
    'Cache-Control': "no-cache",
    
} #authorization credentials

response = requests.request("POST", url, data=my_data, headers=headers)
#Sending the response to to the url.
#print(response.text)
#load json data from source

returned_msg = json.loads(response.text)

# print the send message
print(returned_msg['message'])