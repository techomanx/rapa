import requests


url = 'https://staging.sparkbackend.cerebry.co'
geturlpoint = url + '/api/v5/partner/students/'


topic_id=1765


Masterjwttoken =  'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyNDc3NCwidXNlcm5hbWUiOiJ0ZWFjaGVyMTIzQHZlZGFudHUuY29tIiwiZXhwIjoxNjI0NzIzMTQ2LCJlbWFpbCI6InRlYWNoZXIxMjNAdmVkYW50dS5jb20iLCJvcmlnX2lhdCI6MTYyNDcwODc0NiwiYXVkIjoiUHl0aG9uQXBpIiwiaXNzIjoiQ2VyZWJyeSJ9.Gb_q1MXs9ggtgtWSOYltuPyuIevA8bp5ptJRGmuspeY'

ARGS = {'jwt-token':Masterjwttoken,'Content-Type':'application/json'}

r = requests.get(geturlpoint, headers={'jwt-token':Masterjwttoken,'Content-Type':'application/json'})
data = r.json()
sampStu=data[0]['username']

# 1. get a student
# 2. get his auth token
# 3. use auth token to call get list of questions for the topic ID provided

stuTokenUrl = f'{url}/api/v5/partner/user/{sampStu}/token/'

# stuToken= requests.get(stuTokenUrl,)

tokenRes = requests.get(stuTokenUrl,headers={'jwt-token':Masterjwttoken,'Content-Type':'application/json'})
tokenData = tokenRes.json()
stuToken = "jwt "+tokenData['token']
# use token data to get list of questions in a given topic
stuTopictUrl = f'{url}/api/v5/partner/topic/{topic_id}/question'

# create header argument as per aPI requrieemnts
stuARGS = {'Authorization':stuToken,'Content-Type':'application/json'}
# fire the request to get the questions assigned to a particular student
topicRes = requests.get(stuTopictUrl,headers=stuARGS)
topicData=topicRes.json()

# decode the question to generate html raw
strDecode=topicData['data']['question']
print(strDecode)
import base64
decoddedData = base64.b64decode(strDecode)
print(decoddedData.decode('utf-8'))

