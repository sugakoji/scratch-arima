# scratch-arima
ARIMAモデル系統をスクラッチで書く

# AR

真のモデルは

```math
y[t]=2+0.2* y[t-1] + 0.3* y[t-2] + e    e ~  N(0,4.0)
```

![ar_2](https://user-images.githubusercontent.com/29496312/58689979-74072f00-83c3-11e9-94a3-a6427e96838c.png)

モデルの推定結果は

```math
y[t]=1.99+0.2* y[t-1] + 0.3* y[t-2] + e    e ~  N(0,4.01)
```

でうまくいっている。
# WIP: MA

# WIP: ARMA