import requests
from bs4 import BeautifulSoup

CSV = 'notebook.csv'
HOST = 'https://rt.pornhub.com/model/sweetie_fox/videos'
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'ru-RU,ru;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 OPR/73.0.3856.396',
}

def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS)
    return r

def get_content(html):
    f = open('authors.txt')
    f1 = open('links.txt', 'w')
    for line in f:
        page_num = 1
        catalog = []
        html = get_html(line + '?page=' + str(page_num))
        soup = BeautifulSoup(html.text, 'html.parser')
        a = soup.find_all('h1')
        while True:
            html = get_html(line + '?page=' + str(page_num))
            soup = BeautifulSoup(html.text, 'html.parser')
            aaa = soup.find_all('h1')
            if(aaa == a):
                catalog.append(line + '?page=' + str(page_num))
                page_num += 1
                a = soup.find_all('h1')
                aaa.clear()
            else:
                break
        for url in catalog:
            html = get_html(url)
            soup = BeautifulSoup(html.text, 'html.parser')
            items = soup.find('ul', id='mostRecentVideosSection').find_all('li')
            for item in items:
                if('https://rt.pornhub.com' + item.find('a').get('href') + '\n' != 'https://rt.pornhub.comjavascript:void(0)' +'\n'):
                    f1.write('https://rt.pornhub.com' + item.find('a').get('href') + '\n')
                else:
                    continue
    f.close()
    f1.close()

def parser():
    html = get_html(HOST)
    content = get_content(html.text)
    print(content)
    if html.status_code == 200:
        pass
    else:
        print('error')

parser()
print('LINKS DOWNLOADED')
