import random
ArrayData = [[random.randint(1,100) for x in range(10)] for y in range(10)]

ArrayLength = 10
for x in range(ArrayLength):
     for y in range(ArrayLength - 1):
        for z in range(ArrayLength - y - 1):
            if ArrayData[x][z] > ArrayData[x][z+1]:
                TempValue = ArrayData[x][z]
                ArrayData[x][z] = ArrayData[x][z+1]
                ArrayData[x][z+1] = TempValue

def outputsorted(ArrayData):
    for x in range(10):
        empty = ""
        for y in range(10):
            num = str(ArrayData[x][y])
            empty = empty + "|" + num
        print(empty)       

outputsorted(ArrayData)
