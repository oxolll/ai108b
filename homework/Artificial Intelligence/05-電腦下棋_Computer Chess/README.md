# 電腦下棋(Computer Chess)

## Introduction
要使電腦下棋，有三個點要考量，第一個是盤面的表達，第二個是評估函數，第三個是搜尋技巧。

● 盤面表達 ：用一個陣列代表盤面，使用字元代表棋子。\
● 評估函數 ：用函數來評估某個盤面的分數。\
● 搜尋策略 ：可以利用 Min-Max 演算法 及 Alpha-Beta Cut 修剪法優化並設想後面的情況，自我對局，將相對優的策略回傳。

## Algorithm
### 極小化極大演算法(Minimax, MinMax or MM)
該演算法是一個零總和演算法，一方在可選的選項中選擇最有優勢的選擇，另一方則選擇對對手最不利的方法。

### Alpha-beta修剪法(Alpha-beta pruning)
一種對抗性搜尋演算法，當演算法評估某策略的後續走法比之前策略的還差時，停止該策略的後續發展。\
該演算法和極小化極大演算法所得結論相同，且剪去了不影響最終決定的分枝，優化效能。

## Reference

[參考1](https://misavo.com/blog/%E9%99%B3%E9%8D%BE%E8%AA%A0/%E6%9B%B8%E7%B1%8D/%E4%BA%BA%E5%B7%A5%E6%99%BA%E6%85%A7/05-%E9%9B%BB%E8%85%A6%E4%B8%8B%E6%A3%8B)\
[極小化極大演算法(Minimax, MinMax or MM)](https://zh.wikipedia.org/wiki/%E6%9E%81%E5%B0%8F%E5%8C%96%E6%9E%81%E5%A4%A7%E7%AE%97%E6%B3%95)\
[Alpha-beta修剪法(Alpha-beta pruning)](https://zh.wikipedia.org/wiki/Alpha-beta%E5%89%AA%E6%9E%9D)
