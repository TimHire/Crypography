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

def prepare(cipher):
    cipher = cipher.upper()
    cipher = cipher.replace(" ", "").replace(".", "").replace(",", "").replace("?", "").replace("-", "").replace("’", "").replace("!", "").replace(";", "")
    return cipher

def cost(cipher):
    total = 0
    for x in range(len(cipher) - 2):
        tri_list = cipher[x] + cipher [x+1] + cipher[x+2]
        if tri_list in ngrams.keys():
            total += np.log10((ngrams.get(tri_list, 0) / ngram_sum))
        else:
            total += -10                # Exception if there is no frequency value for the inputted string
    return total

def accept_prob(temp, last, potential):
    try:
        #print(potential-last)
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

def neighbour(now, type, key):       #function to swap two letter with each other
    alphabet = dict(zip(range(1, 27), string.ascii_uppercase))
    if type == "substitution":
        n1, n2 = random.sample(range(1, 27), 2)
        return swap(now, str(alphabet[n1]), str(alphabet[n2]))
    if type == "columnar":
        #n1, n2 = random.sample(range(0, key-1), 2)
        n1, n2 = 0, 1
        data_list = list(now)
        for x in range(0, int((len(now) / key)+1)):
            try:
                first = data_list[n1 + key * x]
                second = data_list[n2 + key * x]
                data_list[n1 + key * x] = str(second)
                data_list[n2 + key * x] = str(first)
            except:
                pass
        return "".join(data_list)
    """if type == "rail":
        key1 = random.randint(2, 20)
        extra_x = int(key1 - (len(now) % key1))
        for z in range(extra_x):
            now = now + "X"
        cipher_in = list(now)
        output = []
        row = 0
        for i in range(key1):
            for y in range(0, int((len(cipher_in) / key1) - 1)):
                output.append(cipher_in[row + y * row * (2 * key1 - 2)])
            row += 1
        output = "".join(cipher_in)
        return output[:len(output) - extra_x + 1]"""


def SA_mine(cipher, type, key):       #where f is the input function and a and b are the bounds between which a solution is looked for
    focus = 0.99
    t = 1
    t_min = 0.001
    best = cipher
    initial_x = cipher
    current = cost(initial_x)
    count = 0                   ####
    prob_accept = 0             ####
    while t > t_min:
        for i in range(10):                             # Number of iterations at each temperature
            next_x = neighbour(initial_x, type, key)
            new = cost(next_x)
            if new >= current:
                initial_x = next_x
                current = new
                if new >= cost(best):
                    best = initial_x
            if accept_prob(t, current, new) > random.random():
                initial_x = next_x
                current = new
                prob_accept += 1
            count += 1
        t = focus * t
    print("Total: {}    Prob_accept: {}".format(count, prob_accept))
    return best

def substitution_decrypt(cipher, x, type):
    if type == "substitution":
        for i in range(x - 1):
            print(SA_mine(prepare(cipher), type, 0))
        return SA_mine(prepare(cipher), type, 0)
    if type == "columnar":
        dict_out = {}
        for i in range(9, 10):               #range of key lengths to try
            attempt = SA_mine(prepare(cipher), type, i)
            dict_out[cost(attempt)] = attempt
            #print(attempt)                             Uncomment this to get best value for each key iteration if required
        return dict_out[max(dict_out.keys())]
    if type == "rail":
        for i in range(x-1):
            print(SA_mine(prepare(cipher), type, 0))
        return SA_mine(prepare(cipher), type, 0)

second = prepare("KHUPRPKDGZDUQHGKHUVKHKDGEHHQZDUQHGWLPHDQGDJDLQEXWVKHKDGUHIXVHGWREHOLHYHKHUVKHKDGGRQHHYHUBWKLQJULJKWDQGVKHNQHZVKHZRXOGEHUHZDUGHGIRUGRLQJVRZLWKWKHSURPRWLRQVRZKHQWKHSURPRWLRQZDVJLYHQWRKHUPDLQULYDOLWQRWRQOBVWXQJLWWKUHZKHUEHOLHIVBVWHPLQWRGLVDUUDBLWZDVKHUILUVWELJOHVVRQLQOLIHEXWQRWWKHODVWMRVKKDGVSHQWBHDUDQGBHDUDFFXPXODWLQJWKHLQIRUPDWLRQKHNQHZLWLQVLGHRXWDQGLIWKHUHZDVHYHUDQBRQHORRNLQJIRUDQHASHUWLQWKHILHOGMRVKZRXOGEHWKHRQHWRFDOOWKHSUREOHPZDVWKDWWKHUHZDVQRERGBLQWHUHVWHGLQWKHLQIRUPDWLRQEHVLGHVKLPDQGKHNQHZLWBHDUVRILQIRUPDWLRQSDLQVWDNLQJOBPHPRULCHGDQGVRUWHGZLWKQRWDVROHJLYLQJHYHQDQRXQFHRILQWHUHVWLQWKHWRSLFVRPHWLPHVWKDWVMXVWWKHZDBLWKDVWREHVXUHWKHUHZHUHSUREDEOBRWKHURSWLRQVEXWKHGLGQWOHWWKHPHQWHUKLVPLQGLWZDVGRQHDQGWKDWZDVWKDWLWZDVMXVWWKHZDBLWKDGWREHVSHQGLQJWLPHDWQDWLRQDOSDUNVFDQEHDQHAFLWLQJDGYHQWXUHEXWWKLVZDVQWWKHWBSHRIHAFLWHPHQWVKHZDVKRSLQJWRHASHULHQFHDVVKHFRQWHPSODWHGWKHVLWXDWLRQVKHIRXQGKHUVHOILQVKHNQHZVKHGJRWWHQKHUVHOILQDOLWWOHPRUHWKDQVKHEDUJDLQHGIRULWZDVQWRIWHQWKDWVKHIRXQGKHUVHOILQDWUHHVWDULQJGRZQDWDSDFNRIZROYHVWKDWZHUHORRNLQJWRPDNHKHUWKHLUQHAWPHDOVKHVDWLQWKHGDUNHQHGURRPZDLWLQJLWZDVQRZDVWDQGRIIKHKDGWKHSRZHUWRSXWKHULQWKHURRPEXWQRWWKHSRZHUWRPDNHKHUUHSHQWLWZDVQWIDLUDQGQRPDWWHUKRZORQJVKHKDGWRHQGXUHWKHGDUNQHVVVKHZRXOGQWFKDQJHKHUDWWLWXGHDWWKUHHBHDUVROGVDQGBVVWXEERUQSHUVRQDOLWBKDGDOUHDGBEORRPHGLQWRIXOOYLHZ")
c_text = "KHUPRPKDGZDUQHGKHUVKHKDGEHHQZDUQHGWLPHDQGDJDLQEXWVKHKDGUHIXVHGWREHOLHYHKHUVKHKDGGRQHHYHUBWKLQJULJKWDQGVKHNQHZVKHZRXOGEHUHZDUGHGIRUGRLQJVRZLWKWKHSURPRWLRQVRZKHQWKHSURPRWLRQZDVJLYHQWRKHUPDLQULYDOLWQRWRQOBVWXQJLWWKUHZKHUEHOLHIVBVWHPLQWRGLVDUUDBLWZDVKHUILUVWELJOHVVRQLQOLIHEXWQRWWKHODVWMRVKKDGVSHQWBHDUDQGBHDUDFFXPXODWLQJWKHLQIRUPDWLRQKHNQHZLWLQVLGHRXWDQGLIWKHUHZDVHYHUDQBRQHORRNLQJIRUDQHASHUWLQWKHILHOGMRVKZRXOGEHWKHRQHWRFDOOWKHSUREOHPZDVWKDWWKHUHZDVQRERGBLQWHUHVWHGLQWKHLQIRUPDWLRQEHVLGHVKLPDQGKHNQHZLWBHDUVRILQIRUPDWLRQSDLQVWDNLQJOBPHPRULCHGDQGVRUWHGZLWKQRWDVROHJLYLQJHYHQDQRXQFHRILQWHUHVWLQWKHWRSLFVRPHWLPHVWKDWVMXVWWKHZDBLWKDVWREHVXUHWKHUHZHUHSUREDEOBRWKHURSWLRQVEXWKHGLGQWOHWWKHPHQWHUKLVPLQGLWZDVGRQHDQGWKDWZDVWKDWLWZDVMXVWWKHZDBLWKDGWREHVSHQGLQJWLPHDWQDWLRQDOSDUNVFDQEHDQHAFLWLQJDGYHQWXUHEXWWKLVZDVQWWKHWBSHRIHAFLWHPHQWVKHZDVKRSLQJWRHASHULHQFHDVVKHFRQWHPSODWHGWKHVLWXDWLRQVKHIRXQGKHUVHOILQVKHNQHZVKHGJRWWHQKHUVHOILQDOLWWOHPRUHWKDQVKHEDUJDLQHGIRULWZDVQWRIWHQWKDWVKHIRXQGKHUVHOILQDWUHHVWDULQJGRZQDWDSDFNRIZROYHVWKDWZHUHORRNLQJWRPDNHKHUWKHLUQHAWPHDOVKHVDWLQWKHGDUNHQHGURRPZDLWLQJLWZDVQRZDVWDQGRIIKHKDGWKHSRZHUWRSXWKHULQWKHURRPEXWQRWWKHSRZHUWRPDNHKHUUHSHQWLWZDVQWIDLUDQGQRPDWWHUKRZORQJVKHKDGWRHQGXUHWKHGDUNQHVVVKHZRXOGQWFKDQJHKHUDWWLWXGHDWWKUHHBHDUVROGVDQGBVVWXEERUQSHUVRQDOLWBKDGDOUHDGBEORRPHGLQWRIXOOYLHZ"
c_actual_text = "HERMOMHADWARNEDHERSHEHADBEENWARNEDTIMEANDAGAINBUTSHEHADREFUSEDTOBELIEVEHERSHEHADDONEEVERYTHINGRIGHTANDSHEKNEWSHEWOULDBEREWARDEDFORDOINGSOWITHTHEPROMOTIONSOWHENTHEPROMOTIONWASGIVENTOHERMAINRIVALITNOTONLYSTUNGITTHREWHERBELIEFSYSTEMINTODISARRAYITWASHERFIRSTBIGLESSONINLIFEBUTNOTTHELASTJOSHHADSPENTYEARANDYEARACCUMULATINGTHEINFORMATIONHEKNEWITINSIDEOUTANDIFTHEREWASEVERANYONELOOKINGFORANEXPERTINTHEFIELDJOSHWOULDBETHEONETOCALLTHEPROBLEMWASTHATTHEREWASNOBODYINTERESTEDINTHEINFORMATIONBESIDESHIMANDHEKNEWITYEARSOFINFORMATIONPAINSTAKINGLYMEMORIZEDANDSORTEDWITHNOTASOLEGIVINGEVENANOUNCEOFINTERESTINTHETOPICSOMETIMESTHATSJUSTTHEWAYITHASTOBESURETHEREWEREPROBABLYOTHEROPTIONSBUTHEDIDNTLETTHEMENTERHISMINDITWASDONEANDTHATWASTHATITWASJUSTTHEWAYITHADTOBESPENDINGTIMEATNATIONALPARKSCANBEANEXCITINGADVENTUREBUTTHISWASNTTHETYPEOFEXCITEMENTSHEWASHOPINGTOEXPERIENCEASSHECONTEMPLATEDTHESITUATIONSHEFOUNDHERSELFINSHEKNEWSHEDGOTTENHERSELFINALITTLEMORETHANSHEBARGAINEDFORITWASNTOFTENTHATSHEFOUNDHERSELFINATREESTARINGDOWNATAPACKOFWOLVESTHATWERELOOKINGTOMAKEHERTHEIRNEXTMEALSHESATINTHEDARKENEDROOMWAITINGITWASNOWASTANDOFFHEHADTHEPOWERTOPUTHERINTHEROOMBUTNOTTHEPOWERTOMAKEHERREPENTITWASNTFAIRANDNOMATTERHOWLONGSHEHADTOENDURETHEDARKNESSSHEWOULDNTCHANGEHERATTITUDEATTHREEYEARSOLDSANDYSSTUBBORNPERSONALITYHADALREADYBLOOMEDINTOFULLVIEW"
print(cost(c_text))
print(cost(c_actual_text))
print(SA_mine(second, "substitution", 0))


def decode(cipher, key):            #used for adding a ceaser shift to the ciphertext
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    output  = ''
    for c in cipher:
        if c in alphabet:
            output += alphabet[(alphabet.index(c)-key)%(len(alphabet))]
    return output
