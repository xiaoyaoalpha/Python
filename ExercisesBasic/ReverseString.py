# coding=utf-8
# ___author___ = 'xy'


##############################################################################
# 翻转字符串
# 方法一：将字符串构造成list，翻转list后再构造成新的字符串
##############################################################################

Sentence = str(input('please input a sentence:'))
tempstr = ''
L=[]
for i, word in enumerate(Sentence):
    if word != ' ':
        if i != (len(Sentence)-1):
            tempstr = tempstr + word
        else:
            tempstr = tempstr + word
            L.append(tempstr)
    else:
        L.append(tempstr)
        tempstr = ''
L.reverse()
NewSentence = ' '.join(L)
print(NewSentence)