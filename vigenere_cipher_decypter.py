from substitution_tim import prepare, cost, accept_prob
import string
import random

cipher_text1 = prepare("altd wo o kpva xz dsa kypwoic eva qfohy azcyo, sjahjmlwzu kypq sszvsz ok nrttwtqwhvo zvvod gqqy lv gimcoo oeo phxctqag nsljl lwgk bvpg as mp raqijsaio ec iobp vbvp evwh kslz tczunod ndu wzwja oejwomyr hdok tv wye tb bffyw vj te")
cipher_text2 = prepare("FCBJA YNMVN PMMAZ NMMAG ALQPQ YLQIL IYMLA BJCRA LAHAZ CSZHC MQIPA SIGIP MQAEC FWFQI TCIIP HNRMC XNHAB PPNBP AGQMM NWFQI BMATG APMVM BJNLZ AFAPA BPENA LOHNR ATYCF AHHNB RALQR AMALI GMCBP JQPAM IPGNA PMHIC PNRCH QGGIR LQIWA EMNCV BTMCB RCBTV LIPRN YABPH IARHA ZCFFA PHCBP CTMQW AAYIP VLPHQ IRABP HCELI TPAHL QIVHI VFCSN ABZHC VFALA OFFCT ATPUA HIWIP PNBTP QIELI TIPWI CLAJP NBPAM QHNRA TWHNA FCBTN AENPF FCTPN BPPQO MERIP MHTIL CABPJ QWFCQ OVABP FCPHQ AGCPY ILAPP NGNVF HIMCP CHNEQ DLYIF ILPHI RHAEN PASNB MMABP PNBPT IHLAP NTVSN ABABP APNQR NSAIP AFONM NTLAC FFNLQ ACMHI GPNBP WNFZV LASAG MAENG AZNMM AGABP AQFRZ CONAG ASNZP NBPWH NGQCL APMCH CGMZH QBACX LAMBR CALAB PLIYP AZLNP PHNPL IJGCH NMNTI LWVBE MLIHA RHCML IYEII FIPPN BTNAW CAGIM WNBCV FCERQ FHICP CMIJM HNLPL NHGQF IRNPA VHAAM ASNBA TLABJ CRALQ RAMPM IGABP AMQML AWLIA BPVFZ HCMCL JLQMH QMAZH NBRPN BPAMN RHCAR HAZCF FAPHC AENYL IYPQI EIIFI PWAAH FFCTA TPQOW APRAP AWHAA OPAVP IHMNB GAPMV MRCBJ NLZAF APALQ RAMAB PIPHC JNPLC ABPFF APHNR ATMNL NYMNA ZHNBR UAAHI BJAFA PABPI PPUAH MLAPL NQKWN ABNWA BMCFO NPMAA SNBIB TFNPC JNRAB PHCMP HAZNM MIOVO WAPJA RLAPH CALAT MLAWL IHICM NSHCW ABRNP PNABP HICMM ALZZN BMCPC LOIRH NLYPM HCNZN VPCFN LPQAH MVLPH QIRAB PPRAP ILJIP ALABP ALNPB RNGLB ATABP MCAHC FFNCR CYYIA BPNWH NZNJI LJCXN HABPY IPLNJ PHNRC YCHZC MNTIH MCPNB PWHNA LSQAI HNGLA PHQIR NZHCM MQRMC WVFHA JIHAA OWNBB MCPCL OABPA HIVHN IPERI BMIHM NAGIR MNBPC HICMN SHCAB PPQIO NTIHV OWLNA BASNB QIVMM AQZCV LLNB")
cipher_text3 = "ALTDWLHBWALTHWWXPVWXLAYQRHYKAIESVWZLCTXGVKIPDQGESGECRKMHWPDQBICVMQHNRONMDPSMXZBALMLAQFSBAEVVTPKZVMQHGBPVTQCMOOUTKZSWQMFIOG"
cipher9 = prepare("IRZDQ PSEID VQHWW THVUY MDWGQ BYSRO UFZFR TPIBE XKCZW XRTXG POOSV KBTWX TSIDK AAXMV RYTRI RJTWQ XIVAQ UHBQE SPBMJ ZSGWP WBTWT HGEDB EQJXH UITKI FAHBN XSACW SGHUI JELGK MFVEM KZMUD GNREK PQLKO POUFD QEHFX AIZTQ LASEE JCEMQ MFNGL JBTWF GRPWV ADWFO VRPGM DSMWB RBCIO GGGVH FIIND XOZSV EBAXK CYPJE OELHQ XABJA QJBCH WMPLM ETURH XZBTL PCYSD FUALB JRWFZ OTLVO EKPNI SGGGN REJMH WGDNW TVVSW KKNKP EAEMY TRVJE OPSFO TIPLZ MYXBG WJEBT WIZNR UYIHW VCAJJ IUQVM VNXUY QEZTG FPPNM PLAST ISDIZ HEOAX PJPUH MVRVF DIUFB BTWUF KWKHT CSURA EANAC ISFFU VXHBH JVIXU ASZMT KMZJX GREST PRSVW YMUZM EAGPR VMZVU FIFRT BIIFA HBSSS KPQKA WCQFE BOAOW YMBEA MJXBB PPEOQ JTZYS XVLMU VSFWU FBTWK OVPXR GMFWD NXSFT EZTJR FFVVE LXDCI ELXEW VIEMU PIFSE ZGLFI IUDPO LWURB UGGGU ETSMQ FLWTR JWQOS GHYCJ EKDWT GRHTN IXDHK UEWVU MLVVR HUYQE TRWAG SVIEA GUGLF ZZAOG GHVWV QXDTB PIPEB TWKXH OBETU FXOAH QIWBG LSQEO LUNWK CSTMR VELHW AXFIK QHMHU ITYQB EXBGF VKBTW XBUEO TMPKX QHVJK GYSDS VXWVZ KMGZV OFCGF ZTHNW URVPS KRFEC FBMYX KBYMU AGUVS RHJEL AAGUZ SSVBT SGRRP BPQZY MVRWI ZXYWG HNPUV ZZSMW IITZV ODNRV RHKPQ DHQNP GVZDQ KCHXF JIDWU SVRHR KFAOS YCDFV EAWSE IERAI AMVGL FRQDJ TWQGJ MQXAT BPETL IXLBS FESVI YSCCE GPEAU VXFNX JFVNM MHUIQ CIZLW WEIDK WDTCO ERFEQ XKLSA MTJGY HTHUI UZKMF WANCC VINDX HBMOW TGWGQ RXIVL MLXOA HUZUQ GYGUM QDMZL BBBVE VZFGK SQYDV BTWKW FOPEK QEHFR SVIIS WGHFL BMMNW XBFYD TMEKY IYMOZ VFWKQ RTUZV SWGSZ CDFUY MGWPE UZWZK VCAGF IVUFZ HUINZ AEAHB NREKP QWGQY STVLF WESTV BDAGE FOEMT ZVSLA SCPBE AOGGT VVNJW GJHKA MOMME LBUNX JFVEO BHUXI ZAUFA OAHJK PUFDH UITNI XDHKG IBDEU DEPRE CCMFG XLRGV KMMKN QPITJ NGDLO OSURO QSGRU SQVNG DEMGI SDQZS MSGLF XMDET BAYDC MMJPS NTPEA BJHUE ENCMF KACCI XVKMF XBQXI ZAEGH BCLJC")

def string_to_numbers(cipher):
    output = []
    for char in cipher:
        output.append(ord(char) - 65)
    return output

def vigenere_decrypt(cipher, key, cipher_type):
    output = []
    string_out = ""
    key_number = string_to_numbers(key)
    cipher_number = string_to_numbers(cipher)
    if cipher_type == "Vigenere":
        for x in range(len(cipher)):
            key1 = key_number[x % len(key)]
            output.append(((cipher_number[x] - key1 + 26) % 26) + 65)
    if cipher_type == "Autokey":
        for x in range(len(cipher)):
            output.append(((cipher_number[x] - key_number[x] + 26) % 26) + 65)
            key_number.append((cipher_number[x] - key_number[x] + 26) % 26)
    if cipher_type == "Beaufort":
        for x in range(len(cipher)):
            key1 = key_number[x % len(key)]
            output.append(((key1 - cipher_number[x]) % 26) + 65)
    for y in output:
        string_out = string_out + chr(y)
    return string_out

def create_key(length):
    output = ""
    for y in range(length):
        output = output + "A"
    return output

def neighbour(key):       #function to swap a letter with another
    alphabet = dict(zip(range(1, 27), string.ascii_uppercase))
    key_list = list(key)
    n1 = random.randint(0, len(key_list) - 1)
    n2 = random.randint(0, 25)
    key_list[n1] = chr(n2 + 65)
    return "".join(key_list)

def SA_mine(cipher, key, vigenere):       #where f is the input function and a and b are the bounds between which a solution is looked for
    focus = 0.99
    t = 1
    t_min = 0.0001
    initial_key = key
    best = vigenere_decrypt(cipher, initial_key, vigenere)
    current = cost(vigenere_decrypt(cipher, initial_key, vigenere))
    while t > t_min:
        i = 1
        while i <= 10:          #iterations at each temperature
            next_key = neighbour(initial_key)
            new = cost(vigenere_decrypt(cipher, next_key, vigenere))
            if new >= current:
                initial_key = next_key
                current = new
                if new >= cost(best):
                    best = vigenere_decrypt(cipher, initial_key, vigenere)
            if accept_prob(t, current, new) > random.random():
                initial_key = next_key
                current = new
            i += 1
        t = focus * t
    return best

def solve(cipher, min_key_len, max_key_len, vigenere="Vigenere"):
    out_dict = {}
    first = min_key_len
    for y in range(max_key_len - first + 1):
        out_dict[cost(SA_mine(cipher, create_key(first), vigenere))] = SA_mine(cipher, create_key(first), vigenere)
        first += 1
    return out_dict[max(out_dict.keys())]


def beaufort_decrypt(cipher, key):
    output = []
    string_out = ""
    key_number = string_to_numbers(key)
    print(key_number)
    cipher_number = string_to_numbers(cipher)
    print(cipher_number)
    for x in range(len(cipher)):
        key1 = key_number[x % len(key)]
        output.append(((key1 - cipher_number[x]) % 26) + 65)
    for y in output:
        string_out = string_out + chr(y)
    return string_out

#print(vigenere_decrypt(cipher_text, cipher_text_key))
#print(SA_mine(cipher_text, create_key(10)))
#print(neighbour("AAAAAAAA"))
#print(solve(cipher_text3, 5, 5, False))
#print(vigenere_decrypt("OXDTGPESHWOLXTKDIEHVAAUZQSNXFXHSPXXXM", "HELLO", "Beaufort"))
#ciphertext = prepare("Hvmd,Gsjfc A vensr’l piwb mf hsmql eigz, Qlmfgzwpd owcsh TCWK hs ksx md ef ctwfelwsfg aabk ab xzs YC irvsv lvi foqw cj lvi Kdiuwed Ctwfelwsfg Ipsgmhmns efr xzox zow gqgmdmwr e dcx gt qq hmes. Ek gsgb ek ki ycx ksx md M oow hix ab xgigz kmlv Iabej Goabrsfpsbh, sb ifumfsij tvga Zwasjy azc lsr laxeuyiv o ggowlop khisaij orv geaziv hs Spijriwb xg xsab xzs asf ixtsjh lwfi. Uvyjqlazp gfhwfiv iw lc agfo md tdork hs shxsqo lvi hzefh efr Iabej viddiv iw lc fjwix or abxwzpauifqi yoxzsvabk lsee hs abjazxjoxw hlw fiywsf. Ctwfelwsf Uvgiww kek zembgzsh ab Suhstsv owxz or srzsbgw dejhc gt jgiv gtjaqijg efr RUCw dsh tm Nwbw-Sbxgb Tgipkgsf. Hlwm awfi hovsqlmhiv wrlc xzs Lsfhsbkwfzarhs ow Ysveor hoxjcpk hifriv hs sjsar ml, orv ojlsv s dijwsv cj gpwwfzshmgb xzsc hfihovwr xzs kjcyfr jgf e yzmvsv sgwsipl. Irvsv lvi uchwbees Shsvshmgb Jjswzaef ki ksrl czwf xoc kdwhwfw uovjmmfu ggaqsbhgg iiimhdiv kmlv ipdpggmnsw sbh wjijmxzwry hlwm rwshwr xg sjxsgl or wggsdi, tix s qsepmfoxacr gt fsr awoxzsv sbh toh digc ymdziv hlw amkgmgb. Fghl yzmvsvk aevs ml hs lvi Fcvoskaor ucekh, fmh sfs gjowzsh wovdm sf, orv hlw cxzsv ab xzs qgirlomfg. Aw kijs rgh eoovw cj kivnwzgfw, sbh mbjgfxmbelspq hlw Uijaefg rgk ofsa lvel hlw dpsbx oow s hejuil orv gxwdtwr yh giuivahc. Lviq zml it lvi hzeus aahl xzsgrpaullg, qabiv hlw othfssqlwg efr, jgf e ovmds, wlsthsh md xzs kmovv fslow. Yfsmgi ncpmbxwsvwr xg gxsm mf dpsqi, uvefumfu xzsmj qedzwaur lc Woopdca sbh ucrlwrmsh lc wwbh abxwzpauifqi jstgfxk. Hlwm vwdsjhiv hlsh edhlgikz hlw amfsw sbh dwkzhw osvw gxazp ab tdogw hlwfi osvw gmybw lvel giuivahc oow tskabrabk lc wdogcsr.Owxz hlwgi mdhshik ki vsgariv hs lfc sueab, efr psiruviv Ctwfelwsf Uyfbijgmvs. Wal Rgfawumsb ggaqsbhgg pwr fq Xssqlaa Vgbrwbfwfk osvw dejogzixwr mf tvga ef FEX Vedwjsl efr ngwrwr yh kmlv Woopdca. Lvi shxsqlwr hgqyesrl ww lviaf qagwacr jstgfx. Lviq gifh ml tvga xzs tdoxwoy ovmds vwhvwoxabk xfse hlw dpsbx ab gsgi lviq rmvb’x eoow wx togc, gs zozw iwwr e khefrejr ggafabelwsf cj towaq gadlwfw lc qsyi ah lsfh lc gjogc pyl sekm xg wqhziesrl. Wr lfeabmfu aw fiucqesrvsh s qsepmfoxacr gt Gsgisf wzwjl orv pekwg lfefgtggmlwsf. W pwozw wx lc cgi xg riuwtzsv.F AHHNB RALQR AMALI GMCBP JQPAM IPGNA PMHIC PNRCH QGGIR LQIWA EMNCV BTMCB RCBTV LIPRN YABPH IARHA ZCFFA PHCBP CTMQW AAYIP VLPHQ IRABP HCELI TPAHL QIVHI VFCSN ABZHC VFALA OFFCT ATPUA HIWIP PNBTP QIELI TIPWI CLAJP NBPAM QHNRA TWHNA FCBTN AENPF FCTPN BPPQO MERIP MHTIL CABPJ QWFCQ OVABP FCPHQ AGCPY ILAPP NGNVF HIMCP CHNEQ DLYIF ILPHI RHAEN PASNB MMABP PNBPT IHLAP NTVSN ABABP APNQR NSAIP AFONM NTLAC FFNLQ ACMHI GPNBP WNFZV LASAG MAENG AZNMM AGABP AQFRZ CONAG ASNZP NBPWH NGQCL APMCH CGMZH QBACX LAMBR CALAB PLIYP AZLNP PHNPL IJGCH NMNTI LWVBE MLIHA RHCML IYEII FIPPN BTNAW CAGIM WNBCV FCERQ FHICP CMIJM HNLPL NHGQF IRNPA VHAAM ASNBA TLABJ CRALQ RAMPM IGABP AMQML AWLIA BPVFZ HCMCL JLQMH QMAZH NBRPN BPAMN RHCAR HAZCF FAPHC AENYL IYPQI EIIFI PWAAH FFCTA TPQOW APRAP AWHAA OPAVP IHMNB GAPMV MRCBJ NLZAF APALQ RAMAB PIPHC JNPLC ABPFF APHNR ATMNL NYMNA ZHNBR UAAHI BJAFA PABPI PPUAH MLAPL NQKWN ABNWA BMCFO NPMAA SNBIB TFNPC JNRAB PHCMP HAZNM MIOVO WAPJA RLAPH CALAT MLAWL IHICM NSHCW ABRNP PNABP HICMM ALZZN BMCPC LOIRH NLYPM HCNZN VPCFN LPQAH MVLPH QIRAB PPRAP ILJIP ALABP ALNPB RNGLB ATABP MCAHC FFNCR CYYIA BPNWH NZNJI LJCXN HABPY IPLNJ PHNRC YCHZC MNTIH MCPNB PWHNA LSQAI HNGLA PHQIR NZHCM MQRMC WVFHA JIHAA OWNBB MCPCL OABPA HIVHN IPERI BMIHM NAGIR MNBPC HICMN SHCAB PPQIO NTIHV OWLNA BASNB QIVMM AQZCV LLNB")
#print(SA_mine(cipher9, create_key(7), "Vigenere"))

