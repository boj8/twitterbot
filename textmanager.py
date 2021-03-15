import os
import random
from nltk.tokenize import sent_tokenize


def getRandomSentence():
    dirList = os.listdir("MIM-GOLD-1_0")
    choice = random.choice(dirList)
    f = open('MIM-GOLD-1_0/' + choice, 'r', encoding='utf8')
    text = f.read()
    text = text.split('\n')
    textString = ''
    punct = ['.', ',', ':', ' ', '!', '?']

    for i in range(len(text)):
        if text[i] == '':
            text[i] = ' '
        else:
            text[i] = text[i].split('\t')[0]
    for i in range(len(text) - 1):
        if text[i + 1] not in punct and text[i] != ' ':
            textString += (text[i] + ' ')
        else:
            textString += text[i] 
    textString += text[len(text) - 1]
    sents = sent_tokenize(textString)
    return(random.choice(sents))

def getTwitterKeys():
    f = open('keys.txt', 'r', encoding='utf8')
    keys = f.read()
    keys = keys.split('\n')

    return keys