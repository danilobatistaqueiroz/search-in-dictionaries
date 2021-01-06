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
    txt_definitions = []
    txt_ipas = []
    with requests.Session() as session:
        source = session.get(f'https://www.collinsdictionary.com/us/dictionary/english/{word}', headers=headers).text
        soup = BeautifulSoup(source, "html.parser")
        div_definitions = soup.find_all('div', class_='definitions')
        for div_definition in div_definitions:
            definitions = div_definition.find_all('div', class_='def')
            for definition in definitions:
                text = definition.text.replace('\n',' ').replace('  ',' ')
                text = text.capitalize()
                txt_definitions.append(text)
        sp_ipas = soup.find_all('span', class_=['pron', 'type-'])
        for sp_ipa in sp_ipas:
            text = sp_ipa.text.replace('  ',' ').strip()
            txt_ipas.append(text)

    return ['<br>\n'.join(txt_definitions),', '.join(txt_ipas)]
