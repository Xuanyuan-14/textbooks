# 07-第7章 参数估计

[返回全书目录](../../README.md)

> PDF 页码：89–100

<!-- page: 89 -->

<div style="text-align: center;"><div style="text-align: center;">习题7-1 点估计 习题7-2 估计量的评选标准</div> </div>


1. 设总体 $X$ 具有分布律 $\begin{bmatrix} X & 1 & 2 & 3 \\ p_k & \theta^2 & 2\theta(1-\theta) & (1-\theta)^2 \end{bmatrix}$, 其中 $\theta (0 < \theta < 1)$ 为未知数。已知取得了样本值 $x_1 = 1, x_2 = 2, x_3 = 1$，试求 $\theta$ 的矩估计值和极大似然估计值。

解：(1) 由矩估计法可知，$\mu_1 = E(X) = A_1 = \frac{1}{n} \sum_{i=1}^{n} x_i = \overline{x}$，而 $E(X) = 1 \times \theta^2 + 2 \times 2\theta(1 - \theta) + 3 \times (1 - \theta)^2 = 3 - 2\theta$，即有 $3 - 2\theta = \overline{x}$，求出 $\theta$ 的矩估计值为 $\theta = \frac{3 - \overline{x}}{2}$，又 $\overline{x} = \frac{1}{3}(1 + 2 + 1) = \frac{4}{3}$，故 $\theta$ 的矩估计值为 $\theta = \frac{1}{2}\left(3 - \frac{4}{3}\right) = \frac{5}{6}$。

(2) 似然函数 $L(\theta) = \prod_{i=1}^{3} p(x_i, \theta) = P\{X = x_1\} \cdot P\{X = x_2\} \cdot P\{X = x_3\} = \theta^4 \cdot 2\theta(1 - \theta) = 2\theta^5(1 - \theta)$，取对数得 $\text{In}L(\theta) = \text{In}2 + 5\text{In}\theta + \text{In}(1 - \theta)$，令 $\frac{\text{dIn}L(\theta)}{\text{d}\theta} = 0$，得 $\frac{5}{\theta} - \frac{1}{1 - \theta} = 0$，即 $\theta$ 的极大似然估计值为 $\theta = \frac{5}{6}$。

<!-- page: 90 -->

2. 设总体X的概率密度为 $ f(x)=\begin{cases}(\theta+1)x^\theta, & 0<x<1, \\ 0, & \text{其他}.\end{cases} $，

 $ X_1, X_2, \cdots, X_n $是来自总体X的样本，求 $ \theta $的矩估计和极大似然估计。

解: (1)  $ E(X)=\int_{-\infty}^{+\infty} x f(x) \, \mathrm{d}x=\int_{0}^{1} x \cdot (\theta+1) x^\theta \, \mathrm{d}x=\int_{0}^{1} (\theta+1) x^{\theta+1} \, \mathrm{d}x=\frac{\theta+1}{\theta+2} $，由矩估计法可知， $ E(X)=\overline{X} $，即 $ \frac{\theta+1}{\theta+2}=\overline{X} $，解出 $ \hat{\theta}=\frac{2\overline{X}-1}{1-\overline{X}}=\frac{-2\left(1-\overline{X}\right)+1}{1-\overline{X}}=\frac{1}{1-\overline{X}}-2 $。

(2)  $ \theta $的似然函数为 $ L(\theta)=\prod_{i=1}^{n} f(x_i, \theta)=(\theta+1)^n\left(\prod_{i=1}^{n} x_i\right)^{\theta+1} $，取对数，

得 $ \ln L(\theta)=n\ln(\theta+1)+(\theta+1)\sum_{i=1}^{n} \ln x_i $，再求导数得， $ \frac{\mathrm{d}}{\mathrm{d}\theta} \ln L(\theta)=\frac{n}{\theta+1}+\sum_{i=1}^{n} \ln x_i $，

由似然方程 $ \frac{\mathrm{d}}{\mathrm{d}\theta} \ln L(\theta)=0 $，解出 $ \theta $的极大似然估计值为 $ \hat{\theta}=-\frac{n}{\sum_{i=1}^{n} \ln x_i}-1 $。

<!-- page: 91 -->

3.一地质学家为研究密歇根湖的湖滩地区的岩石成分，自该地区随机抽取由100个样品构成的一个容量为100的样本，每个样品有10块石子，地质学家记录了每个样品中石灰石的石子数。求该地区石子中石灰石最可能的比例值。该地质学家所得的数据如下： $ \frac{\text{样品中石灰石的石子数}}{\text{样品个数}} \left| \begin{array}{ccc|c|c|c|c} 0 & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 \\ 0 & 1 & 6 & 7 & 23 & 26 & 21 & 12 & 3 \\ 1 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0\end{array} \right| $。

解：由题意可知，100个样品，每个样品有10块石子，故共有石子1000块，石灰石的石子数共有：

 $ \sum_{i=0}^{10}x_{i}=1\times1+2\times6+3\times7+4\times23+5\times26+6\times21+7\times12+8\times3+9\times1=499 $

故该地区石子中石灰石最可能的比例值为： $ \frac{\sum_{i=0}^{10}x_{i}}{1000}=0.499 $

<!-- page: 92 -->

4.设总体X服从正态分布 $ N(\mu,\sigma^2) $， $ X_1 $、 $ X_2 $是从此总体中抽取的一个样本.试验证下面三个估计量都是 $ \mu $的无偏估计，并指出哪一个估计量最有效：

 $ (1)^{\stackrel{\wedge}{}}\mu_1=\frac{2}{3}X_1+\frac{1}{3}X_2;\quad(2)^{\stackrel{\wedge}{}}\mu_2=\frac{1}{4}X_1+\frac{3}{4}X_2;\quad(3)^{\stackrel{\wedge}{}}\mu_3=\frac{1}{2}X_1+\frac{1}{2}X_2. $

 $ \sim $



解：由已知， $ E(X_{i})=\mu $， $ D(X_{i})=\sigma^{2} $，则

 $$ E\binom{\stackrel{\wedge}{}}{\mu_{1}}=E\bigg(\frac{2}{3}X_{1}+\frac{1}{3}X_{2}\bigg)=\frac{2}{3}E\big(X_{1}\big)+\frac{1}{3}E\big(X_{2}\big)=\mu, $$ 

 $$ E\binom{\stackrel{\wedge}{}}{\mu_{2}}=E\bigg(\frac{1}{4}X_{1}+\frac{3}{4}X_{2}\bigg)=\frac{1}{4}E\big(X_{1}\big)+\frac{3}{4}E\big(X_{2}\big)=\mu, $$ 

 $ E\left(\hat{\mu}_3\right)=E\left(\frac{1}{2}X_1+\frac{1}{2}X_2\right)=\frac{1}{2}E\left(X_1\right)+\frac{1}{2}E\left(X_2\right)=\mu $，故 $ \hat{\mu}_1,\hat{\mu}_2,\hat{\mu}_3 $都是 $ \mu $的无偏估计.

 $$ D\binom{\stackrel{\wedge}{}}{\mu_{1}}=D\bigg(\frac{2}{3}X_{1}+\frac{1}{3}X_{2}\bigg)=\frac{4}{9}D\big(X_{1}\big)+\frac{1}{9}D\big(X_{2}\big)=\frac{5}{9}\sigma^{2}, $$ 

 $$ D\binom{\stackrel{\wedge}{}}{\mu_{2}}=D\bigg(\frac{1}{4}X_{1}+\frac{3}{4}X_{2}\bigg)=\frac{1}{16}D\big(X_{1}\big)+\frac{9}{16}D\big(X_{2}\big)=\frac{5}{8}\sigma^{2}, $$ 

$$D\left(\mu_{3}\right)=D\left(\frac{1}{2}X_{1}+\frac{1}{2}X_{2}\right)=\frac{1}{4}D\left(X_{1}\right)+\frac{1}{4}D\left(X_{2}\right)=\frac{1}{2}\sigma^{2}$$，所以$\mu_{3}^{\wedge}$最有效

<!-- page: 93 -->

<div style="text-align: center;"><div style="text-align: center;">习题7-3 区间估计 习题7-4 正态总体参数的区间估计</div> </div>






1.某批钢球的质量 $ X \sim N(\mu,4) $，从中抽取了一个容量为 $ n=16 $的样本且测得 $ \overline{x}=22.5 $， $ s=3.98 $，试在置信度为 $ 1-\alpha=0.95 $下，求出 $ \mu $的置信区间。

解：由已知 $ n=16 $， $ \sigma=2 $， $ \alpha=0.05 $，查表得 $ u_{0.025}=1.96 $，代入公式有， $ \overline{x}-u_{\frac{\alpha}{2}}\frac{\sigma}{\sqrt{n}}=22.5-1.96\times\frac{2}{4}=21.52 $， $ \overline{x}+u_{\frac{\alpha}{2}}\frac{\sigma}{\sqrt{n}}=22.5+1.96\times\frac{2}{4}=23.48 $，所以 $ \mu $的置信区间为 $ (21.52,23.48) $。

<!-- page: 94 -->

2. 设总体  $ X \sim N(\mu, \sigma^{2}) $， $ \sigma^{2} $ 已知，问样本容量 n 取多大时，才能保证  $ \mu $ 的置信水平为95%的置信区间的长度不大于 k.







解：由已知，置信水平为95%= $ 1-\alpha $，则 $ \alpha=0.05,\frac{\alpha}{2}=0.025 $， $ u_{\frac{\alpha}{2}}=1.96 $，因为 $ \mu $的置信区间为 $ \left(\bar{x}-u_{\frac{\alpha}{2}}\frac{\sigma}{\sqrt{n}},\bar{x}+u_{\frac{\alpha}{2}}\frac{\sigma}{\sqrt{n}}\right) $，

所以置信区间的长度 $ L=2u_{\frac{\alpha}{2}}\frac{\sigma}{\sqrt{n}} $，变形后有： $ n=\left(2u_{\frac{\alpha}{2}}\frac{\sigma}{L}\right)^2 $，

故当置信区间的长度不大于k时，即 $ 2u_{\frac{\alpha}{2}}\frac{\sigma}{\sqrt{n}}\leq k $，

解出 $ n\geq\left(2u_{\frac{\alpha}{2}}\frac{\sigma}{k}\right)^2=\left(3.92\times\frac{\sigma}{k}\right)^2 $，即n最少取 $ \left(3.92\times\frac{\sigma}{k}\right)^2 $。

<!-- page: 95 -->

3.设有一组来自正态分布 $ X\sim N(\mu,\sigma^{2}) $的样本观测值：

0.497,0.506,0.518,0.524,0.488,0.510,0.510,0.515,0.512,

(1)已知 $ \sigma=0.01 $，求 $ \mu $的置信区间(设置信度为0.95);

(2)若 $ \sigma^{2} $未知，求 $ \mu $的置信区间(设置信度为0.95).

解：由已知，有 $ n=9 $， $ \sigma=0.01 $， $ \alpha=0.05 $，查表得 $ u_{0.025}=1.96 $， $ t_{0.025}(8)=2.306 $，计算得 $ \overline{x}=0.508 $，s=0.01，

(1) $ \mu $的置信区间为 $ \overline{x}-u_{\frac{\alpha}{2}}\frac{\sigma}{\sqrt{n}}=0.508-1.96\times\frac{0.01}{3}=0.5024 $，

 $ \overline{x}+u_{\frac{\alpha}{2}}\frac{\sigma}{\sqrt{n}}=0.508+1.96\times\frac{0.01}{3}=0.5154 $，

所以 $ \mu $的置信区间为(0.5024,0.5154).

(2)若 $ \sigma^{2} $未知，就要用t分布的公式，

 $ \mu $的置信区间为 $ \overline{x}-t_{\frac{\alpha}{2}}(8)\frac{\sigma}{\sqrt{n}}=0.508-2.306\times\frac{0.01}{3}=0.5006 $，

 $ \overline{x}-t_{\frac{\alpha}{2}}(8)\frac{\sigma}{\sqrt{n}}=0.508+2.306\times\frac{0.01}{3}=0.5172 $，

所以 $ \mu $的置信区间为(0.5006,0.5172).

<!-- page: 96 -->

4. 某厂生产一批金属材料，其抗弯强度服从正态分布，现从这批金属材料中抽取11个测试件，测得它们的抗弯强度为(单位：kg): 42.5, 42.7, 43.0, 42.3, 43.4, 44.5, 44.0, 43.8, 44.1, 43.9, 43.7.







求：抗弯强度标准差 $ \sigma $的置信水平为0.90的置信区间.

解：因为 $ \sigma $未知，故选估计量 $ \chi^{2}=\frac{n-1}{\sigma^{2}}S^{2} $，则 $ \sigma $的置信水平为 $ 1-\alpha $的置信区间为

 $$ \left(\left(\frac{(n-1)S^{2}}{\chi_{\frac{\alpha}{2}}^{2}(n-1)}\right),\left(\frac{(n-1)S^{2}}{\chi_{1-\frac{\alpha}{2}}^{2}(n-1)}\right)\right), $$ 

由已知，有 $ n=11,\frac{\alpha}{2}=0.05,1-\frac{\alpha}{2}=0.95 $，查表得 $ \chi_{0.05}^{2}(10)=18.307,\chi_{0.95}^{2}(10)=3.940 $

计算得， $ s^{2}=0.523 $，再代入上面的公式计算得，

 $ \sigma $的置信水平为0.90的置信区间为(0.53,1.15)

<!-- page: 97 -->

5.某厂利用两条自动化流水线灌装番茄酱，分别从两条流水线上抽取样本： $ X_1, X_2, \cdots, X_{12} $，及 $ Y_1, Y_2, \cdots, Y_{17} $，算出 $ \overline{x} = 10.6, \overline{y} = 9.5, s_1^2 = 2.5, s_2^2 = 4.7 $。假设这两条流水线上灌装的番茄酱的质量都服从正态分布，且相互独立，其均值分别为 $ \mu_1, \mu_2 $。

(1)设两总体方差 $ \sigma_{1}^{2}=\sigma_{2}^{2} $，求 $ \mu_{1}-\mu_{2} $的置信水平为95%的置信区间；

(2)求 $ \sigma_{1}^{2}/\sigma_{2}^{2} $的置信水平为95%的置信区间.

解: (1) 总体方差未知且相等，要用  $ t(n_1 + n_2 - 2) $ 的分布，

查表 $ t_{\frac{\alpha}{2}}(n_1+n_2-2)=t_{0.025}(27)=2.05 $，计算 $ S_w=\sqrt{\frac{(n_1-1)s_1^2+(n_2-1)s_2^2}{n_1+n_2-2}}=\sqrt{3.8}=1.95 $，于是有， $ \overline{x}-\overline{y}-t_{\frac{\alpha}{2}}(n_1+n_2-2)S_w\sqrt{\frac{1}{n_1}+\frac{1}{n_2}}=10.6-9.5-2.05\times1.95\times\sqrt{\frac{1}{12}+\frac{1}{17}}=-0.401 $， $ \overline{x}-\overline{y}+t_{\frac{\alpha}{2}}(n_1+n_2-2)S_w\sqrt{\frac{1}{n_1}+\frac{1}{n_2}}=10.6-9.5+2.05\times1.95\times\sqrt{\frac{1}{12}+\frac{1}{17}}=2.601 $，所以，解方程组 $ \frac{1}{n_1+n_2}=10.6-9.5=1.95 $是原方程的解。

所以， $ \mu_{1}-\mu_{2} $的置信水平为95%的置信区间为 $ (-0.401,2.601) $.

(2)求 $ \sigma_{1}^{2}/\sigma_{2}^{2} $的置信区间要用 $ F(n_{1}-1,n_{2}-1) $分布，查表 $ F_{\frac{\alpha}{2}}(n_{1}-1,n_{2}-1)=F_{0.025}(11,16)=2.89 $， $ F_{1-\frac{\alpha}{2}}(n_{1}-1,n_{2}-1)=F_{0.975}(11,16)=\frac{1}{F_{0.025}(16,11)}=\frac{1}{3.33}=0.3 $，于是有， $ \sigma_{1}^{2}/\sigma_{2}^{2} $的置信水平为95%的置信区间为 $ \left(\frac{s_{1}^{2}}{s_{2}^{2}}\bullet\frac{1}{F_{\frac{\alpha}{2}}},\frac{s_{1}^{2}}{s_{2}^{2}}\bullet\frac{1}{F_{1-\frac{\alpha}{2}}}\right)=(0.174,1.690) $

<!-- page: 98 -->

### 习题7-6 单侧置信区间

2.从轮胎厂生产的某种轮胎中抽取10个样品进行磨损试验，直至轮胎磨损到破坏为止，测得它们的行驶路程(km)如下：

设汽车轮胎行驶路程服从正态分布 $ N(\mu,\sigma^{2}) $，求：

(1) $ \mu $的置信水平为95%的单侧置信下限(2) $ \sigma $的置信水平为95%的单侧置信上限

解: (1)由 $ T = \frac{\overline{x} - \mu}{s/\sqrt{n}} \sim t(n-1) $分布，得 $ P\left\{\frac{\overline{x} - \mu}{s/\sqrt{n}} \leq t_{\alpha}(n-1)\right\} = 1 - \alpha $，即

$P\left\{\mu > \overline{x} - \frac{s}{\sqrt{n}} t_\alpha(n-1)\right\} = 1 - \alpha$，故有

$\mu$的置信水平为95%的单侧置信下限为$\underline{\mu}=\overline{x}-\frac{s}{\sqrt{n}}t_{0.05}(n-1)$,

根据已知数据，计算得样本均值和样本标准差为：

 $ \mu=41220,\ s=1424.8, $ 查表有 $ t_{0.05}(9)=1.833, $ 代入上式计算得：

 $$ \underline{\mu}=\overline{x}-\frac{s}{\sqrt{n}}t_{0.05}(n-1)=41220-\frac{1424.8}{\sqrt{10}}\times1.833=40394. $$

<!-- page: 99 -->

(2)由 $ \chi^{2}=\frac{(n-1)S^{2}}{\sigma^{2}}\sim\chi^{2}(n-1) $分布，

得 $ P\left\{\frac{(n-1)S^2}{\sigma^2}\geq\chi_{1-\alpha}^2(n-1)\right\}=1-\alpha $，即 $ P\left\{\sigma^2\leq\frac{(n-1)S^2}{\chi_{1-\alpha}^2(n-1)}\right\}=1-\alpha $，

故有  $ \sigma $ 的置信水平为 95% 的单侧置信上限为

 $ \overline{\sigma} = \sqrt{\frac{(n-1)S^{2}}{\chi_{1-\alpha}^{2}(n-1)}} $，查表有， $ \chi_{1-\alpha}^{2}(n-1) = \chi_{0.95}^{2}(9) = 3.325 $，

再根据 $ ^{(1)} $的结果，代入上式计算得：

 $$ \overline{\sigma}=\sqrt{\frac{9\times1424.8^{2}}{3.325}}=2344. $$

<!-- page: 100 -->

3.随机从A批导线中抽取4根，又从B批导线中抽取5根，测得电阻( $ \Omega $)为A批导线:0.143,0.142,0.143,0.137,

B批导线:0.140,0.142,0.136,0.138,0.140,







设测定数据分别来自总体 $ N(\mu_1,\sigma^2) $， $ N(\mu_2,\sigma^2) $，且两样本相互独立，又 $ \mu_1,\mu_2,\sigma^2 $均未解决求 $ \mu_1-\mu_2 $的置信水平为0.95的单侧置信下限

解：因为 $ \sigma_1^2=\sigma_2^2=\sigma^2 $为未知的，则根据统计量

 $ T=\frac{(\overline{X}_1-\overline{X}_2)-(\mu_1-\mu_2)}{S_w\sqrt{\frac{1}{n_1}+\frac{1}{n_2}}}\sim t(n_1+n_2-2) $分布，其中 $ S_w=\sqrt{\frac{(n_1-1)S_1^2+(n_2-1)S_2^2}{n_1+n_2-2}} $，

即有， $ P\{\mu_1-\mu_2\geq\overline{X}_1-\overline{X}_2-t_\alpha(n_1+n_2-2)S_w\sqrt{\frac{1}{n_1}+\frac{1}{n_2}}\}=1-\alpha $，

所以， $ \mu_1-\mu_2 $的置信水平为0.95的单侧置信下限为

 $ \frac{\mu_1-\mu_2}{\overline{x}_A-\overline{x}_B}=x_A-\overline{x}_B-t_{0.05}(7)s_w\sqrt{\frac{1}{n_1}+\frac{1}{n_2}} $，根据已知数据计算得，

 $ \frac{\mu_1-\mu_2}{x_A-\overline{x}_B}=0.002 $， $ s_w=0.00255 $，查表 $ t_{0.05}(7)=1.895 $，代入上式计算得，

 $ \frac{1}{4}+\frac{1}{5}=-0.00124 $

