import requests
from bs4 import BeautifulSoup
from .basic import html_headers, convert_lang, capitalize_first, color_word, insert_end_dot

def blur_color_text(txt):
    return f'<font color="#c7c7c7"><i>{txt}</i></font>'

def blur_explanation_bold_phrase(txt):
    dot = txt.find(':')
    if dot > 0:
        explanation = txt[:dot+1]
        phrase = txt[dot+1:]
        explanation = blur_color_text(explanation)
        phrase = f'<b>{phrase}</b>'
        txt = explanation + phrase
    else:
        txt = f'<b>{txt}</b>'
    return txt

def search(word):
    txt_definitions = []
    txt_examples = []
    txt_ipas = []
    with requests.Session() as session:
        source = session.get(f'https://www.macmillandictionary.com/us/dictionary/american/{word}', headers=html_headers).text
        soup = BeautifulSoup(source, "html.parser")
        cntdef=0
        senses = soup.find_all('div', class_='SENSE-CONTENT')
        for sense in senses:
            span_definition = sense.find('span', class_='DEFINITION')

            cntdef+=1
            txt_def = span_definition.text.replace('\n',' ').replace('  ',' ')
            txt_def = capitalize_first(txt_def)
            sections = txt_def.split(':')
            if len(sections) > 1:
                sections[1] = capitalize_first(sections[1])
                txt_def = '<u>'+sections[0]+'</u>: '+sections[1]
            else:
                txt_def = sections[0]
            txt_def = insert_end_dot(txt_def)
            txt_definitions.append(f'{cntdef}. {txt_def}')

            span_prons = sense.find_all('span', class_='PRON')
            for pron in span_prons:
                txt_ipa = pron.text.replace('  ',' ').replace('/','')
                txt_ipas.append(txt_ipa)

            div_examples = sense.find_all('div', class_='EXAMPLES')
            if len(div_examples) > 0:
                txt_def = blur_color_text(f'{cntdef}. {txt_def}')
                txt_examples.append(txt_def)
            for p_example in div_examples:
                text = p_example.text.replace('\n',' ').replace('  ',' ')
                text = capitalize_first(text)
                text = insert_end_dot(text)
                text = color_word(word,text)
                text = blur_explanation_bold_phrase(text)
                txt_examples.append(text)

    return ['', '<br>\n'.join(txt_definitions), ', '.join(txt_ipas), '<br>\n'.join(txt_examples)]

#print(search('overcome'))