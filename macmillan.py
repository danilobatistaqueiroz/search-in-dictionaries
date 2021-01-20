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

def insert_end_dot(text):
    text = text.strip()
    if text[-1:] != '.':
        text = text.strip()+'.'
    return text

def capitalize_first(txt):
    """capitalize the first letter"""
    if txt is not None and len(txt)>1:
        return txt[0:1].upper()+txt[1:]
    else:
        return txt

def color_word(word,txt):
    txt = txt.replace(word,f'<font color="#ff0000">{word}</font>')
    txt = txt.replace(f'{word.capitalize()}',f'<font color="#ff0000">{word.capitalize()}</font>')
    return txt

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
            text = capitalize_first(text)
            sections = text.split(':')
            sections[1] = capitalize_first(sections[1])
            if len(sections) > 1:
                text = '<u>'+sections[0]+'</u>: '+sections[1]
            else:
                text = sections[0]
            text = insert_end_dot(text)
            txt_definitions.append(f'{cnt}. {text}')
        span_prons = soup.find_all('span', class_='PRON')
        for pron in span_prons:
            text = pron.text.replace('  ',' ').replace('/','')
            txt_ipas.append(text)
        cnt=0
        div_examples = soup.find_all('div', class_='EXAMPLES')
        for p_example in div_examples:
            cnt+=1
            text = p_example.text.replace('\n',' ').replace('  ',' ')
            text = capitalize_first(text)
            text = insert_end_dot(text)
            text = color_word(word,text)
            txt_examples.append(f'{cnt}. {text}')

    return ['', '<br>\n'.join(txt_definitions), ', '.join(txt_ipas), '<br>\n'.join(txt_examples)]

#print(search('fight'))