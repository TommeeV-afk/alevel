#Initialize queue
foq = 0
eoq = -1
num_in_q = 0
max_q = 6
my_q = [None] * max_q

def add_to_q(item):
    global eoq, num_in_q, my_q
    if num_in_q < max_q:
        eoq = (eoq + 1)% max_q
        my_q[eoq] = item
        num_in_q = num_in_q + 1

def remove_from_q():
    global foq,eoq,num_in_q,my_q
    if num_in_q > 0:
        item = my_q[foq]
        num_in_q = num_in_q -1
        if num_in_q == 0:
            foq = 0
            eoq = 1
        else:
            foq = (foq+1)%max_q
        return item

add_to_q("A")
add_to_q("B")
print(remove_from_q())
print(remove_from_q())
print(remove_from_q())