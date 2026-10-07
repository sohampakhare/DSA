#smallest num second smallest num largest num and second largest num

arr=[]
n=int(input("enter number of element"))

for i in range(n):
    e=int(input(f"enter {i+1} element "))
    arr.append(e)
lv=arr[0]
sv=arr[0]
for i in arr:
    if i > lv:
        lv=i
    if i < sv:
        sv=i
print(lv,sv)
slv=arr[0]
ssv=arr[0]
for i in arr:
    if i > slv and i <lv:
        slv=i
    if i < ssv and i > sv:
        ssv=i

print("largest value  ",lv)
print(" second largest value  ",slv)
print("smallest  value  ",sv)
print("second smallest value ",ssv)
