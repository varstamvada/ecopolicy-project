import requests
import json

count = 0

# response = requests.get('https://api.congress.gov/v3/member?api_key=aJEvEOH8VBfrmQHGVZ3z5G72AcAGIrGgv0WaXFNQ')
# response = requests.get('https://api.congress.gov/v3/member?offset=0&limit=20&api_key=aJEvEOH8VBfrmQHGVZ3z5G72AcAGIrGgv0WaXFNQ')

for offset in range(0, 750, 250):
   response = requests.get('https://api.congress.gov/v3/member?format=json&offset={offset}&limit=250&fromDateTime=2001-01-01T00%3A00%3A00Z&api_key=TcAsfbl78LnPadowZCoBIL25bFdTArErtcqSKt9J')
   print(response)


#for data in response.json()['members']:
#    with open("output.txt", "a") as file:
#        print(count, data['bioguideId'], data['name'], data['partyName'], data['district'], data['chamber'], data['endYear'], ['item'], file=file)
#    count += 1  # Increment the counter on each iteration
#  print(data['terms']['item'])
#   memberchamber = data['terms']['item']['chamber']
#   print(memberchamber)
#   print()


# response = requests.get('https://api.congress.gov/v3/member?offset=20&limit=10&api_key=aJEvEOH8VBfrmQHGVZ3z5G72AcAGIrGgv0WaXFNQ')
# for data in response.json()['members']:
#    print(count, data['name'], data['terms']['item'])
#    count += 1  # Increment the counter on each iteration