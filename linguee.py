import requests
from bs4 import BeautifulSoup
from bs4 import NavigableString
from .basic import html_headers, convert_lang, capitalize_first, color_word, insert_end_dot, emphasie_text

def search(word, lang_source, lang_target):
    lang_source = convert_lang(lang_source)
    lang_target = convert_lang(lang_target)
    lst_definitions = []
    lst_examples = []
    lst_examples_translated = []
    with requests.Session() as session:
        source = session.get(f'https://www.linguee.com.br/{lang_source}-{lang_target}/search?source=auto&query={word}', headers=html_headers).text
        soup = BeautifulSoup(source, "html.parser")

        definitions = soup.find_all('a', class_='dictLink featured')
        for result in definitions:
            lst_definitions.append(result.get_text())

        examples = soup.find_all('div', class_='example')
        cnt = 0
        if len(examples) > 0:
            lst_examples.append('<b>. Phrases .</b>')
            lst_examples_translated.append('<b>. Phrases .</b>')
        for result in examples:
            cnt+=1
            lst_txt = result.get_text().split('—')
            example = insert_end_dot(capitalize_first(lst_txt[0].strip()))
            example = color_word(word,example)
            translated = insert_end_dot(capitalize_first(lst_txt[1].strip()))
            lst_examples.append(str(cnt)+'. '+example)

            term = result.parent.parent.find('h3').find('a')
            term = "".join([t for t in term.contents if type(t)==NavigableString])
            term = term.strip()

            lst_examples_translated.append(f'{cnt}. {translated} {emphasie_text(term)}')

        cnt=0
        inexact = soup.find('div', class_='example_lines inexact')
        if inexact is not None:
            lemmas = inexact.find_all('div', class_='lemma singleline')
            if len(lemmas) > 0:
                lst_examples.append('<b>. Examples .</b>')
                lst_examples_translated.append('<b>. Examples .</b>')
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

#print(search('streak','english','portuguese'))