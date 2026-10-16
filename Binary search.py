def binary(list,number):
    low,high = 0,len(list)-1
    while low <= high:
        mid = (low + high) // 2
        if list[mid] == number:
            print("found")
            return mid
            
        elif list[mid] <= number:
            low = mid+1
        else:
            high = mid-1
    return -1






list = [1,2,3,4,5,6,7,8,9,10]
number = int(input("enter number"))
foundAt = binary(list,number)
if foundAt != -1:
    print(foundAt)
else:
    print("not found")