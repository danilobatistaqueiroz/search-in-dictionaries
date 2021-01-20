import requests
from bs4 import BeautifulSoup
import string 

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
    if text.startswith('"') or text.startswith("'") or text.startswith("´") or text.startswith("`"):
        return text
    else:
        return '"'+text+'"'

def insert_end_dot(text):
    text = text.strip()
    if text[-1:] != '.':
        text = text+'.'
    return text

def color_word(word,txt):
    txt = txt.replace(word,f'<font color="#ff0000">{word}</font>')
    txt = txt.replace(f'{word.capitalize()}',f'<font color="#ff0000">{word.capitalize()}</font>')
    return txt

def capitalize_first(txt):
    """capitalize the first letter"""
    if txt is not None and len(txt)>1:
        return txt[0:1].upper()+txt[1:]
    else:
        return txt

def generate_index(lst):
    cnt=0
    lsttmp = []
    for item in lst:
        cnt+=1
        lsttmp.append(f'{cnt:02}. {item}')
    return lsttmp

def remove_dust(txt):
    txt = txt.replace('()','').replace('→','').replace(' = ','').replace('  ',' ')
    txt = txt.replace('[]','').replace(';;','').replace('()','')
    txt = txt.replace('( )','').replace(';   ;','').replace('  ',' ')
    txt = txt.replace('(= )','').replace('( = )','').replace('(=)','')
    txt = txt.replace('→','').replace('  ;   ','').replace('  ;  ','')
    txt = txt.replace('[+ ]','').replace('[+]','')
    txt = txt.replace(' ; ','').replace('[ ]','')
    txt = remove_first_last_chars(txt)
    return txt

def remove_first_last_chars(txt):
    if len(txt) > 5:
        if ';,.[=: '.find(txt[0:1]) > -1:
            txt = txt[1:]
        if ';,.[=: '.find(txt[-1]) > -1:
            txt = txt[0:-1]
    return txt

def without_good_definition(definition):
    if definition is None:
        return True
    definition = definition.replace(' ','')
    if len(definition) < 5:
        return True
    if contains_special_chars(definition) > 2:
        if len(definition) < 8:
            return True

def contains_special_chars(txt):
    cnt = 0
    invalidcharacters= set(string.punctuation)
    if any(char in invalidcharacters for char in txt):
        cnt+=1
    return cnt

def remove_ini_number(txt):
    for i in range(1,15):
        txt = txt.replace(str(i)+'. ','')
    return txt

def remove_ini_letter(txt):
    for i in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q']:
        if txt.strip().startswith(str(i)+'. '):
            txt = txt.replace(str(i)+'. ','')
    return txt

def definition_in_dictionary(dic_section, lst_definitions):
    if dic_section is not None:
        results = dic_section.find_all('div', 'ds-list')
        for result in results:
            definition = result.get_text().split(':')[0]
            definition = definition.strip()
            if definition.startswith('1.') or definition.startswith('2.') or definition.startswith('3.'):
                definition = remove_ini_number(definition)
                definition = remove_ini_letter(definition)
                definition = insert_end_dot(definition)
                definition = capitalize_first(definition)
                lst_definitions.append(definition)


def search(word, lang, country):
    lst_definitions = []
    lst_phrases = []
    lst_translations = []
    with requests.Session() as session:
        source = session.get(f'https://www.thefreedictionary.com/{word}', headers=headers).text
        soup = BeautifulSoup(source, "html.parser")

        hc_dict = soup.find('section', attrs={"data-src" : "hc_dict"})
        definition_in_dictionary(hc_dict,lst_definitions)
        american = soup.find('section', attrs={"data-src" : "hm"})
        definition_in_dictionary(american,lst_definitions)
        rHouse = soup.find('section', attrs={"data-src" : "rHouse"})
        definition_in_dictionary(rHouse,lst_definitions)

        dictionaries = soup.find('div', attrs={"id" : "Definition"})
        if dictionaries is None:
            return ['','','']

        results = dictionaries.find_all('span', class_='illustration')
        for result in results:
            contents = result.parent.get_text().split(':')
            definition = contents[0]
            phrase = ''
            if len(contents) > 1:
                phrase = contents[1]
            definition = remove_ini_number(definition)
            definition = remove_ini_letter(definition)
            definition = insert_end_dot(definition)
            definition = capitalize_first(definition)
            phrase = insert_end_dot(phrase)
            phrase = capitalize_first(phrase)
            phrase = insert_quotations(phrase)
            phrase = color_word(word,phrase)
            lst_phrases.append(definition+' <b>'+phrase+'</b>')

        translations = soup.find('div', attrs={"id" : "Translations"})
        if translations is not None:
            results = translations.find_all('span', class_='illustration')
            for result in results:
                phrase = result.get_text()
                translate = result.parent.find('span', attrs={"class":"trans","lang":country})
                if translate is None:
                    translate = result.parent.find('span', attrs={"class":"trans","lang":lang})
                definition = result.parent.findAll(text=True, recursive=False)
                definition = " ".join(definition)
                definition = remove_dust(definition)
                definition = capitalize_first(definition)
                txt_translate = ''
                if translate is not None:
                    txt_translate = translate.get_text()
                if txt_translate == '' and without_good_definition(definition):
                    continue
                phrase = capitalize_first(phrase.strip())
                phrase = insert_end_dot(phrase)
                phrase = insert_quotations(phrase)
                phrase = phrase.replace('not to be confused with.','')
                phrase = color_word(word,phrase)
                lst_phrases.append("".join(definition)+f' <b>{phrase}</b> <i><u>{txt_translate}</u></i>')

            kdict = translations.find('section', attrs={"data-src" : "kdict"})
            if kdict is not None:
                for child in kdict.descendants:
                    child_text = ''
                    if str(type(child)) == "<class 'bs4.element.Tag'>":
                        child_text = child.get_text().replace('\n','').strip()
                    if child.name == 'h2':
                        lst_translations.append(f'<b>{child_text}</b>')
                    elif child.name == 'i':
                        lst_translations.append(f'<b>{child_text}</b>')
                    elif child.name == 'b':
                        lst_translations.append(f'<b>{child_text}</b>')
                    else:
                        if str(type(child)) == "<class 'bs4.element.Tag'>":
                            if child.has_attr('lang') and child.has_attr('class'):
                                if child['class'][0] == 'trans' and child['lang'] == 'br':
                                    lst_translations.append(f'{child_text}')

    lst_definitions = list(set(lst_definitions))
    lst_phrases = list(set(lst_phrases))
    lst_definitions.sort()
    lst_phrases.sort()
    lst_definitions = generate_index(lst_definitions)
    lst_phrases = generate_index(lst_phrases)

    return [' '.join(lst_translations), '<br>'.join(lst_definitions), '', '<br>'.join(lst_phrases)]



#print(search('milk','pt','br'))