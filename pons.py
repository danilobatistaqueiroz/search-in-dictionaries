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

languagues = {'ingles':'english','portugues':'portuguese','espanol':'spanish','frances':'french','alemao':'germani'}

def convert_lang(language):
    if language in languagues:
        return languagues[language]
    else:
        return language

def search(word, lang_source, lang_target):
    lang_source = convert_lang(lang_source)
    lang_target = convert_lang(lang_target)
    dic_phrases = []
    dic_phrases_pt = []
    lst_definitions = []
    lst_phonetics = []
    all_content = []
    with requests.Session() as session:
        source = session.get(f'https://en.pons.com/translate/{lang_source}-{lang_target}/{word}', headers=headers).text
        soup = BeautifulSoup(source, "html.parser")
        span_phonetics = soup.find_all('span', class_='phonetics')
        for phonetic in span_phonetics:
            lst_phonetics.append(phonetic.get_text().replace('[','').replace(']',''))
        lst_phonetics = list(set(lst_phonetics))
        str_phonetics = ' '.join(lst_phonetics)

        examples = soup.find('div', class_='result-page-examples-template')
        phrases = examples.find_all('dl', class_='dl-horizontal')
        for phrase in phrases:
            dt = phrase.find('dt',class_='dt-inner')
            dd = phrase.find('dd',class_='dd-inner')
            if dt is not None:
                div = dt.find('div',class_='source')
                target = dd.find('div',class_='target')
                dic_phrases.append(div.get_text())
                dic_phrases_pt.append(target.get_text())

        results = soup.find('div', class_='results')
        definitions = results.find_all('dl', class_='dl-horizontal')
        for definition in definitions:
            dt = definition.find('dt',class_='dt-inner')
            dd = definition.find('dd',class_='dd-inner')
            if dt is not None:
                div = dt.find('div',class_='source')
                target = dd.find('div',class_='target')
                word_definition = div.get_text().replace('\n','').capitalize()
                lst_definitions.append('<u>'+word_definition+'</u>: '+target.get_text().strip())

    str_definitions = '.  '.join(lst_definitions)
    str_definitions = str_definitions.replace('\n','')

    str_phrases = ''
    str_phrases_pt = ''
    cnt = 0
    for phrase in dic_phrases:
        cnt+=1
        str_phrases += f'{cnt}. {phrase}.<br>'
    cnt = 0
    for phrase in dic_phrases_pt:
        cnt+=1
        str_phrases_pt += f'{cnt}. {phrase}.<br>'

    all_content.append(str_definitions)
    all_content.append(str_phonetics)
    all_content.append(str_phrases)
    all_content.append(str_phrases_pt)

    return all_content

#print(search('milk','english','portuguese'))