import json

f = open("data.json")
data = json.load(f)


currency = 'INR'
start_date = '2019-01-01'
end_date = '2019-01-31'



max_rate = 0.00
min_rate = 10000000

for date in sorted(data['rates']):
    rate = float(data['rates'][date][currency])
    if rate!= 0.0:
        if start_date <= date and end_date >= date :
            
            if min_rate > rate:
                min_rate = rate
            if max_rate < rate:
                max_rate = rate



unit = 0.1
scale = 1
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
    print(k + " |" + graphics * int(dic[k][0]) + " " + str(dic[k][1]))
    
    
