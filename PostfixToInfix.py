"""
Test Cases:

postfix:
A B + C - D +
infix: A + B - C + D

postfix:
A B * D /
infix: A * B / D

postfix:
A B C * D * +
infix: A + B * C * D

postfix:
A B - C D - +
infix: (A - B) + (C - D)

postfix:
A C * D - B * D A / + C -
infix: (A * C - D) * B + ( D / A ) - C

postfix:
A B C * + D +
infix: A + B * C + D

postfix:
A -
infix: - A

postfix:
A B ^ C +
infix: A ^ B + C

postfix:
A B C ^ ^
infix: A ^ (B ^ C)

postfix:
A B C D ^ * ^
infix: A ^ (B * C ^ D)
"""
from Stack import ArrayStack

def main():
    word = input("Postfix expression: ").replace(" ", "")
    s = ArrayStack()

    for char in word:
        if char.isalpha():
            s.push(char)
        else: 
            if not s.isEmpty():
                temp = s.pop().getValue()

            if not s.isEmpty():
                string = s.pop().getValue() + " " + char + " " + temp
            else:
                string = char + " " + temp

            s.push(string)
 
    print("Infix expression: " + s.pop().getValue())

if __name__ == "__main__":    
    main()