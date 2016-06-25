#import socks
#import socket
import time
import urllib2
import feedparser
import re
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup


class scrape():
	def scrapeapp(self, urls):
		self.urls = urls
		print "hello"
		for url in urls:
			print "Scraping for : ", url
			count = 0
			driver = webdriver.Firefox()
			driver.get(url)
			try:
				x = driver.find_elements_by_css_selector('.expand-button.expand-next')[1]
				xpath = "//button[@class='expand-button expand-next']"
				y = driver.find_element_by_xpath(xpath)
				print "here..."
				for i in range(0,2):
					try:
						x.click()
						count = count + 1
						#print count
						time.sleep(5)
					except:
						break
				print count
				content = driver.page_source
				soup = BeautifulSoup(content)
				tag2 = soup.find_all('div', class_="single-review")
				#tag3 = 
				driver.close()
				filename = "/../data/"+url[-6:]+".txt"
				f = open(filename, 'w')
				f.write(content.encode('utf-8'))
				f.close()
			except:
				pass