
#Importing the stack class from the general_stack

from General_stack import Stack

#To check the two poped item and next parenthesis are equal
def is_match(p1,p2):
    if p1 =='(' and p2==')':
        return True
    elif p1 == '{' and p2 =='}':
        return True
    elif p1=='[' and p2 == ']':
        return True
    else:
        return False

def is_paren_balanced(parenthesis_string):
    s = Stack()
    is_balanced = True
    index = 0

    #looping through the parenthesis string and adding them to the stack
    while index < len(parenthesis_string) and is_balanced:
        paren = parenthesis_string[index]
        if paren in "({[":
            s.push(paren)
        else:
            top = s.pop()
            if not is_match(top,paren):
                is_balanced = False
        index+=1

    #TO check the stack is empty and Balanced is True
    if s.is_empty and is_balanced:
        return True
    else:
        return False

print(is_paren_balanced("[]"))