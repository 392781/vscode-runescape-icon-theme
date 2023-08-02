import requests
from bs4 import BeautifulSoup
import re

URL_BASE = "https://oldschool.runescape.wiki"

def scrape_img_urls():
    imgs = []
    next_url = "https://oldschool.runescape.wiki/w/Category:Item_inventory_images"
    while next_url != None:
        req = requests.get(next_url)
        soup = BeautifulSoup(req.text, features="html.parser")
        img_srcs = [asdf.attrs['src'] for asdf in soup.select(".image > img")]
        for src in img_srcs:
            imgs.append(src)
        possible_next_urls = [x.parent for x in soup(text=re.compile(r'next page'))]
        next_url = None
        for pnu in possible_next_urls:
            if "href" in pnu.attrs:
                next_url = URL_BASE + pnu.attrs["href"]
                break
    return imgs

imgs = scrape_img_urls()

for img_path in imgs:
    img = URL_BASE + img_path
    # do some downloading
    # :)
