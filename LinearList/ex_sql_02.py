from LinearList.ex_sql_01 import SqList


def SQLcombine(sql0, sql1):
    SQLc = SqList(sql0.length() + sql1.length())
    i = 0
    j = 0
    while i < sql0.length() and (j < sql1.length()):
        c = SQLc.length()
        if sql0.get(i) >= sql1.get(j):
            SQLc.insert(c, sql1.get(j))
            j += 1
        else:
            SQLc.insert(c, sql0.get(i))
            i += 1
    while i < sql0.length():
        c = SQLc.length()
        SQLc.insert(c, sql0.get(i))
        i += 1
    while j < sql1.length():
        c = SQLc.length()
        SQLc.insert(c, sql1.get(j))
        j += 1
    '''
    c = 0
    while SQLa.length() > 0 and SQLb.length() > 0:
        if SQLa.get(0) > SQLb.get(0):
            SQLc.insert(c, SQLb.get(0))
            SQLb.remove(0)
        else:
            SQLc.insert(c, SQLa.get(0))
            SQLa.remove(0)
        c += 1
    if sql0.isEmpty() == True and sql1.isEmpty() == False:
        for i in range(0, sql1.length()):
            SQLc.insert(SQLc.length(), sql1.get(i))
    else:
        for j in range(0, sql0.length()):
            SQLc.insert(SQLc.length(), sql0.get(j))
    '''
    return SQLc


SQLa = SqList(9)
SQLb = SqList(10)
a = [0, 2, 4, 6, 8, 10, 11, 12, 15]
b = [1, 3, 5, 7, 9, 10, 13, 56, 98]
for i in range(0, len(a)):
    SQLa.insert(i, a[i])
for i in range(0, len(b)):
    SQLb.insert(i, b[i])
SQLcombine(SQLa, SQLb).display()
