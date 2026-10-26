# 02-第2章 随机变量及其分布

[返回全书目录](../../README.md)

> PDF 页码：19–34

<!-- page: 19 -->

<div style="text-align: center;"><div style="text-align: center;">习题2-1 随机变量 习题2-2 离散型随机变量</div> </div>






1. 掷一枚不均匀的硬币，直至正、反面都出现为止，设正面出现的概率为  $ p (0 < p < 1) $，以 X 表示投掷硬币的次数，求 X 的分布律。

解：设 $ A_i = \{\text{投掷第} i \text{次出现正面}\} $，则 $ \overline{A}_i = \{\text{投掷第} i \text{次出现反面}\} $， $ p + q = 1 $

正反面都出现为止，最少投掷2次，即有 $ P(X=2)=P\left(A_{1}\overline{A_{2}}\right)+P\left(\overline{A_{1}}A_{2}\right)=pq+qp $

 $$ P(X=3)=P\big(A_{1}A_{2}\overline{A_{3}}\big)+P\big(\overline{A_{1}}\overline{A_{2}}A_{3}\big)=p^{2}q+q^{2}p,\cdots\cdots $$ 

 $$ P(X=k)=P\big(A_{1}A_{2}\cdots\overline{A_{k}}\big)+P\big(\overline{A_{1}}\overline{A_{2}}\cdots A_{k}\big)=p^{k-1}q+q^{k-1}p,\ k=2,3,\cdots $$ 

2. 将一颗骰子抛掷两次，以  $ X_{1} $ 表示两次所得到的点数之和， $ X_{2} $ 表示两次中得到的较小点数，试分别求  $ X_{1}, X_{2} $ 的分布律。

解：两次所得点数之和最少为2点，最多为12点，故有，

 $$ \begin{array}{l|cccccc}{{{X_{1}}}}&{{{2}}}&{{{3}}}&{{{4}}}&{{{5}}}&{{{6}}}&{{{7}}}&{{{8}}}&{{{9}}} \\{{{\hline p_{1}}}}&{{{1/36}}}&{{{2/36}}}&{{{3/36}}}&{{{4/36}}}&{{{5/36}}}&{{{6/36}}}&{{{5/36}}}&{{{4/36}}}&{{{3/36}}} \\{{{\end{array}\quad} $$ 

两次中得到的较小点数最少为1点，最多为6点，故有，

 $$ \frac{X_{2}}{p_{2}}\left|\begin{array}{c c c c c}{1}&{2}&{3}&{4}&{5}\\ {11/36}&{9/36}&{7/36}&{5/36}&{3/36}\end{array}\right|\frac{6}{1/36} $$

<!-- page: 20 -->

3. 设一批产品共100只，其中有10只次品，从中取三次，每次任取1只，以X表示取出的3只中次品的只数，分别求出在下列两种情形下X的分布律：(1) 不放回抽样；(2) 放回抽样.







解: (1) 从100只中抽三次，共有 $ C_{100}^{3} $种情况，三次中有k件次品，则有3-k件正品，

一共有 $ C_{10}^{k}C_{90}^{3-k} $种情况，所以三次中有k件次品的概率为 $ P(X=k)=\frac{C_{10}^{k}C_{90}^{3-k}}{C_{100}^{3}} $，k=0,1,2,3.

(2)有放回的抽样，相当于一个3重伯努利试验，即 $ X \sim b(3,0.1) $，故有 $ P(X = k) = C_3^k 0.1^k \cdot 0.9^{3-k} $， $ k = 0,1,2,3 $.

(1)在一周内恰好发生两次交通事故的概率是多少?

(2)在一周内至少发生一次交通事故的概率是多少?

解：设X表示该城市一周内发生交通事故的次数，则 $ X \sim \pi(0.3) $，

 $$ (1)P\big(X=2\big)=\frac{\big(0.3\big)^{2}}{2!}e^{-0.3}=P\big(X\leq2\big)-P\big(X\leq1\big)=\sum_{k=0}^{2}\frac{\big(0.3\big)^{2}}{2!}e^{-0.3}-\sum_{k=0}^{1}\frac{\big(0.3\big)^{1}}{1!}e^{-0.3}=0.996-0.963=0.033. $$ 

 $$ )P\big(X\geq1\big)=1-P\big(X=0\big)=1-\frac{\big(0.3\big)^{0}}{0!}e^{-0.3}=1-0.741=0.259. $$

<!-- page: 21 -->

5. 某地区有5个加油站，调查表明在任一时刻每个加油站被使用的概率为0.1，试问：

(1)恰有2个加油站被使用的概率是多少?





(2)至少有3个加油站被使用的概率是多少?

(3)至多有3个加油站被使用的概率是多少?

解：设X表示加油站被同时使用的个数，则 $ X \sim b(5,0.1) $，

(1) $ P(X=2)=C_{5}^{2}(0.1)^{2}(0.9)^{3} $

 $$ P\left(X\geq3\right)=P\left(X=3\right)+P\left(X=4\right)+P\left(X=5\right) $$ 

 $$ =C_{5}^{3}(0.1)^{3}(0.9)^{2}+C_{5}^{4}(0.1)^{4}(0.9)+C_{5}^{5}(0.1)^{5}=0.00856. $$ 

 $$ (3)P\big(X\leq3\big)=1-P\big(X=4\big)-P\big(X=5\big) $$ 

 $$ =1-C_{5}^{4}\big(0.1\big)^{4}\big(0.9\big)-C_{5}^{5}\big(0.1\big)^{5}=0.99954. $$

<!-- page: 22 -->

#### 习题2-3 随机变量的分布函数

1. 分析下列函数中，哪个是随机变量 X 的分布函数。

(1) $ F(x)=\left\{\begin{array}{ll}0,&x<-2\\ \frac{1}{2},&-2\leq x<0.\\ 2,&x\geq0\end{array}\right. $ (2) $ F(x)=\left\{\begin{array}{ll}0,&x<0\\ \sin x,&0\leq x<\pi.\\ 1,&x\geq\pi\end{array}\right. $ (3) $ F(x)=\frac{1}{1+x^{2}},x\in R. $

解: (1) 不是，因为有  $ 0 \leq F(x) \leq 2 $，即  $ F(+\infty) \neq 1 $。

(2)不是，因为有 $ \lim_{x\to\pi^{+}}F(x)=1\neq F(\pi) $，且 $ F(x) $不是不减的函数。

(3)不是，因为 $ F(+\infty) \neq 1 $，且不是不减的函数。

3.设随机变量  $ X $ 的分布函数为  $ F(x) = A + B \arctan x $， $ x \in \mathbb{R} $，试求(1)  $ A, B $ 的值；(2)  $ P\{-1 < X \leq 1\} $.

解: (1) 根据分布函数的性质:  $ F(+\infty)=1, F(-\infty)=0 $, 有

 $ A + B \arctan(-\infty) = 0, A + B \arctan(+\infty) = 1 $，即有 $ A - \frac{\pi}{2}B = 0 $， $ A + \frac{\pi}{2}B = 1 $，解出， $ A = \frac{1}{2} $， $ B = \frac{1}{\pi} $.

 $$ P\left\{-1<X\leq1\right\}=F(1)-F(-1)=A+B\arctan1-\left(A+B\arctan(-1)\right)=\frac{\pi}{4}B+\frac{\pi}{4}B=\frac{1}{2}. $$ 

4.设随机变量X的分布函数为 $ F(x)=\begin{cases}A(1-e^{-x}),&x\geq0\\0,&x<0\end{cases} $，试求(1)系数 $ A $;(2) $ P\{1<X<3\} $.

解:(1)由分布函数的性质 $ F(+\infty)=1 $，有 $ A(1-e^{-\infty})=1 $，得A=1;

(2) $ P\{1<X<3\}=F(3)-F(1)=1-e^{-3}-(1-e^{-1})=e^{-1}-e^{-3}. $

<!-- page: 23 -->

2. 箱中有8个同样的球，编号为1,2, $ \cdots $,8，从中任取3个球，以X表示所取到的3个球的最小号码，试求X的分布函数。

解:8个球中任取3个，共有 $ C_8^3 = 56 $种情况，X的可能取值为 $ 1, \cdots, 6 $。 $ \{X = 1\} $表示3球中1号最小，另两个是 $ 2 \cdots 8 $中的两个，则 $ P\{X = 1\} = \frac{C_7^2}{C_8^3} = \frac{21}{56} $； $ \{X = 2\} $表示3球中2号最小，另两个是 $ 3 \cdots 8 $中的两个，则 $ P\{X = 2\} = \frac{C_6^2}{C_8^3} = \frac{15}{56} $； $ \{X = 3\} $表示3球中3号最小，另两个是 $ 4 \cdots 8 $中的两个，则 $ P\{X = 3\} = \frac{C_5^2}{C_8^3} = \frac{10}{56} $； $ \{X = 4\} $表示3球中4号最小，另两个是 $ 5 \cdots 8 $中的两个，则 $ P\{X = 4\} = \frac{C_4^2}{C_8^3} = \frac{6}{56} $； $ \{X = 5\} $表示3球中5号最小，另两个是6,7,8中的两个，则 $ P\{X = 5\} = \frac{C_3^2}{C_8^3} = \frac{3}{56} $； $ \{X = 6\} $表示3球中6号最小，另两个只能是7,8，则 $ P\{X = 6\} = \frac{1}{56} $，即有X的分布律： $ \frac{X}{p_i} \left| \begin{array}{ccc} 1 & 2 & 3 \\ \hline 21 & 15 & 10 \\ 56 & 56 & 56 \end{array} \right| \quad \frac{4}{56} \quad \frac{4}{56} \quad \frac{5}{3} \quad \frac{6}{1}  $。X的分布函数 $ F(x) = \begin{array}{ccc} 0 & x < 1 & \\ \hline \frac{21}{56}, & 1 \leq x < 2 & \\ \hline \frac{36}{56}, & 2 \leq x < 3 & \\ \hline \frac{46}{56}, & 3 \leq x < 4 & \\ \hline \frac{52}{56}, & 4 \leq x < 5 & \\ \hline \frac{55}{56}, & 5 \leq x < 6 & \\ 1, & x \geq 6 & \end{array}\right| $。

<!-- page: 24 -->

5.设随机变量X的分布律为: $ \frac{X}{p_i}\left|\begin{array}{cccc}0&1&2&3\\\frac{1}{16}&\frac{3}{16}&\frac{1}{2}&\frac{1}{4}\end{array}\right| $

(1)求X的分布函数 $ F(x) $，并画出 $ F(x) $的图形； (2) $ P\{X \leq 2\} $及 $ P\{0 < X < 3\} $.

解： $ F(x)=\left\{\begin{aligned}&0,&x<0\\ &\frac{1}{16},&0\leq x<1\\ &\frac{1}{4},&1\leq x<2.\\ &\frac{3}{4},&2\leq x<3\\ &1,&x\geq3\end{aligned}\right. $

 $$ (2)P\{X\leq2\}=\frac{1}{16}+\frac{3}{16}+\frac{1}{2}=\frac{3}{4};\qquad P\{0<X<3\}=\frac{3}{16}+\frac{1}{2}=\frac{11}{16}. $$

<!-- page: 25 -->

<div style="text-align: center;"><div style="text-align: center;">习题2-4 连续型随机变量及其概率密度</div> </div>






1.设连续型随机变量X的分布函数为 $ F(x)=\left\{\begin{array}{ll}0, & x\leq-a \\ A+B\arcsin\frac{x}{a}, & -a<x\leq a. \\ 1, & x>a\end{array}\right. $试求：

(1)A、B的值；(2)X的概率密度；(3) $ P\left\{X>\frac{a}{2}\right\} $.

解: (1)∵  $ F(-a)=0 $,  $ F(a)=1 $, 所以有  $ A+B\arcsin\frac{-a}{a}=0 $,  $ A+B\arcsin\frac{a}{a}=1 $, 即  $ A-\frac{\pi}{2}B=0 $,  $ A+\frac{\pi}{2}B=1 $, 解得  $ A=\frac{1}{2} $,  $ B=\frac{1}{\pi} $.

(2) $ f(x)=F'(x)=\left\{\begin{aligned}&\frac{1}{\pi\sqrt{a^{2}-x^{2}}},&-a<x<a\\&0,& 其他 \end{aligned}\right. $

 $$ (3)P\biggl\{X>\frac{a}{2}\biggr\}=F\bigl(a\bigr)-F\biggl(\frac{a}{2}\biggr)=1-\frac{1}{2}-\frac{1}{\pi}\arcsin\frac{1}{2}=\frac{1}{2}-\frac{1}{\pi}\times\frac{\pi}{6}=\frac{1}{2}-\frac{1}{6}=\frac{1}{3}. $$

<!-- page: 26 -->

2.设随机变量X的概率密度为 $ f(x)=\left\{\begin{aligned}&Ax^{2},&1\leq x<2\\ &Ax,&2\leq x<3.\\ &0,& 其他\end{aligned}\right. $

(1)系数A； (2)X的分布函数； (3) $ P\{|X|<2\} $.

解: (1) 由  $ \int_{1}^{2} A x^{2} \, \mathrm{d}x + \int_{2}^{3} A x \, \mathrm{d}x = 1 $，得  $ A\left(\frac{1}{3} x^{3} \bigg|_{1}^{2} + \frac{1}{2} x^{2} \bigg|_{2}^{3}\right) = 1 \Rightarrow A\left(\frac{7}{3} + \frac{5}{2}\right) = 1 $，即  $ A = \frac{6}{29} $。



 $$ \begin{aligned}(2)F(x)=&\begin{cases}0,&x<1\\\int_{1}^{x}Ax^{2}\mathrm{d}x,&1\leq x<2\\\int_{2}^{x}Axdx,&2\leq x<3\\1,&x\geq3\end{cases}\Rightarrow\begin{cases}0,&x<1\\\frac{2}{29}\big(x^{3}-1\big),&1\leq x<2\\\frac{3}{29}x^{2}+\frac{2}{29},&2\leq x<3\\1,&x\geq3\end{cases}\end{aligned} $$ 

 $$ (3)P\big\{\big|X\big|<2\big\}=P\big\{-2<X<2\big\}=P\big\{1<X<2\big\}=\int_{1}^{2}\frac{6}{29}x^{2}\mathrm{d}x=\frac{6}{29}\bigg(\frac{1}{3}x^{3}\bigg)_{1}^{2}=\frac{14}{29}. $$

<!-- page: 27 -->

3.设 $ X \sim N(3,4), (1) $求 $ P\{2 < X \leq 5\}, P\{|x| > 2\} $;





(2)确定c,使得 $ P\{X>c\}=P\{X\leq c\} $?

解: (1) 因为  $ X \sim N(3,4) $，故有

 $$ P\left\{a<X\leq b\right\}=P\left\{\frac{a-3}{2}<\frac{X-3}{2}\leq\frac{b-3}{2}\right\}=\varPhi\left(\frac{b-3}{2}\right)-\varPhi\left(\frac{a-3}{2}\right), $$ 

 $$ \begin{align*}\therefore P\left\{2<X\leq5\right\}&=\varPhi\left(\frac{5-3}{2}\right)-\varPhi\left(\frac{2-3}{2}\right)=\varPhi\left(1\right)-\varPhi\left(-0.5\right)\\&=\varPhi\left(1\right)-\left(1-\varPhi\left(0.5\right)\right)=0.8413-1+0.6915=0.5328.\end{align*} $$ 

 $$ \begin{aligned}P\left\{\left|x\right|>2\right\}&=\mathbf{1}-P\left\{\left|x\right|\leq2\right\}=\mathbf{1}-P\left\{-2<X\leq2\right\}\\&=\mathbf{1}-\varPhi\left(-\mathbf{0.5}\right)+\varPhi\left(-2.5\right)=\varPhi\left(\mathbf{0.5}\right)-\varPhi\left(2.5\right)+\mathbf{1}=\mathbf{0}.6977.\end{aligned} $$

<!-- page: 28 -->

4.某种型号的电子管寿命 $ X $(以h计)具有概率密度 $ f(x)=\left\{\begin{aligned}&\frac{1000}{x^{2}},x>1000\\&0,\quad 其他\end{aligned}\right. $.现有一大批 

解：电子管寿命大于1500h的概率为 $ P\{X>1500\}=\int_{1500}^{+\infty}\frac{1000}{x^2}dx=1000\left(-\frac{1}{x}\right)_{1500}^{+\infty}=\frac{2}{3} $.

设Y表示5只电子管中寿命大于1500h的个数，故 $ Y\sim b\left(5,\frac{2}{3}\right) $，

则有 $ P\{Y\geq2\}=1-P\{Y=0\}-P\{Y=1\}=1-C_{5}^{0}\left(\frac{2}{3}\right)^{0}\left(\frac{1}{3}\right)^{5}-C_{5}^{1}\left(\frac{2}{3}\right)^{1}\left(\frac{1}{3}\right)^{4}=1-\frac{1}{3^{5}}-5\times\frac{2}{3}\times\frac{1}{3^{4}}=\frac{232}{243} $.

5. 设 K 在  $ (0,5) $ 内服从均匀分布，求方程  $ 4x^{2} + 4Kx + K + 2 = 0 $ 有实根的概率。

解：由已知有 $ f(k)=\begin{cases}\frac{1}{5},0<k<5,\\0,\quad\text{其他}\end{cases} $，方程有实根，则有 $ 16k^{2}-16k-32\geq0 $，解出 $ k\geq2 $或 $ k\leq-1 $，故方程有实根的概率为 $ P\{k\geq2\}=\int_{2}^{5}\frac{1}{5}\mathrm{d}x=\frac{3}{5} $.

<!-- page: 29 -->

<div style="text-align: center;"><div style="text-align: center;">习题2-5 随机变量的函数的分布</div> </div>






1. 设随机变量 X 的分布律为  $ \frac{X}{p_k}\left|\begin{array}{cccc}-2&-1&0&1\\\frac{1}{6}&\frac{1}{3}&\frac{1}{6}&\frac{1}{3}\end{array}\right. $

试求(1) $ Y=2X-1 $; (2) $ Z=X^{2} $的分布律。

解:(1)Y的所有可能取值为-5,-3,-1,1,

由 $ P\{Y=2k-1\}=P\{X=k\}=p_k $，得Y的分布律为 $ \frac{Y}{p_k}\left|\begin{array}{cccc}-5&-3&-1&1\\ \frac{1}{6}&\frac{1}{3}&\frac{1}{6}&\frac{1}{3}\end{array}\right| $.

(2)Z的所有可能取值为1,0,4,

由 $ P\{Z=k^2\}=P\{X=k\}=p_k $，得Z的分布律为 $ \frac{Z}{p_k}\left|\begin{array}{cccc}0&1&4\\\frac{1}{6}&\frac{2}{3}&\frac{1}{6}\end{array}\right| $.

<!-- page: 30 -->

2. 设随机变量  $ X \sim U(0,1) $，求  $ Y = -2\ln X $ 的密度函数。

，

解：由 $ X \sim U(0,1) $，而 $ Y = -2\ln X $为X的单调减函数，

故有反函数为 $ x = e^{-\frac{y}{2}} $，因此y的概率密度为

 $ f_Y(y) = f_X\left(e^{-\frac{y}{2}}\right)\left|\left(e^{-\frac{y}{2}}\right)^\prime\right| = \begin{cases} \dfrac{1}{2}e^{-\frac{y}{2}}, & \text{当} y \geq 0 \text{时}, \\ 0, & \text{当} y < 0 \text{时}, \end{cases} $

即Y服从参数为 $ \dfrac{1}{2} $的指数分布 $ E\left(\dfrac{1}{2}\right) $。

<!-- page: 31 -->

3.设随机变量 $ X\sim N(0,1) $，求 $ Y=|X| $的密度函数。





解：对于 $ Y=|X| $，显然当 $ y<0 $时，有 $ f_Y(y)=0 $；

当 $ y\geq0 $时，因为 $ X\sim N(0,1) $，故有

 $$ \begin{aligned}F_{Y}\left(y\right)&=P\left\{Y\leq y\right\}=P\left\{\left|X\right|\leq y\right\}=P\left\{-y\leq X\leq y\right\}\\&=\varPhi\left(y\right)-\varPhi\left(-y\right)=2\varPhi\left(y\right)-1,\end{aligned} $$ 

故当y>0时，对上式二边求导数，则有

$$F_{Y}^{\prime}(y)=f_{y}(y)=\left(2\Phi(y)-1\right)^{\prime}=2\varphi(y)=2\bullet\frac{1}{\sqrt{2\pi}}e^{-\frac{y^{2}}{2}},$$

因此，$Y=|X|$的概率密度为$$f_{y}(y)=\left\{\begin{array}{ll}\sqrt{\frac{2}{\pi}}\cdot e^{-\frac{y^{2}}{2}},&y\geq0,\\0,&y<0.\end{array}\right.$$

<!-- page: 32 -->

4. 设随机变量  $ X $ 的概率密度为  $ f(x) = \begin{cases} \dfrac{2x}{\pi^2}, & 0 < x < \pi, \\ 0, & \text{其他}, \end{cases} $

求  $ Y = \sin X $ 的概率密度。



解： $ X $在 $ (0,\pi) $上取值时， $ Y=\sin x $在 $ [0,1] $上取值，

故若 $ y<0 $或 $ y>1 $时， $ f_Y(y)=0 $，

而当 $ 0 \leq y \leq 1 $时，Y的分布函数为：

<!-- page: 33 -->

$$ \begin{aligned}&F_{Y}\left(y\right)=P\left\{Y\leq y\right\}=P\left\{\mathbf{0}\leq Y\leq y\right\}\\ &=P\left\{\left(\mathbf{0}\leq\sin x\leq y\right)\right\}\bigcup\left(\mathbf{0}\leq\sin\left(\pi-x\right)\leq y\right)\Big\}\\ &=P\left\{\mathbf{0}\leq x\leq\arcsin y\right\}+P\left\{\mathbf{0}\leq\pi-x\leq\arcsin y\right\}\\ &=P\left\{\mathbf{0}\leq x\leq\arcsin y\right\}+P\left\{\left(\pi-\arcsin y\right)\leq x\leq\pi\right\}\\ &=\int_{0}^{\arcsin y}\frac{2x}{\pi^{2}}\mathrm{d}x+\int_{\pi-\arcsin y}^{\pi}\frac{2x}{\pi^{2}}\mathrm{d}x\\ &=\frac{1}{\pi^{2}}\left(\arcsin y\right)^{2}+1-\frac{1}{\pi^{2}}\left(\pi-\arcsin y\right)^{2}=\frac{2}{\pi}\arcsin y.\\ &\\ & 故所求概率为 f_{Y}\left(y\right)=F_{Y}^{\prime}\left(y\right)=\left\{\begin{matrix}\frac{2}{\pi\sqrt{1-y^{2}}},&0<y<1\\ 0,& 其他 .\end{matrix}\right.\\ \end{aligned} $$

<!-- page: 34 -->

5.假设随机变量X服从参数为2的指数分布，证明 $ Y=1-e^{-2X} $在区间 $ (0,1) $上服从均匀分布。

证：∵  $ X \sim E(2) $，即  $ f_X(x) = \begin{cases} 2e^{-2x}, & x > 0, \\ 0, & \text{其他} \end{cases} $

∴  $ x \in (0, +\infty) $，∴  $ y \in (0, 1) $，∴ 当  $ y \leq 0 $ 时， $ F_Y(y) = 0 $，

当  $ y \geq 1 $ 时， $ F_Y(y) = 1 $，当  $ 0 < y < 1 $ 时，有

 $ F_Y(y) = P\{Y \leq y\} = P\{1 - e^{-2X} \leq y\} = P\{e^{-2X} \geq 1 - y\} = P\{X \leq -\frac{1}{2} \ln(1 - y)\} = F_X\left(-\frac{1}{2} \ln(1 - y)\right) $，

故  $ f_Y(y) = F_Y'(y) = f_X\left(-\frac{1}{2} \ln(1 - y)\right) \cdot \left(\frac{1}{2} \cdot \frac{1}{1 - y}\right) = 1 $，

故有  $ f_Y(y) = \begin{cases} 1, & 0 < y < 1, \\ 0, & \text{其它} \end{cases} $ 因此  $ Y \sim U(0,1) $。

