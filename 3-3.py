import numpy as np
import matplotlib.pyplot as plt

# --- パラメータと初期値 -------------------------------
a, b = 1.4, 0.3          # x_{n+1}=1−a x_n^2 + y_n,  y_{n+1}=b x_n
n_total  = 10000        # 総ステップ数
discard  = 1000         # 捨てる初期過渡
x, y     = 0.0, -0.3     # 初期値

xs, ys = [], []          
for n in range(n_total):
    x_next = 1.0 - a * x**2 + y
    y_next = b * x

    if n >= discard:      
        xs.append(x_next)
        ys.append(y_next)

    x, y = x_next, y_next

plt.plot(xs, ys, '.', ms=2)
plt.xlim(-1.4, 1.4); plt.ylim(-1.0, 1.0)
plt.show()
