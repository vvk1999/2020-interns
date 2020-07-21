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



units = 100
n = 0
j = 1
while(n <= units):
    n =min_rate*0.1*j
    j += 1
print(j)
#units = 30

print("graph of "+currency+" exchange rate against EUR from "+start_date+" to "+end_date)
print("-"*100+">")

for date in sorted(data['rates']):
    if start_date <=  date and end_date >=  date :
        rate = float(data['rates'][date][currency])
        if rate !=  0 :
            print(date+" |"+"▇"*int((rate-min_rate*0.99)*j)+" "+str(rate))
    
