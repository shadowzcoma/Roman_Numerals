import math
import numpy as np
import os

exitCond = 0

while (exitCond == 0):
    print('')
    numArabic = int(input("Please enter a number [0-quit]: "));
    #os.system('cls')
    
    if (numArabic == 0):
        exitCond = 1
    
    C_10 = ['I', 'X', 'C', 'M', 'x', 'c']
    C_5 = ['V', 'L', 'D', 'v', 'l', 'd']

    txtRoman = ' '
    tmpArabic = numArabic

    if numArabic < 10**len(C_10):
        for k in range(len(C_10), -1 , -1):
            #print('Temp Arabic : ', tmpArabic);
            tmpVal = math.floor(tmpArabic / 10**k);
            tmpRoman = '';
            
            if tmpVal in [1,2,3]:
                tmpRoman = C_10[k]*tmpVal
                
            if tmpVal in [4]:
                tmpRoman = C_10[k] + C_5[k]
            
            if tmpVal in [5]:
                tmpRoman = C_5[k]
            
            if tmpVal in [6,7,8]:
                tmpRoman = C_5[k] + C_10[k]*(tmpVal-5)
                
            if tmpVal in [9]:
                tmpRoman = C_10[k] + C_10[k+1]

            txtRoman = txtRoman + tmpRoman;
            tmpArabic = tmpArabic - (tmpVal * 10**k);
        
        print(numArabic, ' --> ', txtRoman);
    else:
        print('Unsupported number')
