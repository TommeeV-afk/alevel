
def insertion (lis):
    for i in range(1,len(lis)):
        store = lis[i]
        j = i-1
        while j >= 0 and store < lis[j]:
            lis[j+1] = lis[j]
            j = j-1
            print(lis)
        lis[j+1] = store
        
        print(lis)



lis = [5,6,4,3,8,9,2]
insertion(lis)
