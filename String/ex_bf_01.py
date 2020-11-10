from String.ex_sqstr_01 import SqString

s = SqString("abcabcdabcdeabcdefabcdefg")
t = SqString("abc")
i = s.indexOf(t, 0)
if i == -1:
    print("没有符合的子串")
else:
    print("符合要求的子串在%d位" % i)
