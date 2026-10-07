#in aar search element is present in arr or not and show is position and element
arr=[]
n=int(input("enter number of element"))

for i in range (n):
    ele=int(input(f"enter {i+1}element"))
    arr.append(ele)
    
s=int(input("enter a number for searching"))

for index,i in enumerate(arr):
    if i==s:
        print(f" {i+1}element is present at {index} position  ")
        break;

    else:
         print("element is not present  ")
         