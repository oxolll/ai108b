# OOXX遊戲簡介

這是一個圈圈叉叉的遊戲\
使用了minimax演算法進行自我對局尋最佳解\
在這個遊戲內，玩家無法勝利，因為電腦總是尋求最佳解\
也就是在這個勝負當中除了平局，就是電腦獲勝。
## 程式碼
[OOXX_ai.py](https://github.com/oxolll/ai108b/blob/master/homework/hw4-OOXX/OOXX_ai.py) 此為主要專案程式碼\
在顯示表現的程式碼部分同參考資料\
(1)[ai參考](https://github.com/Cledersonbc/tic-tac-toe-minimax/blob/master/py_version/minimax.py)\
(2)[無ai參考](https://www.itread01.com/content/1550310855.html)\
● 主程式架構並無特別變更\
● 刪去了不影響運行的程式碼\
● 修改了大部分主程式碼的內文\
● 更改了資料處理的陣列，由二維陣列修改成使用一維陣列進行運算的模式\
● 對於參考資料的理解為100%\
● 對修改後的程式碼的理解為100%\
[OOXX_noai.py](https://github.com/oxolll/ai108b/blob/master/homework/hw4-OOXX/OOXX_noai.py) 此為練習製作僅使用對局搜尋的程式碼\
● 主程式架構並無特別變更\
● 刪去了不影響運行的程式碼\
● 修改了部分主程式碼的內文\
● 對於參考資料的理解為100%\
● 對修改後的程式碼的理解為100%

## RESULT
以下為對局兩盤，分別是玩家先手(O)、玩家後手(X)

```
$ py OOXX.py 
Choose one icon O(first) or X(second) for you
O
   |   |
   |   |
   |   |
-----------
   |   |
   |   |
   |   |
-----------
   |   |
   |   |
   |   |
Choose one for your next step(1-9)
5
computer turn [X]
   |   |
   |   |
   |   |
-----------
   |   |
   | O |
   |   |
-----------
   |   |
   |   |
   |   |
Your turn! [O]
   |   |
 X |   |
   |   |
-----------
   |   |
   | O |
   |   |
-----------
   |   |
   |   |
   |   |
Choose one for your next step(1-9)
3
computer turn [X]
   |   |
 X |   | O
   |   |
-----------
   |   |
   | O |  
   |   |
-----------
   |   |
   |   |
   |   |
Your turn! [O]
   |   |
 X |   | O
   |   |
-----------
   |   |
   | O |  
   |   |
-----------
   |   |
 X |   |  
   |   |
Choose one for your next step(1-9)
4
computer turn [X]
   |   |
 X |   | O
   |   |
-----------
   |   |
 O | O |
   |   |
-----------
   |   |
 X |   |
   |   |
Your turn! [O]
   |   |
 X |   | O
   |   |
-----------
   |   |
 O | O | X
   |   |
-----------
   |   |
 X |   |
   |   |
Choose one for your next step(1-9)
2
computer turn [X]
   |   |
 X | O | O
   |   |
-----------
   |   |
 O | O | X
   |   |
-----------
   |   |
 X |   |
   |   |
Your turn! [O]
   |   |
 X | O | O
   |   |
-----------
   |   |
 O | O | X
   |   |
-----------
   |   |
 X | X |
   |   |
Choose one for your next step(1-9)
9
   |   |
 X | O | O
   |   |
-----------
   |   |
 O | O | X
   |   |
-----------
   |   |
 X | X | O
   |   |
Game is over
Play again?(y or n)
y
Choose one icon O(first) or X(second) for you
x
computer turn [O]
   |   |
   |   |
   |   |
-----------
   |   |
   |   |
   |   |
-----------
   |   |
   |   |
   |   |
Your turn! [X]
   |   |
   |   |
   |   |
-----------
   |   |
   |   |
   |   |
-----------
   |   |
 O |   |
   |   |
Choose one for your next step(1-9)
3
computer turn [O]
   |   |
   |   | X
   |   |
-----------
   |   |
   |   |  
   |   |
-----------
   |   |
 O |   |
   |   |
Your turn! [X]
   |   |
 O |   | X
   |   |
-----------
   |   |
   |   |
   |   |
-----------
   |   |
 O |   |
   |   |
Choose one for your next step(1-9)
4
computer turn [O]
   |   |
 O |   | X
   |   |
-----------
   |   |
 X |   |
   |   |
-----------
   |   |
 O |   |
   |   |
Your turn! [X]
   |   |
 O |   | X
   |   |
-----------
   |   |
 X |   |
   |   |
-----------
   |   |
 O |   | O
   |   |
Choose one for your next step(1-9)
5
computer turn [O]
   |   |
 O |   | X
   |   |
-----------
   |   |
 X | X |
   |   |
-----------
   |   |
 O |   | O
   |   |
Your turn! [X]
   |   |
 O |   | X
   |   |
-----------
   |   |
 X | X |
   |   |
-----------
   |   |
 O | O | O
   |   |
You lose!
Play again?(y or n)
n
```
## 程式碼解析

### ai_turn()

ai_turn 函式內包含著整個最關鍵的電腦演算法 (minimax)\
在 ai_trun() 中先判斷可下棋盤位置 List 是否為空，或是否有人勝出\
如果沒有則列印當前棋盤，如果是電腦先手，在這裡設計\
以隨機方式下第一手，接著便以 minimax() 來決策後面的下棋位置

```
def ai_turn(c_icon, p_icon):
    depth = len(check_free(theboard))
    if depth == 0 or game_over(theboard):
        return
    
    print(f'computer turn [{c_icon}]')
    drawBoard(theboard, c_icon, p_icon)

    if depth == 9:
        i = choice([0,1,2,3,4,5,6,7,8])
    else:
        move = minimax(theboard, depth, C)
        i = move[0]

    move_(i, C)
```

### minimax()

minimax() 為整個運算的關鍵函示，藉由自我對局，計算分數\
來選擇出最不容易輸的下法\
函式一開始先設定回傳資料的 List，並設定最低值\
接著判斷可下棋盤位置 List 是否為空，或是否有人勝出\
如果有，則計算分數，並回傳分數\
如果沒有，則進行自我對局，使用 check_free 回傳的可下位置 List\
進行盤面修改 (mark)，並再度呼叫 minimax() 進行可能性的評估\
在 minimax() 回傳最佳解後，重置上一點(對應 mark)\
因為 score 回傳的值 (index:0)為 minimax() 在最底層的移動 ，所以得將 cell (欲下的位置) 值導入 score\
最後判斷所有 minimax() 的分數誰相對比較好\
好的則回傳到 move_() 進行移動判斷及移動。

```
def minimax(state, depth, player):
    if player == C:
        best = [-1, -infinity]
    else :
        best = [-1, +infinity]

    if depth == 0 or game_over(state):
        score = evaluate(state)
        return [-1, score]

    for cell in check_free(state):
        
        state[cell] = player
        score = minimax(state, depth-1, -player)
        state[cell] = 0
        score[0] = cell

        if player == C:
            if score[1] > best[1]:
                best = score
        elif player == P:
            if score[1] < best[1]:
                best = score

    return best
```

## 補充
目錄解釋:\
[OOXX_ai.py](https://github.com/oxolll/ai108b/blob/master/homework/hw4-OOXX/OOXX_ai.py) 為使用 minimax() 的程式\
[OOXX_noai.py](https://github.com/oxolll/ai108b/blob/master/homework/hw4-OOXX/OOXX_noai.py) 為僅使用 位置權重的 List 來決定\
[reference_ai.py](https://github.com/oxolll/ai108b/blob/master/homework/hw4-OOXX/reference_ai.py) 為 [ai參考](https://github.com/Cledersonbc/tic-tac-toe-minimax/blob/master/py_version/minimax.py)\
[reference_noai.py](https://github.com/oxolll/ai108b/blob/master/homework/hw4-OOXX/reference_noai.py) 為 [無ai參考](https://www.itread01.com/content/1550310855.html)\
ps: 最近github不太穩，超連結容易出錯，多開幾次應該就可以進入!!
