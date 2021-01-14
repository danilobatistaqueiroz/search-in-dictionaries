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

def insert_quotations(text):
    text = text.strip()
    if text.startswith('"') or text.startswith("'"):
        return text
    else:
        return '"'+text+'"'

def insert_end_dot(text):
    text = text.strip()
    if text[-1:] != '.':
        text = text+'.'
    return text

def definition_in_dictionary(dic_section, cnt, lst_definitions):
    if dic_section is not None:
        results = dic_section.find_all('div', 'ds-list')
        for result in results:
            cnt+=1
            definition = result.get_text().split(':')[0]
            definition = definition.strip()
            if definition.startswith('1.') or definition.startswith('2.'):
                definition = remove_ini_number(definition)
                definition = remove_ini_letter(definition)
                lst_definitions.append(f'{cnt:02}. '+insert_end_dot(definition))
    return cnt


def search(word, lang):
    lst_definitions = []
    lst_phrases = []
    with requests.Session() as session:
        source = session.get(f'https://www.thefreedictionary.com/{word}', headers=headers).text
        soup = BeautifulSoup(source, "html.parser")

        cnt = 0
        hc_dict = soup.find('section', attrs={"data-src" : "hc_dict"})
        cnt = definition_in_dictionary(hc_dict,cnt,lst_definitions)
        american = soup.find('section', attrs={"data-src" : "hm"})
        cnt = definition_in_dictionary(american,cnt,lst_definitions)
        rHouse = soup.find('section', attrs={"data-src" : "rHouse"})
        cnt= definition_in_dictionary(rHouse,cnt,lst_definitions)

        cnt = 0
        dictionaries = soup.find('div', attrs={"id" : "Definition"})
        results = dictionaries.find_all('span', class_='illustration')
        for result in results:
            cnt+=1
            contents = result.parent.get_text().split(':')
            definition = contents[0]
            phrase = ''
            if len(contents) > 1:
                phrase = contents[1]
            definition = remove_ini_number(definition)
            definition = remove_ini_letter(definition)
            definition = insert_end_dot(definition)
            definition = definition.capitalize()
            phrase = insert_end_dot(phrase)
            phrase = phrase.capitalize()
            phrase = insert_quotations(phrase)
            lst_phrases.append(f'{cnt:02}. '+definition+' <b>'+phrase+'</b>')

        translations = soup.find('div', attrs={"id" : "Translations"})
        if translations is not None:
            results = translations.find_all('span', class_='illustration')
            for result in results:
                cnt+=1
                phrase = result.get_text()
                translate = result.parent.find('span', attrs={"class":"trans","lang":lang})
                definition = result.parent.findAll(text=True, recursive=False)
                definition = " ".join(definition)
                definition = definition.replace('()','').replace('→','').replace(' = ','').replace('  ',' ')
                definition = definition.replace('[]','').replace(';;','').replace('()','')
                definition = definition.replace('( )','').replace(';   ;','').replace('  ',' ')
                txt_translate = ''
                if translate is not None:
                    txt_translate = translate.get_text()
                phrase = phrase.strip().capitalize()
                phrase = insert_end_dot(phrase)
                phrase = insert_quotations(phrase)
                lst_phrases.append(f'{cnt:02}. '+"".join(definition)+' <b>'+phrase+'</b> '+txt_translate+'')

    lst_definitions = list(set(lst_definitions))
    lst_phrases = list(set(lst_phrases))
    lst_definitions.sort()
    lst_phrases.sort()
    return ['<br>'.join(lst_definitions), '', '<br>'.join(lst_phrases)]

def remove_ini_number(txt):
    for i in range(1,15):
        txt = txt.replace(str(i)+'. ','')
    return txt

def remove_ini_letter(txt):
    for i in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q']:
        if txt.strip().startswith(str(i)+'. '):
            txt = txt.replace(str(i)+'. ','')
    return txt

#print(search('milk','pt'))