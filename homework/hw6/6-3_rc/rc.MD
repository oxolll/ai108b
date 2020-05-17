# RESULT

RC => C*Derivative(V(t))+V(t)/R \
使用 dsolve() 去解,\
再將答案用 doit() 回傳,
程式碼如下
```
ans = dsolve(C*Derivative(V(t))+V(t)/R ,V(t))
print("dsolve(C*Derivative(V(t))+V(t)/R ,V(t))=", ans.doit())
```

以下為執行結果:
```
$ py rc.py
dsolve(C*Derivative(V(t))+V(t)/R ,V(t))= Eq(V(t), exp((C1 - t/R)/C))
``