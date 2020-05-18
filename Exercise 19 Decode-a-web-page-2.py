import bs4, requests

url = "https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture"
r = requests.get(url)
r_html = r.text

soup = bs4.BeautifulSoup(r_html, "html.parser")
article = soup.find_all("p")

print([i.text for i in article])
