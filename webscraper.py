from bs4 import BeautifulSoup
import requests
import xlsxwriter

workbook = xlsxwriter.Workbook('scraper_results.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write('A1', 'Hello world')

workbook.close()


# specify the url
page_link = 'https://www.otodom.pl/sprzedaz/mieszkanie/wroclaw/'

# doing request to a site after timeout
page_response = requests.get(page_link, timeout=5)

# declaring variable with page_content using parser
page_content = BeautifulSoup(page_response.content, "html.parser")

# looping over content, finding a specific class, getting value
price_list = []
for price in page_content.find_all(class_='offer-item-price'):
	price_list.append(price.get_text("|", strip=True))

print(price_list)