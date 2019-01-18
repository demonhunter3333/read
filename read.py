#! /usr/bin/env python3
from selenium import webdriver
import requests, pyperclip, re
from bs4 import BeautifulSoup

while True:
	input('Copy URL and press Enter.')
	url = pyperclip.paste()
	print(url)
	res = requests.get(url)
	bs = BeautifulSoup(res.text, 'html.parser')
	mainpagePath = r'articles/'
	filename = re.sub(r'[^\w\s]', '', bs.find('title').get_text().strip()) + '.html'
	article = open(mainpagePath + filename, 'w')
	article.write(res.text)
	article.close()
	browser = webdriver.Chrome()
	browser.get('file://' + mainpagePath + filename)