import string
import numpy as np
import math
import random
import requests

ngrams = {}
req = requests.get("https://gist.githubusercontent.com/DomDale/9a582deed33b20bb47e0363301d2c6c4/raw/62e7416f6be95893649398f0470f1dcd2668e608/english_trigrams.txt")
ngram_list = req.text
ngram_list = list(ngram_list.splitlines())
for i in ngram_list:
    ngrams[i[0:3]] = int(i[4:])      #dictionary with all the scores for the trigrams
ngram_sum = sum(ngrams.values())

letterFrequency = {1: 8.497, 2: 1.492, 3: 2.202, 4: 4.253, 5: 11.162, 6: 2.228, 7: 2.015, 8: 6.094, 9: 7.546,
                       10: 0.153, 11: 1.292, 12: 4.025, 13: 2.406, 14: 6.749, 15: 7.507, 16: 1.929, 17: 0.095,
                       18: 7.587, 19: 6.327, 20: 9.256, 21: 2.758, 22: 0.978, 23: 2.560, 24: 0.150, 25: 1.994,
                       26: 0.077}

def prepare(cipher):
    cipher = cipher.upper()
    cipher = cipher.replace(" ", "").replace(".", "").replace(",", "").replace("?", "").replace("-", "").replace("’", "").replace("!", "")
    return cipher

def cost(cipher):
    def analysis(cipher):
        zeros = []
        for i in range(26):
            zeros.append(0)
        dict_out = dict(zip([x + 1 for x in list(range(26))], zeros))
        for char in cipher:
            dict_out[ord(char) - 64] += 1
        return dict_out
    total = 0
    dict_sum = analysis(cipher)
    for x in range(1, 27):
        total += abs(float(letterFrequency[x] * 0.001 - (dict_sum[x] / len(cipher))))
    return total

def accept_prob(temp, last, potential):
    try:
        return (math.exp(potential - last) / temp)
    except:
        return 0

def swap(data, a, b):
    position_a = []
    position_b = []
    for l in range(len(data)):
        if data[l] == a:
            position_a.append(l)
        if data[l] == b:
            position_b.append(l)
    data_string = list(data)
    for g in position_a:
        data_string[g] = str(b)
    for h in position_b:
        data_string[h] = str(a)
    return "".join(data_string)

def neighbour(now):       #function to swap two letter with each other
    alphabet = dict(zip(range(1, 27), string.ascii_uppercase))
    n1, n2 = random.sample(range(1, 27), 2)
    return swap(now, str(alphabet[n1]), str(alphabet[n2]))

def SA_mine(cipher):       #where f is the input function and a and b are the bounds between which a solution is looked for
    focus = 0.999
    t = 1
    t_min = 0.0001
    best = cipher
    initial_x = cipher
    current = cost(initial_x)
    while t > t_min:
        i = 1
        while i <= 10:          #iterations at each temperature
            next_x = neighbour(initial_x)
            new = cost(next_x)
            if new <= current:
                initial_x = next_x
                current = new
                if new <= cost(best):
                    best = initial_x
            if accept_prob(t, current, new) > random.random():
                initial_x = next_x
                current = new
            i += 1
        t = focus * t
    print(cost(best))
    return best

def substitution_decrypt_statistics(cipher, x):
    for i in range(x - 1):
        print(SA_mine(prepare(cipher)))
    return SA_mine(prepare(cipher))

"""second = prepare("Owxz hlwgi mdhshik ki vsgariv hs lfc sueab, efr psiruviv Ctwfelwsf Uyfbijgmvs. Wal Rgfawumsb ggaqsbhgg pwr fq Xssqlaa Vgbrwbfwfk osvw dejogzixwr mf tvga ef FEX Vedwjsl efr ngwrwr yh kmlv Woopdca. Lvi shxsqlwr hgqyesrl ww lviaf qagwacr jstgfx. Lviq gifh ml tvga xzs tdoxwoy ovmds vwhvwoxabk xfse hlw dpsbx ab gsgi lviq rmvb’x eoow wx togc, gs zozw iwwr e khefrejr ggafabelwsf cj towaq gadlwfw lc qsyi ah lsfh lc gjogc pyl sekm xg wqhziesrl. Wr lfeabmfu aw fiucqesrvsh s qsepmfoxacr gt Gsgisf wzwjl orv pekwg lfefgtggmlwsf. W pwozw wx lc cgi xg riuwtzsv.")
print(cost(second))

ciphertext = prepare("ETMHB NBOIA GORIE NDVRM AOKAS WCIRO REDUD TIUDR NLAGY HINGT VNOOB ESMET IRXNE TETAH HEATS TCAQK UODOR NINCS ISOTN HFGTT INREA PELSN LESII PTONO TTOGW RSUCP EAHAM NKWIG UOTRO NHSNA ETTER WGTCH SIPHA APDRE EBTHO EOETN KRDSH PRYOE OTWRI ASTAO TNNNH DERIE TAAPT LTNET HIERM SLTET EHOET AESTT AHTKA SCWTN AORFE OENES NWOIR ANTSI RTPEC DTEEA BCYIE ORVNR LADFL AOETT HAKAT CGIRN AACIR SFMTE HTEOE ATVRN UERFE MDRET OHSMO ISYNI EIEEW TESNS TSESA ATTHN TRITT MEINT LETDO CUVCA OEEPR PEAOR DSDTI PRHUT TETAC TUAKH TBTAE RMJYI OTTOE FHLXE PIOSS VOAER DUINT YRHTN TEOSD RWEPR DOPTW EIEHH VRHIY GCAAC UOCRY HNITE ATNRP TNELN TAOTL TYWHO OTERN ETISO HHTOT ERWPE ASOTT NNIAH DETEF IRNCO SREUT DRUCW TRHIE TOSTT OWHDE SOFRT ETOHS ALSAH TUTOE SBMIF BADLD ETAAO MTGRE HUEEB TIULD RTEEM IEUER CLTYO SLSCF IAIIA LTONY DNUSR ECTWO OKESF YAHVT WWAEE ERROP CRTDT EETBS YHEEE VTNES OOYRS EFFRI CONRC ECDOT RNEBE EAOWH VOEEH VROET PRWAE PINLT ETHSL BAFSN EMEDE AAGND HADSI TSOER CNDAD ITOPN HNLEA ATERI HSSTO EIPSL BSIYI ATTUT HONRI EEHEM SEAEV ASNGT RWNOK IGIWI TTHND IINCI SSUNI SOTWF IHCFO ILIRA SDOFM AIHEL IECME SRTNP OGUHI BTANE SECDE EIHDD TTAFT HIAEC TLHIY LOSUE DUBSO THDEW SNXNT IITGK SOFSC OAHWE VEAYT NROAD STPAU SYIMO DHRDX IIEBL WLHEP SITEP DHORT EBLIA AORRT SIOED ANNMA UAFUC NTRAG IFLCI IIIET SENAG RFNMY FOTRU RHRER EHNIN MCENT XADRP EEEIA MNOTT IINNG VETEH SRFIK CLOOE AILSA OPNWG IEENL WLDES ETNIO GIINF CYTAL HECNA EENSR CYUIR FTOIT PHSAE OROTI INLNF AWLHY ELOSU ODTNT THEAE TTHAK ATCLK DILET EWYNE TORNN OGWNE IVCAI IISLA ITNHS SLIVB UAAPL PERAA OGAND DARON UEASG NEATR IDTON IHGEE RHBSE ETRDA LNIDO NNTON NORSE UHETT ANHTE WOIRE PAGNU OTPLN IAODU SNENT RAWDI SHOSO TABFL MTOER SHEEE LENDS EASDS TEH")
print(cost(ciphertext))

print(cost(plaintext))
print(plaintext)

vigenere = prepare("Hvmd,Gsjfc A vensr’l piwb mf hsmql eigz, Qlmfgzwpd owcsh TCWK hs ksx md ef ctwfelwsfg aabk ab xzs YC irvsv lvi foqw cj lvi Kdiuwed Ctwfelwsfg Ipsgmhmns efr xzox zow gqgmdmwr e dcx gt qq hmes. Ek gsgb ek ki ycx ksx md M oow hix ab xgigz kmlv Iabej Goabrsfpsbh, sb ifumfsij tvga Zwasjy azc lsr laxeuyiv o ggowlop khisaij orv geaziv hs Spijriwb xg xsab xzs asf ixtsjh lwfi. Uvyjqlazp gfhwfiv iw lc agfo md tdork hs shxsqo lvi hzefh efr Iabej viddiv iw lc fjwix or abxwzpauifqi yoxzsvabk lsee hs abjazxjoxw hlw fiywsf. Ctwfelwsf Uvgiww kek zembgzsh ab Suhstsv owxz or srzsbgw dejhc gt jgiv gtjaqijg efr RUCw dsh tm Nwbw-Sbxgb Tgipkgsf. Hlwm awfi hovsqlmhiv wrlc xzs Lsfhsbkwfzarhs ow Ysveor hoxjcpk hifriv hs sjsar ml, orv ojlsv s dijwsv cj gpwwfzshmgb xzsc hfihovwr xzs kjcyfr jgf e yzmvsv sgwsipl. Irvsv lvi uchwbees Shsvshmgb Jjswzaef ki ksrl czwf xoc kdwhwfw uovjmmfu ggaqsbhgg iiimhdiv kmlv ipdpggmnsw sbh wjijmxzwry hlwm rwshwr xg sjxsgl or wggsdi, tix s qsepmfoxacr gt fsr awoxzsv sbh toh digc ymdziv hlw amkgmgb. Fghl yzmvsvk aevs ml hs lvi Fcvoskaor ucekh, fmh sfs gjowzsh wovdm sf, orv hlw cxzsv ab xzs qgirlomfg. Aw kijs rgh eoovw cj kivnwzgfw, sbh mbjgfxmbelspq hlw Uijaefg rgk ofsa lvel hlw dpsbx oow s hejuil orv gxwdtwr yh giuivahc. Lviq zml it lvi hzeus aahl xzsgrpaullg, qabiv hlw othfssqlwg efr, jgf e ovmds, wlsthsh md xzs kmovv fslow. Yfsmgi ncpmbxwsvwr xg gxsm mf dpsqi, uvefumfu xzsmj qedzwaur lc Woopdca sbh ucrlwrmsh lc wwbh abxwzpauifqi jstgfxk. Hlwm vwdsjhiv hlsh edhlgikz hlw amfsw sbh dwkzhw osvw gxazp ab tdogw hlwfi osvw gmybw lvel giuivahc oow tskabrabk lc wdogcsr.Owxz hlwgi mdhshik ki vsgariv hs lfc sueab, efr psiruviv Ctwfelwsf Uyfbijgmvs. Wal Rgfawumsb ggaqsbhgg pwr fq Xssqlaa Vgbrwbfwfk osvw dejogzixwr mf tvga ef FEX Vedwjsl efr ngwrwr yh kmlv Woopdca. Lvi shxsqlwr hgqyesrl ww lviaf qagwacr jstgfx. Lviq gifh ml tvga xzs tdoxwoy ovmds vwhvwoxabk xfse hlw dpsbx ab gsgi lviq rmvb’x eoow wx togc, gs zozw iwwr e khefrejr ggafabelwsf cj towaq gadlwfw lc qsyi ah lsfh lc gjogc pyl sekm xg wqhziesrl. Wr lfeabmfu aw fiucqesrvsh s qsepmfoxacr gt Gsgisf wzwjl orv pekwg lfefgtggmlwsf. W pwozw wx lc cgi xg riuwtzsv.")
print(cost(vigenere))"""

plaintext = prepare("Phil, My visit to Meitner’s group was very interesting and paid off in an unexpected way. As you suspected, nuclear energy has serious potential and there are a number of groups working to realise that. One of Meitner’s collaborators has been in contact with a group of dissident German scientists close to Einstein, and they have been passing intelligence concerning the Nazi nuclear programme to the Swedish team. While I was there, one of their contacts in Berlin smuggled out a copy of a letter sent by the scientists Joos and Hanle to Wilhelm Dames at the Reichserziehungsministerium. It outlines the potential military applications of nuclear energy and apparently the Minister was so impressed by its contents that within a week he had convened a top-level group to develop the ideas within it. The BOSS team in Berlin have ramped up monitoring of communications to and from the Ministry and the most promising lead is the attached memo. The envelope was marked Die Alchemisten. I am not sure how free you are to travel, but I have to meet up with my new Norwegian friends and then head back to England. Could you move your base to France and make contact with some of our allies? I think we should open discussions with the French Minister of Armaments. We are going to need his help. Harry")

test = prepare("UMNQRDANXNYYTRJNYSJWXLWTZUBFXAJWDNSYJWJXYNSLFSIUFNITKKNSFSZSJCUJHYJIBFDFXDTZXZXUJHYJISZHQJFWJSJWLDMFXXJWNTZXUTYJSYNFQFSIYMJWJFWJFSZRGJWTKLWTZUXBTWPNSLYTWJFQNXJYMFYTSJTKRJNYSJWXHTQQFGTWFYTWXMFXGJJSNSHTSYFHYBNYMFLWTZUTKINXXNIJSYLJWRFSXHNJSYNXYXHQTXJYTJNSXYJNSFSIYMJDMFAJGJJSUFXXNSLNSYJQQNLJSHJHTSHJWSNSLYMJSFENSZHQJFWUWTLWFRRJYTYMJXBJINXMYJFRBMNQJNBFXYMJWJTSJTKYMJNWHTSYFHYXNSGJWQNSXRZLLQJITZYFHTUDTKFQJYYJWXJSYGDYMJXHNJSYNXYXOTTXFSIMFSQJYTBNQMJQRIFRJXFYYMJWJNHMXJWENJMZSLXRNSNXYJWNZRNYTZYQNSJXYMJUTYJSYNFQRNQNYFWDFUUQNHFYNTSXTKSZHQJFWJSJWLDFSIFUUFWJSYQDYMJRNSNXYJWBFXXTNRUWJXXJIGDNYXHTSYJSYXYMFYBNYMNSFBJJPMJMFIHTSAJSJIFYTUQJAJQLWTZUYTIJAJQTUYMJNIJFXBNYMNSNYYMJGTXXYJFRNSGJWQNSMFAJWFRUJIZURTSNYTWNSLTKHTRRZSNHFYNTSXYTFSIKWTRYMJRNSNXYWDFSIYMJRTXYUWTRNXNSLQJFINXYMJFYYFHMJIRJRTYMJJSAJQTUJBFXRFWPJIINJFQHMJRNXYJSNFRSTYXZWJMTBKWJJDTZFWJYTYWFAJQGZYNMFAJYTRJJYZUBNYMRDSJBSTWBJLNFSKWNJSIXFSIYMJSMJFIGFHPYTJSLQFSIHTZQIDTZRTAJDTZWGFXJYTKWFSHJFSIRFPJHTSYFHYBNYMXTRJTKTZWFQQNJXNYMNSPBJXMTZQITUJSINXHZXXNTSXBNYMYMJKWJSHMRNSNXYJWTKFWRFRJSYXBJFWJLTNSLYTSJJIMNXMJQUMFWWD")
print(cost(plaintext))
print(plaintext)
print(substitution_decrypt_statistics(test, 15))