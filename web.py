# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service

import re
from bs4 import BeautifulSoup
from aptext import putin, getchar
# from bs4 import NavigableString, Tag
# import requests


our_lang = ['ĀlKu.', 'Bel.', 'Br.', 'Dr.', 'Ga.', 'Go.', 'Ir.', 'Ka.', 'Ko.', 'Koḍ.', 'Kol.', 'Kor.', 'Kur.', 'Kurub.', 'Ma.', 'Malt.', 'Manḍ.', 'Nk.', 'Nk.(Ch.)', 'Pa.', 'PālKu.', 'PDr.', 'Pe.', 'Ta.', 'Te.', 'To.', 'Tu.', 'Konḍa', 'Kui', 'Kuwi']
our_lang_names = ['Ālu Kuṟumba', 'Belari', 'Brahui', 'Dravidian', 'Gadba', 'Gondi', 'Iruḷa', 'Kannaḍa', 'Kota', 'Koḍagu', 'Kolami', 'Koraga', 'Kuṛux', 'Beṭṭa Kuruba', 'Malayalam', 'Malto', 'Manḍa', 'Naikṛi', 'Naiki of Chanda', 'Parji', 'Pālu Kuṟumba', 'proto-Dravidian', 'Pengo', 'Tamil', 'Telugu', 'Toda', 'Tulu', 'Konḍa', 'Kui', 'Kuwi']
other_lang = ['Ar.', 'Bal.', 'Pers.', 'Ass.', 'Beng.', 'BHS', 'Guj.', 'H.', 'IA', 'Konk.', 'Kum.', 'Mar.', 'Nep.', 'OMar.', 'Or.', 'Pali', 'Panj.', 'Pkt.', 'Sgh.', 'Si.', 'Skt.']   
other_lang_names = ['Arabic', 'Baluchi', 'Persian', 'Assamese', 'Bengali', 'Buddhist Hybrid Sanskrit', 'Gujarati', 'Hindi', 'Indo-Aryan', 'Konkani', 'Kumaon', 'Marathi', 'Nepali', 'Old Marathi', 'Oriya', 'Pali', 'Panjabi', 'Prakrit', 'Sin(g)halese', 'Sindhi', 'Sanskrit']
grammer = ['adj.', 'adv.', 'caus.', 'coll.', 'cpd.', 'excl.', 'fem.', 'hon.', 'imper.', 'impf.', 'inscr.', 'interj.', 'intr.', 'lex.', 'loc.', 'masc.', 'n.', 'neg.', 'neut.', 'n. pr.', 'obl.', 'onom. (expr.)', 'pass.', 'pl.', 'pl. action', 'refl.', 'tr.', 'vb.', 'vb.n.', 'v. i.', 'masc.; pl.', 'Voc.']
grammer_name = ['adjective', 'adverb', 'causative', 'colloquial', 'compound', 'exclamation', 'feminine (gender), female', 'honorific', 'imperative', 'imperfect', 'inscriptional, in inscriptions', 'interjection', 'intransitive', 'lexical', 'locative; local (usage)', 'masculine (gender)', 'noun', 'negative', 'neuter (gender)', 'nomen proprium (proper name)', 'oblique stem', 'onomatopoeic (expression)', 'passive', 'plural', 'plural action', 'reflexive', 'transitive', 'verb', 'verbal noun', 'intransitive verb', 'unknown', 'voice?']


def hur(t):
    mean = t.next_sibling
    # print(mean.name)
    try:
        mean = mean.replace('\n', '')
        try:
            if mean[-1] == ' ':
                mean = mean[:-1]
        except IndexError:
            mean = 'bad_word'
    except TypeError:
        mean = 'bad_word'
    except AttributeError:
        mean = 'bad_word'
    if mean and mean != 'bad_word':
        return cleanup(mean)
    else: return None

def cleanup(this: str) -> str:
    this = re.sub("\(.*?\)","",this)
    this = re.sub("\[.*?\]","",this)
    this = this.replace('[','').replace(')','').replace(']','').replace('(','').replace('\n', '')
    this = this.strip()
    if not this:
        this = " "
    return this



def scrape(page_no: int):
    ULR = f"https://dsal.uchicago.edu/cgi-bin/app/burrow_query.py?page={page_no}"
    r = requests.get(ULR)
    soup = BeautifulSoup(r.content , features="html.parser")


    # ULR = f"H:\\Visual_Studia\\python projects\\kannada dictnory\\Dravidian\\page{page_no}.html"
    # with open(ULR, 'r', encoding='utf-8') as data:
    #     soup = BeautifulSoup(data.read(), features="html.parser")
    #     soup = soup.find("div", {"id": "results_display"})
    # print(soup)
    language = ''
    word = ''
    word_number = 0
    meaning = ''
    # other_langugae = 'None'
    # print(soup.contents)


    for t in soup.find_all():
        mean = ''
        if t.name  == 'number':
            word_number = cleanup(t.text)
        if t.name == 'i':
            language = getname(t.text, language, 'language')
            mean = hur(t)
                    
        
        if t.name == 'b':
            i = ''
            for x in t.find_all('i'):
                language = getname(x.text, language, 'language')
                i = x.text
                x.decompose()
            if t.parent.name == 'i':
                # print("\nI Found\n")
                continue
            x = t.text
            if i:
                x = x.replace(i,'')
            word += ','
            word += cleanup(x)
            mean = hur(t)
            

        if mean:
            meaning += str(mean)
        t.extract()
        if not meaning or len(meaning) <= 4:
            continue

        

        if meaning[-1] == ';' or meaning[-1] == '.':
            # print(f"{language},{meaning[-1]}")
            meaning = meaning[:-1]
            if meaning[0] == '/':
                meaning = meaning[1:]
            word = word[1:]
            word = word.replace(' ','')
            putin(language,word,meaning,word_number)
            if language == 'Kannaḍa':
                getchar(word, meaning, word_number)
                # print(f'{word_number}:{word} : {meaning}')
            word = ''
            meaning = ''



def getname(abb: str, word: str, what: str) -> str:
    abb = abb.replace('\n', '')
    abb = abb.replace(' ', '')
    flag = False
    if words_in_string(our_lang, abb):
        for x in words_in_string(our_lang, abb):
            abb = x
        flag = True
    if what == 'language' and abb in our_lang and flag:
        return our_lang_names[our_lang.index(abb)]
    elif what == 'other' and abb in other_lang:
        return other_lang_names[other_lang.index(abb)]
    elif what == 'grammer' and abb in grammer:
        return grammer_name[grammer.index(abb)]
    else:
        return word
    

def words_in_string(word_list: list, a_string: str):
    return set(word_list).intersection(a_string.split())


# class Web_Scrape:
#     def __init__(self):
#         chrome_driver = Service("H:\\Visual_Studia\\python projects\\support\\chromedriver.exe")
#         self.driver = webdriver.Chrome(service=chrome_driver)
#         self.page_no = 0
#         self.end_page = 514

#     def next(self):
#         self.page_no += 3
#         scrape(self.page_no)

#     def __del__(self):
#         print("Completed with exit code 0")
        
