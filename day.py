import datetime
x = datetime.datetime.now()
day = x.strftime("%A")
days={'Sunday':0, 'Monday':1, 'Tuesday':2, 'Wednesday':3, 'Thursday':4,'Friday':5,'Saturday':6}
day_no = days[day]
vac = input(" Type Yes if vacation ,otherwise type No :")
#day_no = int(input(" Enter day 0-S,1-M,2-T,3-W,4-T,5-F,6-S :"))
if vac == 'No' :
    if 1<= day_no <=6 :
        print(" work Alarm Time is 7.00")
    else:
        print("work Alarm Time is 10.00")
else:
    if 1<= day_no <=6 :
        print("vac Alarm Time is 10.00")
    else:
        print("vac Alarm is Off")
    

