import requests
import json

count = 1

#response = requests.get('https://api.congress.gov/v3/member?api_key=aJEvEOH8VBfrmQHGVZ3z5G72AcAGIrGgv0WaXFNQ')
response = requests.get('https://api.congress.gov/v3/member?offset=0&limit=20&api_key=aJEvEOH8VBfrmQHGVZ3z5G72AcAGIrGgv0WaXFNQ')

for data in response.json()['members']:
    with open("output.txt", "a") as file:
        print(count, data['name'], data['terms']['item'], file=file)
    count += 1  # Increment the counter on each iteration
    #print(data['terms']['item'])
   # memberchamber = data['terms']['item']['chamber']
   # print(memberchamber)
    # print()


response = requests.get('https://api.congress.gov/v3/member?offset=20&limit=10&api_key=aJEvEOH8VBfrmQHGVZ3z5G72AcAGIrGgv0WaXFNQ')

for data in response.json()['members']:
    print(count, data['name'], data['terms']['item'])
    count += 1  # Increment the counter on each iteration