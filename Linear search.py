def linear(list,number):
    for i in range(0,len(list)):
        if number == list[i]:
            print("found")
    print("not found100")


list = [1,5,7,6,8,9]
number = int(input("Enter your number"))
linear(list,number)