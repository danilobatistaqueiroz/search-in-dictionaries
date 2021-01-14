import requests
from bs4 import BeautifulSoup
import time
import asyncio
from pyppeteer import launch

headers = {
   'Content-Type': 'application/xhtml+xml',
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET, POST,OPTIONS',
    'Access-Control-Allow-Headers': '*',
    'Access-Control--Max-Age': '86400',
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36'

}

doc = """

<div class="J0lOec"><span class="VIiyi" jsaction="mouseup:BR6jm" jsname="jqKxS" lang="pt">fundida</span><span aria-hidden="true" class="XKE1nd">...</span><span class="zEswK"><span class="yieiFb">(Editado)</span><span class="kihvAe" jsaction="click:zUqxqb,IPcVpf" jsname="O4MOEe"><span class="zpaZf"><svg focusable="false" width="16" height="16" viewBox="0 0 24 24" class=" NMm5M hhikbc"><path d="M14.1 8H7.83l2.59-2.59L9 4 4 9l5 5 1.41-1.41L7.83 10h6.27c2.15 0 3.9 1.57 3.9 3.5S16.25 17 14.1 17H7v2h7.1c3.25 0 5.9-2.47 5.9-5.5S17.35 8 14.1 8z"></path></svg></span>Restaurar original</span></span><div class="NlvNvf">(feminino)</div></div>

<div class="J0lOec"><span class="VIiyi" jsaction="mouseup:BR6jm" jsname="jqKxS" lang="pt">fundido</span><span aria-hidden="true" class="XKE1nd">...</span><span class="zEswK"><span class="yieiFb">(Editado)</span><span class="kihvAe" jsaction="click:zUqxqb,IPcVpf" jsname="O4MOEe"><span class="zpaZf"><svg focusable="false" width="16" height="16" viewBox="0 0 24 24" class=" NMm5M hhikbc"><path d="M14.1 8H7.83l2.59-2.59L9 4 4 9l5 5 1.41-1.41L7.83 10h6.27c2.15 0 3.9 1.57 3.9 3.5S16.25 17 14.1 17H7v2h7.1c3.25 0 5.9-2.47 5.9-5.5S17.35 8 14.1 8z"></path></svg></span>Restaurar original</span></span><div class="NlvNvf">(masculino)</div></div>

<div class="GQpbTd">
<div jsname="YVjlBb">
<div class="I87fLc oLovEc Xz0hkf sMVRZe">
<div class="Dwvecf">
<table class="CFNMfb">
<tbody class="U87jab">

<tr class="TKwHGb"><th class="yYp8Hb" scope="rowgroup" rowspan="12"><div class="G8Go6b"><div class="eIKIse Nv4rrc">substantivo</div></div></th><th class="rsNpAc S18kfe" scope="row"><div class="KnIHac" jsname="mnCBDf" role="presentation" lang="pt"><span class="j7bWb">o</span> <span class="kgnlhe" jsaction=" blur: Om5fgd; click: JUJgG; focus: kFg5W; mouseout: Om5fgd; mouseover: kFg5W;XIxNK:LOG0D;w02ePb:RzCLcc" jsname="gm7qse" data-term-type="tl" role="button" tabindex="0" data-sl="pt" data-tl="en" dir="ltr">elenco</span></div></th><td class="rsNpAc xex4Kc"><ul role="list" class="FgtVoc OvhKBb"><li class="DshmM"><span class="MtFg0" jsaction=" blur: Om5fgd; click: JUJgG; focus: kFg5W; mouseout: Om5fgd; mouseover: kFg5W;XIxNK: LOG0D;w02ePb: RzCLcc" jsname="zBOkhd" data-term-type="sl" role="button" tabindex="0" data-sl="en" data-tl="pt" lang="en">cast</span><span aria-hidden="true">, </span></li><li class="DshmM"><span class="MtFg0" jsaction=" blur: Om5fgd; click: JUJgG; focus: kFg5W; mouseout: Om5fgd; mouseover: kFg5W;XIxNK: LOG0D;w02ePb: RzCLcc" jsname="zBOkhd" data-term-type="sl" role="button" tabindex="0" data-sl="en" data-tl="pt" lang="en">list</span><span aria-hidden="true">, </span></li><li class="DshmM"><span class="MtFg0" jsaction=" blur: Om5fgd; click: JUJgG; focus: kFg5W; mouseout: Om5fgd; mouseover: kFg5W;XIxNK: LOG0D;w02ePb: RzCLcc" jsname="zBOkhd" data-term-type="sl" role="button" tabindex="0" data-sl="en" data-tl="pt" lang="en">index</span></li></ul></td><td class="rsNpAc ROtxYd"><div jscontroller="HwavCb" jsshadow="" jsaction="mouseover: kptBG(Fs81Kd); mouseout: o9UdU(Fs81Kd),o9UdU(V6DMGe)" data-show-delay-ms="250" data-append-to-body="true" data-propagate-tooltip-mouseover-events="true" data-anchor-corner="bottom-left" data-popup-corner="top-left" id="ow193" __is_owner="true"><div jsname="Fs81Kd"><span jsslot=""><span role="img" class="YF3enc" aria-label="Comum"><div aria-hidden="true" class="ksE5nf EiZ8Dd"></div><div aria-hidden="true" class="ksE5nf EiZ8Dd"></div><div aria-hidden="true" class="ksE5nf EiZ8Dd"></div></span></span></div></div></td></tr>

<tr class="TKwHGb"><th class="rsNpAc S18kfe" scope="row"><div class="KnIHac" jsname="mnCBDf" role="presentation" lang="pt"><span class="j7bWb">o</span> <span class="kgnlhe" jsaction=" blur: Om5fgd; click: JUJgG; focus: kFg5W; mouseout: Om5fgd; mouseover: kFg5W;XIxNK:LOG0D;w02ePb:RzCLcc" jsname="gm7qse" data-term-type="tl" role="button" tabindex="0" data-sl="pt" data-tl="en" dir="ltr">lance</span></div></th><td class="rsNpAc xex4Kc"><ul role="list" class="FgtVoc OvhKBb"><li class="DshmM"><span class="MtFg0" jsaction=" blur: Om5fgd; click: JUJgG; focus: kFg5W; mouseout: Om5fgd; mouseover: kFg5W;XIxNK: LOG0D;w02ePb: RzCLcc" jsname="zBOkhd" data-term-type="sl" role="button" tabindex="0" data-sl="en" data-tl="pt" lang="en">throw</span><span aria-hidden="true">, </span></li><li class="DshmM"><span class="MtFg0" jsaction=" blur: Om5fgd; click: JUJgG; focus: kFg5W; mouseout: Om5fgd; mouseover: kFg5W;XIxNK: LOG0D;w02ePb: RzCLcc" jsname="zBOkhd" data-term-type="sl" role="button" tabindex="0" data-sl="en" data-tl="pt" lang="en">move</span><span aria-hidden="true">, </span></li><li class="DshmM"><span class="MtFg0" jsaction=" blur: Om5fgd; click: JUJgG; focus: kFg5W; mouseout: Om5fgd; mouseover: kFg5W;XIxNK: LOG0D;w02ePb: RzCLcc" jsname="zBOkhd" data-term-type="sl" role="button" tabindex="0" data-sl="en" data-tl="pt" lang="en">cast</span><span aria-hidden="true">, </span></li><li class="DshmM"><span class="MtFg0" jsaction=" blur: Om5fgd; click: JUJgG; focus: kFg5W; mouseout: Om5fgd; mouseover: kFg5W;XIxNK: LOG0D;w02ePb: RzCLcc" jsname="zBOkhd" data-term-type="sl" role="button" tabindex="0" data-sl="en" data-tl="pt" lang="en">shot</span><span aria-hidden="true">, </span></li><li class="DshmM"><span class="MtFg0" jsaction=" blur: Om5fgd; click: JUJgG; focus: kFg5W; mouseout: Om5fgd; mouseover: kFg5W;XIxNK: LOG0D;w02ePb: RzCLcc" jsname="zBOkhd" data-term-type="sl" role="button" tabindex="0" data-sl="en" data-tl="pt" lang="en">hurl</span><span aria-hidden="true">, </span></li><li class="DshmM"><span class="MtFg0" jsaction=" blur: Om5fgd; click: JUJgG; focus: kFg5W; mouseout: Om5fgd; mouseover: kFg5W;XIxNK: LOG0D;w02ePb: RzCLcc" jsname="zBOkhd" data-term-type="sl" role="button" tabindex="0" data-sl="en" data-tl="pt" lang="en">shy</span></li></ul></td><td class="rsNpAc ROtxYd"><div jscontroller="HwavCb" jsshadow="" jsaction="mouseover: kptBG(Fs81Kd); mouseout: o9UdU(Fs81Kd),o9UdU(V6DMGe)" data-show-delay-ms="250" data-append-to-body="true" data-propagate-tooltip-mouseover-events="true" data-anchor-corner="bottom-left" data-popup-corner="top-left"><div jsname="Fs81Kd"><span jsslot=""><span role="img" class="YF3enc" aria-label="Incomum"><div aria-hidden="true" class="ksE5nf EiZ8Dd"></div><div aria-hidden="true" class="ksE5nf EiZ8Dd"></div><div aria-hidden="true" class="ksE5nf fXx9Lc"></div></span></span></div><div jsshadow="" class=" B2mKhd  eQGGme FYRjob" jsname="V6DMGe" style="display: none;"><span jsslot=""><span jsslot="">Incomum</span></span></div></div></td></tr>

<tr class="TKwHGb"><th class="rsNpAc S18kfe" scope="row"><div class="KnIHac" jsname="mnCBDf" role="presentation" lang="pt"><span class="j7bWb">o</span> <span class="kgnlhe" jsaction=" blur: Om5fgd; click: JUJgG; focus: kFg5W; mouseout: Om5fgd; mouseover: kFg5W;XIxNK:LOG0D;w02ePb:RzCLcc" jsname="gm7qse" data-term-type="tl" role="button" tabindex="0" data-sl="pt" data-tl="en" dir="ltr">matiz</span></div></th><td class="rsNpAc xex4Kc"><ul role="list" class="FgtVoc OvhKBb"><li class="DshmM"><span class="MtFg0" jsaction=" blur: Om5fgd; click: JUJgG; focus: kFg5W; mouseout: Om5fgd; mouseover: kFg5W;XIxNK: LOG0D;w02ePb: RzCLcc" jsname="zBOkhd" data-term-type="sl" role="button" tabindex="0" data-sl="en" data-tl="pt" lang="en">hue</span><span aria-hidden="true">, </span></li><li class="DshmM"><span class="MtFg0" jsaction=" blur: Om5fgd; click: JUJgG; focus: kFg5W; mouseout: Om5fgd; mouseover: kFg5W;XIxNK: LOG0D;w02ePb: RzCLcc" jsname="zBOkhd" data-term-type="sl" role="button" tabindex="0" data-sl="en" data-tl="pt" lang="en">tint</span><span aria-hidden="true">, </span></li><li class="DshmM"><span class="MtFg0" jsaction=" blur: Om5fgd; click: JUJgG; focus: kFg5W; mouseout: Om5fgd; mouseover: kFg5W;XIxNK: LOG0D;w02ePb: RzCLcc" jsname="zBOkhd" data-term-type="sl" role="button" tabindex="0" data-sl="en" data-tl="pt" lang="en">shade</span><span aria-hidden="true">, </span></li><li class="DshmM"><span class="MtFg0" jsaction=" blur: Om5fgd; click: JUJgG; focus: kFg5W; mouseout: Om5fgd; mouseover: kFg5W;XIxNK: LOG0D;w02ePb: RzCLcc" jsname="zBOkhd" data-term-type="sl" role="button" tabindex="0" data-sl="en" data-tl="pt" lang="en">tinge</span><span aria-hidden="true">, </span></li><li class="DshmM"><span class="MtFg0" jsaction=" blur: Om5fgd; click: JUJgG; focus: kFg5W; mouseout: Om5fgd; mouseover: kFg5W;XIxNK: LOG0D;w02ePb: RzCLcc" jsname="zBOkhd" data-term-type="sl" role="button" tabindex="0" data-sl="en" data-tl="pt" lang="en">cast</span><span aria-hidden="true">, </span></li><li class="DshmM"><span class="MtFg0" jsaction=" blur: Om5fgd; click: JUJgG; focus: kFg5W; mouseout: Om5fgd; mouseover: kFg5W;XIxNK: LOG0D;w02ePb: RzCLcc" jsname="zBOkhd" data-term-type="sl" role="button" tabindex="0" data-sl="en" data-tl="pt" lang="en">iris</span></li></ul></td><td class="rsNpAc ROtxYd"><div jscontroller="HwavCb" jsshadow="" jsaction="mouseover: kptBG(Fs81Kd); mouseout: o9UdU(Fs81Kd),o9UdU(V6DMGe)" data-show-delay-ms="250" data-append-to-body="true" data-propagate-tooltip-mouseover-events="true" data-anchor-corner="bottom-left" data-popup-corner="top-left"><div jsname="Fs81Kd"><span jsslot=""><span role="img" class="YF3enc" aria-label="Rara"><div aria-hidden="true" class="ksE5nf EiZ8Dd"></div><div aria-hidden="true" class="ksE5nf fXx9Lc"></div><div aria-hidden="true" class="ksE5nf fXx9Lc"></div></span></span></div><div jsshadow="" class=" B2mKhd  eQGGme FYRjob" jsname="V6DMGe" style="display: none;"><span jsslot=""><span jsslot="">Rara</span></span></div></div></td></tr>

</tbody>
</table>
</div>
</div>
</div>
</div>
"""

languagues = {'english':'en','portuguese':'pt','spanish':'es','french':'fr','germani':'gm'}

def convert_lang(language):
    if language in languagues:
        return languagues[language]
    else:
        return language

async def search(word, lang_source, lang_target, target_country):
    lang_source = convert_lang(lang_source)
    lang_target = convert_lang(lang_target)

    url = f'https://translate.google.com/?hl={target_country}&sl={lang_source}&tl={lang_target}&text={word}&op=translate'

    browser = await launch(headless=True)
    page = await browser.newPage()
    await page.goto(f'https://translate.google.com/#view=home&op=translate&sl={lang_source}&tl={lang_target}')
    await page.focus('textarea[class="er8xn"]')
    element = await page.querySelector('textarea[class="er8xn"]')

    #await page.evaluate(f'(element) => element.value = "{word}"', element)
    await page.waitForSelector('div[class="tm8pq"]')
    time.sleep(2)
    await page.keyboard.type(word)
    time.sleep(2)
    source = await page.content()
    #r = requests.get(url, timeout=(3.05, 3))
    #with requests.Session() as session:
        
    #    source = session.get(url, timeout=(3.05, 27), headers=headers).text
    #source = r.text

    soup = BeautifulSoup(source, "html.parser")
    
    txt_main = ''
    mains = soup.find_all('div', class_='J0lOec')
    for main in mains:
        gen = main.find('div', class_='NlvNvf')
        if gen is not None:
            if gen.get_text() == '(masculino)' or gen.get_text() == '(masculine)':
                txt_main = main.find('span', class_='VIiyi').get_text()
        else:
            txt_main = main.find('span', class_='VIiyi').get_text()

    translations = soup.find_all('tr', class_='TKwHGb')
    lst_translate = []
    for translation in translations:
        txt = translation.find('div', class_='KnIHac').find('span', class_='kgnlhe').get_text()
        frequency = translation.find('span', class_='YF3enc')
        if 'EiZ8Dd' in frequency.contents[2]['class'][1]:
            lst_translate.append(f'(3){txt}')
        elif 'EiZ8Dd' in frequency.contents[1]['class'][1]:
            lst_translate.append(f'(2){txt}')

    await browser.close()
    return txt_main+','+','.join(lst_translate)

print(asyncio.get_event_loop().run_until_complete(search('cast', 'en', 'pt', 'pt-br')))