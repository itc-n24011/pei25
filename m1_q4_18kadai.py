phrase = 'PythonProgramming'
list_p = []
for p in phrase:
        if p not in list_p: # 同じ文字が2回以上出た場合、最初の1回しかリストに入れないため、list_p には重複のない文字だけが残ります。
            list_p.append(p)
print(len(phrase) - len(list_p)) # 元の文字列の長さから重複を除いた文字数を引くことで、重複していた文字の数を求めています。
for p in list_p:
     print(p, end="")
print() # 改行のみ
