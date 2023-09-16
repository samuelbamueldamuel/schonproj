import requests


sym = 'IBM'
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol={sym}&apikey=PQJ2FCRQSA3OVH36'

resp = requests.get(url)

