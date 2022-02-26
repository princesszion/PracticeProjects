import requests
import bs4
import time

url = "https://www.amazon.com/best-sellers-books-Amazon/zgbs/books/ref=zg_bs_pg_1?_encoding=UTF8&pg=1"

print("Fetching, please wait...\n")

time.sleep(2)

try:

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 '
                      'Safari/537.36',
        "Upgrade-Insecure-Requests": "1",
        "DNT": "1",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate"
    }
    response = requests.get(url, headers=headers, params={"wait": 2})

    soup = bs4.BeautifulSoup(response.text, 'html.parser')

    book_component = soup.select(".zg-item-immersion")

    if not len(book_component):
        print("No response from webpage, try again!")

    popular_books = []
    for book in book_component:

        if "a-star-5" in str(book):
            for book_names in book.select(".p13n-sc-truncate"):
                popular_books.append(book_names.getText().strip())

    popular_books_prices = []
    for book in book_component:
        if "a-star-5" in str(book):
            for prices in book.find(name="span", class_="p13n-sc-price"):
                popular_books_prices.append(float(prices.replace("$", "")))

    sorted_top_ten_prices = []
    for price in popular_books_prices:
        sorted_top_ten_prices.append(price)

    max_range = 10

    sorted_top_ten_prices.sort()
    sorted_top_ten_prices = sorted_top_ten_prices[-max_range:]

    ten_most_expensive = []

    unsorted_prices = []

    for book in book_component:
        if "a-star-5" in str(book):
            for val in sorted_top_ten_prices:
                if f"${val}" in str(book):
                    ten_most_expensive.append(
                        (book.find(name="div", class_="p13n-sc-truncate").text.strip()))

                    for prices in book.find(name="span", class_="p13n-sc-price"):
                        unsorted_prices.append(prices)

    final_result = [{ten_most_expensive[i]: unsorted_prices[i]
                     for i in range(len(ten_most_expensive))}]

    for book in final_result:
        for k, v in book.items():
            print(f"{k} : {v}")

except requests.exceptions.RequestException as e:
    print("Error\n", e)