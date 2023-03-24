single = ['Zero','One', 'Two','Three','Four','Five','Six','Seven','Eight','Nine']
double = ['Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']
double_1 = ['','Ten','Twenty','Thirty','Fourty','Fifty','Sixty','Seventy','Eighty','Ninety']

while(True):
    res = ""
    number = input('Enter the number (0-999): ')
    if(len(number)==1):
        res += single[ int(number) ]
    elif len(number)==2:
        text = double_1[int(int(number)/10)]
        if 11 <= int(number) <= 19:
            res += double[ int(number)-11 ]
        else:
            if int(number)%10 == 0:
                res += text
            else:
                res = text + " " + single[ int(number)%10 ]
    elif len(number)==3:
        thr_dig = single[ int(int(number)/ 100) ]
        text = thr_dig + " hundred "
        if int(number)%100 == 0:
            res = text
        else:
            number = str(int(number)%100)
            if 11 <= int(number) <= 19:
                res = text + " and " + double[ int(number)-11 ]
            else:
                ten_dig = double_1[int(int(number)/10)]
                if int(number)%10 == 0:
                    res = text + " and " + ten_dig
                else:
                    res = text + " and " + ten_dig + " " + single[ int(number)%10 ] 
    else:
        print("error")

    print(res,"\n ---------------------")
    
