# Example files

## be careful

  In case of RAW2169-CORE-test, you shoud be careful that this tess is implemented on window 10 with spyder 3.1.2 and python 3.6
  
  So, probable, when you run [A_B_X_C_D.py](https://github.com/hyunyoung2/Recommending_System/blob/master/Python/3.6/A_B_X_C_D.py)
  
  Encoding problem might happen in particular on **MAC_OS, Linux** and so on.
  
  Then, you use iconv tool as followings
  
  > $ iconv -c -s -f "euckr" -t "utf-8" input.txt > output.txt
  
  For example, the simple way to use this iconv tool as follow : 
  
  > iconv -f <source format> -t <target foramt> source_file > target_file   
  > cp949 encoded to utf8 like :
  > iconv -f cp949 -t utf-8 source.txt > target.txt     
  > In order to check list of encoding iconv tool support   
  > iconv -l  
  
  **BUT,** basically, When you use this tool,iconv. you want to use simply, type in like this :
  
  > $ iconv -f "euckr" -t input.txt > output.txt    
  
  > \-f : the encoding of input file    
  > \-t : the encoding of output file 
  
## Reference
 
  - http://cafe.naver.com/nlpk/23
  
