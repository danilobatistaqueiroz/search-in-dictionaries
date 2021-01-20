import requests
from bs4 import BeautifulSoup
from bs4 import NavigableString
import json
import re

headers = {
   'Content-Type': 'application/xhtml+xml',
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET, POST,OPTIONS',
    'Access-Control-Allow-Headers': '*',
    'Access-Control--Max-Age': '86400',
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36'
}

headers_post = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET, POST,OPTIONS',
    'Access-Control-Allow-Headers': '*',
    'Access-Control--Max-Age': '86400',
    'Content-Type': 'application/json',
    'Accept': 'text/plain',
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36'
}

languagues = {'ingles':'english','portugues':'portuguese','espanol':'spanish','frances':'french','alemao':'germani'}

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
    else:
        return txt

def color_word(txt):
    txt = re.sub(r'<em class="both">(.*)</em>', '<font color="#ff0000">\g<1></font>', txt)
    txt = re.sub(r'<em>(.*)</em>','<font color="#ff0000">\g<1></font>',txt)
    return txt

def dic_translations_to_text(lst_dic):
    txt = ''
    if len(lst_dic) == 0:
        return ''
    for dic in lst_dic:
        txt+=f'({dic["freq"]}){dic["text"]},'
    return txt[:-1]

def phrases(word,term,abrv_target,lang_target):
    data = {"source_text":word,"target_text":term,"source_lang":"en","target_lang":abrv_target,"npage":1,"mode":0}
    source = requests.post(f'https://context.reverso.net/translation/english-{lang_target}/{word}', json=data, headers=headers_post)
    r_json = source.json()
    phrases=[]
    phrases.append({'phrase':color_word(r_json['list'][0]['s_text']), 'translation':color_word(r_json['list'][0]['t_text'])})
    phrases.append({'phrase':color_word(r_json['list'][1]['s_text']), 'translation':color_word(r_json['list'][1]['t_text'])})
    phrases.append({'phrase':color_word(r_json['list'][2]['s_text']), 'translation':color_word(r_json['list'][2]['t_text'])})
    return phrases

def phrases_text(items):
    text = ''
    cnt = 0
    for item in items:
        cnt+=1
        text+=f'.{cnt}.<br>'
        for phrase in item:
            text+=phrase['phrase']+'<br>'
    return text

def phrases_tr_text(items):
    text = ''
    cnt = 0
    for item in items:
        cnt+=1
        text+=f'.{cnt}.<br>'
        for phrase in item:
            text+=phrase['translation']+'<br>'
    return text

def search(word,abrv_target,lang_target):
    lang_target = convert_lang(lang_target)
    lst_translations = []
    with requests.Session() as session:
        source = session.get(f'https://context.reverso.net/translation/english-{lang_target}/{word}', headers=headers).text
        soup = BeautifulSoup(source, "html.parser")
        cnt=0
        freq=0
        text=''
        div_translations = soup.find('div', attrs={"id" : "translations-content"})
        for translation in div_translations.children:
            cnt+=1
            if type(translation) == NavigableString:
                continue
            text = translation.get_text()
            freq = int(translation['data-freq'])
            text = text.replace('\n','').strip()
            if text.lower() == word or len(text) == 0:
                continue
            lst_translations.append({'freq':freq,'text':text})
    sorted_words = sorted(lst_translations, key=lambda row: (row['freq']), reverse=True)
    txt_translations = dic_translations_to_text(sorted_words)
    cnt = 0
    items = []
    for term in sorted_words:
        cnt+=1
        items.append(phrases(word,term['text'],abrv_target,lang_target))
        if cnt == 5:
            break
    txt_phrases = phrases_text(items)
    txt_phrases_tr = phrases_tr_text(items)
    return [txt_translations,'','',txt_phrases,txt_phrases_tr]

#print(search('weed','pt','portuguese'))
#print(phrases('whacked','matar'))