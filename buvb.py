def BubbleSort(Array):
    Passes = 0
    Maxpasses = len(Array) - 1
    Swapped = True
    while Swapped == True and Passes <= Maxpasses:
        Swapped = False
        for i in range(Maxpasses - Passes):
            if Array[i] > Array[i+1]:
                Temp = Array[i]
                Array[i] = Array[i+1]
                Array[i+1]= Temp
                Swapped = True
        Passes = Passes +1

    return Array


A = [7,8,4,2,5]

print(BubbleSort(A))