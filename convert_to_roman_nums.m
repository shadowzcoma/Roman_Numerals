clc; clear; close all;

numArabic = 99999;


C_10 = ['I', 'X', 'C', 'M', 'x', 'c'];
C_5 = ['V', 'L', 'D', 'v', 'l', 'd'];

txtRoman = '';
tmpArabic = numArabic;

if numArabic < (10^(length(C_10)-1))
    for k = length(C_10) : -1 : 0
        tmpVal = floor(tmpArabic / 10^k);
        tmpRoman = '';
        switch tmpVal
            case num2cell(1 : 3)
                tmpRoman = repmat(C_10(k+1),1,tmpVal);
            case 4
                tmpRoman = [C_10(k+1) C_5(k+1)];
            case num2cell(5 : 8)
                tmpRoman = [C_5(k+1) repmat(C_10(k+1),1,(tmpVal-5))];
            case 9
                tmpRoman = [C_10(k+1) C_10(k+2)];
        end
        txtRoman = [txtRoman tmpRoman];
        tmpArabic = tmpArabic - (tmpVal * 10^k);
    end
    disp([num2str(numArabic) ' --> ' txtRoman]);
else
    disp('Unsupported number')
end

