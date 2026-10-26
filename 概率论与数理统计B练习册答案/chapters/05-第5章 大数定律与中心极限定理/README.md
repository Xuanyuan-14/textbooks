# 05-第5章 大数定律与中心极限定理

[返回全书目录](../../README.md)

> PDF 页码：77–82

<!-- page: 77 -->

<div style="text-align: center;"><div style="text-align: center;">习题5-1 大数定律 习题5-2 中心极限定理</div> </div>


1. 设随机变量  $ X_1, \cdots, X_n $，…相互独立，且服从同一分布，数学期望  $ E(X_k) = \mu, D(X_k) = \sigma^2 (k = 1, 2, \cdots) $，令  $ \overline{Y_n} = \frac{1}{n} \sum_{k=1}^{n} (X_k - \mu)^2 $， $ (n = 1, 2, \cdots) $，证明： $ \left\{\overline{Y_n}\right\} $ 依概率收敛于  $ \sigma^2 $。

证明：由已知 $ X_1, X_2, \cdots, X_n, \cdots $，相互独立，且服从同一分布，所以 $ (X_1 - \mu)^2, (X_2 - \mu)^2, \cdots, (X_n - \mu)^2 $，也相互独立，且服从同一分布，而且， $ E(X_k - \mu)^2 = D(X_k) = \sigma^2 $，

根据辛钦大数定理，则有

 $$ \lim_{n\to+\infty}P\left\{\left|\frac{1}{n}\sum_{k=1}^{n}\left(X_{k}-\mu\right)^{2}-\sigma^{2}\right|<\varepsilon\right\}=1, $$ 

 $ \lim_{n \to +\infty} P \left\{ \left| \overline{Y}_n - \sigma^2 \right| < \varepsilon \right\} = 1 $，所以 $ \left\{ \overline{Y}_n \right\} $依概率收敛于 $ \sigma^2 $。

<!-- page: 78 -->

2. 一食品店有三种蛋糕出售，由于售出哪一种蛋糕是随机的，因而售出一只蛋糕的价格是一个随机变量，它取1元，1.2元，1.5元各个值的概率分别为0.3，0.2，0.5，若售出300只蛋糕，利用中心极限定理，求总收入至少为400元的概率。

解：设售出第$i$个蛋糕的价格为$X_i$（$i=1,2,\cdots,300$），则

$X_i \sim \begin{bmatrix} 1 & 1.2 & 1.5 \\ 0.3 & 0.2 & 0.5 \end{bmatrix}$，于是有$E(X_i) = 1.29, D(X_i) = 0.049$，则

总收入$X = X_1 + \cdots + X_{300} = \sum_{i=1}^{300} X_i$，则$E(X) = 387, D(X) = 14.7$，

由独立同分布中心极限定理，$\frac{X - 387}{\sqrt{14.7}} \sim N(0,1)$，则$P\{X \geq 400\} = 1 - P\{X \leq 400\} \approx 1 - \Phi\left(\frac{400 - 387}{\sqrt{14.7}}\right) \approx 1 - \Phi(3.394) = 0.0005$。

<!-- page: 79 -->

3. 由100个相互独立起作用的部件组成一个系统，在运行过程中每个部件能正常工作的概率都为90%，为了使整个系统能正常运行，至少必须有85%的部件在正常工作，利用中心极限定理求整个系统能正常运行的概率。

解：设X为系统中能正常工作的部件数，

则 $ X \sim b(100,0.9) $，故有 $ E(X) = np = 90, D(X) = npq = 9 $，

依题意，系统能正常运行必须满足： $ P\{X > 85\} $，

根据中心极限定理，有：

 $$ P\left\{X>85\right\}=1-P\left\{X\leq85\right\} $$ 

 $$ \approx1-\Phi\left(\frac{85-90}{3}\right)=1-\Phi\left(-\frac{5}{3}\right)=\Phi\left(\frac{5}{3}\right)=0.9525 $$

<!-- page: 80 -->

4. 利用中心极限定理确定当投掷一枚均匀硬币时，至少需要投掷多少次才能保证使得正面出现的频率在  $ 0.4 \sim 0.6 $ 之间的概率不小于90%.

解：设$X$为掷硬币$n$次正面出现的次数，

则$X \sim b(n,0.5)$，且$E(X)=0.5n$，$D(X)=0.25n$，根据中心极限定理，有

$P\left\{0.4<\frac{X}{n}<0.6\right\}=P\left\{0.4n<X<0.6n\right\}=P\left\{\frac{-0.1n}{\sqrt{0.25n}}<\frac{X-0.5n}{\sqrt{0.25n}}<\frac{0.1n}{\sqrt{0.25n}}\right\}$

$=2\Phi\left(\frac{0.1n}{\sqrt{0.25n}}\right)-1\geq0.9$，即$\Phi\left(\frac{0.1n}{\sqrt{0.25n}}\right)\geq\frac{1+0.9}{2}=0.95=\Phi(1.65)$，

所以有：$\frac{0.1n}{\sqrt{0.25n}}\geq1.65$，解得$n\geq68$。

<!-- page: 81 -->

5. 计算器进行加法运算时，把每个加数取为最接近它的整数来计算，设所有的取整误差是独立的，且在 $ [-0.5, 0.5] $上服从均匀分布。

(1)若将1500个数相加，问误差总和超过15的概率是多少？







(2)最多有几个数相加可使得误差总和的绝对值小于10的概率不小于0.90?

解:(1)设$X_i$为第$i$个数的取整误差，$i\in(1,1500)$，则$X_i\sim U(-0.5,0.5)$，

$E(X_i)=0$，$D(X_i)=\frac{1}{12}$，$E\left(\sum_{i=1}^{1500}X_i\right)=0$，$D\left(\sum_{i=1}^{1500}X_i\right)=125$，

根据中心极限定理，故有$P\left\{\sum_{i=1}^{1500}X_i>15\right\}=1-P\left\{\sum_{i=1}^{1500}X_i\leq15\right\}$

$\approx1-\Phi\left(\frac{15-0}{\sqrt{125}}\right)=1-\Phi\left(\frac{15}{11.2}\right)=1-\Phi(1.339)=1-0.9099=0.09$

<!-- page: 82 -->

(2)设最多有$n$个数相加可使得误差总和的绝对值小于10的概率

不小于0.90，

即有$P\left\{\left|\sum_{i=1}^{n}X_{i}\right|<10\right\}\geq0.90$，因为$E\left(\sum_{i=1}^{n}X_{i}\right)=0$，$D\left(\sum_{i=1}^{n}X_{i}\right)=\frac{n}{12}$，

根据中心极限定理，有

$P\left\{\left|\sum_{i=1}^{n}X_{i}\right|<10\right\}=P\left\{-10<\sum_{i=1}^{n}X_{i}<10\right\}\approx2\Phi\left(\frac{10}{\sqrt{\frac{n}{12}}}\right)-1\geq0.90$，

即$\Phi\left(\frac{10}{\sqrt{\frac{n}{12}}}\right)\geq0.95\approx\Phi(1.65)$，所以有：$\frac{10}{\sqrt{\frac{n}{12}}}\geq1.65$，解出$n\leq441$。

