from Stack.ex_sqs_01 import SqStack


def isMatch(str):
    s0 = SqStack(100)
    s1 = SqStack(100)
    s2 = SqStack(100)
    for c in str:
        if c == '(':
            s0.push(c)
        elif c == ')' and not s0.isEmpty():
            s0.pop()
        elif c == ')' and s0.isEmpty():
            print("括号不匹配")
            return False

        if c == '[':
            s1.push(c)
        elif c == ']' and not s1.isEmpty():
            s1.pop()
        elif c == ']' and s1.isEmpty():
            print("括号不匹配")
            return False

        if c == '{':
            s2.push(c)
        elif c == '}' and not s2.isEmpty():
            s2.pop()
        elif c == '}' and s2.isEmpty():
            print("括号不匹配")
            return False

    if s0.isEmpty() and s1.isEmpty() and s2.isEmpty():
        print("括号匹配")
        return False
    else:
        print("括号不匹配")
        return False


isMatch("{([)(abcd)]}")
