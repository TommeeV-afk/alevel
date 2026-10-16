#varible initialized
head_pointer = 0
tail_pointer = 0
num_items = 0
max_q = 9
QueueArray = 10 * [None]

def Enqueue (item):
    global tail_pointer,num_items, QueueArray
    if num_items == 10:
        return False

    QueueArray[tail_pointer] = item
    if tail_pointer >= max_q:
        tail_pointer = (tail_pointer + 1)% max_q
    else:
        tail_pointer = tail_pointer + 1

    num_items = num_items +1
    return True

def Dequeue():
    global head_pointer, tail_pointer, num_items
    if num_items == 0:
        return "FALSE"
    Item = QueueArray[head_pointer]

    if head_pointer >= max_q:
        head_pointer = 0
    else:
        head_pointer = head_pointer + 1
    num_items = num_items -1
    return Item


for i in range(11):
    data = input("Input a letter")
    if Enqueue(data):
        print("added")
    else:
        print("full")

print(Dequeue())
print(Dequeue())
