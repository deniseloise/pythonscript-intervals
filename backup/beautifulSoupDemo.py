#! python3
# beautifulSoupDemo.py - web scrapping; gets the price of the book on the web page

import bs4, requests

def getbookTitle(productUrl):
    headers = {'User-Agent': 'Mozilla/5.0'}

    res = requests.get(productUrl, headers=headers)

    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    #elems = soup.select('body > div > main > div > h1')
    elems = soup.select('a')

    #return elems[0].text.strip()
    print(str(elems[0]))
    print(elems[0].get('href'))
    print(elems[0].getText().strip())

getbookTitle('https://automatetheboringstuff.com/')
