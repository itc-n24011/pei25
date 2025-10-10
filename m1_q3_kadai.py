a = 12
b = 5
print(b - a) # (12)
print(abs(-7)) # (13)
print("{0:08b}".format(64)) # (14)
c = [2, 7, 15, 12, 9]
c.sort(reverse=True)
print(c) # (15)
print(c[1:4]) # (16) 
print(f'{(a - b) / c[3]:-<8.1f}')
# ↑　幅八文字、左寄せ、小数点以下一桁、余った右側のスペースを'_'(アンダーバー）>で埋める

