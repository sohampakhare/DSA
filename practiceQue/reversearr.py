arr=[]
n=int(input("enter number of element"))

for i in range (n):
    ele=int(input(f"enter {i+1}element"))
    arr.append(ele)

print("original string ",arr)
for i in range(len(arr)-1,-1,-1):
    print(arr[i],end=" ")