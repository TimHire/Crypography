#For creating a .h file with the trigram scores on
import requests
import math

ngrams = {}
req = requests.get("https://gist.githubusercontent.com/DomDale/9a582deed33b20bb47e0363301d2c6c4/raw/62e7416f6be95893649398f0470f1dcd2668e608/english_trigrams.txt")
ngram_list = req.text
ngram_list = list(ngram_list.splitlines())
for i in ngram_list:
    ngrams[i[0:3]] = int(i[4:])      #dictionary with all the scores for the trigrams
ngram_sum = sum(ngrams.values())

print(math.log10(ngrams["THE"] / ngram_sum))

def num_to_str(num):
    output = []
    string = ""
    output.append(int(num / (26**2)))
    output.append(int((num - 26**2 * output[0]) / 26))
    output.append(num - 26**2 * output[0] - 26 * output[1])
    for i in range(3):
        string = string + chr(output[i] + 65)
    return string

def str_to_num(string):
    a = (ord(string[0]) - 65) * 26**2
    b = (ord(string[1]) - 65) * 26
    c = (ord(string[2]) - 65)
    return a + b + c

for k in range(0, 5000, 2000):
    print(num_to_str(k))
    print(str_to_num(num_to_str(k)))

    

with open("trigrams.h", "w") as tri:
    tri.write("float trigrams[17576] = {\n")
    for i in range(26**3):
        try:
            tri.write("{},\n".format(math.log10(ngrams[num_to_str(i)] / ngram_sum)))
        except:
            tri.write("-10,\n")
    tri.write("};")
        
    
