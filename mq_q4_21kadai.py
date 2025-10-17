list_n = [6, 3, 3, 1]
list_s = []

for num in list_n:
    print(num)  # numの値を出力
    if num % 2 == 0:   # 偶数なら
        list_s.append(num // 3)
    elif num % 3 == 0: # 3で割り切れるなら
        list_s.append(num // 1)

print(list_s)  # 最後にlist_sを出力
