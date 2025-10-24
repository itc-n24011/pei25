a = 2                # 最初に変数aに2を代入
list_a = []          # 空のリストを用意

for i in range(6):   # 6回繰り返す（要素が6個）
    list_a.append(a)  # 現在のaの値をリストに追加（appendで末尾に要素を加える）
    a *= 2            # aを2倍にして次の値を準備

print(list_a)

