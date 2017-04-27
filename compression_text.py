import string
import operator
import sys

c = {}
alphabet = ""
outputText = ""
outputDigrams = ""
inputfile = sys.argv[1]
outputfile = sys.argv[2]
text = open(inputfile)
digrams = []
# Create a list of 2-character keys

for i in range(33,47):
    alphabet += chr(i)
for i in range(58,126):
    alphabet += chr(i)

for i in alphabet :
    for j in alphabet + string.digits:
        digrams.append(i+j)
# Split text in trigrams
while True:
    t = text.read(3)
# How many occurences of given trigram
    if t in c:
        c[t] += 1
    else:
        c[t] = 1

    if not t:
        print('end of File')
        break
sorted_c = sorted(c.items(),key=operator.itemgetter(1), reverse=True)

print(len(c),">",len(digrams))
print('\n\u001B[31mIMPOSSIBLE : le nombre de trigrammes est superieur au nombre de digrammes disponibles.\u001B[0m\n\u001B[31mEssayez de rajouter des caracteres disponibles a la variable alphabet\u001B[0m\n')if len(c)>len(digrams) else print('\u001B[32mOK\u001B[0m')
# Associate each trigram with a key
for i in range(10):
    c[sorted_c[i][0]] = str(i)
    outputDigrams += sorted_c[i][0]

for i in range(10,len(c)):
    c[sorted_c[i][0]] = digrams[i-10]
    outputDigrams += sorted_c[i][0]

text = open(inputfile)
while True:
    t = text.read(3)
    if t in c:
        outputText += c[t]
    if not t:
        break

nbKeys = str(len(c))
while len(nbKeys) < 8:
    nbKeys = "0" + nbKeys

with open(outputfile,'wb') as text:
    text.write(nbKeys.encode('utf8'))
    text.write(outputDigrams.encode('utf8'))
    text.write(outputText.encode('utf8'))
