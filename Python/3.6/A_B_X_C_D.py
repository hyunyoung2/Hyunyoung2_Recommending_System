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

# @ function : write wordcounting into file


# @ function : remove specailChar 
# input : a string including specialChar
# output : a string without specialChar
def removalOfSpecialChar (inputStr) :
    specialChar = "[!\"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~]"
    
    inputStr = re.sub(specialChar, "", inputStr)
         
    return inputStr



# @ intial fucntion in if __name__ == "main" :
# a sequance of this program. 
def main () :
    testPath = "C:\\Users\\hyunyoung2\\corpus\\RAW2169-CORE-test.txt"
    timerStr = ["====== recommendation system starts ======\n",
                "====== readFile function is done :",
                "====== removal of specialchar function is done :",]
    
    print (timerStr[0]) # start of this program
    begin = time.clock()
    tempStr = readFile(testPath)
    end = time.clock()
    elapsedTime = end - begin 
    print (timerStr[1], elapsedTime, "Seconds ======\n") # end of IO of a file

    print (tempStr)
    print ()
    begin = time.clock()
    tempStr1=removalOfSpecialChar(tempStr)
    end = time.clock()
    elapsedTime = end - begin 
    print (timerStr[2], elapsedTime, "Seconds ======\n") # end of IO of a file
    print (tempStr1)

    
# @ if statement for execution of this file   
if __name__ == "__main__" : 
    # just from Unigram to fiveGram
    # idx(0) : Unigram ... idx(4) fiveGram
    
    main()
