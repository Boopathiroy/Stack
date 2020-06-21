
from General_stack import Stack

def decimal_binary(num):
    s = Stack()
    while num>0:
        remainder = num % 2
        s.push(remainder)
        num = num//2
    bin_num =""
    while not s.is_empty():
        bin_num+=str(s.pop())
    return bin_num

print(decimal_binary(242))


























