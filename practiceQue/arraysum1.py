l=[]
sum=0
n=int(input("enter  num how many element you enter : "))


for i in range(n):
    e=int(input(f"enter { i} elent : "))
    l.append(e)

print(l)
for i in l:
    sum+=i
print("sum is ",sum)

