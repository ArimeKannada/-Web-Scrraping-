import requests
from bs4 import BeautifulSoup
import os
os.system('cls||clear')


remove = 'burrow_query.py?'

def start(page_no):
    ULR = f"https://dsal.uchicago.edu/cgi-bin/app/burrow_query.py?page={page_no}"
    path = f"H:\\Visual_Studia\\python projects\\kannada dictnory\\Dravidian\\page{page_no}.html"
    link = 'H:\\Visual_Studia\\python projects\\kannada dictnory\\Dravidian\\images\\'
    r = requests.get(ULR)
    soup = BeautifulSoup(r.content , features="html.parser")
    for a in soup.find_all('a'):
        if a['href'] == f"/cgi-bin/app/burrow_query.py?page={page_no - 1}":
            a['href'] = f"H:\\Visual_Studia\\python projects\\kannada dictnory\\Dravidian\\page{page_no - 1}.html"
        elif a['href'] == f"/cgi-bin/app/burrow_query.py?page={page_no + 1}":
            a['href'] = f"H:\\Visual_Studia\\python projects\\kannada dictnory\\Dravidian\\page{page_no + 1}.html"
        elif a['href'] == f"/dictionaries/":
            a['href'] = path
        elif a['href'] == f"/dictionaries/burrow/":
            a['href'] = path
        else:
            pass

    for l in soup.find_all('link'):
        if l['href'] == '/dictionaries/resp.css':
            l['href'] = link + 'resp.css'
        if l['href'] == '/dictionaries/jquery-ui.css':
            l['href'] = link + 'jquery-ui.css'

    for i in soup.find_all('img'):
        if i['src'] == '/dictionaries/graphics/ddsa-small.jpg':
            i['src'] = link + 'ddsa-small.jpg'
        elif i['src'] == '/dictionaries/graphics/burrow.jpg':
            i['src'] = link + 'burrow.jpg'

    for s in soup.find_all('script'):
        if s['src'] == 'https://code.jquery.com/jquery-1.10.2.js':
            s['src'] = link + 'jquery-1.10.2.js'
        elif s['src'] == 'https://code.jquery.com/ui/1.10.4/jquery-ui.js':
            s['src'] = link + 'jquery-ui.js'

    html = soup.contents
    html = soup.prettify(encoding='utf-8')
    with open(path, 'wb') as file:
        file.write(html)


# start(4)

for i in range(1, 515):
    print("")
    perc = i/514
    perc = perc * 100
    print(f"page no = {i}   ---   ", end='')
    print(f"{perc:.2f}% Completed")
    perc = int(perc)
    for x in range(0, perc+ 1):
        print("#", end='')
    start(i)
    os.system('cls||clear')
