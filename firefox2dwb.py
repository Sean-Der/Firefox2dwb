from bs4 import BeautifulSoup as soup

html = soup(open("bookmarks.html"))

for link in html.find_all('a'):
	    print str(link.get('href'))  + " - " + str(link.contents[0].encode("utf-8"))
