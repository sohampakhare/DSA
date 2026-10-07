arr=[]
n=int(input("enter number of element"))

for i in range (n):
    ele=int(input(f"enter {i+1}element"))
    arr.append(ele)
zero=[]
newarr=[]
for i in arr:
    if i== 0:
        zero.append(0)
    else:
        newarr.append(i)

newarr=newarr+zero
print(newarr)