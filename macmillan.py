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
    txt_examples = []
    txt_ipas = []
    with requests.Session() as session:
        source = session.get(f'https://www.macmillandictionary.com/us/dictionary/american/{word}', headers=headers).text
        soup = BeautifulSoup(source, "html.parser")
        cnt=0
        span_definitions = soup.find_all('span', class_='DEFINITION')
        for span_definition in span_definitions:
            cnt+=1
            text = span_definition.text.replace('\n',' ').replace('  ',' ')
            text = text.capitalize()
            txt_definitions.append(f'{cnt}. {text}')
        span_prons = soup.find_all('span', class_='PRON')
        for pron in span_prons:
            text = pron.text.replace('  ',' ')
            txt_ipas.append(text)
        cnt=0
        div_examples = soup.find_all('div', class_='EXAMPLES')
        for p_example in div_examples:
            cnt+=1
            text = p_example.text.replace('\n',' ').replace('  ',' ')
            text = text.capitalize()
            txt_examples.append(f'{cnt}. {text}')

    return ['<br>\n'.join(txt_definitions), ', '.join(txt_ipas), '<br>\n'.join(txt_examples)]

#print(search('fight'))