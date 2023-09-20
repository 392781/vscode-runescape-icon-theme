import requests
from bs4 import BeautifulSoup
import re
import time

URL_BASE = "https://oldschool.runescape.wiki"

def scrape_img_urls():
    img_srcs = []
    img_names = []
    counter = 1
    next_url = "https://oldschool.runescape.wiki/w/Category:Item_inventory_images"
    while next_url != None:
        req = requests.get(next_url)
        soup = BeautifulSoup(req.text, features="html.parser")
        srcs = [asdf.attrs['src'] for asdf in soup.select(".image > img")]
        img_srcs += srcs
        names = [name.string for name in soup.select(".gallerytext > a")]
        img_names += names

        possible_next_urls = [x.parent for x in soup(text=re.compile(r'next page'))]
        next_url = None
        for pnu in possible_next_urls:
            if "href" in pnu.attrs:
                next_url = URL_BASE + pnu.attrs["href"]
                break
        counter += 1
        print(f"Gathering... {counter}")
    return img_srcs, img_names

img_srcs, img_names = scrape_img_urls()
counter = 0

for src, name in zip(img_srcs, img_names):
    while True:
        try:
            url = URL_BASE + src
            data = requests.get(url).content
            f = open(f'./item_icons/{name}','wb')
            f.write(data)
            counter += 1
            print(f"Writing... {counter}")
            break
        except ConnectionResetError as e:
            time.sleep(10)
            pass

    
f.close()
