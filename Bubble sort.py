lis = [5,6,4,3,8,9,2]

def bubble(lis):
    swapped = True
    passes = 0
    while swapped == True:
        swapped = False
        for i in range (0,len(lis)-1-passes):
            if lis[i] > lis[i+1]:
                temp = lis[i]
                lis[i] = lis[i+1]
                lis[i+1] = temp
                swapped = True
        passes = passes + 1
    return lis

print(lis)

lis = bubble(lis)

print(lis)