# -*- coding: utf-8 -*-

"""
Created on Thu Jun 15 15:19:38 2017

@author: hyunyoung2
"""

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

# -- functions to deal with inputstring on command like A B X C D

# @ function : 'X' uppercase change to lowercase
# in spyder, I made it 
# input : input string that you want to look for including 'x' or 'X'
# output : changed string uppercase into lowercase about 'X'
def upperCaseToLowerCase (inputStr) :
    
    if "X" in inputStr :
       return inputStr.replace("X", "x")
    

# @ function : check if inputstring on command includes 'x'
# input : inputstring including 'x'
# ouput : idx of 'x', if there is not, return None object
def isIncludingX (inputStr) :
    
    if "x" in inputStr :
        return inputStr.index("x")
    else :
        return None

# @ function : seperate inputstring into three types
# first : A B X mode
# seconde :  X C D mode 
# third : A B X C D mode
# input : list of inputstring on command which is what user are looking for as patter like A B X C D
# ouput : list including each of those mode(first, seconde, third)
  
def seperateMode (inputStr) :
    # tempList is 2 matrixes with two Lists
    tempList = []
    tempLen = len(inputStr)
    
    xIdx = isIncludingX(inputStr)
    
    if xIdx == None :
        print ("inputString(", inputStr, ") doesn't have 'x' or 'X' ")
        return 
    
    # only A B x
    if xIdx == tempLen-1 :
        ABx = inputStr[0:xIdx+1]
        tempList.append(ABx.split())
        tempList.append(None)
        tempList.append(None)
    # only x C D 
    elif xIdx == 0 :
        xCD = inputStr[xIdx:tempLen]
        tempList.append(None)
        tempList.append(xCD.split())
        tempList.append(None)
    else :
        ABx = inputStr[0:xIdx+1]
        xCD = inputStr[xIdx:tempLen]
        tempList.append(ABx.split())
        tempList.append(xCD.split())
        tempList.append(inputStr.split())
    
    # to check if this function work well
    #print(inputStr)
    
    #for idx, var in enumerate(tempList) :
        #print (var)
    
    return tempList 


# -- specific function to operate as each mode, [[A B X], [X C D], [A B X C D]]

# @ function :  X A B 
# input : list of  nGram from bigram to fivegram and [A B X], plus length of [A B X]
# output : ??? 
def modeXAB (nGramDict, rightSideStr) :
    # the same list 
    totalSameList = []
    
    # List length
    lenOfrightStr = len(rightSideStr)
    
    if lenOfrightStr == 1 : 
        print ("we cannot find out it!! because the str you want to search for ", rightSideStr)
        return 
    
    while lenOfrightStr > 1 :
        tempStr = []
        maxNumber = 0
        for idx, var in nGramDict[lenOfrightStr-2].items() :
                dict_key = []
                dict_key.extend(idx.split())
                if dict_key[1:lenOfrightStr] == rightSideStr[1:lenOfrightStr] :
                    #print ("if :", dict_key[1:lenOfrightStr], leftSideStr[1:lenOfrightStr], var)
                    if maxNumber <= var :
                        if maxNumber < var :
                            totalSameList.clear()
                            
                        tempStr = dict_key
                        maxNumber = var
                        totalSameList.append((rightSideStr[0:lenOfrightStr],tempStr,maxNumber))
        if tempStr == [] :
            print ("======== ", rightSideStr[0:lenOfrightStr] ," ============")
            print ("we can search for nothing to bs similar to ", rightSideStr[0:lenOfrightStr])
        else :
            print ("======== ", rightSideStr ," ============")
            print (rightSideStr[0:lenOfrightStr], ", Count : ", tempStr, ",", maxNumber)
    
        lenOfrightStr -= 1
    
    #print ("===for statement====")
    
    #for idx, var in enumerate(samelist) : 
        #print ("\n======== ", rightSideStr ," ============\n")
        #print (var[0], ", Count : ", var[1], ",", var[2]
            
    
    return True


# @ function :  X C D
# input : list of  nGram from bigram to fivegram and [X C D], plus length of [X C D] 
# output : ??? 
def modeXCD (nGramDict, leftX, lenOfLeftX) :
    # the same list 
    outputList = []
    maxNumber = 0

    for idx, var in nGramDict[lenOfLeftX-2].items() :
        dict_key = []
        dict_key.extend(idx.split())
        if dict_key[1:lenOfLeftX] == leftX[1:lenOfLeftX] :
            #print ("for test, dict_key : ", dict_key)
            #print ("rightX : ", rightX)
            if maxNumber <= var :
                if maxNumber < var :
                    #print ("outputList.clear()")
                    #print (outputList)
                    maxNumber = var
                    outputList.clear()
                
                outputList.append((var, dict_key))
    
    if outputList == [] :
        print ("the same sting doesn't exist for", leftX, "\n")
    else :
        print ("======= target :", leftX, "=======")
        for idx, var in enumerate(outputList) :
            print ("(string , count) : (", var[1]," ,", var[0], ")")
            print ("x : ", var[1][0]) 
            
    # if you want to return the result of modeXCD 
    # use outputList
    return True    

# @ function : call function in main function for X C D
# input : list of  nGram from bigram to fivegram
# output : ??? 

def XCD (nGramDict, leftX) :
    
     # List length
    lenOfleftX = len(leftX)
    
    if lenOfleftX == 1 : 
        print ("we cannot find out it!! because the str you want to search for ", lenOfleftX, "\n")
        return 
    
    while lenOfleftX > 1 :
        modeXCD(nGramDict, leftX[0:lenOfleftX], lenOfleftX)
        lenOfleftX -= 1
        
# @ function :  A B X C D

# @ intial fucntion in if __name__ == "main" :
# a sequance of this program. 
def main () :
    testPath = "C:\\Users\\hyunyoung2\\corpus\\RAW2169-CORE-test.txt"
    timerStr = ["====== recommendation system starts ======\n",
                "====== readFile function is done :",
                "====== removal of specialchar function is done :",
                "====== tokenization function is done :",
                "====== nGram is done :",
                "====== wordcounting is done :",
                "====== upperCaseToLowerCase is done :",
                "====== seperateMode is done :",]
    nGramList = []
    
    print (timerStr[0]) # start of this program
    
    begin = time.clock()
    tempStr = readFile(testPath)
    end1 = time.clock()
    elapsedTime = end1 - begin 
    print (timerStr[1], elapsedTime, "Seconds ======\n") # end of IO of a file
    #print (tempStr)      

    tempStr1=removalOfSpecialChar(tempStr)
    end2 = time.clock()
    elapsedTime = end2 - end1 
    print (timerStr[2], elapsedTime, "Seconds ======\n") # end of removal of specialChar
    #print (tempStr1)
    

    tempStr2=tokenization(tempStr1)
    end3 = time.clock()
    elapsedTime = end3 - end2 
    print (timerStr[3], elapsedTime, "Seconds ======\n") # end of tokenization
    #print (tempStr2)  
    
    # document is divided into between 2 gram and 5 gram 
    # each of nGram is put into nGramList
    # nGramList[0] : bigram in other word, nGramList[idx] ->  idx + 2 gram
    for i in range(1,5) :
        begin = time.clock()
        tempList2 = nGram(tempStr2, i+1) # this bigram 
        end4 = time.clock()
        elapsedTime = end4 - begin
        print (i+1,"Gram",  timerStr[4], elapsedTime, "Seconds ======\n") # end of nGram
        dict_return = wordCounting(tempList2)
        end5 = time.clock()
        elapsedTime = end5 - end4 
        print (i+1, "Gram", timerStr[5], elapsedTime, "Seconds ======\n") # end of wordcouting
        nGramList.append(dict_return)
    
    #tempStr3=nGram(tempStr2)
    #end4 = time.clock()
    #elapsedTime = end4 - end3 
    #print (timerStr[4], elapsedTime, "Seconds ======\n") # end of nGram
    #print (tempStr3)    

    #tempStr4=wordCounting(tempStr3)
    #end5 = time.clock()
    #elapsedTime = end5 - end4 
    #print (timerStr[5], elapsedTime, "Seconds ======\n") # end of wordcouting
    #print (tempStr4)  
    
    testInputString = "그분들의 뜻이 X 있는지 공부하고"
    
    print("inputString : ", testInputString, "\n")
    tempStr5=upperCaseToLowerCase(testInputString)
    end6 = time.clock()
    elapsedTime = end6 - end5 
    print (timerStr[6], elapsedTime, "Seconds ======\n") # end of upperCaseToLowerCase
    #print (tempStr5)
    
    tempStr6 = seperateMode(tempStr5)
    end6 = time.clock()
    elapsedTime = end6 - end5 
    print (timerStr[7], elapsedTime, "Seconds ======\n") # end of wordcouting
    print(tempStr6)
    
    # always keep in mind, tempStr6 is [[A B X], [X C D], [A B X C D]]
    print ("\nstart to find out the result of every mode which [A B X], [X C D], [A B X C D]\n")
    
    print ("\n====== below is mode [A B X] which is", tempStr6[0], "======\n")
    # mode : A B X
    modeXAB (nGramList, tempStr6[0])
    
    
    # mode :  X C D
    print ("\n====== below is mode [X C D] which is", tempStr6[1], "======\n")
    XCD (nGramList, tempStr6[1])
    
    # mode : A B X C D
    
# @ if statement for execution of this file   
if __name__ == "__main__" : 
    # just from Unigram to fiveGram
    # idx(0) : Unigram ... idx(4) fiveGram
    
    main()
