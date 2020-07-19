import json

f=open("data.json")

data=json.load(f)



start='2019-01-01'
end='2019-01-31'

print(start+"\n"+end)

maxV=0.00
minV=10000000

for i in sorted(data['rates']):
    val=float(data['rates'][i]['INR'])
    if val!=0.0:
        if start<=i and end>=i :
            print(i+" "+str(val))
            if minV > val:
                minV=val
            if maxV < val:
                maxV=val

print(str(minV)+"\n"+str(maxV))
minV=minV-0.1*minV
rng=maxV-minV

units=30

for i in sorted(data['rates']):
    if start<=i and end>=i :
        val=float(data['rates'][i]['INR'])
        if val != 0 :
            print("="*(int(units)//int(val-minV)))
