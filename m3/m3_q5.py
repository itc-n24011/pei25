list_date = [1, 9, 9, 1, 2, 7]

print(max(list_date) >= min(list_date) * 5)　# 9 >= 5

month = ''
day = ''
for i in list_date[4:5]: # インデックス4の要素だけ
    month += str(i) # '2'を文字列としmonthに追加
for i in list_date[-1:]: # 最後の要素だけ取得
    day += str(i) # '7'を文字列としてdayに追加
print(f'{month:0>2}月 {day:0>2}日') # 右寄せ2桁で 0>埋め

list_a = [] # 空のリスト
list_c = list_date[::-1]
index = 0
while index < len(list_date): # index 0~5で繰り返し
    list_b.append(list_date[index] + list_c[index]) # 対応する要素を足している
    index += 1
print(list_b) # [8, 11, 10, 10, 11, 8]

total = sum(list_date) # 29
if total != 11 and total != 22 and total != 33 and total !=44: # True
    while total > 9:
        new_total = 0
        for i in str(total):
            new_total += int(i)
        total = new_total
print(total)
