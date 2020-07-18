import json

f=open("data.json")

data=json.load(f)



start='2019-01-01'
end='2019-01-31'

print(start+"\n"+end)

for i in sorted(data['rates']):
    if start<=i and end>=i:
        print(i)
        print("="*int(data['rates'][i]['INR']))
        print("\n")
