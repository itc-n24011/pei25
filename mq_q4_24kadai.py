animals = ['Dog', 'Cat', 'Rabbit', 'Horse', 'Dolphin']
total = 0
for animal in animals:
    print(total)
    from_D = animal.startswith('D') #animalが'D'で始まる場合はTrue、そうでない場合はFalseを返す
    is_long = len(animal) > 5 #animalの文字数が6文字以上ならTrue
    if from_D and is_long:
        break #どちらもTrueならbreak
    elif not from_D and is_long:
        total += animal.find('b') #最初に'b'が現れるインデックスを返し、見つからなければ-1を返す
    else:
        total += len(animal)
print(total)
