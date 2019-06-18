from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card'

uClient = uReq(my_url)		#opening connection
page_html = uClient.read()	#grabbing the page
uClient.close()				#closing connection

page_soup = soup(page_html, "html.parser")								#html parser
containers = page_soup.findAll("div",{"class":"item-container"})		#grabs each product

filename = "graphic_cards_newegg.csv"
f = open(filename, "w")

headers = "brand,product_name,current_price,shipping,link\n"

f.write(headers)


for container in containers:
	brand = container.div.div.a.img["title"]

	title_container = container.findAll("a", {"class":"item-title"})
	product_name = title_container[0].text

	price_container = container.findAll("li", {"class":"price-current"})
	current_price = price_container[0].text.replace('\n', ' ').replace('\r', '').replace('–', '').replace('|', '').strip("")

	shipping_container = container.findAll('li', {"class":"price-ship"})
	shipping = shipping_container[0].text.strip()

	link_container = container.findAll("a", {"class":"item-img"})
	link = link_container[0].get('href')


	f.write(brand + "," + product_name.replace(",", "|") + "," + current_price + "," + shipping + "," + link + "\n")

f.close()