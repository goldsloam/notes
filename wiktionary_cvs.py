# wiktionary_cvs.py
#
import requests
from bs4 import BeautifulSoup

def main():
	location = 'https://en.wiktionary.org/wiki/%E3%81%AE#Japanese'
	page = requests.get(location)
	encoding = page.encoding if 'charset' in page.headers.get('content-type', '').lower() else None
	soup = BeautifulSoup(page.content, from_encoding=encoding)

	print(soup("html.parser"))

main()
