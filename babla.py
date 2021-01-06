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

def search(word, abrv_lang, language):
    txt_definitions = []
    with requests.Session() as session:
        source = session.get(f'https://{abrv_lang}.bab.la/dicionario/ingles-{language}/{word}', headers=headers).text
        soup = BeautifulSoup(source, "html.parser")
        quick_results = soup.find_all('div', class_='quick-result-overview')
        for result in quick_results:
            txt = result.get_text().split('\n')
            if abrv_lang.upper() in txt:
                txt = [x for x in txt if x]
                txt.remove(abrv_lang.upper())
                txt_definitions.append(','.join(txt))
    return ['<br>\n'.join(txt_definitions)]
