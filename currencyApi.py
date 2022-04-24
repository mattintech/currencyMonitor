from requests_html import HTMLSession

session = HTMLSession()
url = "https://www.x-rates.com/calculator/?from=USD&to=CAD&amount=1"
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15'
}

def getUsdToCad():
    #result = {}
    result = ""

    ## fetch page from x-rates
    r = session.get(url, headers=headers)
    #print(r.request.headers)
    
    # render the page for processing
    r.html.render(wait=1, keep_page=True)
    #print(r.status_code)
    
    #print(r.text)
    if(r.status_code == 200):
        ## get the result of the currency par from the span element with the classname of ccOutputRslt
        currencyPair = r.html.find('span.ccOutputRslt', first=True)
        currencyTime = r.html.find('span.calOutputTS', first=True)
        #result.update(currencyPair = currencyPair.text.strip(' CAD'))
        #result.update(currencyTime = currencyTime.text)
        result = currencyPair.text.strip(' CAD')
        #print(result)
    else:
        #result={"currencyPair": "0.00", "currencyTime": "none..."}
        result="0.00"
    return result