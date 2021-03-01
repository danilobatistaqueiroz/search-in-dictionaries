import requests
from bs4 import BeautifulSoup
from .basic import html_headers, color_word, blur_color_text, emphasie_text


def get_result(cnt, word, results):
    terms = []
    translations = []
    definitions = []
    phrases = []

    term = ''
    translation = ''
    sense = ''

    for result in results:
        td_term = result.find('td',class_='FrWrd')
        td_translation = result.find('td',class_='ToWrd')
        all_dsense = result.findAll('td')
        td_dsense = None
        if len(all_dsense) >= 2:
            td_dsense = all_dsense[1]
        td_en_phrase = result.find('td',class_='FrEx')
        td_tr_phrase = result.find('td',class_='ToEx')
        if td_term is not None:
            term = td_term.find(text=True)
            terms.append(term)
        if td_translation is not None:
            translation = td_translation.find(text=True)
            translation = translation.strip()
            translations.append(translation)
        if td_term is not None and td_dsense is not None:
            sense = td_dsense.get_text()
        if td_en_phrase is not None:
            cnt+=1
            definitions.append(f'{cnt:02}. <b>{term}</b> {sense}')
            en_phrase = td_en_phrase.get_text()
            for t in terms:
                en_phrase = color_word(t,en_phrase)
            if en_phrase.find(word) == -1:
                continue
            phrases.append(f'{cnt:02}. '+blur_color_text(f'{term} {sense}')+'<br><b>"'+en_phrase+'"</b> '+emphasie_text(translation))
            term = ''
            sense = ''
            translation = ''
        if td_tr_phrase is not None:
            tr_phrase = ''
            tr_phrase = td_tr_phrase.get_text()
            for t in terms:
                tr_phrase = color_word(t,tr_phrase)
            if tr_phrase.find('Esta frase não é uma tradução da frase em inglês') == -1:
                if len(phrases) > 0:
                    phrases[len(phrases)-1]+=f'<br><i>"{tr_phrase}"</i>'

    return {'cnt':cnt,'translations':translations,'definitions':definitions,'phrases':phrases}

def search(word, abrv_source, abrv_target):
    with requests.Session() as session:
        cnt = 0
        source = session.get(f'https://www.wordreference.com/{abrv_source}{abrv_target}/{word}', headers=html_headers).text
        soup = BeautifulSoup(source, "html.parser")
        even = soup.find_all('tr', class_='even')
        even_results = get_result(cnt,word,even)
        cnt = even_results['cnt']
        odd = soup.find_all('tr', class_='odd')
        odd_results = get_result(cnt,word,odd)

        even_results['translations'].extend(odd_results['translations'])
        even_results['definitions'].extend(odd_results['definitions'])
        even_results['phrases'].extend(odd_results['phrases'])

        even_results['translations'] = list(set(even_results['translations']))

        translations = ','.join(even_results['translations'])
        definitions = '<BR>'.join(even_results['definitions'])
        phrases = '<BR><BR>'.join(even_results['phrases'])

    return [translations,definitions,'',phrases]


#print(search('tricky', 'en', 'pt'))



