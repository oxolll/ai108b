# 邏輯推論(Logic Reasoning) 

## Introduction

## Theory
### Advantage
### Disadvantages
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

[參考1](https://misavo.com/blog/%E9%99%B3%E9%8D%BE%E8%AA%A0/%E6%9B%B8%E7%B1%8D/%E4%BA%BA%E5%B7%A5%E6%99%BA%E6%85%A7/06-%E9%82%8F%E8%BC%AF%E6%8E%A8%E8%AB%96)\
[參考2]()\
[參考3]()\
[參考4]()\
[參考5]()
