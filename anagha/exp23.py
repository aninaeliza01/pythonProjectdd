str=str(input("enter the string:"))
dic={}
for n in str:
    if n in dic:
        dic[n]+=1
    else:
        dic[n]=1
print(dic)
print("character frequency:")
for x,y in dic.items():
    print(x,y)