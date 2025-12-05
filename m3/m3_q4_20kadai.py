def check_num(num):
    a = num[1] #'1'
    b = num[-1] #'9'
    c = len(num) == 919 #False
    d = len(num) > 0 #3 > 0つまりTrue

    if a == b and c and d: #False and False and TrueなのでFalse
        print(a * b)
    elif a == b or c or d: #dがTrueなので実行される
        print(b * 2)
    print(type(a))
    print(type(b))
    print(type(c))
    print(type(d))

num = '919'
check_num(num)
