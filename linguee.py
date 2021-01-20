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

languagues = {'english':'ingles','portuguese':'portugues','spanish':'espanol','french':'frances','germani':'alemao'}

def convert_lang(language):
    if language in languagues:
        return languagues[language]
    else:
        return language

def insert_end_dot(text):
    text = text.strip()
    if text[-1:] != '.':
        text = text.strip()+'.'
    return text

def capitalize_first(txt):
    """capitalize the first letter"""
    if txt is not None and len(txt)>1:
        return txt[0:1].upper()+txt[1:]

def color_word(word,txt):
    txt = txt.replace(word,f'<font color="#ff0000">{word}</font>')
    txt = txt.replace(f'{word.capitalize()}',f'<font color="#ff0000">{word.capitalize()}</font>')
    return txt

def search(word, lang_source, lang_target):
    lang_source = convert_lang(lang_source)
    lang_target = convert_lang(lang_target)
    lst_definitions = []
    lst_examples = []
    lst_examples_translated = []
    with requests.Session() as session:
        source = session.get(f'https://www.linguee.com.br/{lang_source}-{lang_target}/search?source=auto&query={word}', headers=headers).text
        soup = BeautifulSoup(source, "html.parser")

        definitions = soup.find_all('a', class_='dictLink featured')
        for result in definitions:
            lst_definitions.append(result.get_text())

        examples = soup.find_all('div', class_='example')
        cnt = 0
        for result in examples:
            cnt+=1
            lst_txt = result.get_text().split('—')
            example = insert_end_dot(capitalize_first(lst_txt[0].strip()))
            example = color_word(word,example)
            translated = insert_end_dot(capitalize_first(lst_txt[1].strip()))
            lst_examples.append(str(cnt)+'. '+example)
            lst_examples_translated.append(str(cnt)+'. '+translated)

        inexact = soup.find('div', class_='example_lines inexact')
        if inexact is not None:
            lemmas = inexact.find_all('div', class_='lemma singleline')
            for lemma in lemmas:
                cnt+=1
                taglemma = lemma.find('span', class_='tag_lemma')
                dictLink_source = taglemma.find('a', class_='dictLink')

                lemmacontent = lemma.find('div', class_='lemma_content')
                dictLink2_target = lemmacontent.find('a', class_='dictLink')

                example = insert_end_dot(dictLink_source.get_text())
                translated = insert_end_dot(dictLink2_target.get_text())

                example = color_word(word,example)
                lst_examples.append(str(cnt)+'. '+example)
                lst_examples_translated.append(str(cnt)+'. '+translated)

    return ['', ','.join(lst_definitions), '', '<br>'.join(lst_examples), '<br>'.join(lst_examples_translated)]

#print(search('slayer','english','portuguese'))