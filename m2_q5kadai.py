names = ['鈴木太郎', '田中花子']
print(names[-2])

list_a = [12,9,13,3,7,10]
list_b = []
for i in list_a:
    list_b.append(int(i / 2 + 4))
print(f'私は{list_b[4]}歳です。')

month = 0
for i in list_a[-4:-2]:
    month += int(i / 2)
day = (list_a[2] + 30) // 2
print(f'{names[1]}の誕生日:{month}月{day}日')

list_c = []
for i in range(0, 12,2):
    if i % 3 == 2:
        list_c.pop()
    else:
        list_c.append(i)
print(f'{names[-1][-2:]}の誕生日:{list_c[0]}月{list_c[1]}日')

names.append(names[1][0:2])
names += ['小山田明子', '小森鈴太郎']

total = 0
for s in names:
    if s.startswith('田'):
        total += 1
    elif s.find('鈴') > 0:
        total += s.find('鈴')
    elif len(s) > 4:
        total += len(s)

print(total)

name_kadai = "小山田花子"
m_kadai = 10
d_kadai = 13
print(f"課題:{name_kadai}の誕生日:{m_kadai}月{d_kadai}日")
