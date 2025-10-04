str1 = "NAINA"
str2 = "REENA"
str3 = "AABBFEAACCED"
str4 = 'Sheena loves eating mango and apple Her sistem also loves eating mango and apple'


def inBuildMeth():
    set1 = set(str1)
    set2 = set(str2)

    setIn = set1 & set2 # Intersection of two
    str3 = ''.join(setIn)

#  Dictionary
def logic():
    dictCommonChar = {
    }

    

    for ch in str1:
        if(ch in dictCommonChar):
            dictCommonChar[ch] = dictCommonChar[ch] +1
        else:
            dictCommonChar[ch] = 1


    for ch in str2:
        if(ch in dictCommonChar):
            print(ch)
            val  = dictCommonChar[ch]
            if(val >1):
                dictCommonChar[ch] = dictCommonChar[ch]-1
            else:
                del dictCommonChar

def countFreqWordInorder(str3):
    dictWord = {}   

    for ch in str3:
        if(ch in dictWord):
            dictWord[ch] = dictWord[ch] + 1
        else:
            dictWord[ch] = 1

    ansStr = ''
    for key in dictWord:
        ansStr = ansStr + key + str(dictWord[key])

    print(ansStr)

def countfreWordOrder(str3):
    ansStr = str3[0]
    count = 1
    for i in range (1,len(str3)):
        if(str3[i] != str3[i-1]):
            ansStr = ansStr + str(count)
            ansStr = ansStr + str3[i]
            count = 1
        else:
            count = count +1

    ansStr = ansStr + str(count)
    print(ansStr)

def wordCount(str4):
    wordList = str4.split()
    dictWord = {}

    for word in wordList:
        if word in dictWord:
            dictWord[word] = dictWord[word] + 1
        else:
            dictWord[word] = 1
    
    print(dictWord)

wordCount(str4)