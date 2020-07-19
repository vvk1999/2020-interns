import json

f=open("data.json")

data=json.load(f)


cur='INR'
start='2019-01-01'
end='2019-01-31'

#print(start+"\n"+end)

maxV=0.00
minV=10000000

for i in sorted(data['rates']):
    val=float(data['rates'][i][cur])
    if val!=0.0:
        if start<=i and end>=i :
            #print(i+" "+str(val))
            if minV > val:
                minV=val
            if maxV < val:
                maxV=val

#print(str(minV)+"\n"+str(maxV))
minV=minV-0.05*minV
rng=maxV-minV

units=30

print("graph of "+cur+" exchange rate against EUR from "+start+" to "+end)
print("-"*100+">")

for i in sorted(data['rates']):
    if start<=i and end>=i :
        val=float(data['rates'][i][cur])
        if val != 0 :
            print(i+" |"+"▇"*int((val-minV)*10)+" "+str(val))
