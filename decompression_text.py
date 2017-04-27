# UTILISATION
# python decompression_text.py <fichier à décompresser> <fichier de sortie>
import sys
import string

c = {}
outputText = ""
inputfile = sys.argv[1]
outputfile = sys.argv[2]
text = open(inputfile,'r')
nbTrig = 0 # nombre de trigrammes dans le texte
specChars = ""
alphabet = ""
digrams = []

for i in range(33,47):
    alphabet += chr(i)
for i in range(58,126):
    alphabet += chr(i)

# Create a list of 2-character keys
for i in alphabet :
    for j in alphabet + string.digits:
        digrams.append(i+j)
# print(digrams)
# récupérer les 8 premiers caractères et les int-ify => Longueur de la chaîne de trigrammes
nbTrig = int(text.read(8)) # 8 premiers = nombre de clés
mostFr = text.read(10*3) # 30 suivants = 10 trigrammes les plus fréquents
otKeys = text.read(nbTrig*3-len(mostFr)) # nbKeys-30 suivants = autres trigrammes
textCo = text.read() # tout le reste = à décrypter

# recréer les trigrammes
# Associate each trigram with a key
w=0
n=3
for i in range(0, len(mostFr), n):
    c[str(w)] = mostFr[i:i+n]
    w+=1

w=0
for i in range(0,len(otKeys),n):
    c[digrams[w]] = otKeys[i:i+n]
    w+=1
# c = {j:mostFr[i:i+n] for i in range(0, len(mostFr), n) for j in range(10)}
# d = {digrams[j]:otKeys[i:i+n] for i in range(0, len(otKeys), n) for j in range(len(otKeys))}
# dico = {**c, **d}
# c[str(i)] = t

skip = False
for i in range(len(textCo)):
    if skip:
        skip = False
        continue
# lis le texte par un charactère
#     si c'est entre 0 et 9 tu le remplaces par c[t] et tu passes au suivant
#     sinon tu lis aussi le suivant et tu remplaces par c[t] et tu passes au +2
    if textCo[i] in '0123456789':
        outputText += c[textCo[i]]
    else:
        d = textCo[i] + textCo[i+1]
        outputText += c[d]
        skip = True

print("Decompression finished")
with open(outputfile,'w') as text:
    text.write(outputText)
