path = "H:\\Visual_Studia\\python projects\\kannada dictnory\\language\\"

def putin(l: str, w: str, m: str, n: int) -> None:
    m = m.replace('id.', '(Dravidian Root)').replace(';', ',')
    w = w.replace(';', ',').replace(",,", ',')
    with open(f'{path}{l}.txt', 'a', encoding="utf-8") as file:
        if w != '':
            file.write("\n")
        file.write(f'{n}:{w} = {m}')


# putin('unknown', 'words', 'meaning')
# putin('unknown', 'words', 'meaning')
# putin('unknown', '', 'meaning')
# putin('unknown', 'words', 'meaning')
# putin('unknown', 'words', 'meaning')

vovels = ['a','ã','i','ï','u','ū','e','ē','o','ō','ṃ']
chars = [',', ' ']
constants = ['k','g','c','j','ṭ','ḍ','ṉ','t','d','n','p','b','m','y','r','l','v','ṣ','s','h','ḷ']
meluli = ['ಅ','ಆ','ಇ','ಈ','ಉ','ಉ','ಎ','ಏ','ಒ','ಓ', 'o']
gunita = ['಼', 'ಾ','ಿ', 'ೀ', 'ು', 'ೂ', 'ೆ', 'ೇ', 'ೊ', 'ೋ', 'o']
uli = ['ಕ','ಗ','ಚ','ಜ','ಟ','ಡ','ಣ','ತ','ದ','ನ','ಪ','ಬ','ಮ','ಯ','ರ','ಲ','ವ','ಶ','ಸ','ಹ','ಳ']
stop = '್'

def getchar(w: str, m: str, n: int):
    m = m
    w = w.replace('/', ',')
    k = polish(w)
    w = polish(w, False)
    with open(f'{path}ಕನ್ನಡದ್ದೇ.txt', 'a', encoding="utf-8") as file:
        if w != '':
            file.write("\n")
        k = k.replace(',', ', ')
        w = w.replace(',', ', ')
        file.write(f'{n}>{k}: {m} ~ {w}')


# def newlist():
#     for i in stop:
#         pass

# newlist()
#     print(uli)

def polish(w: str, yes=True):
    k = ''
    w = w.replace('-', ' ').replace('/', ',').replace(';', ',').replace('=', ',')
    w = w.replace(',,', ',').replace('.', ',')
    w = w.lower()
    w = w.replace('Skt.', '').replace('Mar.', '').replace('W.', '').replace('Koḍ.', '').replace('incutomakeanoise.DED1926.', '').replace('befull,increase,overflow,tekir̤tobefull,tekuḷamfullness,abundance,tekuṭṭutocloy,glut,tekiṭṭusurfeit,teviṭṭutobecomefull,besated,glutted,cloyed,loathing,tevvutofill,tikaitocomplete,cometoanend.tikayukatobecomefull,complete,befulfilled,finished,tikafullness,tikaccal,tikavucompletion,satiety,tikekkatocomplete,fillup,fulfil,tiviṟṟukatoforceintoavessel,cram.tīvutobecomefull,abound,spread,filltegutobefinished,ended,tegudalaend,termination,completion.DED2801. del', '').replace('gooseberrybushoftheNilgiris,redmyrtle,DED2538.', '').replace('?pü·ł̣,*vey<->uḷ.', '').replace('DED', '')

    if yes:
        w = w.replace('w', 'v').replace('ẽ', 'e').replace('ṅ', 'ṃ')
        w = w.replace('ṇ', 'ṉ').replace('ṛ', 'r').replace('ṟ', 'r').replace('ŋ', 'ṉ')
        w = w.replace('ḥ', 'h').replace('ụ', 'u').replace('ā', 'ã').replace('ů', 'u')
        w = w.replace('ü', 'u').replace('ɔ', 'ã').replace('á', 'ã').replace('ī', 'i')
        w = w.replace('ĩ', 'i').replace('ë', 'e').replace('è', 'e').replace('š', 's')
        w = w.replace('ñ', 'n').replace('ö', 'o').replace('õ', 'o').replace('ś', 's')
        w = w.replace('ɨ', 'u').replace('ə', 'a')
        for i in w:
            if i in vovels or i in constants or i in chars:
                k += i
        w = kan(k)
        return w
    return w



def pre(l: str, c):
    if c == 0:
        p = None
    else:
        p = l[c - 1]
    try:
        n = l[c + 1]
    except IndexError:
        n = None
    return p,l[c],n



def kan(w: str):
    r = ''
    for x in range(len(w)):
        p,i,n  = pre(w, x)
        if i in vovels:
            if p in constants and i != 'a':
                r += gunita[vovels.index(i)]
            elif i == 'a' and p in constants:
                pass
            else:
                r += meluli[vovels.index(i)]
        elif i in constants:
            r += uli[constants.index(i)]
            if n not in vovels:
                r += stop
        else:
            r += i
    return r



# print(polish('agacāṭlu,agacāṭle,agacāṭu'))

def clearmean(w: str):
    a = 0
    w = w.replace('id.', '').replace(';', ',')
    if 'DED' in w:
        a = w.index('DED')
        if '. DED' in w:
            a = w.index('. DED')
    w = w[:a]
    if w[0] == ' ' or w[0] ==',':
        w = w[1:]

    return w
        
