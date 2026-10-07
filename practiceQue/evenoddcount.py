#count even and odd element in arry
arr=[]
n=int(input("enter number of element : "))

for i in range(n):
    ele=int(input(f"enter your {i+1} element : "))
    arr.append(ele)
even=0
odd=0
for i in arr:
    if i %2==0:
        even+=1
    else:
        odd+=1
print("total even element is ",even)
print("total odd element is ",odd)