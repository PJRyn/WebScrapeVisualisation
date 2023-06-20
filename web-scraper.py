from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)
url = 'https://books.toscrape.com/'
browser.visit(url)
titles = []
for x in range(1, 51):

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    titles_found = soup.find_all('h3')
    products = soup.find_all('article', class_='product_pod')
    print(f"+Page: ", x)
    for product in titles_found:
        titles.append(product.text)
        
    if browser.links.find_by_partial_text('next'):
        browser.links.find_by_partial_text('next').click()
    else:
        print("-Done")
print("Collected ", len(titles), " Titles")
browser.quit()