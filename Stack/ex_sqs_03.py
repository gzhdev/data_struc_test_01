from Stack.ex_sqs_01 import SqStack


def isPalindrome(str):
    s = SqStack(100)
    for i in str:
        s.push(i)
    for i in str:
        if s.pop() != i:
            print("该单词不是回文单词")
            break
    if s.isEmpty():
        print("该单词是回文单词")


str0 = "ababa"
isPalindrome(str0)