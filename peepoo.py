
def bubble(theArray):
    swapped = True
    passes = 0
    while swapped == True:
        swapped = False
        for i in range (0,len(theArray)-1-passes):
            if theArray[i] < theArray[i+1]:
                temp = theArray[i]
                theArray[i] = theArray[i+1]
                theArray[i+1] = temp
                swapped = True
        passes = passes + 1
    return theArray



done = bubble(theArray)

print(done)