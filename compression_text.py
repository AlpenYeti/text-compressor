import string
import operator
import sys
import os.path

inputfile = sys.argv[1]
outputfile = sys.argv[2]
c = {}
alphabet = ""
outputText = ""
outputDigrams = ""
text = open(inputfile)
digrams = []
tri=""
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
    tri=""
    letter = text.read(1)
    if not letter:
        print('end of File after full trigram')
        break
    else:
        letter2 = text.read(1)
        tri=letter
        if not letter2:
            c[tri] = 1
            print('end of File after one character as a key')
            break
        else:
            letter3 = text.read(1)
            tri+=letter2
            if not letter3:
                c[tri] = 1
                print('end of File  after two characters as a key')
                break
            else:
                tri+=letter3
                if tri in c:
                    c[tri] += 1
                else:
                    c[tri] = 1

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

nbKeys = str((len(c)-1)*3 + len(c[tri]))
while len(nbKeys) < 8:
    nbKeys = "0" + nbKeys

with open(outputfile,'wb') as text:
    text.write(nbKeys.encode('utf8'))
    text.write(outputDigrams.encode('utf8'))
    text.write(outputText.encode('utf8'))

def output_exists():
    test = os.path.isfile(outputfile)
    if test:
        print("Output file '", outputfile ,"' has been created")
    else:
        print("A problem might have occured")
output_exists()
