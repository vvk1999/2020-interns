import json

f = open("data.json")
data = json.load(f)


currency1 = 'INR'
currency2 = 'GBP'
start_date = '2019-01-01'
end_date = '2019-01-31'

if start_date > end_date :
    start_date,end_date = end_date,start_date

max_rate1 = max_rate2 = 0.00
min_rate1 = min_rate2 =10000000

for date in sorted(data['rates']):
    rate1 = float(data['rates'][date][currency1])
    rate2 = float(data['rates'][date][currency2])
    if rate1!= 0.0 or rate2!=0.0:
        if start_date <= date and end_date >= date :
            
            if min_rate1 > rate1:
                min_rate1 = rate1
            if max_rate1 < rate1:
                max_rate1 = rate1

            if min_rate2 > rate2:
                min_rate2 = rate2
            if max_rate2 < rate2:
                max_rate2 = rate2



units = 100
n = 0
j1 = j2 = 1
while(n <= units):
    n = min_rate1 * 0.1 * j1
    j1 += 1
n = 0
while(n <= units):
    n = min_rate2 * 0.1 * j2
    j2 += 1
#print(j)
#units = 30

print("graph of "+currency1+" and "+currency2+" exchange rates against EUR from "+start_date+" to "+end_date+" Graph starts from "+str(min_rate1*0.90)+currency1+" and "+str(min_rate2*0.9)+currency2)
print("-"*100+">")

for date in sorted(data['rates']):
    if start_date <=  date and end_date >=  date :
        rate1 = float(data['rates'][date][currency1])
        rate2 = float(data['rates'][date][currency2])
        if rate1 !=  0 or rate2 != 0 :
            print(date+" |"+"▇"*int((rate1-min_rate1*0.99)*j1)+" "+str(rate1))
            print("          "+" |"+"▇"*int((rate2-min_rate2*0.99)*j2)+" "+str(rate2)+"\n")

'''unit = 0.1
scale = 10
graphics = "▇"

for i in range(1,scale):
    graphics += graphics

start_rate = min_rate
dic={}

#converting rate into integer frequency
for date in sorted(data['rates']):
    if rate!= 0.0:
        if start_date <= date and end_date >= date :
            rate = float(data['rates'][date][currency])
            freq = (rate - start_rate) // unit
            dic[date]=(freq,rate)
            print(date+" -> "+str(rate)+" "+str(freq/10))

print("graph of "+currency+" exchange rate against EUR from "+start_date+" to "+end_date)
print("-"*100+">")

for k in dic :
    print(k + " |" + graphics * int(dic[k][0]) + " " + str(dic[k][1]))'''
    
    
