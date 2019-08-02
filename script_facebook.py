from bs4 import BeautifulSoup

file_path = "(25) ISUZU UNT Club - โพสต์.html"
with open(file_path, "rb") as f:
    html_doc = f.read()
    soup = BeautifulSoup(html_doc, 'html.parser')
    hidden_elem = soup.select('div.hidden_elem')


    x = str(hidden_elem[4])
    comment = x[x.find('<!--') : x.find('-->')]
    contents = BeautifulSoup(comment, 'html.parser')
    blank = []
    con = contents.find_all('div', {'class': '_1dwg _1w_m _q7o'})
    
    for item in con:
        blank.append(item.text)
    print(blank)

    time = contents.find_all('abbr', {'class': '_5ptz'})
    for row in time:
        print(row['title'])
    link = contents.find_all("a", {"class": "_4-eo _2t9n _50z9"})
    for img in link:
        print(img['data-ploi'])
    for fb_post in link:
        print(fb_post['href'])
