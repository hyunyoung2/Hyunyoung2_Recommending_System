# -*- coding: utf-8 -*-

#"""
# Created on Thu Jun 15 15:19:38 2017
#
# @author: hyunyoung2
#"""

# -- python version : 3.6 --
# for execution command
#import sys
# for replace specialchar with ""
import re
# for time measurement betweem statement below 
import time

# project : recommending system on X in A B X C D
# A B X C D : if words nearby X are A, B, C and D, what is the most possible X?  

## -- Basic function of IO --

# @ function : read files as one strig. 
# input : file path you want to read as one string
# output : a string from beginning of file to EOF 
def readFile (absPath) :
    f = open(absPath, "r")
    
    listOfStr = f.read()
    
    f.close()
    
    return listOfStr


# @ function : remove specailChar 
# input : a string including specialChar
# output : a string without specialChar
def removalOfSpecialChar (inputStr) :
    specialChar = "[!\"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~…]"
    
    inputStr = re.sub(specialChar, "", inputStr)
         
    return inputStr


# -- natural lanuage processing function -- 

# @ function : tokenizing words into a word and sorting 
# input : string 
# output : List of token of words
def tokenization (wordstring) :
    tempList = wordstring.split()
    tempList.sort()
    return tempList


# @ function :  how to make nGram like bigram, threegram
# input : a sorted list  
# output : nGram list sorted like bigram, threegram 
def nGram (listOfWord, n = 5) :
    newWord = [] 
    # len of List 
    lenOfList = len(listOfWord)
    flag = 0
    # this for statement is zero-based. 
    for idx, var in enumerate(listOfWord) :
        tempStr = ""
        for i in range(0,n):
            if idx + n > lenOfList :
                flag = 1
                break
            elif i == 0 : 
                tempStr += var
            elif i + idx < lenOfList :
                #print ("no addition into list")
                #print ("total : %d, current idx : %d" % (lenOfList, (i+idx)))
                tempStr += " " + listOfWord[idx+i]
        
        if flag == 1 :
            break           
        newWord.append(tempStr)

    #sorting newWord list ahead of making dictionary of wordcounting
    #newWord.sort()
    
    return newWord


# @ function : wordcounting of nGram
# input : list of nGram
# ouput : dictionary of wordcounting 
# my case is also dicionary is sorted.
def wordCounting (nGram) :
    nDic = {}
    
    for idx, var in enumerate(nGram) :
        if nDic.get(var) == None : 
            nDic[var] = 1
        else :
            nDic[var] += 1

    return nDic




# @ intial fucntion in if __name__ == "main" :
# a sequance of this program. 
def main () :
    testPath = "C:\\Users\\hyunyoung2\\corpus\\RAW2169-CORE.txt"
    timerStr = ["====== recommendation system starts ======\n",
                "====== readFile function is done :",
                "====== removal of specialchar function is done :",
                "====== tokenization function is done :",
                "====== nGram is done :",
                "====== wordcounting is done :"]
    
    print (timerStr[0]) # start of this program
    
    begin = time.clock()
    tempStr = readFile(testPath)
    end = time.clock()
    elapsedTime = end - begin 
    print (timerStr[1], elapsedTime, "Seconds ======\n") # end of IO of a file
    #print (tempStr)      

    begin = time.clock()
    tempStr1=removalOfSpecialChar(tempStr)
    end = time.clock()
    elapsedTime = end - begin 
    print (timerStr[2], elapsedTime, "Seconds ======\n") # end of removal of specialChar
    #print (tempStr1)
    
    begin = time.clock()
    tempStr2=tokenization(tempStr1)
    end = time.clock()
    elapsedTime = end - begin 
    print (timerStr[3], elapsedTime, "Seconds ======\n") # end of tokenization
    #print (tempStr2)  

    begin = time.clock()
    tempStr3=nGram(tempStr2)
    end = time.clock()
    elapsedTime = end - begin 
    print (timerStr[4], elapsedTime, "Seconds ======\n") # end of wordcouting
    #print (tempStr3)    

    begin = time.clock()
    tempStr4=wordCounting(tempStr3)
    end = time.clock()
    elapsedTime = end - begin 
    print (timerStr[5], elapsedTime, "Seconds ======\n") # end of wordcouting
    #print (tempStr4)  
    
    
    
    
    
# @ if statement for execution of this file   
if __name__ == "__main__" : 
    # just from Unigram to fiveGram
    # idx(0) : Unigram ... idx(4) fiveGram
    
    main()
