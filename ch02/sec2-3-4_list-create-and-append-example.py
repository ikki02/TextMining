# -*- coding: utf-8 -*-
# sec2.3.4  いろいろな型が用意されている　リスト
s = [] #              ←要素が1つもない、空のシーケンスを作る
for u in range(5): #  ←uはrange(5)（つまり[0, 1, 2, 3, 4]）を順に取る
    s.append(u*2)  #  ←u*2をリストに追加する
print(s)           #  ←結果は[0, 2, 4, 6, 8]
