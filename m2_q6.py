# 複利計算（元本×10000 をして万円→円に変換）
def fukuri(ganpon, nenri, nensu):
    # 初期残高を計算（万円 → 円）
    zandaka = ganpon * 10000

    # 毎年増加した残高を更新（複利）
    for i in range(nensu):
        zandaka = zandaka * (1 + nenri)

    # 最終残高を整数で返す
    return int(zandaka)


# 単利計算
def tanri(ganpon, nenri, nensu):
    # 初期残高（万円 → 円）
    zandaka = ganpon * 10000

    # 単利は元本に対して毎年一定額の利子がつく
    for i in range(nensu):
        zandaka += ganpon * 10000 * nenri

    return int(zandaka)


# 複利と単利の差を比較する関数
def hikaku(ganpon, nenri, nensu):
    print(f'元本{ganpon}万円、年利{nenri:.0%}で{nensu}年間預けた場合')

    # 円→万円に戻す
    fu = fukuri(ganpon, nenri, nensu) / 10000
    ta = tanri(ganpon, nenri, nensu) / 10000

    print(f'複利の方が {fu - ta:.1f} 万円多く受け取ることができます')


# 受け取りたい利子額まで何年必要か
def hitsuyou_nensu(ganpon, nenri, uketori):
    print(f'年利{nenri:.0%}で利子を{uketori}万円受け取るには')

    # --- 複利 ---
    kaku_f = 0
    year_f = 0
    while kaku_f < uketori * 10000:
        kaku_f = fukuri(ganpon, nenri, year_f + 1) - ganpon * 10000
        year_f += 1

    # --- 単利 ---
    kaku_t = 0
    year_t = 0
    while kaku_t < uketori * 10000:
        kaku_t = tanri(ganpon, nenri, year_t + 1) - ganpon * 10000
        year_t += 1

    print(f'複利で{year_f}年、単利で{year_t}年かかります')


# 動作確認
hikaku(100, 0.05, 10)
hitsuyou_nensu(100, 0.05, 300)

