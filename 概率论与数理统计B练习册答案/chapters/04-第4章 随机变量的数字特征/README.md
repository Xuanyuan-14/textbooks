# 04-第4章 随机变量的数字特征

[返回全书目录](../../README.md)

> PDF 页码：57–76

<!-- page: 57 -->

<div style="text-align: center;"><div style="text-align: center;">习题4-1 数学期望</div> </div>


1. 设X的分布律为:  $ \frac{X}{p_k}\left|\frac{-2}{0.1}\right|=\frac{-1}{0.3}\left|\frac{0}{0.4}\right|=\frac{1}{0.2} $,

求: (1)  $ E(X) $; (2)  $ E(-X+1) $; (3)  $ E(X^2) $.

解: (1)  $ E(X)=(-2)\times0.1+(-1)\times0.3+0\times0.4+1\times0.2=-0.3 $;

(2)  $ E(-X+1)=-E(X)+1=1.3 $;

(3)  $ E(X^2)=(-2)^2\times0.1+(-1)^2\times0.3+0\times0.4+1\times0.2=0.9 $.

2. 设二维随机变量(X,Y)的联合分布律为:  $ \frac{Y\mid X}{-1}\left|\frac{1}{1/4}\right|=\frac{2}{1/2} $. 求  $ E(X) $,  $ E(Y) $,  $ E(X-2Y) $,  $ E(3XY) $.

解:  $ E(X)=1\times\frac{1}{4}+1\times0+2\times\frac{1}{2}+2\times\frac{1}{4}=\frac{7}{4} $;

 $ E(Y)=(-1)\times\frac{1}{4}+(-1)\times\frac{1}{2}+1\times0+1\times\frac{1}{4}=-\frac{1}{2} $;

 $ E(X-2Y)=E(X)-2E(Y)=\frac{7}{4}-2\times\left(-\frac{1}{2}\right)=\frac{11}{4} $;

 $ E(3XY)=3\times\left[1\times(-1)\times\frac{1}{4}+2\times(-1)\times\frac{1}{2}+2\times1\times\frac{1}{4}\right]=-\frac{9}{4} $.

<!-- page: 58 -->

3. 把四个球随机的放入4个盒子中去，设X表示空盒子的个数，求 $ E(X) $.







解法一：先求X的分布律，4个球放到4个盒子中去，共有 $ 4^{4} $种放法，则

 $$ P\left\{X=\mathbf{0}\right\}=\frac{C_{4}^{0}A_{4}^{4}}{4^{4}}=\frac{6}{64};\qquad P\left\{X=1\right\}=\frac{C_{4}^{1}C_{4}^{2}A_{3}^{3}}{4^{4}}=\frac{36}{64}; $$ 

 $$ P\left\{X=2\right\}=\frac{C_{4}^{2}\left(2^{4}-2\right)}{4^{4}}=\frac{21}{64};P\left\{X=3\right\}=\frac{C_{4}^{3}}{4^{4}}=\frac{1}{64}. $$

<!-- page: 59 -->

解法二：引入随机变量 $ X_{i} $，令





 $ X_i = \begin{cases} 1, & 第i个盒子空, \\ 0, & 第i个盒子非空. \end{cases} (i = 1, 2, 3, 4) $,

则有 $ P\{X_i = 1\} = \left(\frac{3}{4}\right)^4 $， $ P\{X_i = 0\} = 1 - \left(\frac{3}{4}\right)^4 $

且 $ X = X_{1} + X_{2} + X_{3} + X_{4} $，

因为 $ E(X_i) = P\{X_i = 1\} = \left(\frac{3}{4}\right)^4 = \frac{81}{256} $，故有

 $$ E\left(X\right)=E\left(X_{1}\right)+E\left(X_{2}\right)+E\left(X_{3}\right)+E\left(X_{4}\right)=4\times\frac{81}{256}=\frac{81}{64}. $$

<!-- page: 60 -->

4. 设连续型随机变量 $X$ 的概率密度为 $f(x) = \begin{cases} ax, & 0 < x < 2 \\ cx + b, & 2 \leq x \leq 4, \\ 0, & \text{其他} \end{cases}$,

已知 $E(X) = 2$, $P\{1 < X < 3\} = \frac{3}{4}$. 求: $(1) a, b, c$ 的值; $(2) \text{令 } Y = e^X$, 求 $E(Y)$.

解: (1) 由已知有: $\int_0^2 ax \, \mathrm{d}x + \int_2^4 (cx + b) \, \mathrm{d}x = 1$,

$\int_0^2 ax^2 \, \mathrm{d}x + \int_2^4 (cx^2 + bx) \, \mathrm{d}x = 2$, $\quad\int_1^2 ax \, \mathrm{d}x + \int_2^3 (cx + b) \, \mathrm{d}x = \frac{3}{4}$, 化简得:

$\begin{cases} 2a + 2b + 6c = 1 \\ 8a + 18b + 56c = 6, \\ 6a + 4b + 10c = 3 \end{cases}$ 解这个方程组得: $a = \frac{1}{4}, b = 1, c = -\frac{1}{4}$.

(2) $E(Y) = E(e^x) = \int_{-\infty}^{+\infty} e^x f(x) \, \mathrm{d}x = \int_0^2 \frac{1}{4} xe^x \, \mathrm{d}x + \int_2^4 \left( -\frac{1}{4}x + 1 \right) e^x \, \mathrm{d}x = \frac{1}{4} \left\{ [xe^x]_0^2 - \int_0^2 e^x \, \mathrm{d}x] - \frac{1}{4} \left\{ [xe^x]_2^4 - \int_2^4 e^x \, \mathrm{d}x] + \int_2^4 e^x \, \mathrm{d}x \right\} = \frac{1}{4} (e^2 + 1) - \frac{1}{4} (3e^4 - e^2) + e^4 - e^2 = \frac{1}{4} e^4 - \frac{1}{2} e^2 + \frac{1}{4} = \frac{1}{4} (e^2 - 1)^2$.

<!-- page: 61 -->

5.设(X,Y)服从在A上的均匀分布，其中A为x轴、y轴及直线 $ x+y+1=0 $所围成的区域，求(1) $ E(X) $;(2) $ E(-3X+2Y) $;(3) $ E(XY) $.

解：如图，A的面积为 $ \frac{1}{2} $，则(X,Y)的概率密度为 $ f(x,y)=\left\{\begin{aligned}&2,-1<x<0,-x-1<y<0,\\&0,\quad 其他.\end{aligned}\right. $

 $$ \left)E\left(X\right)=\int_{-\infty}^{+\infty}\int_{-\infty}^{+\infty}x f\left(x,y\right)\mathrm{d}x\mathrm{d}y=\int_{-1}^{0}2x\mathrm{d}x\int_{-x-1}^{0}\mathrm{d}y=-\frac{1}{3}; $$ 

 $$ E\left(Y\right)=\int_{-\infty}^{+\infty}\int_{-\infty}^{+\infty}yf\left(x,y\right)\mathrm{d}x\mathrm{d}y=-\frac{1}{3}, $$ 

$$  E\left(-3X+2Y\right)=-3E\left(X\right)+2E\left(Y\right)=\frac{1}{3};   \tag*{(3)}$$

 $$ E\left(XY\right)=\int_{-\infty}^{+\infty}\int_{-\infty}^{+\infty}xyf\left(x,y\right)dxdy=\int_{-1}^{0}\int_{-x-1}^{0}2xydxdy=\frac{1}{12}. $$

<!-- page: 62 -->

6.某工厂生产的某种设备的寿命X(以年计)服从指数分布，其概率密度为：

 $ f(x)=\begin{cases}\dfrac{1}{4}e^{-\frac{x}{4}},&x>0\\0,&x\leq0\end{cases} $.工厂规定，出售的设备在售出一年之内可以调换。若工厂售出一台设备赢利100元，调换一台设备厂方需花费300元，试求厂方出售一台设备净赢利的数学期望。

注意：设备的寿命不到一年，就表示可以调换。

解：一台设备在一年内调换的概率为： $ P\{X<1\}=\int_{0}^{1}\frac{1}{4}e^{-\frac{x}{4}}dx=1-e^{-\frac{1}{4}} $。

计Y表示工厂售出一台设备的净赢利值，由题意可得Y的分布律为： $ \frac{Y}{p_k}\left|\frac{100}{e^{-\frac{1}{4}}}\right|\frac{100-300}{1-e^{-\frac{1}{4}}} $，故有 $ E(Y)=100\times e^{-\frac{1}{4}}+(-200)\times\left(1-e^{-\frac{1}{4}}\right)\approx33.64 $元。

<!-- page: 63 -->

<div style="text-align: center;"><div style="text-align: center;">习题4-2 方差</div> </div>


1. 一台设备由三大部件构成，在设备运转过程中，各部件需要调整的概率相应为0.1, 0.2, 0.3，假设各部件的状态相互独立，以X表示同时需要调整的部件数，试求X的数学期望 $ E(X) $和方差 $ D(X) $。

解：引入随机变量 $ X_i = \begin{cases} 1, & 第i个部件需要调整, \\ 0, & 第i个部件不需要调整. \end{cases} $， $ i = 1, 2, 3 $，

则 $ X=X_1+X_2+X_3 $， $ \because X_i\sim\mathbb{0}-1 $分布， $ \therefore E(X_i)=P\{X_i=1\}=p $，

由已知得， $ E(X_1) = 0.1 $， $ E(X_2) = 0.2 $， $ E(X_3) = 0.3 $，

又因为 $ D(X_{i})=E(X_{i}^{2})-E^{2}(X_{i})=p(1-p) $，

由已知得， $ D(X_1) = 0.09, D(X_2) = 0.16, D(X_3) = 0.21 $，

所以  $ E(X)=E(X_1)+E(X_2)+E(X_3)=0.6 $,

 $$ D\left(X\right)=D\left(X_{1}\right)+D\left(X_{2}\right)+D\left(X_{3}\right)=0.46. $$

<!-- page: 64 -->

2. 设随机变量 $X$ 的概率密度为 $f(x) = \begin{cases} \dfrac{1}{2}\cos\dfrac{x}{2}, & 0 \leq x \leq \pi, \\ 0, & \text{其他} \end{cases}$

对 $X$ 独立的重复观察 $4$ 次，用 $Y$ 表示观测值大于 $\dfrac{\pi}{3}$ 的次数，求 $Y^2$ 的数学期望。

解：$P\left\{X > \dfrac{\pi}{3}\right\} = \int_{\dfrac{\pi}{3}}^{\pi} \dfrac{1}{2}\cos\dfrac{x}{2} \, \mathrm{d}x = \int_{\dfrac{\pi}{3}}^{\pi} \cos\dfrac{x}{2} \, \mathrm{d}\left(\dfrac{x}{2}\right) = \sin\dfrac{x}{2}\bigg|_{\dfrac{\pi}{3}}^{\pi} = 1 - \dfrac{1}{2} = \dfrac{1}{2},$

故 $Y \sim b\left(4, \dfrac{1}{2}\right)$，$P\{Y = k\} = C_4^k\left(\dfrac{1}{2}\right)^k\left(\dfrac{1}{2}\right)^{4-k} = \dfrac{1}{16}C_4^k$，$E(Y) = np = 2, D(Y) = npq = 1$，$E(Y^2) = D(Y) + E^2(Y) = 1 + 4 = 5$。

<!-- page: 65 -->

3.设(X,Y)的概率密度为 $ f(x,y)=\begin{cases}12y^2,0\leq y\leq x\leq1\\0,\end{cases} $.求 $ D(X) $和 $ D(Y) $解： $ E(X)=\int_{-\infty}^{+\infty}\int_{-\infty}^{+\infty}xf(x,y)\mathrm{d}x\mathrm{d}y=\int_{0}^{1}12x\mathrm{d}x\int_{0}^{x}y^2\mathrm{d}y=\int_{0}^{1}4x^4\mathrm{d}x=\frac{4}{5} $， $ E(X^2)=\int_{-\infty}^{+\infty}\int_{-\infty}^{+\infty}x^2f(x,y)\mathrm{d}x\mathrm{d}y=\int_{0}^{1}12x^2\mathrm{d}x\int_{0}^{x}y^2\mathrm{d}y=\int_{0}^{1}4x^5\mathrm{d}x=\frac{2}{3} $，所以， $ D(X)=E(X^2)-E^2(X)=\frac{2}{3}-\left(\frac{4}{5}\right)^2=\frac{2}{75} $， $ E(Y)=\int_{-\infty}^{+\infty}\int_{-\infty}^{+\infty}yf(x,y)\mathrm{d}x\mathrm{d}y=\int_{0}^{1}12\mathrm{d}x\int_{0}^{x}y^3\mathrm{d}y=\int_{0}^{1}3x^4\mathrm{d}x=\frac{3}{5} $， $ E(Y^2)=\int_{-\infty}^{+\infty}\int_{-\infty}^{+\infty}y^2f(x,y)\mathrm{d}x\mathrm{d}y=\int_{0}^{1}12\mathrm{d}x\int_{0}^{x}y^4\mathrm{d}y=\int_{0}^{1}\frac{12}{5}x^5\mathrm{d}x=\frac{2}{5} $，所以， $ D(Y)=E(Y^2)-E^2(Y)=\frac{2}{5}-\left(\frac{3}{5}\right)^2=\frac{1}{25} $。

<!-- page: 66 -->

4. 设两个随机变量X,Y相互独立, 且都服从均值为0, 方差为 $ \frac{1}{2} $的正态分布, 求随机变量 $ \left|X-Y\right| $的方差。



解：令 $ Z = X - Y $，由于 $ X,Y \sim N\left(0, \frac{1}{2}\right) $，且相互独立，则 $ Z \sim N(0,1) $。

又 $ D\left(\left|X - Y\right|\right) = D\left(\left|Z\right|\right) = E\left(\left|Z\right|^2\right) - E^2\left(\left|Z\right|\right) = E\left(Z^2\right) - E^2\left(\left|Z\right|\right) $，

而 $ E\left(Z^2\right) = D\left(Z\right) + E^2\left(Z\right) = 1 $，

 $ E\left(\left|Z\right|\right) = \int_{-\infty}^{+\infty}\left|z\right|\frac{1}{\sqrt{2\pi}}e^{-\frac{z^2}{2}}dz = \frac{2}{\sqrt{2\pi}}\int_{0}^{+\infty} ze^{-\frac{z^2}{2}}dz = \sqrt{\frac{2}{\pi}} $，

所以， $ D\left(\left|X - Y\right|\right) = 1 - \frac{2}{\pi} $。

不要把 $ D\left(\left|X - Y\right|\right) $拆为 $ \begin{cases} D(X-Y), X > Y \\ D(Y-X), X < Y \end{cases} $来计算，

因为拆开以后， $ X $就受 $ Y $的限制，它们不再独立了。

所以也不能再用独立的公式 $ D(X - Y) = DX + DY $。

<!-- page: 67 -->

5.在每次试验中，事件A发生的概率为0.6，利用切比雪夫不等式估计在1000次试验中，事件A发生的次数在500～700之间的概率。

解：设X为1000次试验中A发生的次数，则 $ X \sim b(1000,0.6) $，其中 $ E(X)=np=600 $， $ D(X)=npq=240 $，

根据切比雪夫不等式，

 $$  有 P\left\{500<X<700\right\}=P\left\{\left|X-600\right|<100\right\}\geq1-\frac{240}{100^{2}}=1-0.024=0.976. $$

<!-- page: 68 -->

<div style="text-align: center;"><div style="text-align: center;">习题4-3 协方差与相关系数</div> </div>






1.已知随机变量X与Y都服从二项分布B(20,0.1)，且X与Y的相关系数 $ \rho_{XY}=-0.5 $，试求X-Y的方差及X与2Y+X的协方差.

解：由已知有， $ X \sim B(20,0.1) $， $ Y \sim B(20,0.1) $，则

 $ E(X) = E(Y) = 2 $， $ D(X) = D(Y) = 1.8 $，

 $$ \mathbf{c o v}\left(X,Y\right)=\rho_{_{X Y}}\sqrt{D\left(X\right)}\bullet\sqrt{D\left(Y\right)}=-\mathbf{0.5\times1.8}=-\mathbf{0.9}, $$ 

故有， $ D(X - Y) = D(X) + D(Y) - 2\text{cov}(X, Y) = 1.8 + 1.8 + 2 \times 0.9 = 5.4 $， $ \text{cov}(X, 2Y + X) = 2\text{cov}(X, Y) + \text{cov}(X, X) = 2 \times (-0.9) + 1.8 = 0 $。

<!-- page: 69 -->

2. 设二维随机变量  $ (X, Y) $ 服从单位圆内的均匀分布，验证：X 和 Y 不相关，但 X 和 Y 互为无理数，则 X 独立的。

解: $ (X,Y) $的概率密度为 $ f(x,y)=\left\{\begin{aligned}&\frac{1}{\pi},x^{2}+y^{2}\leq1,\\&0,\quad 其他\end{aligned}\right. $

因为X和Y是对称的，故有 $ E(X)=E(Y) $， $ D(X)=D(Y) $，

 $$ \begin{aligned}&E\big(X\big)=\int_{-\infty}^{+\infty}\int_{-\infty}^{+\infty}x f\big(x,y\big)\mathrm{d}x\mathrm{d}y=\frac{1}{\pi}\int_{-1}^{1}x\mathrm{d}x\int_{-\sqrt{1-x^{2}}}^{\sqrt{1-x^{2}}}\mathrm{d}y=\frac{1}{\pi}\int_{-1}^{1}2x\sqrt{1-x^{2}}\mathrm{d}x=-\frac{1}{\pi}\int_{-1}^{1}\sqrt{1-x^{2}}\mathrm{d}\big(1-x^{2}\big)\\ &=-\frac{1}{\pi}\times\frac{2}{3}\times\big(1-x^{2}\big)^{\frac{3}{2}}\Big|_{-1}^{1}=\mathbf{0}=E\big(Y\big),\\ \end{aligned} $$ 

 $$ E\big(X Y\big)=\int_{-\infty}^{+\infty}\int_{-\infty}^{+\infty}x y f\big(x,y\big)\mathrm{d}x\mathrm{d}y=\frac{1}{\pi}\int_{-1}^{1}x\mathrm{d}x\int_{-\sqrt{1-x^{2}}}^{\sqrt{1-x^{2}}}y\mathrm{d}y=\frac{1}{2\pi}\int_{-1}^{1}x\mathrm{d}x\times y^{2}\bigg|_{\sqrt{1-x^{2}}}^{\sqrt{1-x^{2}}}=0, $$ 

所以， $ \mathrm{cov}(X,Y)=E(XY)-E(X)E(Y)=0,\quad\rho_{XY}=0,\quad X $和 $ Y $不相关.

又因为， $ f_x(x)=\int_{-\infty}^{+\infty}f(x,y)\mathrm{d}y=\left\{\begin{aligned}&\frac{1}{\pi}\int_{-\sqrt{1-x^2}}^{\sqrt{1-x^2}}\mathrm{d}y,-1\leq x\leq1\\&0,\quad 其他\end{aligned}\right.=\left\{\begin{aligned}&\frac{2}{\pi}\sqrt{1-x^2},-1\leq x\leq1\\&0,\quad 其他\end{aligned}\right. $

$$f_{Y}(y)=\left\{\begin{array}{ll}\dfrac{2}{\pi}\sqrt{1-y^{2}},-1\leq y\leq1,&\text{显然，}f_{X}(x)f_{Y}(y)\neq f(x,y),\\0,&\text{其他}\end{array}\right.$$ 故X和Y不是相互独立的。

<!-- page: 70 -->

3.设二维随机变量(X,Y)的概率密度为： $ f(x,y)=\left\{\begin{array}{ll}k,0<x<1,0<y<x \\ 0,\end{array}\right. $

其他

求:(1)常数k; (2)E(XY)及 $ \mathrm{cov}(X,Y) $.

解:(1)由 $ \int_{0}^{1}dx\int_{0}^{x}kdy=1 $，得 $ k\int_{0}^{1}xdx=1\Rightarrow\frac{k}{2}x^{2}\bigg|_{0}^{1}=1\Rightarrow\frac{k}{2}=1\Rightarrow k=2 $.

(2)E(XY)=2 $ \int_{0}^{1}xdx\int_{0}^{x}y dy=\int_{0}^{1}x dx\cdot y^{2}\bigg|_{0}^{x}=\int_{0}^{1}x^{3}dx=\frac{1}{4}x^{4}\bigg|_{0}^{1}=\frac{1}{4} $,

E(X)=2 $ \int_{0}^{1}xdx\int_{0}^{x}dy=2\int_{0}^{1}x^{2}dx=\frac{2}{3} $,

E(Y)=2 $ \int_{0}^{1}dx\int_{0}^{x}y dy=\int_{0}^{1}x^{2}dx=\frac{1}{3} $,

所以有， $ \mathrm{cov}(X,Y)=E(XY)-E(X)E(Y)=\frac{1}{4}-\frac{2}{3}\times\frac{1}{3}=\frac{1}{36} $.

<!-- page: 71 -->

4. 设随机变量  $ Y $ 服从参数为1的指数分布，随机变量  $ X_k = \begin{cases} 0, & Y \leq k, \\ 1, & Y > k, \end{cases} $  $ k = 1, 2 $，







(1) 求  $ X_{1} $ 和  $ X_{2} $ 的联合分布律及边缘分布律；

(2) 求  $ \mathrm{cov}(X_1, X_2) $ 和  $ \rho_{X_1 X_2} $.

解: (1) 由已知得Y的概率密度为 $ f_Y(y) = \begin{cases} e^{-y}, & y > 0, \\ 0, & \text{其他}, \end{cases} $ 则

 $ P\{X_1 = 0, X_2 = 0\} = P\{Y \leq 1, Y \leq 2\} = \int_0^1 e^{-y} \, \mathrm{d}y = 1 - e^{-1} $,

 $ P\{X_1 = 0, X_2 = 1\} = P\{Y \leq 1, Y > 2\} = P\{\varnothing\} = 0 $,

 $ P\{X_1 = 1, X_2 = 0\} = P\{Y > 1, Y \leq 2\} = \int_1^2 e^{-y} \, \mathrm{d}y = e^{-1} - e^{-2} $,

 $ P\{X_1 = 1, X_2 = 1\} = P\{Y > 1, Y > 2\} = \int_2^{+\infty} e^{-y} \, \mathrm{d}y = e^{-2} $,

<!-- page: 72 -->

即联合分布律和边缘分布律为： $ \begin{array}{c}X_{1}|X_{2}\quad0\quad1\quad p_{i}.\\\quad0\quad1-e^{-1}\quad0\quad1-e^{-1}\\\quad1\quad e^{-1}-e^{-2}\quad e^{-2}\quad e^{-1}\\p_{\cdot j}\quad1-e^{-2}\quad e^{-2}\quad1\end{array} $

(2)由(1)可知： $ E(X_1X_2) = e^{-2} $，

 $ E(X_1) = P\{X_1 = 1\} = e^{-1} $， $ E(X_2) = P\{X_2 = 1\} = e^{-2} $，

 $ D(X_1) = e^{-1}(1 - e^{-1}) $， $ D(X_2) = e^{-2}(1 - e^{-2}) $，

则 $ \text{cov}(X_1, X_2) = E(X_1X_2) - E(X_1)E(X_2) = e^{-2} - e^{-3} $，

 $ \rho_{X_1X_2} = \frac{\text{cov}(X_1, X_2)}{\sqrt{D(X_1)D(X_2)}} = \frac{1}{\sqrt{e+1}} $。

<!-- page: 73 -->

<div style="text-align: center;"><div style="text-align: center;">习题4-4 矩 协方差 习题4-5 二维正态分布</div> </div>






1. 设随机变量X在区间 $ (a,b) $上服从均匀分布，求k阶原点矩和三阶中心矩。

 $$ \begin{aligned}& 解： 由已知，有 f(x)=\left\{\begin{aligned}&\frac{1}{b-a},a<x<b,\\&0,\quad 其他 \end{aligned}\right.E(X)=\frac{a+b}{2},D(X)=\frac{(b-a)^{2}}{12},\\& 则有，E\left(X^{k}\right)=\int_{-\infty}^{+\infty}x^{k}f(x)\mathrm{d}x=\frac{1}{b-a}\times\frac{1}{k+1}\times x^{k+1}\bigg|_{a}^{b}=\frac{1}{b-a}\times\frac{1}{k+1}\times\left(b^{k+1}-a^{k+1}\right)\\&=\frac{1}{k+1}\left(a^{k}+a^{k-1}b+\cdots+ab^{k-1}+b^{k}\right),\\&E\left(X-E(X)\right)^{3}=\frac{1}{b-a}\int_{a}^{b}\left(x-\frac{a+b}{2}\right)^{3}\mathrm{d}x=\frac{1}{b-a}\int_{a}^{b}\left(x-\frac{a+b}{2}\right)^{3}\mathrm{d}\left(x-\frac{a+b}{2}\right)\\&=\frac{1}{b-a}\times\frac{1}{4}\times\left(x-\frac{a+b}{2}\right)^{4}\bigg|_{a}^{b}=\frac{1}{b-a}\times\frac{1}{4}\times\left[\left(\frac{b-a}{2}\right)^{4}-\left(\frac{a-b}{2}\right)^{4}\right]=0.\end{aligned} $$

<!-- page: 74 -->

2.已知随机变量 $ X\sim N(2,4) $， $ Y\sim N(0,36) $，X与Y的相关系数为 $ \rho_{XY}=-0.5 $，且 $ Z=\frac{X}{2}+\frac{Y}{3} $。求(1)Z的数学期望和方差；(2)X与Z的相关系数。

解：(1) $ E(Z)=E\left(\frac{X}{2}+\frac{Y}{3}\right)=\frac{1}{2}E(X)+\frac{1}{3}E(Y)=\frac{1}{2}\times2+\frac{1}{3}\times0=1 $， $ D(Z)=D\left(\frac{X}{2}+\frac{Y}{3}\right)=\frac{1}{4}D(X)+\frac{1}{9}D(Y)+2\times\frac{1}{2}\times\frac{1}{3}\operatorname{cov}(X,Y)=\frac{1}{4}\times4+\frac{1}{9}\times36+\frac{1}{3}\times(-0.5)\times2\times6=1+4-2=3 $。

(2) $ \operatorname{cov}(X,Z)=\operatorname{cov}\left(X,\frac{X}{2}+\frac{Y}{3}\right)=\frac{1}{2}\operatorname{cov}(X,X)+\frac{1}{3}\operatorname{cov}(X,Y)=\frac{1}{2}\times4+\frac{1}{3}\times(-0.5)\times2\times6=2-2=0 $，所以有， $ \rho_{XZ}=\frac{\operatorname{cov}(X,Z)}{\sqrt{D(X)}\sqrt{D(Z)}}=0 $。

<!-- page: 75 -->

3. 设  $ (X, Y) $ 服从二维正态分布，且  $ D(X) = \sigma_X^2 $， $ D(Y) = \sigma_Y^2 $。证明：







当 $ a^{2}=\frac{\sigma_{X}^{2}}{\sigma_{Y}^{2}} $时，随机变量W=X-aY与V=X+aY相互独立.

证明：因为(X,Y)服从二维正态分布，而W与V分别是X,Y的线性组合，根据性质3(正态变量的线性变换不变性)可知,(W,V)也是服从二维正态分布，而 $ \mathrm{cov}(W,V)=\mathrm{cov}(X-aY,X+aY)=\mathrm{cov}(X,X)+a\mathrm{cov}(X,Y)-a\mathrm{cov}(Y,X)-a^2\mathrm{cov}(Y,Y)=\sigma_X^2-\frac{\sigma_X^2}{\sigma_Y^2}\times\sigma_Y^2=0 $，

所以， $ \rho_{wv}=0 $，即W与V是不相关的，

根据性质4，在n维正态分布中，线性相关与相互独立是等价的，

故知W与V是相互独立的。

<!-- page: 76 -->

4.五家商店联营，它们每两周售出的某种农产品的数量(以kg计)分别为 $ X_{1},X_{2},X_{3},X_{4} $（ $ X_{1} $小于X_{2}， $ X_{3} $小于X_{4}），X_{4}小于X_{1}，X_{2}小于X_{3}，X_{4}小于X_{1}）。已知 $ X_{1}\sim N(200,225) $， $ X_{2}\sim N(240,240) $， $ X_{3}\sim N(180,225) $， $ X_{4}\sim N(260,265) $， $ X_{5}\sim N(320,270) $，且相互独立，商店每隔两周进货一次，为使新的供货到达前商店不会脱销的概率大于0.99，问商店的仓库至少应储存多少千克该产品？

解：设Y表示这5家商店该产品的总销售量，即 $ Y=X_{1}+X_{2}+X_{3}+X_{4}+X_{5} $，因为这5个变量相互独立且服从正态分布，故Y也服从正态分布(性质1)，且 $ E(Y)=200+240+180+260+320=1200 $， $ D(Y)=225+240+225+265+270=35^{2} $。

再设仓库至少应储存n千克该产品，才能使新的供货到达前商店不会脱销的概率大于0.99，依题意，n应满足条件 $ P\{Y\leq n\}>0.99 $。

由于 $ Y\sim N(1200,35^{2}) $，

故有 $ P\{Y\leq n\}=P\left\{\frac{Y-1200}{35}\leq\frac{n-1200}{35}\right\}=\Phi\left(\frac{n-1200}{35}\right) $，

则有 $ \Phi\left(\frac{n-1200}{35}\right)>0.99=\Phi(2.33) $，从而有， $ \frac{n-1200}{35}>2.33 $，

解出， $ n>1281.55 $，即 $ n=1282 $。

