import requests
from bs4 import BeautifulSoup

headers = {
   'Content-Type': 'application/xhtml+xml',
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET, POST,OPTIONS',
    'Access-Control-Allow-Headers': '*',
    'Access-Control--Max-Age': '86400',
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36'
}

def search(word):
    lst_definitions = []
    with requests.Session() as session:
        source = session.get(f'https://www.linguee.com.br/portugues-ingles/search?qe={word}&source=&cw=1020&ch=268&as=shownOnStart', headers=headers).text
        soup = BeautifulSoup(source, "html.parser")
        quick_results = soup.find_all('div', class_='autocompletion_item')
        translation = quick_results[0].find('div', class_='translation_item')
        print(translation.get_text())
        for result in quick_results:
            lst_txt = result.get_text().split('\n')
            lst_txt = [x for x in lst_txt if x]
            lst_definitions.append(lst_txt)
    return ['. '.join(lst_definitions)]

print(search('show'))