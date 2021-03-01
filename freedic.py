import requests
from bs4 import BeautifulSoup
from bs4.element import Tag
import string 
from .basic import html_headers, convert_lang, capitalize_first, color_word, insert_end_dot, blur_color_text, emphasie_text, insert_quotations

def generate_index(lst):
    cnt=0
    lsttmp = []
    for item in lst:
        cnt+=1
        lsttmp.append(f'{cnt:02}. {item}')
    return lsttmp

def generate_phrases_index(lst):
    cnt=0
    lsttmp = []
    a_definition = ''
    a_phrase = ''
    lst = sorted(lst, key=lambda row: (row['definition']))
    for item in lst:
        if item['definition'] == a_definition:
            if item['phrase'] != a_phrase:
                lsttmp.append(item['phrase'])
        else:
            cnt+=1
            lsttmp.append(f'{cnt:02}. '+blur_color_text(item['definition'])+'<br>'+item['phrase'])
            a_definition = item['definition']
            a_phrase = item['phrase']
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

class House:
    def select(self,r_house,word):
        if r_house is not None:
            return self.get_pronun(r_house)
        return ''

    def get_pronun(self,r_house):
        pron = r_house.find('span', attrs={"class" : "pron"})
        if pron is not None:
            return pron.get_text().strip()
        else:
            return ''

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

def join_all_definitions(definitions_hc, definitions_hm, definitions_house):
    definitions_hc = generate_index(definitions_hc)
    definitions_hm = generate_index(definitions_hm)
    definitions_house = generate_index(definitions_house)
    all_definitions = []
    if len(definitions_hc) > 0:
        all_definitions.append('<b>. Collins English Dictionary .</b>')
        all_definitions.extend(definitions_hc)
    if len(definitions_hm) > 0:
        all_definitions.append('<b>. American Heritage .</b>')
        all_definitions.extend(definitions_hm)
    if len(definitions_house) > 0:
        all_definitions.append('<b>. Random House Kernerman .</b>')
        all_definitions.extend(definitions_house)
    return all_definitions

def search(word, lang, country):
    definitions_hc = []
    definitions_hm = []
    definitions_house = []
    lst_phrases = []
    lst_translations = []
    with requests.Session() as session:
        source = session.get(f'https://www.thefreedictionary.com/{word}', headers=html_headers).text
        soup = BeautifulSoup(source, "html.parser")

        hc_dict = soup.find('section', attrs={"data-src" : "hc_dict"})
        definition_in_dictionary(hc_dict,definitions_hc)
        american = soup.find('section', attrs={"data-src" : "hm"})
        definition_in_dictionary(american,definitions_hm)
        rHouse = soup.find('section', attrs={"data-src" : "rHouse"})
        definition_in_dictionary(rHouse,definitions_house)

        house = House()
        ipa = house.select(rHouse,word)

        dictionaries = soup.find('div', attrs={"id" : "Definition"})
        if dictionaries is None:
            return ['','','','']

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
            lst_phrases.append({'definition':definition,'phrase':'<b>'+phrase+'</b>'})

        translations = soup.find('div', attrs={"id" : "Translations"})
        if translations is not None:
            kdict = translations.find('section', attrs={"data-src" : "kdict"})
            if kdict is not None:
                results = kdict.find_all('span', class_='illustration')
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
                        txt_translate = translate.get_text().strip()
                    if txt_translate == '' and without_good_definition(definition):
                        continue
                    phrase = capitalize_first(phrase.strip())
                    phrase = insert_end_dot(phrase)
                    phrase = insert_quotations(phrase)
                    phrase = phrase.replace('not to be confused with.','')
                    phrase = color_word(word,phrase)
                    lst_phrases.append({'definition':"".join(definition),'phrase':f' <b>{phrase}</b> '+emphasie_text(txt_translate)})

            simple_trans = translations.find('section', attrs={"class" : "simpleTrans"})
            if simple_trans is not None:
                terms = simple_trans.find('div', attrs={"lang" : country})
                if terms is None:
                    terms = simple_trans.find('div', attrs={"lang" : lang})
                if terms is not None:
                    simple_translations = terms.find_all('a')
                    txt_trs = ''
                    for trs in simple_translations:
                        txt_trs += trs.get_text()+', '
                    if len(simple_translations) > 0:
                        lst_translations.append(txt_trs[:-2])
            
            kdict = translations.find('section', attrs={"data-src" : "kdict"})
            if kdict is not None:
                for child in kdict.descendants:
                    child_text = ''
                    if type(child) == Tag:
                        child_text = child.get_text().replace('\n','').strip()
                    if child.name == 'h2':
                        child_text = remove_abrv(child_text)
                        lst_translations.append(f'<b>{child_text}</b>')
                    elif child.name == 'i':
                        child_text = remove_abrv(child_text)
                        lst_translations.append(f'<b>{child_text}</b>')
                    elif child.name == 'b':
                        child_text = remove_abrv(child_text)
                        lst_translations.append(f'<b>{child_text}</b>')
                    else:
                        if type(child) == Tag:
                            if child.has_attr('lang') and child.has_attr('class'):
                                if child['class'][0] == 'trans' and child['lang'] == country:
                                    lst_translations.append(f'{child_text}')

    lst_phrases = generate_phrases_index(lst_phrases)

    all_definitions = join_all_definitions(definitions_hc, definitions_hm, definitions_house)

    return [' '.join(lst_translations), '<br>'.join(all_definitions), ipa, '<br>'.join(lst_phrases)]


def remove_abrv(txt):
    txt = txt.replace(' etc ','').replace(' eg ','').replace('especially ','')
    if txt.endswith('etc'):
        txt = txt.replace('etc','')
    if txt.endswith('eg'):
        txt = txt.replace('eg','')
    if txt.endswith('especially'):
        txt = txt.replace('especially','')
    return txt

#print(search('humble','pt','br'))