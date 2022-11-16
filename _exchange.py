import requests
import json

x=input("bozdur: ")
y=input("al: ")
t=input("ne kadar: ")

url = f"https://api.apilayer.com/exchangerates_data/convert?to={y}&from={x}&amount={t}"


headers= {
  "apikey": "FuKbG4VTt9LxbiW5mdEcfIZC5qTXLLiT"
}

response = requests.request("GET", url, headers=headers)

status_code = response.status_code
result = response.text
result=json.loads(result)
r=(float(result['result'])/int(t))
print(f"1 {x} = {r} {result['query']['to']}")
print(F"{t} {result['query']['from']} karsiliginda {result['result']} {result['query']['to']} aldiniz.")
















