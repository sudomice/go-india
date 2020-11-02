import requests
import bs4
import string
import random
from multiprocessing.dummy import Pool


def get_response(code):
    response = requests.get(
        "https://gpay.app.goo.gl/" + code)
    if "Dynamic Link Not Found" in response.text:
        return

    html = bs4.BeautifulSoup(
        response.text, features="lxml")
    if "A special" in html.title.text:
        print("https://gpay.app.goo.gl/" + code)
        print(html.title.text)


lu = string.ascii_lowercase
uu = string.ascii_uppercase
nu = '0123456789'
universe = lu + uu + nu

prefix = random.choice(universe) + random.choice(universe)
print(prefix)

for i3 in universe:
    for i4 in universe:
        for i5 in universe:
            all_links = []
            for i6 in universe:
                code = prefix + i3 + i4 + i5 + i6
                all_links.append(code)
            pool = Pool(62)
            pool.map(get_response, all_links)
            pool.close()
            pool.join()
