def adjust_recipe(recipe_kosaji, recipe_servs, cook_servs):
    # 作る人数に応じて小さじの量を調整
    adjust_kosaji = recipe_kosaji * cook_servs / recipe_servs
    return adjust_kosaji

def round_kosaji(adjust_kosaji):
    int_part = int(adjust_kosaji)
    frac_part = adjust_kosaji - int_part   # 小数部分
    if frac_part >= 0.5:
        return str(int_part) + '.5'
    else:
        return str(int_part)

recipe_servs = int(input('レシピは何人前?: '))

saji_type = ''
while saji_type not in ['L', 'S']:
    saji_type = input('レシピのさじの種類は？ (大さじはL, 小さじはS) : ')

saji_name = '大さじ' if saji_type == 'L' else '小さじ'
recipe_saji = float(input(f'レシピは{saji_name}何杯？: '))

cook_servs = int(input('作る料理は何人前？: '))

# 大さじ(L)なら小さじ換算（1L = 小さじ3杯）
recipe_kosaji = recipe_saji * 3 if saji_type == 'L' else recipe_saji

adjust_kosaji = adjust_recipe(recipe_kosaji, recipe_servs, cook_servs)

# 大さじに戻す（小さじ3杯 = 大さじ1杯）
cook_oosaji = adjust_kosaji // 3
adjust_kosaji = adjust_kosaji % 3  # 残りを小さじへ

print(f'{cook_servs}人前では, 大さじが{cook_oosaji:.0f}杯と 小さじが{round_kosaji(adjust_kosaji)}杯です。')

