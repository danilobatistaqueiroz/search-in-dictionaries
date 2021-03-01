import requests
from bs4 import BeautifulSoup
from .basic import html_headers, convert_lang, capitalize_first, color_word, blur_color_text

def text_treatment(word,txt):
    txt = txt.replace('\n','')
    txt = txt.replace('\n',' ').replace('  ',' ').strip()
    txt = capitalize_first(txt)
    txt = color_word(word,txt)
    return txt

def rem_duplications_sort(out):
    if out['definitions'] is not None:
        out['definitions'] = list(set(out['definitions']))
        out['definitions'].sort()
    else:
        out['definitions'] = []
    if out['ipas'] is not None:
        out['ipas'] = list(set(out['ipas']))
        out['ipas'].sort()
    else:
        out['ipas'] = []
    if out['phrases'] is not None:
        out['phrases'] = list(set(out['phrases']))
        out['phrases'].sort()
    else:
        out['phrases'] = []

def generate_indexes(out):
    if out['definitions'] is not None:
        out['definitions'] = generate_index(out['definitions'])
    if out['phrases'] is not None:
        out['phrases'] = generate_index(out['phrases'])

def generate_index(lst):
    cnt=0
    lsttmp = []
    for item in lst:
        cnt+=1
        lsttmp.append(f'{cnt:02}. {item}')
    return lsttmp

def find_dictionary(word, soup, dic):
    txt_definitions = []
    txt_ipas = []
    txt_phrases = []
    div_definitions = soup.select(dic)
    for div_definition in div_definitions:
        definitions = div_definition.find_all('div', class_='def')
        for definition in definitions:
            text = definition.text
            text = text_treatment(word,text)
            text = blur_color_text(text)
            txt_definitions.append(f'{text}')
        senses = div_definition.find_all('div', class_='sense')
        for sense in senses:
            phrase = sense.find('div', class_='quote')
            if phrase is None:
                phrase = sense.find('span', class_='quote')
            if phrase is not None:
                phrase_definition = phrase.find_previous('div', class_='def')
                text_phrase = phrase.get_text().strip()
                text_phrase = text_treatment(word,text_phrase)
                txt_phrase_def = ''
                if phrase_definition is not None:
                    txt_phrase_def = phrase_definition.get_text()
                    txt_phrase_def = blur_color_text(txt_phrase_def)
                    txt_phrase_def = text_treatment(word,txt_phrase_def)
                txt_phrases.append(f'{txt_phrase_def}<BR><b>"{text_phrase}"</b>')
    sp_ipas = soup.find_all('span', class_=['pron', 'type-'])
    for sp_ipa in sp_ipas:
        texts = sp_ipa.text.replace('  ',' ').split(',')
        for text in texts:
            txt_ipas.append(text.strip())
    
    return {'definitions':txt_definitions, 'ipas':txt_ipas, 'phrases':txt_phrases}

def search(word):
    with requests.Session() as session:
        source = session.get(f'https://www.collinsdictionary.com/us/dictionary/english/{word}', headers=html_headers).text
        soup = BeautifulSoup(source, "html.parser")
        all_definitions = []
        out = find_dictionary(word, soup, 'div.definitions.american')
        if len(out['phrases']) == 0:
            all_definitions.append(out['definitions'])
            out = find_dictionary(word, soup, 'div.cobuild.am')
            if len(out['phrases']) == 0:
                all_definitions.append(out['definitions'])
                out = find_dictionary(word, soup, 'div.cobuild.ced')
    out['definitions'] = all_definitions.append(out['definitions'])
    rem_duplications_sort(out)
    generate_indexes(out)
    return ['', '<br>'.join(out['definitions']),', '.join(out['ipas']),'<br>'.join(out['phrases'])]

#print(search('tipped'))