# 06-第6章 样本及抽样分布

[返回全书目录](../../README.md)

> PDF 页码：83–88

<!-- page: 83 -->

## 习题6 样本及抽样分布

1. 设  $ X_1, X_2, \cdots, X_n $ 是来自总体  $ X \sim b(1, p) $ 的样本，求样本的联合分布律。

解：∵ $ P\{X=k\}=p^{k}(1-p)^{1-k},k=0,1 $.

故 $ (X_{1},X_{2},\cdots,X_{n}) $的分布律为：

 $$ P\left\{X_{1}=x_{1},\cdots,X_{n}=x_{n}\right\}=\prod_{i=1}^{n}P\left\{X_{i}=x_{i}\right\}=\prod_{i=1}^{n}p^{x_{i}}\left(1-p\right)^{1-x_{i}} $$ 

 $$ =p^{\sum_{i=1}^{n}x_{i}}\left(\mathbf{1}-p\right)^{n-\sum_{i=1}^{n}x_{i}}=p^{n\overline{x}}\left(\mathbf{1}-p\right)^{n-n\overline{x}}. $$

<!-- page: 84 -->

2. 设某种电灯泡的寿命 X 服从指数分布，求来自这一总条件的简单随机样本  $ X_{1}, X_{2}, \cdots, X_{n} $ 的联合概率密度。

解：依题意有 $ f(x)=\left\{\begin{array}{ll}\lambda e^{-\lambda x},&x>0,\\ 0,&x\leq0.\end{array}\right. $

故简单随机样本 $ X_1, X_2, \cdots, X_n $的联合概率密度为 $ f^*(x_1, x_2, \cdots, x_n) = f(x_1)f(x_2) \cdots f(x_n) = \begin{cases} \lambda^n e^{-\lambda \sum_{i=1}^{n} x_i}, & x_i > 0, \\ 0, & x \leq 0. \end{cases} $

<!-- page: 85 -->

3.设 $ X_1,X_2,\cdots,X_7 $为总体 $ X\sim N(0,0.5^2) $的一个样本.试求：

(1)常数 $ a,b $的值，使得 $ a(X_1+X_2-X_3)^2+b(X_4+X_5+X_6)^2 $服从 $ \chi^2 $分布；

(2) $ P\left\{\sum_{i=1}^{7}X_i^2>4\right\}. $

解:(1)由已知，有 $ X_1+X_2-X_3\sim N(0,0.75) $， $ X_4+X_5+X_6\sim N(0,0.75) $，

故有: $ \frac{X_1+X_2-X_3}{\sqrt{0.75}}\sim N(0,1) $， $ \frac{X_4+X_5+X_6}{\sqrt{0.75}}\sim N(0,1) $，

 $ \left(\frac{X_1+X_2-X_3}{\sqrt{0.75}}\right)^2+\left(\frac{X_4+X_5+X_6}{\sqrt{0.75}}\right)^2\sim\chi^2(2) $，所以， $ a=b=\frac{1}{0.75}=\frac{4}{3} $.

(2) $ \because\frac{X_i}{0.5}=2X_i\sim N(0,1) $， $ \therefore\sum_{i=1}^{7}4X_i^2\sim\chi^2(7) $，

于是有， $ P\left\{\sum_{i=1}^{7}X_i^2>4\right\}=P\left\{4\sum_{i=1}^{7}X_i^2>16\right\}=P\left\{\chi^2>16\right\}=0.025 $.

<!-- page: 86 -->

4. 设  $ X_1, X_2, \cdots, X_n $ 是来自正态总体  $ N(\mu, \sigma^2) $ 的样本，试求样本方差  $ S^2 = \frac{1}{n-1} \sum_{i=1}^{n} (X_i - \overline{X})^2 $ 的数学期望及方差。







解$\because E(X_{i})=\mu,D(X_{i})=\sigma^{2},\therefore$ 有$E(\overline{X})=\mu,D(\overline{X})=\frac{\sigma^{2}}{n},$

$E(X_{i}^{2})=D(X_{i})+E^{2}(X_{i})=\sigma^{2}+\mu^{2},E(\overline{X}^{2})=D(\overline{X})+E^{2}(\overline{X})=\frac{\sigma^{2}}{n}+\mu^{2},$

故有，$E(S^{2})=\frac{1}{n-1}E\left(\sum_{i=1}^{n}\left(X_{i}-\overline{X}\right)^{2}\right)=\frac{1}{n-1}E\left(\sum_{i=1}^{n}X_{i}^{2}-n\overline{X}^{2}\right)$

$=\frac{1}{n-1}\left(\sum_{i=1}^{n}E\left(X_{i}^{2}\right)-nE\left(\overline{X}^{2}\right)\right)=\frac{1}{n-1}\left(n\left(\sigma^{2}+\mu^{2}\right)-n\left(\frac{\sigma^{2}}{n}+\mu^{2}\right)\right)=\sigma^{2},$

又$\because\frac{(n-1)S^{2}}{\sigma^{2}}\sim\chi^{2}(n-1),\therefore D\left(\frac{(n-1)S^{2}}{\sigma^{2}}\right)=2(n-1),$

$\therefore\frac{(n-1)^{2}}{\sigma^{4}}D(S^{2})=2(n-1),\therefore D(S^{2})=\frac{2\sigma^{4}}{n-1}.$

<!-- page: 87 -->

5. 设总体  $ X \sim N(50,6^2) $,  $ Y \sim N(46,4^2) $, 从 X 中抽取容量为 10 的样本, 样本方差为  $ S_1^2 $; 从 Y 中抽取容量为 8 的样本, 样本方差为  $ S_2^2 $, 求下列概率:

(1)  $ P\{0 < \overline{X} - \overline{Y} < 8\} $; (2)  $ P\{S_1^2 / S_2^2 < 8.28\} $. (总体 X 与 Y 相互独立)

解: (1)  $ \because $ 当  $ X \sim N(\mu, \sigma^2) $ 时, 有  $ \overline{X} \sim N\left(\mu, \frac{\sigma^2}{n}\right) $,  $ \therefore E(\overline{X} - \overline{Y}) = 50 - 46 = 4 $,

 $ D(\overline{X} - \overline{Y}) = \frac{6^2}{10} + \frac{4^2}{8} = 5.6 $,  $ \therefore \overline{X} - \overline{Y} \sim N(4, 5.6) $, 即有  $ \frac{\overline{X} - \overline{Y} - 4}{\sqrt{5.6}} \sim N(0, 1) $,

 $ \therefore P\{0 < \overline{X} - \overline{Y} < 8\} = P\left\{\frac{-4}{\sqrt{5.6}} < \frac{\overline{X} - \overline{Y} - 4}{\sqrt{5.6}} < \frac{4}{\sqrt{5.6}}\right\} = 2\Phi\left(\frac{4}{\sqrt{5.6}}\right) - 1 $

(2)  $ \because F = \frac{S_1^2}{\sigma_1^2} / \frac{S_2^2}{\sigma_2^2} = \frac{S_1^2}{6^2} / \frac{S_2^2}{4^2} = \frac{4}{9} \cdot \frac{S_1^2}{S_2^2} \sim F(9, 7) $,  $ \therefore P\left\{\frac{S_1^2}{S_2^2} < 8.28\right\} = P\left\{\frac{4}{9} \cdot \frac{S_1^2}{S_2^2} < \frac{4}{9} \cdot 8.28\right\} = P\{F < 3.68\} = 1 - P\{F \geq 3.68\} \approx 0.95 $.

<!-- page: 88 -->

6. 设总体  $ X \sim N\left(\mu, \sigma^{2}\right) $，抽取样本  $ X_{1}, X_{2}, \cdots, X_{n} $，样本均值为 X，样本方差为  $ S^{2} $，若再抽取一个采样  $ X_{n+1} $，证明：统计量  $ \sqrt{\frac{n}{n+1}} \frac{X_{n+1} - \overline{X}}{S} \sim t(n-1) $。

证：由  $ X \sim N\left(\mu, \sigma^{2}\right) $，故  $ \chi^{2} = \frac{(n-1)S^{2}}{\sigma^{2}} \sim \chi^{2}(n-1) $。

而  $ X_{1}, X_{2}, \cdots, X_{n} $ 相互独立，故  $ X_{n+1} - \overline{X} $ 也服从正态分布，其期望和方差分别为： $ E\left(X_{n+1} - \overline{X}\right) = E\left(X_{n+1}\right) - E\left(\overline{X}\right) = \mu - \mu = 0 $，

 $ D\left(X_{n+1} - \overline{X}\right) = D\left(X_{n+1}\right) + D\left(\overline{X}\right) = \sigma^{2} + \frac{\sigma^{2}}{n} = \frac{n+1}{n} \sigma^{2} $，

故有  $ \frac{X_{n+1} - \overline{X}}{\sqrt{\frac{n+1}{n}} \sigma^{2}} \sim N\left(0,1\right) $， $ \frac{\sqrt{\frac{n+1}{n}} \sigma^{2}}{\sqrt{\frac{(n-1)S^{2}}{\sigma^{2}(n-1)}}} \sim t(n-1) $，

即  $ \sqrt{\frac{n}{n+1}} \frac{X_{n+1} - \overline{X}}{S} \sim t(n-1) $。

