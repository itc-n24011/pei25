a = 17
b = 5
dm = divmod(a, b)      # (3, 2) → 17 ÷ 5 の商と余り
p = pow(dm[0], dm[1])  # 3^2 = 9
all_num = [a, b, dm[0], dm[1], p]
print(all_num)          # リストの中身を確認
min_all = min(all_num)
max_all = max(all_num)
sum_all = sum(all_num)
print(f'{min_all}, {max_all}, {sum_all}')

