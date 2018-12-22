from bs4 import BeautifulSoup
import requests
import xlsxwriter

workbook = xlsxwriter.Workbook('scraper_results.xlsx')
worksheet = workbook.add_worksheet('results')

# specify the url
page_link = 'https://www.otodom.pl/sprzedaz/mieszkanie/wroclaw/?page={}'

# offer-item-price to cena za mieszkanie

price_row = 0
price_col = 0
row_measurement = 0
col_measurement = 1

for page_num in range(2, 4):
	page_response = requests.get(page_link.format(page_num), timeout=5)
	print(page_link.format(page_num))
	page_content = BeautifulSoup(page_response.content, "html.parser")

	for price in page_content.find_all(class_='offer-item-price'):
		worksheet.write(price_row, price_col, price.get_text("|", strip=True))
		price_row += 1

	for measurement in page_content.find_all(class_='hidden-xs offer-item-area'):
		worksheet.write(row_measurement, col_measurement, measurement.get_text("|", strip=True))
		row_measurement += 1
		

workbook.close()