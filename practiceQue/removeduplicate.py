#removing a duplicate element s from array

arr=[]
n=int(input("enter number of element"))

for i in range (n):
    ele=int(input(f"enter {i+1}element"))
    arr.append(ele)
uniele=[]
for i in arr:
    if i not in uniele:
        uniele.append(i)
print(uniele)