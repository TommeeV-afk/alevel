base_stack = 0
max_stack = 5
top_stack = -1

my_stack = [None] * max_stack

def push(item):
    global top_stack
    global my_stack
    if top_stack < max_stack - 1:
        top_stack = top_stack + 1
        my_stack[top_stack] = item

def pop():
    global top_stack, my_stack
    if top_stack > -1:
        item = my_stack[top_stack]
        top_stack = top_stack -1
        return item

push("A")
push("B")
push("C")

print(pop())