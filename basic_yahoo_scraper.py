import requests
from bs4 import BeautifulSoup

ticker_list = ["FB"]
'''
    "GM",
    "WDC",
    "CSIQ",
    "INTC",
    "TEL",
    "DLB",
    "IEA",
    "MSFT"
]
'''

'''
urls = [ f"https://finance.yahoo.com/quote/{string}/options" for string in ticker_list]
pages = [ requests.get(urls) for urls in urls]
'''
url = "https://uk.finance.yahoo.com/quote/AAPL/"
page = requests.get(url)
print(page.headers)

'''
#print(page.text)
for count, result in enumerate(pages):
    soup = BeautifulSoup(result.content,"html.parser")
    raw = soup.find_all('tr')

    for tag in raw:
        for child in tag.children:
            print(child)

'''
