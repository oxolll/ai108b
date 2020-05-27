# 神經網路(Neural Network)

## Introduction
在機器學習和認知科學領域，是一種仿生物神經網路（特別是大腦）的結構和功能的數學模型或計算模型，用於對函式進行估計或近似。\
大多數情況下人工神經網路能在外界資訊的基礎上改變內部結構，是一種自適應系統，通俗的講就是具備學習功能。\
通過數學統計學的應用可以來做人工感知方面的決定問題（也就是通過統計學的方法，人工神經網路能夠類似人一樣具有簡單的決定能力和簡單的判斷能力

## Theory
通過訓練樣本的校正，對各個層的權重進行校正（learning）而建立模型的過程，稱為自動學習過程（training algorithm）。具體的學習方法則因網路結構和模型不同而不同，常用反傳遞演算法（Backpropagation，以 output 利用一次微分來修正權重）來驗證。

### Advantage
● 具有自學習功能，對於預測有特別重要的意義。\
● 具有聯想存儲功能。\
● 具有高速尋找優化解的能力，利用一個針對某問題而設計的反饋型人工神經網路，發揮電腦的高速運算能力，可能很快找到優化解。

### Disadvantages
● 需要大量資料進行訓練\
● 訓練要求很高的硬體配置\
● 模型處於「黑箱狀態」，難以理解內部機制

## Algorithm
### 梯度下降法(Gradient Descendent) 
梯度就是斜率最大的那個方向，所以梯度下降法，朝著斜率最大的方向走。\
要使用梯度下降法找到一個函數的局部極小值，必須向函數上當前點對應梯度（或者是近似梯度）的反方向的規定步長距離點進行疊代搜索。\
 [捲積神經網路（Convolutional Neural Network, CNN)](https://zh.wikipedia.org/wiki/%E5%8D%B7%E7%A7%AF%E7%A5%9E%E7%BB%8F%E7%BD%91%E7%BB%9C)\
[循環神經網路(Recurrent Neural Network：RNN)](https://zh.wikipedia.org/wiki/%E5%BE%AA%E7%8E%AF%E7%A5%9E%E7%BB%8F%E7%BD%91%E7%BB%9C)\
[生成對抗網路(Generative Adversarial Network, GAN)](https://zh.wikipedia.org/wiki/%E7%94%9F%E6%88%90%E5%AF%B9%E6%8A%97%E7%BD%91%E7%BB%9C)

### 反傳遞算法(Back Propagation) 

#### 第1階段：激勵傳播

每次疊代中的傳播環節包含兩步：\
1. 將訓練輸入送入網絡以獲得激勵響應；\
2. 將激勵響應同訓練輸入對應的目標輸出求差，從而獲得輸出層和隱藏層的響應誤差。
#### 第2階段：權重更新

將輸入激勵和響應誤差相乘，從而獲得權重的梯度；\
將這個梯度乘上一個比例並取反後加到權重上。\
這個比例（百分比）將會影響到訓練過程的速度和效果，因此成為「訓練因子」。梯度的方向指明了誤差擴大的方向，因此在更新權重的時候需要對其取反，從而減小權重引起的誤差。\

反覆循環疊代，直到網絡對輸入的響應達到滿意的預定的目標範圍為止。

## Reference

[參考1](https://www.itread01.com/content/1546431330.html)\
[參考2](https://misavo.com/blog/%E9%99%B3%E9%8D%BE%E8%AA%A0/%E6%9B%B8%E7%B1%8D/%E4%BA%BA%E5%B7%A5%E6%99%BA%E6%85%A7/03-%E7%A5%9E%E7%B6%93%E7%B6%B2%E8%B7%AF)\
[參考3](https://zh.wikipedia.org/wiki/%E4%BA%BA%E5%B7%A5%E7%A5%9E%E7%BB%8F%E7%BD%91%E7%BB%9C)\
[參考4](https://zh.wikipedia.org/wiki/%E6%A2%AF%E5%BA%A6%E4%B8%8B%E9%99%8D%E6%B3%95)\
[參考5](https://zh.wikipedia.org/wiki/%E5%8F%8D%E5%90%91%E4%BC%A0%E6%92%AD%E7%AE%97%E6%B3%95)
