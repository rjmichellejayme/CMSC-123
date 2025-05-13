"""
Test Cases:

infix: 
A + B - C + D
postfix: A B + C - D +

infix: 
A * B / D
postfix: A B * D /

infix:
A + B * C * D
postfix: A B C * D * +

infix:
(A - B) + (C - D)
postfix: A B - C D - +

infix:
(A * C - D) * B + ( D / A ) - C
postfix: A C * D - B * D A / + C -

infix:
A + B * C + D
postfix: A B C * + D +

infix:
A ^ B + C
postfix: A B ^ C +

infix:
A ^ (B ^ C)
postfix: A B C ^ ^

infix:
A ^ (B * C ^ D)
postfix: A B C D ^ * ^
"""
from Stack import ArrayStack

def lesserOrEqual(char, top):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    try:
        char_pred = precedence[char]
        top_pred = precedence[top]
        if char_pred <= top_pred:
            return True
        else:
            return False
    except KeyError:
        return False

def main():
    word = input("Infix expression: ").replace(" ", "")
    s = ArrayStack()

    print("Postfix expression: ")
    for char in word:
        if char.isalpha():
            print(char, end = " ")
        elif char == '(':
            s.push(char)
        elif char == ')':
            while(not s.isEmpty()):
                popped = s.pop().getValue()
                if popped == "(":
                    break
                print(popped, end = " ")
        elif s.isEmpty():
            s.push(char)
        else:
            top = s.top().getValue()
            while lesserOrEqual(char, top) and not s.isEmpty():
                popped = s.pop().getValue()
                print(popped, end = " ")
                top = s.top().getValue()
            s.push(char)
    
    while (not s.isEmpty()):
        popped = s.pop().getValue()
        print(popped, end = " ")

if __name__=="__main__":
    main()
