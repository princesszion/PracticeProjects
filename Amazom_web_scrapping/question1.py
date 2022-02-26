import csv
from bs4 import BeautifulSoup
import requests
import selenium
from selenium import webdriver
# driver = webdriver.chrome.webdriver.WebDriver(executable_path='/home/victory/Downloads/chromedriver_linux64/chromedriver')
# url = 'https://www.amazon.com/s?k=Best+sellers+in+books&i=stripbooks-intl-ship&ref=nb_sb_noss_2'
# driver.get(url)
# def get_url(search_term):
#     template = 'https://www.amazon.com/s?k={}&ref=nb_sb_noss_1'
#     search_term = search_term.replace('','+')
#     return template.format(search_term)
# url = get_url('ultrawidemonitor')
# soup = BeautifulSoup(driver.page_source,'html.parser')
# results = soup.find_all('div',{'data-component-type':'s-search-result'})
# item = results[3]
def extract_record(item):
    global review_count, rating
    atag = item.h2.a
    description = atag.text.strip()
    url = 'https://www.amazon.com' + atag.get('href')
    try:
        price_parent = item.find('span','a-price')
        price = price_parent.find('span','a-offscreen').text
    except:
        return
    try:
        rating = item.i.text
        review_count = item.find('span',{'class':'a-size-base','dir':'auto'}).text
    except:
        AttributeError: rating = ''
        review_count = ''
    result = {'description':description,'price': float(price.replace("$", "")),'rating': float(rating.split(' ', 1)[0]),'review_count':review_count,'url':url}
    return result
# records = []
# results = soup.find_all('div',{'data-component-type':'s-search-result'})
# for item in results:
#     record = extract_record(item)
#     records.append(record)

def main():
    # driver = webdriver.chrome.webdriver.WebDriver(executable_path='/home/victory/Downloads/chromedriver_linux64/chromedriver')
    records = []
    url = 'https://www.amazon.com/s?k=Best+sellers+in+books&i=stripbooks-intl-ship&ref=nb_sb_noss_2'
    # driver.get(url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/56.0.2924.76 '
                      'Safari/537.36',
        "Upgrade-Insecure-Requests": "1",
        "DNT": "1",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    results = soup.find_all('div', {'data-component-type': 's-search-result'})
    if len(results) == 0:
        print("No response, please run again!")

    for item in results:
        record = extract_record(item)
        records.append(record)
    # driver.close()
    top_rated = sorted(records, key=lambda d: d['rating'], reverse = True)
    top_priced = sorted(top_rated, key=lambda d: d['price'], reverse = True)
    top_priced_10 = top_priced[:10]
    for book in top_priced_10:
        print(f"{book['description']} :  ${book['price']} : rated {book['rating']} out 5 :{book['review_count']} :{book['url']}")
# print(*records,sep='\n')
    # with open('results.csv','w',newline='',encoding='utf-8') as f:
    #     writer = csv.writer(f)
    #     writer.writerow(['Description','Price','Rating','ReviewCount','Link'])
    #     writer.writerows(records)

main()