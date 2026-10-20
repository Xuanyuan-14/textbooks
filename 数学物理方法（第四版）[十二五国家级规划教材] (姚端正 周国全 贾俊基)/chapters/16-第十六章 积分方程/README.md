# 16-第十六章 积分方程

[返回全书目录](../../README.md)

> PDF 页码：319–332

<!-- page: 319 -->

积分方程是研究数学其他学科和各种物理问题的一个重要数学工具。它在弹性介质理论和流体力学中应用很广，也常见于理论物理中。本章将介绍求解积分方程的理论和方法，主要讨论非奇异积分方程求解的三个方面。首先我们介绍了几种解积分方程的直观明显的方法；其次，我们讨论了如何将施密特-希尔伯特(Schmidt-Hilbert)理论用于解积分方程；最后，我们介绍了维纳-霍普夫(Wiener-Hopf)方法，这是一种用于求解特殊类型积分方程的更简捷的变换方法。

### 16.1 积分方程的几种解法

## 1. 方程的分类

在方程中，若未知函数在积分号下出现，则称这种方程为积分方程。在这章中，我们将仅讨论一些简单类型的积分方程。一般的线性积分方程，可写为如下的形式：

$$  h(x)g(x)-\lambda\int_{a}^{b}K(x,y)g(y)\mathrm{d}y=f(x)   \tag*{(16.1.1)}$$

其中， $ h(x) $ 和  $ f(x) $ 是已知函数， $ g(x) $ 是未知函数， $ \lambda $ 是常数因子（经常起一个本征值的作用），而  $ K(x,y) $ 被称为积分方程的核，也是已知函数。

在方程(16.1.1)中，若 $ h(x)=0,\lambda=1 $，则有

$$  \int_{a}^{b}K(x,y)g(y)\mathrm{d}y=f(x)   \tag*{（16.1.2）}$$

称为第一类的弗雷德霍姆(Fredholm)方程；若 $ h(x)=1 $，则有

$$  g(x)-\lambda\int_{a}^{b}K(x,y)g(y)\mathrm{d}y=f(x)   \tag*{（16.1.3）}$$

称为第二类的弗雷德霍姆方程. 有时候, 对于 y > x 时,  $ K(x, y) = 0 $. 在这种情况下, 积分上限为 x, 即方程 (16.1.2) 和 (16.1.3) 变为

$$  \int_{a}^{x}K(x,y)g(y)\mathrm{d}y=f(x)   \tag*{(16.1.4)}$$

$$  g(x)-\lambda\int_{a}^{x}K(x,y)g(y)\mathrm{d}y=f(x)   \tag*{（16.1.5）}$$

分别称为第一类和第二类的伏特拉(Volterra)方程.

积分方程也可采用算符的形式来表示，即方程(16.1.1)可写为

$$  (h-\lambda\mathbf{K})g(x)=f(x)   \tag*{(16.1.6)}$$

<!-- page: 320 -->

其中 K 为积分算符，它表示用核相乘并对 y 从 a 到 b 的积分。将积分方程写成这种形式，易于与含有矩阵和微分算符的算符方程相比较。

以上各方程中，若  $ f(x)\equiv0 $，则为齐次方程.

## 2. 退化核的方程的解法

如果积分方程的核具有如下的形式

$$  K(x,y)=\sum_{i=1}^{n}\varphi_{i}(x)\psi_{i}(y)   \tag*{(16.1.7)}$$

则被称为是退化的。具有退化核的积分方程，可用初等的方法来求解。下面，我们将通过二个具体的例子来说明如何求解退化核方程。

#### 例 1 求解积分方程

$$  g(x)-\lambda\int_{0}^{1}(xy^{2}+x^{2}y)g(y)\mathrm{d}y=x   \tag*{（16.1.8）}$$

解令

$$  A=\int_{0}^{1}y^{2}g(y)\mathrm{d}y,\quad B=\int_{0}^{1}y g(y)\mathrm{d}y   \tag*{(16.1.9)}$$

则(16.1.8)变为

$$  g(x)=x+\lambda A x+\lambda B x^{2}   \tag*{(16.1.10)}$$

则将(16.1.10)式代入(16.1.9)式得

$$  \left\{\begin{aligned}A&=\frac{1}{4}+\frac{1}{4}\lambda A+\frac{1}{5}\lambda B\\ B&=\frac{1}{3}+\frac{1}{3}\lambda A+\frac{1}{4}\lambda B\end{aligned}\right.   \tag*{（16.1.11）}$$

方程组(16.1.11)的解是

 $$ A=\frac{60+\lambda}{240-120\lambda-\lambda^{2}},\qquad B=\frac{80}{240-120\lambda-\lambda^{2}} $$ 

代入(16.1.10)式，于是得积分方程(16.1.8)的解为

$$  g(x)=\frac{(240-60\lambda)x+80\lambda x^{2}}{240-120\lambda-\lambda^{2}}   \tag*{（16.1.12）}$$

注意，有两个  $ \lambda $ 的值可使我们的解(16.1.12)式变为无穷大。当  $ \lambda $ 取某些特殊值时，齐次积分方程有非零解，这样的  $ \lambda $ 值称为积分方程的本征值，而相应的非零解称做本征函数。

由上例我们看到，如果核是退化的，则解一个积分方程(16.1.3)的问题就简化为解一个大家非常熟悉的代数方程组的问题。如果退化核(16.1.7)有N项，显然将有N个本征值。当然它们不一定都不同。既然退化核方程的解是与相应的线性代数方程组密切相关的，所以退化核方程的许多性质可由相应的代数方程组的有关性质导出。弗雷德霍姆将之简化为一系列理论，这些理论被人们称为弗雷德霍姆定理。我们将不加证明的叙述如下，因为根据学生以往所具有的本征值和代数方程组方面的经验

<!-- page: 321 -->

验，这些理论，应是不难被接受和证明的 $ ^{①} $.

定理 16.1 如果  $ \lambda $ 不是本征值，则对于任何的非齐次项  $ f(x) $，非齐次方程 (16.1.3) 有唯一的解；如果  $ \lambda $ 是本征值，则齐次方程

$$  g(x)-\lambda\int_{a}^{b}K(x,y)g(y)\mathrm{d}y=0   \tag*{(16.1.13)}$$

至少有一个非平凡解即本征函数，而且与一个本征值相对应的、线性独立的本征函数只有一个.

定理 16.2 如果  $ \lambda $ 不是一个本征值，那么  $ \lambda $ 也不是转置方程

$$  g(x)-\lambda\int_{a}^{b}K(y,x)g(y)\mathrm{d}y=f(x)   \tag*{(16.1.14)}$$

的一个本征值；如果  $ \lambda $ 是一个本征值，则  $ \lambda $ 也是转置方程的一个本征值，即

$$  g(x)-\lambda\int_{a}^{b}K(y,x)g(y)\mathrm{d}y=0   \tag*{(16.1.15)}$$

至少有一个非平凡解.

定理 16.3 若  $ \lambda $ 是一个本征值，则非齐次方程（16.1.3）有解的充要条件是： $ f(x) $ 与转置齐次方程（16.1.15）的一切解正交. 即

$$  \int_{a}^{b}\varphi(x)f(x)\mathrm{d}x=0   \tag*{(16.1.16)}$$

其中  $ \varphi(x) $ 满足 (16.1.15) 式.

事实上，定理16.2是这样一个事实的模拟，即矩阵和它的转置具有同样的本征值。如果我们以 $ \varphi(x) $乘以(16.1.3)式并对x积分，便可得到条件(16.1.16)。

顺便提及，弗雷德霍姆定理仅严格地适用于非奇异的积分方程。奇异积分方程 $ ^{②} $的理论是一个不同的问题。

对于具有退化核的伏特拉方程，常常能通过求微分而变为微分方程。我们仍以一个具体的例子说明。

例2

$$  u(x)-\int_{0}^{x}xy u(y)\mathrm{d}y=x   \tag*{(16.1.17)}$$

解令

 $$ g(x)=\int_{0}^{x}y u(y)\mathrm{d}y $$ 

代入方程(16.1.17)，则有

 $$ u(x)=x+x g(x) $$ 

所以

 $$ g^{^{\prime}}(x)=xu(x)=x[x+xg(x)] $$ 

解此微分方程得

 $$ g(x)=-1+c\mathrm{e}^{x^{3}/3} $$ 

于是得

 $$ u(x)=c x\mathrm{e}^{x^{3}/3} $$ 

将之代入原方程(16.1.17)可求得 c=1.

<!-- page: 322 -->

## 3. 具有位移核的方程的求解

如果核仅仅是 $  (x-y)  $的一个函数，即所谓的位移核，且积分范围是一 $ \infty $到 $ +\infty $，则我们可以应用傅里叶变换来求解。考虑方程

$$  g(x)-\lambda\int_{-\infty}^{\infty}K(x-y)g(y)\mathrm{d}y=\varphi(x)   \tag*{（16.1.18）}$$

对此方程进行傅氏变换，并记

 $$ F[g(x)]=\tilde{g}(\omega),\quad F[K(x,y)]=\int_{-\infty}^{\infty}K(x,y)\mathrm{e}^{-\mathrm{i}\omega x}\mathrm{d}x=\tilde{K}(\omega),\quad F[\varphi(x)]=\tilde{\varphi}(\omega) $$ 

则由卷积定理有

 $$ F\Big[\int_{-\infty}^{\infty}K(x-y)g(y)\mathrm{d}y\Big]=\widetilde{K}(\omega)\widetilde{g}(\omega) $$ 

于是积分方程(16.1.18)变为

 $$ \tilde{g}(\omega)=\tilde{\varphi}(\omega)+\lambda\tilde{K}(\omega)\tilde{g}(\omega) $$ 

 $$ \tilde{g}(\omega)=\frac{\tilde{\varphi}(\omega)}{1-\lambda\tilde{K}(\omega)} $$ 

因此

如果我们能求上式的逆变换，则我们就能得到方程(16.1.18)的解.

如果积分区间是从 0 到 x，具有一位移核，且被积函数对于 x<0 等于 0，则我们可用拉氏变换来求解。因为在这种情况下也有相应的卷积积分定理。

## 4. 迭代解法

解积分方程

$$  g(x)=f(x)+\lambda\int_{a}^{b}K(x,y)g(y)\mathrm{d}y   \tag*{(16.1.19)}$$

的一个直接方法是迭代法，我们首先取近似

 $$ g_{0}(x)\approx f(x) $$ 

作为零级近似将此式代入方程(16.1.19)式右边的积分中，便得到第一级近似

 $$ g_{1}(x)=f(x)+\lambda\int_{a}^{b}K(x,y)f(y)\mathrm{d}y $$ 

再将一级近似代入(16.1.19)式右边，便得到二级近似

 $$ g_{2}(x)=f(x)+\lambda\int_{a}^{b}K(x,y)f(y)\mathrm{d}y+\lambda^{2}\int_{a}^{b}\mathrm{d}y\int_{a}^{b}\mathrm{d}y^{\prime}K(x,y)K(y,y^{\prime})f(y^{\prime}) $$ 

重复迭代，于是得级数

$$  g(x)=f(x)+\sum_{n=1}^{\infty}\lambda^{n}\int_{a}^{b}K_{n}(x,y)f(y)\mathrm{d}y   \tag*{（16.1.20）}$$

其中

$$  \left\{\begin{aligned}&K_{1}(x,y)=K(x,y)\\ &K_{n+1}(x,y)=\int_{a}^{b}K(x,y^{\prime})K_{n}(y^{\prime},y)\mathrm{d}y^{\prime},\quad n=1,2,\cdots\end{aligned}\right.   \tag*{(16.1.21)}$$

<!-- page: 323 -->

被称为诺伊曼级数或积分方程(16.1.19)的诺伊曼解. 可以证明, 如果核  $ K(x, y) $ 和  $ f(x) $ 在区间  $ a \leqslant x, y \leqslant b $ 上连续, 对于足够小的  $ \lambda^{\otimes} $, 该级数解将收敛.

例 3 对于粒子散射的问题，描述粒子运动的薛定谔方程是

 $$ -\frac{\hbar^{2}}{2m}\Delta\varphi(\boldsymbol{r})+V(\boldsymbol{r})\varphi(\boldsymbol{r})=E\varphi(\boldsymbol{r}) $$ 

其中， $ \varphi(r) $ 表示粒子的波函数，第一项表示粒子的动能， $ V(r) $ 表示作用势，E 表示系统的总能量，它可表为

 $$ E=\frac{\hbar^{2}k^{2}}{2m} $$ 

故方程又可写为

 $$ \Delta\varphi(\boldsymbol{r})+k^{2}\varphi(\boldsymbol{r})=\frac{2m}{\hbar^{2}}V(\boldsymbol{r})\varphi(\boldsymbol{r}) $$ 

此方程具有边界条件

 $$ \varphi(r)\mid_{r\to\infty}\to\mathrm{e}^{\mathrm{i}k\cdot r}+f(\theta,\varphi)\frac{\mathrm{e}^{\mathrm{i}k r}}{r} $$ 

此式第一项表示入射粒子的平面波，第二项表示入射粒子与 $ V(r) $的作用而散射的粒子的球面波. $ k^{2}=2mE/\hbar^{2} $，（k为波矢， $ |k|=k $）。于是，由格林函数法知亥姆霍兹方程（16.1.22）的格林函数为

 $$ G(\boldsymbol{r},\boldsymbol{r}^{\prime})=\frac{1}{-4\pi}\frac{\mathrm{e}^{i k|\boldsymbol{r}-\boldsymbol{r}^{\prime}|}}{|\boldsymbol{r}-\boldsymbol{r}^{\prime}|} $$ 

这样，我们可以将散射问题转变为积分方程

 $$ \varphi(\boldsymbol{r})=\mathrm{e}^{ik\cdot r}-\frac{2m}{4\pi\hbar^{2}}\int\mathrm{d}\boldsymbol{r}^{\prime}\frac{\mathrm{e}^{ik|\boldsymbol{r}-\boldsymbol{r}^{\prime}|}}{|\boldsymbol{r}-\boldsymbol{r}^{\prime}|}V(\boldsymbol{r}^{\prime})\varphi(\boldsymbol{r}^{\prime}) $$ 

其中第一项是用来调整解使之满足边界条件的补充(修正)函数. 解可以写为诺伊曼级数(16.1.21). 由第一次迭代，即取  $ \varphi_{0}(r)=\mathrm{e}^{ik\cdot r} $，我们可以得到一非常重要的结果，被称做玻恩(Born)近似

 $$ \varphi(\boldsymbol{r})\approx\mathrm{e}^{\mathrm{i}k\cdot r}-\frac{m}{2\pi\hbar^{2}}\int\mathrm{d}\boldsymbol{r}^{\prime}\frac{\mathrm{e}^{\mathrm{i}k|\boldsymbol{r}-\boldsymbol{r}^{\prime}|}}{|\boldsymbol{r}-\boldsymbol{r}^{\prime}|}V(\boldsymbol{r}^{\prime})\mathrm{e}^{\mathrm{i}k\cdot r^{\prime}} $$ 

记

 $$ \varphi_{1}(\boldsymbol{r})=-\frac{m}{2\pi\hbar^{2}}\int\frac{\mathrm{e}^{\mathrm{i}k\left|\boldsymbol{r}-\boldsymbol{r}^{\prime}\right|}}{\left|\boldsymbol{r}-\boldsymbol{r}^{\prime}\right|}V(\boldsymbol{r}^{\prime})\mathrm{e}^{\mathrm{i}k\cdot\boldsymbol{r}^{\prime}}\mathrm{d}\boldsymbol{r}^{\prime} $$ 

继续迭代遂有

 $$ \varphi_{2}(\boldsymbol{r})=\left(-\frac{m}{2\pi\hbar^{2}}\right)^{2}\iint\frac{\mathrm{e}^{\mathrm{i}k\left|\boldsymbol{r}-\boldsymbol{r}^{\prime}\right|}}{\left|\boldsymbol{r}-\boldsymbol{r}^{\prime}\right|}V(\boldsymbol{r}^{\prime})\frac{\mathrm{e}^{\mathrm{i}k\left|\boldsymbol{r}^{\prime}-\boldsymbol{r}^{\prime\prime}\right|}}{\left|\boldsymbol{r}^{\prime}-\boldsymbol{r}^{\prime\prime}\right|}V(\boldsymbol{r}^{\prime\prime})\mathrm{e}^{\mathrm{i}k\cdot\boldsymbol{r}^{\prime\prime}}\mathrm{d}\boldsymbol{r}^{\prime}\mathrm{d}\boldsymbol{r}^{\prime\prime} $$ 

于是解可表为级数

 $$ \varphi(\boldsymbol{r})=\varphi_{0}(\boldsymbol{r})+\varphi_{1}(\boldsymbol{r})+\varphi_{2}(\boldsymbol{r})+\cdots $$ 

这个级数解当  $ V(r) $ 较小时，便能很快收敛.

## 5. 弗雷德霍姆解法

弗雷德霍姆用下述方法，得到了方程（16.1.19）一个更完善的级数解，即通过细

<!-- page: 324 -->

分积分区间 a<x<b，用求和代替积分，解得到的代数方程，然后讨论无限多的细分的极限，结果得到积分方程(16.1.19)的解为

$$  g(x)=f(x)+\lambda\int_{a}^{b}R(x,y;\lambda)f(y)\mathrm{d}y   \tag*{（16.1.23）}$$

其中  $ R(x,y;\lambda) $ 被称为解核，是两个无穷级数的比

$$  R(x,y;\lambda)=\frac{D(x,y;\lambda)}{D(\lambda)}   \tag*{(16.1.24)}$$

$$  D(x,y;\lambda)\equiv\sum_{n=0}^{\infty}\frac{(-1)^{n}}{n!}\lambda^{n}B_{n}(x,y)   \tag*{（16.1.25）}$$

$$  D(\lambda)\equiv\sum_{n=0}^{\infty}\frac{(-1)^{n}}{n!}C_{n}\lambda^{n}   \tag*{（16.1.26）}$$

而 $ B_{n} $的定义为

$$  \left\{\begin{aligned}&B_{0}(x,y)\equiv K(x,y)\\ &B_{n}(x,y)\equiv\int_{a}^{b}\int_{a}^{b}\cdots\int_{a}^{b}K\binom{x\;t_{1}\cdots t_{n}}{y\;t_{1}\cdots t_{n}}\mathrm{d}t_{1}\mathrm{d}t_{2}\cdots\mathrm{d}t_{n},\quad n=1,2,3\cdots\end{aligned}\right.   \tag*{（16.1.27）}$$

其中，行列式

$$  K\binom{x\;t_{1}t_{2}\cdots t_{n}}{y\;t_{1}t_{2}\cdots t_{n}}\equiv\left|\begin{matrix}K(x,y)K(x,t_{1})\cdots K(x,t_{n})\\ K(t_{1},y)K(t_{1},t_{1})\cdots K(t_{1},t_{n})\\ \cdots\cdots\cdots\\ K(t_{n},y)K(t_{n},t_{1})\cdots K(t_{n},t_{n})\end{matrix}\right|   \tag*{（16.1.28）}$$

 $ C_{n} $ 的定义为

$$  C_{0}\equiv1,\quad C_{n}\equiv\int_{a}^{b}\int_{a}^{b}\cdots\int_{a}^{b}K\binom{t_{1}t_{2}\cdots t_{n}}{t_{1}t_{2}\cdots t_{n}}\mathrm{d}t_{1}\mathrm{d}t_{2}\cdots\mathrm{d}t_{n},\quad n=1,2,3\cdots   \tag*{（16.1.29）}$$

可以证明

$$  C_{n+1}=\int_{a}^{b}B_{n}(y,y)\mathrm{d}y,\quad n=0,1,2\cdots   \tag*{（16.1.30）}$$

$$  B_{n}(x,y)=C_{n}K(x,y)-n\int_{a}^{b}K(x,t)B_{n-1}(t,y)\mathrm{d}t,\quad n=1,2,\cdots   \tag*{（16.1.31）}$$

弗雷德霍姆解的重要性在于，(16.1.23)式和(16.1.25)式是收敛的，不像诺伊曼级数却常常发散.本征值可通过分母函数 $ D(\lambda) $求得.

例4 求解方程

 $$ g(x)=f(x)+\lambda\int_{0}^{1}(x+y)g(y)\mathrm{d}y $$ 

其中  $ f(x) $ 是已知函数，而  $ \lambda \neq -6 \pm 4\sqrt{3} $

解 此处核为  $ K(x,y)=x+y $，故由(16.1.29)式和(16.1.27)式有

 $$ C_{0}=1,\qquad B_{0}(x,y)=x+y $$

<!-- page: 325 -->

在此基础上利用(16.1.30)式和(16.1.31)式可计算出

 $$ C_{1}=\int_{0}^{1}(y+y)\mathrm{d}y=1 $$ 

 $$ B_{1}(x,y)=(x+y)-\int_{0}^{1}(x+t)(t+y)\mathrm{d}t=\frac{x+y}{2}-xy-\frac{1}{3} $$ 

 $$ C_{2}=\int_{0}^{1}\left(y-y^{2}-\frac{1}{3}\right)\mathrm{d}y=-\frac{1}{6} $$ 

 $$ B_{2}(x,y)=-\frac{1}{6}(x+y)-2\int_{0}^{1}(x+t)\left(\frac{t+y}{2}-ty-\frac{1}{3}\right)\mathrm{d}t=0 $$ 

从而

 $$ C_{n}\equiv0,\quad B_{n}\equiv0,\quad n\geqslant3 $$ 

故由(16.1.25)式和(16.1.26)式有

 $$ D(x,y;\lambda)=(x+y)-\left(\frac{x+y}{2}-xy-\frac{1}{3}\right)\lambda $$ 

 $$ D(\lambda)=1-\lambda+\frac{1}{2}\Big(-\frac{1}{6}\Big)\lambda^{2}=1-\lambda-\frac{\lambda^{2}}{12} $$ 

代入解核公式得

 $$ R(x,y;\lambda)=\frac{x+y-\left(\frac{x+y}{2}-xy-\frac{1}{3}\right)\lambda}{1-\lambda-\frac{\lambda^{2}}{12}} $$ 

将此结果代入(16.1.23)式，即得需求解方程的解为

 $$ g(x)=f(x)-12\lambda\int_{0}^{1}\frac{(x+y)-\left(\frac{x+y}{2}-xy-\frac{1}{3}\right)\lambda}{\lambda^{2}+12\lambda-12}f(y)\mathrm{d}y $$ 

注 ① 见参考文献[8]，第Ⅰ卷.

②如果积分方程的积分区间为无限或核有奇异性，则称为奇异积分方程.

③易于证明，当 $ \left|\lambda\right|\leqslant\frac{\rho}{M(b-a)}<\frac{1}{M(b-a)},\quad M=\max\left|K(x,y)\right| $时即可.

#### 习题16.1

1. 解积分方程

(1)  $  u(x) = \mathrm{e}^x + \lambda \int_0^1 x \, tu(t) \, \mathrm{d}t;  $

(2) $ u(x)=\lambda\int_{0}^{\pi}u(t)\sin(x-t)dt $ (两个本征值；两个解).

2. 求解

 $$ g(x)=x^{2}+\int_{0}^{1}x y g(y)\mathrm{d}y $$ 

3. 求解积分方程

 $$ (1)u(x)=x+\lambda\int_{0}^{\infty}\mathrm{e}^{-y}u(y)\mathrm{d}y;\quad(2)u(x)=\lambda\int_{-x}^{x}u(y)\cos y\mathrm{d}y. $$

<!-- page: 326 -->

4.（1）求下列积分方程的本征函数和本征值：

 $$ g(x)=\lambda\int_{0}^{1}\mathrm{e}^{x-y}g(y)\mathrm{d}y $$ 

（2）求解积分方程

 $$ g(x)=\mathrm{e}^{x}+\lambda\int_{0}^{1}\mathrm{e}^{x-y}g(y)\mathrm{d}y $$ 

5. 求解下列方程：

(1)  $ g(x) = x + \int_{0}^{x} g(y) \, dy $;

(2)  $ u(x) = x^{\varepsilon} + \lambda \int_{0}^{x} (x - y)^{\varepsilon} u(y) \, \mathrm{d}y $ （ $ \varepsilon $ 为整数）.

6. 求解积分方程

 $$ g(x)=x+\lambda\int_{0}^{1}y(x+y)g(y)\mathrm{d}y. $$ 

（1）用弗雷德霍姆方法；

（2）用诺伊曼方法（保留到 $ \lambda^{2} $项）.

7. 对  $ u(x) $ 求解

 $$ (1)u(x)=\mathrm{e}^{-x^{2}}+\lambda\int_{-\infty}^{\infty}\mathrm{e}^{-(x-y)^{2}}u(y)\mathrm{d}y;\quad(2)u(x)=\frac{1}{\cosh x}+\lambda\int_{-\infty}^{\infty}\frac{u(y)}{\cosh(x-y)}\mathrm{d}y. $$ 

8. 求解积分方程

 $$ g(x)=\mathrm{e}^{-|x|}+\lambda\int_{0}^{\infty}g(y)\cos x y\mathrm{d}y $$ 

提示：对积分方程取余弦变换.

9. 求解积分方程

 $$ g(x)=\mathrm{e}^{-|x|}+\lambda\int_{-\infty}^{\infty}\mathrm{e}^{-|x-y|}g(y)\mathrm{d}y $$ 

当 $ x\to\pm\infty $时， $ g(x) $为有限值.

### 16.2 施密特-希尔伯特理论

现在，我们考虑一种不同于诺伊曼级数和弗雷德霍姆级数的近似方法。这一近似方法是以考虑齐次积分方程的本征值和本征函数为基础的。

一个核  $ K(x,y) $，如果满足

 $$ K(x,y)=K(y,x) $$ 

则  $ K(x,y) $ 被称为对称核. 而如果

 $$ K(x,y)=\bar{K}(y,x) $$ 

则  $ K(x,y) $ 被称为厄米 (Hermite) 核。其中  $ \overline{K}(y,x) $ 表示  $ K(y,x) $ 的共轭。一个厄米核的本征值是实数，而属于不同本征值的本征函数是正交的 $ ^{①} $。这些论述的证明与矩阵的有关证明等同，我们留给学生自己证明。

## 1. 施密特-希尔伯特定理

设对称核  $ K(x,y) $ 的正交归一的本征函数族为  $ \{g_{i}(x)\}(i=1,2,3\cdots) $，相应的本

<!-- page: 327 -->

征值为 $ \lambda_{i} $，且 $ \int_{a}^{b}\left|K(x,y)\right|^{2}\mathrm{d}y $有界，则对于任何平方可积的函数 $ h(x) $，函数

$$  f(x)\equiv\int_{a}^{b}K(x,y)h(y)\mathrm{d}y   \tag*{（16.2.1）}$$

可以展开为本征函数族 $ \left\{g_{i}(x)\right\} $的绝对一致收敛的级数

$$  f(x)=\sum_{i=1}^{\infty}\frac{1}{\lambda_{i}}(g_{i},h)g_{i}(x)   \tag*{（16.2.2）}$$

其中

$$  \left(g_{i},h\right)=\int_{a}^{b}g_{i}(x)h(x)\mathrm{d}x,\quad i=1,2,3\cdots   \tag*{（16.2.3）}$$

 $ \bar{g}_{i}(x) $ 为  $ g_{i}(x) $ 的复共轭.

证 设  $ f(x)=\sum_{i=1}^{\infty}f_{i}g_{i}(x) $，则

 $$ f_{i}=(g_{i},f)=\int_{a}^{b}f(x)\overline{g}_{i}(x)\mathrm{d}x $$ 

将(16.2.1)式代入上式，并利用 $ K(y,x)=\overline{K}(y,x) $和 $ g_{i}(y)=\lambda_{i}\int_{a}^{b}K(y,x)g_{i}(x)dx $，则得

 $$ f_{i}=\int_{a}^{b}\int_{a}^{b}K(x,y)\bar{g}_{i}(x)h(y)\mathrm{d}x\mathrm{d}y=\frac{1}{\lambda_{i}}\int_{a}^{b}\bar{g}_{i}(x)h(y)\mathrm{d}y=\frac{1}{\lambda_{i}}(g_{i},h) $$ 

于是(16.2.2)得证.至于一致收敛性的证明在此略去.

## 2. 具有对称核的方程的解

定理 16.4 设对称核  $ K(x,y) $ 的正交归一的本征函数族为  $ \{g_{i}(x)\} $，相应的本征值是  $ \{\lambda_{i}\} $，如果  $ \int_{a}^{b} |K(x,y)|^{2} \, dx $ 有界，且函数  $ f(x) $ 是平方可积的，则当  $ \lambda \neq \lambda_{i} $ 时，弗雷德霍姆积分方程

$$  g(x)-\lambda\int_{a}^{b}K(x,y)g(y)\mathrm{d}y=f(x)   \tag*{(16.2.4)}$$

的解为

$$  g(x)=\lambda\sum_{i=1}^{\infty}\frac{(g_{i},f)}{\lambda_{i}-\lambda}g_{i}(x)+f(x)   \tag*{（16.2.5）}$$

并称之为施密特公式.

证 由方程(16.2.4)有

 $$ \frac{g(x)-f(x)}{\lambda}=\int_{a}^{b}K(x,y)g(y)\mathrm{d}y $$ 

这与上述的施密特-希尔伯特定理中的(16.2.1)式形式完全相同，故由施密特-希尔伯特定理中的(16.2.2)式，有

$$  \frac{g(x)-f(x)}{\lambda}=\sum_{i=1}^{\infty}\frac{(g_{i},g)}{\lambda_{i}}g_{i}(x)   \tag*{(16.2.6)}$$

<!-- page: 328 -->

以 $ \bar{g}_{j}(x) $乘以上式两边，并对x积分，则有

 $$ \frac{1}{\lambda}\left[\int_{a}^{b}g(x)\overline{g}_{j}(x)\mathrm{d}x-\int_{a}^{b}f(x)\overline{g}_{j}(x)\right]\mathrm{d}x=\sum_{i=1}^{\infty}\frac{(g_{i},g)}{\lambda_{i}}\int_{a}^{b}g_{i}(x)\overline{g}_{j}(x)\mathrm{d}x $$ 

利用本征函数的正交性，于是有

 $$ \frac{(g_{j},g)-(g_{j},f)}{\lambda}=\frac{(g_{j},g)}{\lambda_{j}} $$ 

即

 $$ (g_{j},g)=\frac{\lambda_{j}}{\lambda_{j}-\lambda}(g_{j},f),\quad j=1,2,3\cdots $$ 

将上式代入(16.2.6)式，即可得到施密特公式(16.2.5). 它可改写为

$$  g(x)=f(x)+\lambda\int_{a}^{b}R(x,y;\lambda)f(y)\mathrm{d}y   \tag*{（16.2.7）}$$

其中解核

$$  R(x,y;\lambda)=\sum_{i=1}^{\infty}\frac{1}{\lambda_{i}-\lambda}g_{i}(x)\overline{g}_{i}(y)   \tag*{(16.2.8)}$$

不难证得，解核还可以表示为如下几种形式：

$$  R(x,y;\lambda)=K(x,y)+\lambda\int_{a}^{b}K(x,\xi)R(\xi,y;\lambda)\mathrm{d}\xi   \tag*{(16.2.9)}$$

$$  R(x,y;\lambda)=K(x,y)+\lambda\sum_{i=1}^{\infty}\frac{(g_{i},K)}{\lambda_{i}-\lambda}g_{i}(x)   \tag*{（16.2.10）}$$

$$  R(x,y;\lambda)=K(x,y)+\lambda\sum_{i=1}^{\infty}\frac{\overline{g}_{i}(y)g_{i}(x)}{\lambda_{i}(\lambda_{i}-\lambda)}   \tag*{(16.2.11)}$$

## 3. 积分方程与常微分方程的关系

对于二阶常微分方程的初值问题

$$  \left\{\begin{aligned}y^{\prime \prime}(x)+p(x)y^{\prime}(x)+h(x)y(x)&=f(x)\\ y(0)=C_{0},\quad y^{\prime}(0)&=C_{1}\end{aligned}\right.   \tag*{（16.2.12）}$$

我们易于验证它与伏特拉方程

$$  g(x)+\int_{0}^{x}K(x,y)g(y)\mathrm{d}y=F(x)   \tag*{(16.2.13)}$$

是完全等价的。其中

$$  \begin{cases}g(x)=y^{\prime \prime}(x)\\K(x,y)=p(x)+h(x)(x-y)\\F(x)=f(x)-C_{1}p(x)-h(x)(C_{0}+C_{1}x)\end{cases}   \tag*{(16.2.14)}$$

也就是说，若  $ y(x) $ 是二阶常微分方程初值问题(16.2.12)的解，则  $ g(x)=y''(x) $ 必定是伏特拉方程(16.2.13)的解。反之，若已知积分方程(16.2.13)的解是  $ g(x) $，则不难证明定解问题(16.2.12)的解为

<!-- page: 329 -->

$$  y(x)=C_{0}+C_{1}x+\int_{0}^{x}(x-y)g(y)\mathrm{d}y   \tag*{（16.2.15）}$$

这只要将  $ g(x)=y''(x) $ 从  $ 0 \rightarrow x $ 积分两次即可，即

 $$ y(x)=C_{0}+C_{1}x+\int_{0}^{x}\left[\int_{0}^{a}g(y)\mathrm{d}y\right]\mathrm{d}\alpha $$ 

交换积分次序得

 $$ y(x)=C_{0}+C_{1}x+\int_{0}^{x}\left[\int_{y}^{x}g(y)\mathrm{d}\alpha\right]\mathrm{d}y=C_{0}+C_{1}x+\int_{0}^{x}(x-y)g(y)\mathrm{d}y $$ 

易于验证，将(16.2.14)式代入定解问题(16.2.12)确实满足.显然，若 $ p(x) $， $ h(x) $和 $ f(x) $均连续，定解问题(16.2.12)的解存在且唯一.

由上可见，微分方程的定解问题和积分方程间可互相转换。因此，我们可将不易求解的微分方程的问题转换为积分方程，而方便地用叠加解法求得其近似解。

注 ① 如果  $ \left|\overline{f}(x)g(x)\mathrm{d}x=0\right. $，则称此二函数是互相正交的.

② 见参考书目[8]第Ⅰ卷第三章.

#### 习题16.2

1. 试求解积分方程

 $$ g(x)-\lambda\int_{0}^{1}K(x,y)g(y)\mathrm{d}y=0,\quad0\leqslant x\leqslant1 $$ 

等价的微分方程的本征值问题，其中

 $$ K(x,y)=\left\{\begin{aligned}&\frac{x(2-y)}{2},&x\leqslant&y\\ &\frac{y(2-x)}{2},&y\leqslant&x,\end{aligned}\right. $$ 

2. 求解积分方程

(1)

 $$ g(x)-\lambda\int_{0}^{2\pi}\sin x\sin y g\left(y\right)\mathrm{d}y=f(x)\quad\left[f(x)\right. 已知 ]； $$ 

(2)

 $$ g(x)-\lambda\int_{0}^{1}(xy^{2}+x^{2}y)g(y)\mathrm{d}y=x. $$ 

### 16.3 维纳-霍普夫方法

维纳-霍普夫方法，是一种用来求解某些积分方程的特殊的积分变换方法。被称为维纳-霍普夫类型的积分方程

 $$ g(x)=\varphi(x)+\int_{0}^{\infty}K(x-y)g(y)\mathrm{d}y,\quad-\infty<x<\infty $$ 

其位移核和积分的半无限区间是重要的特色. 令  $ g(x)=g_{+}(x)+g_{-}(x) $，其中对于 x>0,  $ g_{+}(x)=0 $，而对于 x<0,  $ g_{-}(x)=0 $. 那么

 $$ g_{+}\left(x\right)+g_{-}\left(x\right)=\varphi(x)+\int_{-\infty}^{\infty}K(x-y)g_{-}\left(y\right)\mathrm{d}y $$

<!-- page: 330 -->

现在取傅里叶变换，则

 $$ \tilde{g}_{+}\left(\omega\right)+\tilde{g}_{-}\left(\omega\right)=\tilde{\varphi}\left(\omega\right)+\tilde{K}\left(\omega\right)\tilde{g}_{-}\left(\omega\right) $$ 

即

$$  \tilde{g}_{-}\left(\omega\right)\left[1-\tilde{K}\left(\omega\right)\right]+\tilde{g}_{+}\left(\omega\right)=\tilde{\varphi}\left(\omega\right)   \tag*{(16.3.1)}$$

因为对于 x>0, $ g_{+}(x)=0 $,所以  $ \tilde{g}_{+}(\omega) $ 在上半  $ \omega $ 平面中没有奇异性.同样  $ \tilde{g}_{-}(\omega) $ 在下半  $ \omega $ 平面中也没有奇异性.通常,对于某些  $ \alpha $ 和  $ \beta $ 有

 $$ \mid K(x)\mid\lesssim\left\{\begin{aligned}\mathrm{e}^{-\alpha x},x\to\infty\\ \mathrm{e}^{\beta x},x\to-\infty\end{aligned}\right. $$ 

因此 $ \widetilde{K}(\omega) $在窄条区域 $ -\beta<\mathrm{Im}\omega<\alpha $中是解析的.我们假定函数 $ \varphi(x) $在无穷远处至少也有这样的行为，则 $ \widetilde{\varphi}(\omega) $在窄条区域中也是解析的.让我们分解 $ 1-\widetilde{K}(\omega) $为两个函数

 $$ 1-\widetilde{K}(\omega)=\frac{A(\omega)}{B(\omega)} $$ 

其中  $ A(\omega) $ 在  $ \mathrm{Im}\omega<\alpha $ 中解析且不为零，而  $ B(\omega) $ 在  $ \mathrm{Im}\omega>-\beta $ 中解析且不为零.

方程(16.3.1)现在变为

$$  \tilde{g}_{-}\left(\omega\right)A(\omega)+\tilde{g}_{+}\left(\omega\right)B(\omega)=\tilde{\varphi}(\omega)B(\omega)   \tag*{（16.3.2）}$$

其中  $ \tilde{g}_{-}(\omega)A(\omega) $ 在  $ \mathrm{Im}\omega<0 $ 中没有奇点， $ \tilde{g}_{+}(\omega)B(\omega) $ 在  $ \mathrm{Im}\omega>0 $ 中没有奇点，而  $ \tilde{\varphi}(\omega)B(\omega) $ 在两个半平面中可能有奇点。现在我们将  $ \tilde{\varphi}(\omega)B(\omega) $ 按如下形式分开：

 $$ \tilde{\varphi}(\omega)B(\omega)=C(\omega)+D(\omega) $$ 

其中  $ C(\omega) $ 在上半  $ \omega $ 平面中没在奇点，而  $ D(\omega) $ 在下半  $ \omega $ 平面中没有奇点，于是方程 (16.3.2) 变为

$$  \tilde{g}_{-}\left(\omega\right)A(\omega)-D(\omega)=C(\omega)-\tilde{g}_{+}\left(\omega\right)B(\omega)   \tag*{（16.3.3）}$$

上式的左边在下半 $ \omega $平面中没有奇点，而右边在上半 $ \omega $平面没有奇点。因此，两边必须等于一个整函数。更进一步， $ \tilde{g}_{+}(\omega) $和 $ \tilde{g}_{-}(\omega) $在 $ \mathrm{Im}\omega=\pm\infty $时，趋于零。通常能证明函数 $ A,B,\cdots,D $最糟莫过于多项式。因此方程(16.3.3)的两边相当于某些多项式。这就确定了 $ g_{+}(x) $和 $ g_{-}(x) $。其中某些未知常数由物理推理或原积分方程中的代换确定。

例

$$  g(x)=\mathrm{e}^{-|x|}+\lambda\int_{0}^{\infty}\mathrm{e}^{-|x-y|}g(y)\mathrm{d}y   \tag*{（16.3.4）}$$

函数  $ e^{-|x|} $ 的傅氏变换是

 $$ \int_{-\infty}^{\infty}\mathrm{e}^{-|x|}\mathrm{e}^{-i\omega x}\mathrm{d}x=\frac{2}{1+\omega^{2}} $$ 

因而，积分方程(16.3.4)的傅氏变换是

 $$ \tilde{g}_{+}\left(\omega\right)+\tilde{g}_{-}\left(\omega\right)=\frac{2}{1+\omega^{2}}+\frac{2\lambda}{1+\omega^{2}}\tilde{g}_{-}\left(\omega\right) $$ 

或

 $$ \Big(\frac{\omega^{2}-\xi^{2}}{\omega^{2}+1}\Big)\tilde{g}_{-}\left(\omega\right)+\tilde{g}_{+}\left(\omega\right)=\frac{2}{1+\omega^{2}} $$ 

其中  $ \xi^{2}=2\lambda-1 $ 。为了明确，我们将假定  $ \xi $ 为实数  $ \left(\lambda>\frac{1}{2}\right) $

<!-- page: 331 -->

我们下一步是表达系数 $ \frac{\omega^{2}-\xi^{2}}{\omega^{2}+1} $作为 $ A(\omega)/B(\omega) $的商，其中 $ A(\omega) $在 $ \mathrm{Im}\omega<0 $中是解析的，而 $ B(\omega) $在 $ \mathrm{Im}\omega>-1 $中是解析的。很清楚，商仅可能为如下形式：

 $$ A(\omega)=\frac{\omega^{2}-\xi^{2}}{\omega-i},\quad B(\omega)=\omega+i $$ 

代入方程(16.3.2)，得

 $$ \begin{aligned}&\tilde{g}_{-}\text{(}\omega\text{)}\frac{\omega^{2}-\xi^{2}}{\omega-\mathrm{i}}+\tilde{g}_{+}\text{(}\omega\text{)}(\omega+\mathrm{i})=\frac{2}{\omega-\mathrm{i}}\\ &\\ &\tilde{g}_{-}\text{(}\omega\text{)}\Big(\frac{\omega^{2}-\xi^{2}}{\omega-\mathrm{i}}\Big)-\frac{2}{\omega-\mathrm{i}}=-\tilde{g}_{+}\text{(}\omega\text{)}(\omega+\mathrm{i})\\ \end{aligned} $$ 

即

(16.3.5)式的左边，在下半 $ \omega $平面中没有奇点；而右边在上半 $ \omega $平面中没有奇点.因此每边必须等于一个多项式.

现在我们应用基于  $ \tilde{g}_{\pm}(\omega) $ 的渐近行为的理论，来确定所需多项式的次数。设  $ P(\omega) $ 是  $ \omega $ 的某一多项式，于是

 $$ (\omega+i)\tilde{g}_{+}(\omega)=P(\omega) $$ 

 $$ \tilde{g}_{+}\left(\omega\right)=\frac{P(\omega)}{\omega+i} $$ 

如果当 $ \left|\omega\right|\rightarrow\infty $时 $ \tilde{g}_{+}\left(\omega\right) $减少，则 $ P\left(\omega\right) $仅可能是一个常数，我们称之为iA，因此

 $$ \tilde{g}_{+}\left(\omega\right)=\frac{\mathrm{i}A}{\omega+\mathrm{i}} $$ 

 $$ g_{+}\left(x\right)=A\mathrm{e}^{x},\quad x<0 $$ 

同样

 $$ \begin{aligned}\tilde{g}_{-}\left(\omega\right)&\Big(\frac{\omega^{2}-\xi^{2}}{\omega+\mathrm{i}}\Big)-\Big(\frac{2}{\omega-\mathrm{i}}\Big)=-\mathrm{i}A\\\tilde{g}_{-}\left(\omega\right)&=\frac{2}{\omega^{2}-\xi^{2}}-\frac{\mathrm{i}A\left(\omega-\mathrm{i}\right)}{\omega^{2}-\xi^{2}}\end{aligned} $$ 

故

$$  \begin{aligned}&g_{-}\left(x\right)=-\frac{2}{\xi}\sin\xi x+A\Big(\cos\xi x+\frac{1}{\xi}\sin\xi x\Big),\quad x>0\\&g(x)=\left\{\begin{aligned}&A\mathrm{e}^{x},&x<0\\&-\frac{2}{\xi}\sin\xi x+A\Big(\cos\xi x+\frac{1}{\xi}\sin\xi x\Big),&x>0\end{aligned}\right.\\ \end{aligned}   \tag*{（16.3.6）}$$

#### 习题16.3

1. 不用傅氏变换直接求解积分方程（16.3.4）

 $$ g(x)=\mathrm{e}^{-|x|}+\lambda\int_{0}^{\infty}\mathrm{e}^{-|x-y|}g(y)\mathrm{d}y,\quad-\infty<x<\infty;\lambda>\frac{1}{2} $$ 

并将求得的解与(16.3.6)相比较.

2. 如果  $ u(x) = \mathrm{e}^{-|x|} + \lambda \int_{0}^{\infty} |x - y| \mathrm{e}^{-|x - y|} u(y) \, \mathrm{d}y $，求  $ u(x) $.

<!-- page: 332 -->

# 本章小结

在求解非奇异的积分方程时，常常可采用如下的几种有用的方法：

1. 如果核是可分离的，则可用代数方法求解。在实际问题中，常常用可分离的核，近似表示一个复杂的核，这样可得到解答的途径。

2. 如果核仅仅是 $ (x-y) $的一个函数，用卷积理论可简化解的傅氏变换和拉氏变换的计算.

3. 如果有一个足够小的参数  $ \lambda $，积分的迭代法是一个有用的方法，否则需要一个弗雷德霍姆解.

4. 一旦一个厄米核的本征值和本征函数被求得，它们就能被用来构造积分算符的一个格林函数或解核。那么，任一非齐次方程就可运用这个格林函数来求解。

对于具有位移核和半无限积分区域的情况，我们讨论了维纳-霍普夫技术。许多其他的积分变换技术，在特殊情况下是有用的。

