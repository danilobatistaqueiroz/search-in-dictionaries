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

doc_html = """
<div id="Translations"><div id="TranslationsHead"><span id="TranslationsTitle">Translations</span>
<section data-src="kdict">
  <h2>toss
  </h2> (
  <span onclick="pron_key(1)" class="pron">tos
  </span>) 
  <i> verb
  </i>
  <div class="ds-list">
    <b>1. 
    </b> to throw into or through the air. 
    <span class="illustration">She tossed the ball up into the air.
    </span>
    <span class="trans" lang="af" style="display: none;"> opgooi, in die lug gooi 
    </span>
    <span class="trans" lang="ar" style="display: none;"> يَقْذِف 
    </span>
    <span class="trans" lang="bg" style="display: none;"> хвърлям (се) 
    </span>
    <span class="trans" lang="br" style="display: none;"> atirar ao ar 
    </span>
    <span class="trans" lang="cs" style="display: none;"> vyhodit 
    </span>
    <span class="trans" lang="de" style="display: none;">
      <a href="//de.thefreedictionary.com/werfen">werfen
      </a>
    </span>
    <span class="trans" lang="da" style="display: none;"> kaste; smide 
    </span>
    <span class="trans" lang="el" style="display: none;"> πετώ ψηλά, 
      <a href="//el.thefreedictionary.com/%cf%81%ce%af%cf%87%ce%bd%cf%89">ρίχνω
      </a>, 
      <a href="//el.thefreedictionary.com/%cf%84%ce%b9%ce%bd%ce%ac%ce%b6%cf%89">τινάζω
      </a>
    </span>
    <span class="trans" lang="es" style="display: none;">
      <a href="//es.thefreedictionary.com/arrojar">arrojar
      </a>, 
      <a href="//es.thefreedictionary.com/tirar">tirar
      </a>, 
      <a href="//es.thefreedictionary.com/lanzar">lanzar
      </a>
    </span>
    <span class="trans" lang="et" style="display: none;"> õhku viskama 
    </span>
    <span class="trans" lang="fa" style="display: none;"> پرت کردن 
    </span>
    <span class="trans" lang="fi" style="display: none;"> heittää 
    </span>
    <span class="trans" lang="fr" style="display: none;">
      <a href="//fr.thefreedictionary.com/lancer">lancer
      </a>
    </span>
    <span class="trans" lang="he" style="display: none;"> לִזרוֹק 
    </span>
    <span class="trans" lang="hi" style="display: none;"> उछालना 
    </span>
    <span class="trans" lang="hr" style="display: none;"> baciti (u zrak), zavitlati 
    </span>
    <span class="trans" lang="hu" style="display: none;"> dob; lök 
    </span>
    <span class="trans" lang="id" style="display: none;"> melambungkan 
    </span>
    <span class="trans" lang="is" style="display: none;"> kasta 
    </span>
    <span class="trans" lang="it" style="display: none;">
      <a href="//it.thefreedictionary.com/lanciare">lanciare
      </a>
    </span>
    <span class="trans" lang="ja" style="display: none;"> 投げる 
    </span>
    <span class="trans" lang="ko" style="display: none;"> 던져 올리다 
    </span>
    <span class="trans" lang="lt" style="display: none;"> mesti, sviesti 
    </span>
    <span class="trans" lang="lv" style="display: none;"> mest/sviest augšup 
    </span>
    <span class="trans" lang="ml" style="display: none;"> melambung 
    </span>
    <span class="trans" lang="nl" style="display: none;">
      <a href="//nl.thefreedictionary.com/omhooggooien">omhooggooien
      </a>
    </span>
    <span class="trans" lang="no" style="display: none;">
      <a href="//no.thefreedictionary.com/kaste">kaste
      </a>, 
      <a href="//no.thefreedictionary.com/hive">hive
      </a>, 
      <a href="//no.thefreedictionary.com/slenge">slenge
      </a>
    </span>
    <span class="trans" lang="pl" style="display: none;">
      <a href="//pl.thefreedictionary.com/rzuca%c4%87">rzucać
      </a>
    </span>
    <span class="trans" lang="ps" style="display: none;"> غورځول، اچول، ارتول ( لكه پنډوسكه ), غورځېدل، راغورځېدل ( لكه بېړۍ دڅپو پرسر ): ناارامه كېدل، ټكان خوړل 
    </span>
    <span class="trans" lang="pt" style="display: inline;"> atirar ao ar 
    </span>
    <span class="trans" lang="ro" style="display: none;"> a arunca 
    </span>
    <span class="trans" lang="ru" style="display: none;">
      <a href="//ru.thefreedictionary.com/%d0%bf%d0%be%d0%b4%d0%b1%d1%80%d0%b0%d1%81%d1%8b%d0%b2%d0%b0%d1%82%d1%8c">подбрасывать
      </a>
    </span>
    <span class="trans" lang="sk" style="display: none;"> vyhodiť 
    </span>
    <span class="trans" lang="sl" style="display: none;"> zagnati 
    </span>
    <span class="trans" lang="sr" style="display: none;"> baciti 
    </span>
    <span class="trans" lang="sv" style="display: none;"> kasta, slänga 
    </span>
    <span class="trans" lang="th" style="display: none;"> โยน 
    </span>
    <span class="trans" lang="tr" style="display: none;"> havaya atmak/fırlatmak 
    </span>
    <span class="trans" lang="tw" style="display: none;"> 扔，擲 
    </span>
    <span class="trans" lang="uk" style="display: none;"> кидати; підкидати 
    </span>
    <span class="trans" lang="ur" style="display: none;"> ہوا ميں اچھالنا 
    </span>
    <span class="trans" lang="vi" style="display: none;"> tung 
    </span>
    <span class="trans" lang="zh" style="display: none;"> 扔，掷 
    </span>
  </div>
  <div class="ds-list">
    <b>2. 
    </b> (
    <i>often with 
    </i>
    <b>about
    </b>) to throw oneself restlessly from side to side. 
    <span class="illustration">She tossed about all night, unable to sleep.
    </span>
    <span class="trans" lang="af" style="display: none;"> rond rol 
    </span>
    <span class="trans" lang="ar" style="display: none;"> يَتَقَلَّب 
    </span>
    <span class="trans" lang="bg" style="display: none;"> мятам (се) 
    </span>
    <span class="trans" lang="br" style="display: none;"> dar voltas 
    </span>
    <span class="trans" lang="cs" style="display: none;"> převracet se 
    </span>
    <span class="trans" lang="de" style="display: none;">
      <a href="//de.thefreedictionary.com/sich+hin-+und+herwerfen">sich hin- und herwerfen
      </a>, ...rollen 
    </span>
    <span class="trans" lang="da" style="display: none;"> vende og dreje sig 
    </span>
    <span class="trans" lang="el" style="display: none;">
      <a href="//el.thefreedictionary.com/%cf%83%cf%84%cf%81%ce%b9%cf%86%ce%bf%ce%b3%cf%85%cf%81%ce%af%ce%b6%cf%89">στριφογυρίζω
      </a>
    </span>
    <span class="trans" lang="es" style="display: none;">
      <a href="//es.thefreedictionary.com/dar+vueltas">dar vueltas
      </a>, moverse con intranquilidad 
    </span>
    <span class="trans" lang="et" style="display: none;"> vähkrema 
    </span>
    <span class="trans" lang="fa" style="display: none;"> غلت زدن 
    </span>
    <span class="trans" lang="fi" style="display: none;"> pyöriskellä 
    </span>
    <span class="trans" lang="fr" style="display: none;">
      <a href="//fr.thefreedictionary.com/se+tourner+et+se+retourner">se tourner et se retourner
      </a>
    </span>
    <span class="trans" lang="he" style="display: none;"> לְהִתפַּתֵל 
    </span>
    <span class="trans" lang="hi" style="display: none;"> करवटें बदलते रहना 
    </span>
    <span class="trans" lang="hr" style="display: none;"> nemirno spavati, prevrtati se 
    </span>
    <span class="trans" lang="hu" style="display: none;"> hánykolódik 
    </span>
    <span class="trans" lang="id" style="display: none;"> gelisah 
    </span>
    <span class="trans" lang="is" style="display: none;"> bylta sér 
    </span>
    <span class="trans" lang="it" style="display: none;">
      <a href="//it.thefreedictionary.com/agitarsi">agitarsi
      </a>
    </span>
    <span class="trans" lang="ja" style="display: none;"> 寝返りをうつ 
    </span>
    <span class="trans" lang="ko" style="display: none;"> 뒹굴다 
    </span>
    <span class="trans" lang="lt" style="display: none;"> blaškytis 
    </span>
    <span class="trans" lang="lv" style="display: none;"> mētāties; svaidīties 
    </span>
    <span class="trans" lang="ml" style="display: none;"> berkalih badan 
    </span>
    <span class="trans" lang="nl" style="display: none;">
      <a href="//nl.thefreedictionary.com/woelen">woelen
      </a>
    </span>
    <span class="trans" lang="no" style="display: none;">
      <a href="//no.thefreedictionary.com/kaste+seg+fram+og+tilbake">kaste seg fram og tilbake
      </a>
    </span>
    <span class="trans" lang="pl" style="display: none;"> rzucać się 
    </span>
    <span class="trans" lang="ps" style="display: none;"> غورځول 
    </span>
    <span class="trans" lang="pt" style="display: inline;">
      <a href="//pt.thefreedictionary.com/dar+voltas">dar voltas
      </a>
    </span>
    <span class="trans" lang="ro" style="display: none;"> a se zvârcoli 
    </span>
    <span class="trans" lang="ru" style="display: none;">
      <a href="//ru.thefreedictionary.com/%d0%bc%d0%b5%d1%82%d0%b0%d1%82%d1%8c%d1%81%d1%8f">метаться
      </a>
    </span>
    <span class="trans" lang="sk" style="display: none;"> prehadzovať sa 
    </span>
    <span class="trans" lang="sl" style="display: none;"> premetavati se 
    </span>
    <span class="trans" lang="sr" style="display: none;"> prevrtati se 
    </span>
    <span class="trans" lang="sv" style="display: none;"> kasta sig [hit och dit] 
    </span>
    <span class="trans" lang="th" style="display: none;"> กระสับกระส่าย 
    </span>
    <span class="trans" lang="tr" style="display: none;"> dönüp durmak 
    </span>
    <span class="trans" lang="tw" style="display: none;"> 翻來覆去 
    </span>
    <span class="trans" lang="uk" style="display: none;"> тривожно метатися 
    </span>
    <span class="trans" lang="ur" style="display: none;"> کروٹ بدلنا 
    </span>
    <span class="trans" lang="vi" style="display: none;"> trằn trọc 
    </span>
    <span class="trans" lang="zh" style="display: none;">
      <a href="//zh.thefreedictionary.com/%e7%bf%bb%e6%9d%a5%e5%a4%8d%e5%8e%bb">翻来复去
      </a>
    </span>
  </div>
  <div class="ds-list">
    <b>3. 
    </b> (of a ship) to be thrown about. 
    <span class="illustration">The boat tossed wildly in the rough sea.
    </span>
    <span class="trans" lang="af" style="display: none;"> rondrol 
    </span>
    <span class="trans" lang="ar" style="display: none;"> يَتَمايَل 
    </span>
    <span class="trans" lang="bg" style="display: none;"> подхвърлям 
    </span>
    <span class="trans" lang="br" style="display: none;"> ser sacudido 
    </span>
    <span class="trans" lang="cs" style="display: none;"> zmítat se 
    </span>
    <span class="trans" lang="de" style="display: none;"> rollen 
    </span>
    <span class="trans" lang="da" style="display: none;"> kaste 
    </span>
    <span class="trans" lang="el" style="display: none;">
      <a href="//el.thefreedictionary.com/%cf%87%cf%84%cf%85%cf%80%ce%b9%ce%ad%ce%bc%ce%b1%ce%b9">χτυπιέμαι
      </a>, 
      <a href="//el.thefreedictionary.com/%cf%83%ce%ba%ce%b1%ce%bc%cf%80%ce%b1%ce%bd%ce%b5%ce%b2%ce%ac%ce%b6%cf%89">σκαμπανεβάζω
      </a>
    </span>
    <span class="trans" lang="es" style="display: none;">
      <a href="//es.thefreedictionary.com/balancearse">balancearse
      </a>, ser sacudido 
    </span>
    <span class="trans" lang="et" style="display: none;"> heitlema 
    </span>
    <span class="trans" lang="fa" style="display: none;"> بالا و پایین بردن؛ متلاطم کردن 
    </span>
    <span class="trans" lang="fi" style="display: none;"> heittelehtiä 
    </span>
    <span class="trans" lang="fr" style="display: none;">
      <a href="//fr.thefreedictionary.com/tanguer">tanguer
      </a>
    </span>
    <span class="trans" lang="he" style="display: none;"> לְהִיטַלטֵל 
    </span>
    <span class="trans" lang="hi" style="display: none;"> हिलाना 
    </span>
    <span class="trans" lang="hr" style="display: none;"> bacati amo-tamo 
    </span>
    <span class="trans" lang="hu" style="display: none;"> hányódik 
    </span>
    <span class="trans" lang="id" style="display: none;"> terombang-ambing 
    </span>
    <span class="trans" lang="is" style="display: none;"> kastast til, veltast 
    </span>
    <span class="trans" lang="it" style="display: none;"> (essere sballottato) 
    </span>
    <span class="trans" lang="ja" style="display: none;"> 激しく揺れる 
    </span>
    <span class="trans" lang="ko" style="display: none;"> 상하로 흔들리다 
    </span>
    <span class="trans" lang="lt" style="display: none;"> būti svaidomam 
    </span>
    <span class="trans" lang="lv" style="display: none;"> tikt svaidītam 
    </span>
    <span class="trans" lang="ml" style="display: none;"> terumbang-ambing 
    </span>
    <span class="trans" lang="nl" style="display: none;">
      <a href="//nl.thefreedictionary.com/slingeren">slingeren
      </a>
    </span>
    <span class="trans" lang="no" style="display: none;">
      <a href="//no.thefreedictionary.com/bli+slengt+hit+og+dit">bli slengt hit og dit
      </a>
    </span>
    <span class="trans" lang="pl" style="display: none;"> być rzucanym, 
      <a href="//pl.thefreedictionary.com/ko%c5%82ysa%c4%87+si%c4%99">kołysać się
      </a>
    </span>
    <span class="trans" lang="ps" style="display: none;"> ټكان خوړل 
    </span>
    <span class="trans" lang="pt" style="display: inline;"> ser sacudido 
    </span>
    <span class="trans" lang="ro" style="display: none;"> a se legăna 
    </span>
    <span class="trans" lang="ru" style="display: none;"> бросать из стороны в сторону 
    </span>
    <span class="trans" lang="sk" style="display: none;"> zmietať sa 
    </span>
    <span class="trans" lang="sl" style="display: none;"> premetavati 
    </span>
    <span class="trans" lang="sr" style="display: none;"> ljuljati 
    </span>
    <span class="trans" lang="sv" style="display: none;"> rulla, gunga slungas hit och dit 
    </span>
    <span class="trans" lang="th" style="display: none;"> ซัด 
    </span>
    <span class="trans" lang="tr" style="display: none;"> savrulmak 
    </span>
    <span class="trans" lang="tw" style="display: none;"> 顛簸 
    </span>
    <span class="trans" lang="uk" style="display: none;"> носитися; підніматися і опускатися 
    </span>
    <span class="trans" lang="ur" style="display: none;"> ہچکولے کھانا 
    </span>
    <span class="trans" lang="vi" style="display: none;"> chao đảo 
    </span>
    <span class="trans" lang="zh" style="display: none;">
      <a href="//zh.thefreedictionary.com/%e9%a2%a0%e7%b0%b8">颠簸
      </a>
    </span>
  </div>
  <div class="ds-list">
    <b>4. 
    </b> to throw (a coin) into the air and decide a matter according to (a correct guess about) which side falls uppermost. 
    <span class="illustration">They tossed a coin to decide which of them should go first.
    </span>
    <span class="trans" lang="af" style="display: none;"> gooi, munt gooi 
    </span>
    <span class="trans" lang="ar" style="display: none;"> يَقْتَرِع بِقَذْف قِطْعَه مَعْدَنِيَّه 
    </span>
    <span class="trans" lang="bg" style="display: none;"> хвърлям монета 
    </span>
    <span class="trans" lang="br" style="display: none;"> jogar cara ou coroa 
    </span>
    <span class="trans" lang="cs" style="display: none;"> hodit si (mincí) 
    </span>
    <span class="trans" lang="de" style="display: none;">
      <a href="//de.thefreedictionary.com/hochwerfen">hochwerfen
      </a>
    </span>
    <span class="trans" lang="da" style="display: none;"> slå plat eller krone 
    </span>
    <span class="trans" lang="el" style="display: none;"> στρίβω νόμισμα 
    </span>
    <span class="trans" lang="es" style="display: none;"> jugar/echar a cara o cruz 
    </span>
    <span class="trans" lang="et" style="display: none;"> kulli ja kirja viskama 
    </span>
    <span class="trans" lang="fa" style="display: none;"> شیر یا خط کردن 
    </span>
    <span class="trans" lang="fi" style="display: none;"> heittää kolikkoa 
    </span>
    <span class="trans" lang="fr" style="display: none;">
      <a href="//fr.thefreedictionary.com/jouer+%c3%a0+pile+ou+face">jouer à pile ou face
      </a>
    </span>
    <span class="trans" lang="he" style="display: none;"> לְהַטִיל 
    </span>
    <span class="trans" lang="hi" style="display: none;"> फेंक देना, उछाल देना 
    </span>
    <span class="trans" lang="hr" style="display: none;"> baciti 
    </span>
    <span class="trans" lang="hu" style="display: none;"> pénzfeldobással eldönt 
    </span>
    <span class="trans" lang="id" style="display: none;"> melemparkan 
    </span>
    <span class="trans" lang="is" style="display: none;"> varpa hlutkesti, kasta upp á e-ð 
    </span>
    <span class="trans" lang="it" style="display: none;"> (fare a testa o croce) 
    </span>
    <span class="trans" lang="ja" style="display: none;"> 銭投げをする 
    </span>
    <span class="trans" lang="ko" style="display: none;"> 동전 던지기를 하다 
    </span>
    <span class="trans" lang="lt" style="display: none;"> mesti (monetą) 
    </span>
    <span class="trans" lang="lv" style="display: none;"> (lozējot) mest monētu 
    </span>
    <span class="trans" lang="ml" style="display: none;"> melambung 
    </span>
    <span class="trans" lang="nl" style="display: none;">
      <a href="//nl.thefreedictionary.com/opgooien">opgooien
      </a>
    </span>
    <span class="trans" lang="no" style="display: none;">
      <a href="//no.thefreedictionary.com/kaste+krone+og+mynt">kaste krone og mynt
      </a>
    </span>
    <span class="trans" lang="pl" style="display: none;">
      <a href="//pl.thefreedictionary.com/rzuca%c4%87">rzucać
      </a>
    </span>
    <span class="trans" lang="ps" style="display: none;"> پچه ( قرعه ) 
    </span>
    <span class="trans" lang="pt" style="display: inline;"> jogar cara ou coroa 
    </span>
    <span class="trans" lang="ro" style="display: none;"> a da (cu banul) 
    </span>
    <span class="trans" lang="ru" style="display: none;"> бросать жребий 
    </span>
    <span class="trans" lang="sk" style="display: none;"> hodiť si (mincu) 
    </span>
    <span class="trans" lang="sl" style="display: none;"> vreči (kovanec) 
    </span>
    <span class="trans" lang="sr" style="display: none;"> baciti novčić 
    </span>
    <span class="trans" lang="sv" style="display: none;"> singla 
    </span>
    <span class="trans" lang="th" style="display: none;"> ทอย(เหรียญ) 
    </span>
    <span class="trans" lang="tr" style="display: none;"> yazı tura atmak 
    </span>
    <span class="trans" lang="tw" style="display: none;"> 擲硬幣看正反來決定某事 
    </span>
    <span class="trans" lang="uk" style="display: none;"> підкидати монету 
    </span>
    <span class="trans" lang="ur" style="display: none;"> سکہ اچھال کر کسي امر کا فيصلہ کرنا 
    </span>
    <span class="trans" lang="vi" style="display: none;"> tung đồng xu để đi đến phán xét 
    </span>
    <span class="trans" lang="zh" style="display: none;">
      <a href="//zh.thefreedictionary.com/%e6%8e%b7%e7%a1%ac%e5%b8%81%e7%9c%8b%e5%8f%8d%e6%ad%a3%e6%9d%a5%e5%86%b3%e5%ae%9a%e6%9f%90%e4%ba%8b">掷硬币看反正来决定某事
      </a>
    </span>
  </div>
  <i> noun
  </i>
  <div class="ds-single"> an act of tossing. 
    <span class="trans" lang="af" style="display: none;"> gooi 
    </span>
    <span class="trans" lang="ar" style="display: none;"> قَذْف قِطَعَه معْدَنِيَّه للإقْتِراع 
    </span>
    <span class="trans" lang="bg" style="display: none;"> хвърляне 
    </span>
    <span class="trans" lang="br" style="display: none;"> lançamento 
    </span>
    <span class="trans" lang="cs" style="display: none;"> hod 
    </span>
    <span class="trans" lang="de" style="display: none;"> das Werfen 
    </span>
    <span class="trans" lang="da" style="display: none;"> kast 
    </span>
    <span class="trans" lang="el" style="display: none;">
      <a href="//el.thefreedictionary.com/%cf%84%ce%af%ce%bd%ce%b1%ce%b3%ce%bc%ce%b1">τίναγμα
      </a>, 
      <a href="//el.thefreedictionary.com/%cf%81%ce%af%ce%be%ce%b9%ce%bc%ce%bf">ρίξιμο
      </a>, στρίψιμο νομίσματος 
    </span>
    <span class="trans" lang="es" style="display: none;">
      <a href="//es.thefreedictionary.com/sacudida">sacudida
      </a>; 
      <a href="//es.thefreedictionary.com/lanzamiento">lanzamiento
      </a>
    </span>
    <span class="trans" lang="et" style="display: none;"> vise 
    </span>
    <span class="trans" lang="fa" style="display: none;"> پرتاب؛ تکان 
    </span>
    <span class="trans" lang="fi" style="display: none;"> heitto 
    </span>
    <span class="trans" lang="fr" style="display: none;">
      <a href="//fr.thefreedictionary.com/lancer">lancer
      </a>
    </span>
    <span class="trans" lang="he" style="display: none;">
      <a href="//he.thefreedictionary.com/%d7%96%d7%a8%d7%99%d7%a7%d7%94">זריקה
      </a>
    </span>
    <span class="trans" lang="hi" style="display: none;"> उत्क्षेपण 
    </span>
    <span class="trans" lang="hr" style="display: none;"> bacanje 
    </span>
    <span class="trans" lang="hu" style="display: none;"> (fel)dobás; lökés 
    </span>
    <span class="trans" lang="id" style="display: none;"> lemparan 
    </span>
    <span class="trans" lang="is" style="display: none;"> kast 
    </span>
    <span class="trans" lang="it" style="display: none;">
      <a href="//it.thefreedictionary.com/lancio">lancio
      </a>
    </span>
    <span class="trans" lang="ja" style="display: none;"> 投げること 
    </span>
    <span class="trans" lang="ko" style="display: none;"> 토스 
    </span>
    <span class="trans" lang="lt" style="display: none;"> metimas 
    </span>
    <span class="trans" lang="lv" style="display: none;"> lozēšana (metot monētu); mešana 
    </span>
    <span class="trans" lang="ml" style="display: none;"> lambungan 
    </span>
    <span class="trans" lang="nl" style="display: none;"> opgooi 
    </span>
    <span class="trans" lang="no" style="display: none;">
      <a href="//no.thefreedictionary.com/kast">kast
      </a>
    </span>
    <span class="trans" lang="pl" style="display: none;"> rzut monetą 
    </span>
    <span class="trans" lang="ps" style="display: none;"> اچونه، ارتونه: پچه ( قرعه )، وچه لنده 
    </span>
    <span class="trans" lang="pt" style="display: inline;">
      <a href="//pt.thefreedictionary.com/Lan%c3%a7amento">lançamento
      </a>
    </span>
    <span class="trans" lang="ro" style="display: none;"> aruncare 
    </span>
    <span class="trans" lang="ru" style="display: none;">
      <a href="//ru.thefreedictionary.com/%d0%bc%d0%b5%d1%82%d0%b0%d0%bd%d0%b8%d0%b5">метание
      </a>; бросание 
    </span>
    <span class="trans" lang="sk" style="display: none;"> hod 
    </span>
    <span class="trans" lang="sl" style="display: none;"> met 
    </span>
    <span class="trans" lang="sr" style="display: none;"> bacanje 
    </span>
    <span class="trans" lang="sv" style="display: none;"> kastande, kast, slantsingling 
    </span>
    <span class="trans" lang="th" style="display: none;"> การทอย (เหรียญ) 
    </span>
    <span class="trans" lang="tr" style="display: none;"> atma, fırlatma 
    </span>
    <span class="trans" lang="tw" style="display: none;"> 擲 
    </span>
    <span class="trans" lang="uk" style="display: none;"> кидання; підкидання 
    </span>
    <span class="trans" lang="ur" style="display: none;"> اچھالنے کا عمل، ٹاس 
    </span>
    <span class="trans" lang="vi" style="display: none;"> sự tung 
    </span>
    <span class="trans" lang="zh" style="display: none;">
      <a href="//zh.thefreedictionary.com/%e6%8e%b7">掷
      </a>
    </span>
  </div>
  <b>toss up
  </b>
  <div class="ds-single"> to toss a coin to decide a matter. 
    <span class="illustration">We tossed up (to decide) whether to go to the play or the ballet.
    </span>
    <span class="trans" lang="br" style="display: none;"> jogar cara ou coroa 
    </span>
    <span class="trans" lang="pt" style="display: inline;"> jogar cara ou coroa 
    </span>
    <span class="trans" lang="zh" style="display: none;">
      <a href="//zh.thefreedictionary.com/%e6%8e%b7%e7%a1%ac%e5%b8%81%e5%86%b3%e5%ae%9a%e6%9f%90%e4%ba%8b">掷硬币决定某事
      </a>
    </span>
  </div>
  <b>win/lose the toss
  </b>
  <div class="ds-single"> to guess rightly or wrongly which side of the coin will fall uppermost. 
    <span class="illustration">He won the toss so he started the game.
    </span>
    <span class="trans" lang="br" style="display: none;"> ganhar/perder o lançamento da moeda 
    </span>
    <span class="trans" lang="pt" style="display: inline;"> ganhar/perder o lançamento da moeda 
    </span>
    <span class="trans" lang="zh" style="display: none;">
      <a href="//zh.thefreedictionary.com/%e6%8e%b7%e7%a1%ac%e5%b8%81%e7%8c%9c%e8%be%93%e8%b5%a2">掷硬币猜输赢
      </a>
    </span>
  </div>
  <div class="cprh">
    <span class="i A cpr">
    </span>Kernerman English Multilingual Dictionary © 2006-2013 K Dictionaries Ltd.
  </div>
</section>
"""

def search(word, lang):
    lst_translations = []
    source = doc_html
    soup = BeautifulSoup(source, "html.parser")
    translations = soup.find('div', attrs={"id" : "Translations"})

    if translations is not None:
        kdict = translations.find('section', attrs={"data-src" : "kdict"})
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
        return ' '.join(lst_translations)

print(search('',''))