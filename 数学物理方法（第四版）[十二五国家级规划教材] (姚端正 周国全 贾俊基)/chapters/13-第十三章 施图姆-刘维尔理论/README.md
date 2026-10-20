# 13-第十三章 施图姆-刘维尔理论

[返回全书目录](../../README.md)

> PDF 页码：273–280

<!-- page: 273 -->

### 13.1 施图姆-刘维尔本征值问题

本章相当于前面两章，即特殊函数问题的一个小结。

## 1. 施图姆-刘维尔型方程

在运用分离变量法求解偏微分方程时，会出现种种含有参量的常微分方程，如勒让德方程、贝塞尔方程等，这些方程初看起来无什么关系，但只要我们将之稍加变形，便均可写成下述方程：

$$  \frac{\mathrm{d}}{\mathrm{d}x}\bigg[k(x)\frac{\mathrm{d}y}{\mathrm{d}x}\bigg]-q(x)y+\lambda\rho(x)y=0   \tag*{(13.1.1)}$$

其中， $ a \leqslant x \leqslant b, k(x) \geqslant 0, q(x) \geqslant 0, \rho(x) \geqslant 0, \lambda $ 为参数。通常称（13.1.1）为施图姆-刘维尔（Sturm-Liouville）方程，而称  $ \rho(x) $ 为权函数。如贝塞尔方程

 $$ x^{2}y^{\prime \prime}+xy^{\prime}+(k^{2}x^{2}-n^{2})y=0 $$ 

可写为

 $$ \frac{\mathrm{d}}{\mathrm{d}x}\Big[x\frac{\mathrm{d}y}{\mathrm{d}x}\Big]-\frac{n^{2}}{x}y+k^{2}xy=0 $$ 

其中  $ k(x)=x, q(x)=\frac{n^{2}}{x}, \lambda=k^{2}, \rho(x)=x $ 。又如，勒让德方程

 $$ (1-x^{2})y^{\prime \prime}-2xy^{\prime}+l(l+1)y=0 $$ 

可写为

 $$ \frac{\mathrm{d}}{\mathrm{d}x}\bigg[(1-x^{2})\frac{\mathrm{d}y}{\mathrm{d}x}\bigg]+l(l+1)y=0 $$ 

其中  $ k(x)=1-x^{2}, q(x)=0, \lambda=l(l+1), \rho(x)=1. $

任意的二阶常微分方程

 $$ y^{\prime \prime}(x)+p(x)y^{\prime}(x)+h(x)y(x)=0 $$ 

以函数  $ k(x) = \exp\left[\int p(x)dx\right] $ 乘其两端后均可写成施-刘型方程. 如：

对于厄米方程

 $$ y^{\prime \prime}-2xy^{\prime}+2ny=0 $$ 

有

 $$ k(x)=\mathrm{e}^{-x^{2}},\quad\left[\mathrm{e}^{-x^{2}}y^{\prime}\right]^{\prime}+2n\mathrm{e}^{-x^{2}}y=0 $$ 

对卡拉盖尔方程

<!-- page: 274 -->

$$ xy^{\prime \prime}+(1-x)y^{\prime}+\alpha y=0 $$ 

有

 $$ k(x)=x\mathrm{e}^{-x},\quad\left[x\mathrm{e}^{-x}y^{\prime}\right]^{\prime}+\alpha\mathrm{e}^{-x}y=0 $$ 

对于高斯方程

 $$ x(x-1)y^{\prime \prime}+\left[(\alpha+\beta+1)x-\gamma\right]y^{\prime}+\alpha\beta y=0 $$ 

有

 $$ k(x)=x^{\gamma}(x-1)^{\alpha+\beta+1-\gamma} $$ 

 $$ \left[x^{\gamma}(x-1)^{\alpha+\beta+1-\gamma}y^{^{\prime}}\right]^{\prime}+\alpha\beta x^{\gamma-1}(x-1)^{\alpha+\beta-\gamma}y=0 $$ 

对于库默尔方程

 $$ xy^{\prime \prime}+(c-x)y^{\prime}-ay=0 $$ 

有

 $$ k(x)=x^{c}\mathrm{e}^{-x},\quad\left[x^{c+1}\mathrm{e}^{-x}y^{\prime}\right]^{\prime}-x^{c}\mathrm{e}^{-x}y^{\prime}-ax^{c}\mathrm{e}^{-x}y=0 $$ 

等等.

## 2. 自然边界条件

定义在某一区间上的施图姆-刘维尔方程

 $$ \frac{\mathrm{d}}{\mathrm{d}x}\bigg[k(x)\frac{\mathrm{d}y}{\mathrm{d}x}\bigg]-q(x)y+\lambda o(x)y=0,\quad a\leqslant x\leqslant b $$ 

（1）若端点 a 或 b 是 k(x) 的一级零点，则在那个端点就存在着自然的边界条件。因为在此种情况下若(13.1.1)存在一有界解  $ y_{1}(x) $，则由求解公式

 $$ y_{2}(x)=y_{1}(x)\Big[\int_{x_{0}}^{x}\frac{\mathrm{e}^{-\left|p(\zeta)\mathrm{d}\zeta\right.}}{y_{1}^{2}(\zeta)}\mathrm{d}\zeta+c\Big]=y_{1}(x)\Big[\int_{x_{0}}^{x}\frac{\mathrm{d}\zeta}{k(\zeta)y_{1}^{2}(\zeta)}+c\Big]^{\textcircled{1}} $$ 

知，与  $ y_{1}(x) $ 线性无关的解  $ y_{2}(x) $ 在该端点必是无界的. 即

 $$ y_{2}(a)=\infty\quad 或 \quad y_{2}(b)=\infty $$ 

故此时存在有限性的自然边界条件

$$  y(a)= 有限 \quad 或 \quad y(b)= 有限   \tag*{(13.1.2)}$$

如，贝塞尔方程

 $$ \frac{\mathrm{d}}{\mathrm{d}x}\Big[x\frac{\mathrm{d}y}{\mathrm{d}x}\Big]-\frac{n^{2}}{x^{2}}y+k^{2}xy=0,\quad0\leqslant x\leqslant a $$ 

 $ k(x)=x $，在端点 x=0 的值  $ k(0)=0 $，在端点 x=0 存在着自然边界条件  $ y|_{x=0}\rightarrow $ 有限。又如，勒让德方程

 $$ \frac{\mathrm{d}}{\mathrm{d}x}\bigg[(1-x^{2})\frac{\mathrm{d}y}{\mathrm{d}x}\bigg]+l(l+1)y=0,\quad-1\leqslant x\leqslant1 $$ 

 $ k(x)=1-x^{2} $，在端点  $ x=\pm1 $ 的值  $ k(\pm1)=1-(\pm1)^{2}=0 $，在端点存在着自然边界条件  $ y|_{x=\pm1}\rightarrow $ 有限.

（2）若  $ k(a)=k(b) $，则在端点存在有周期性的自然边界条件

$$  y(a)=y(b),\quad y^{^{\prime}}(a)=y^{^{\prime}}(b)   \tag*{(13.1.3)}$$

如，第二篇8.4节中我们所遇到的本征值问题.

<!-- page: 275 -->

$$ \left\{\begin{aligned}\Phi^{\prime \prime}(\varphi)+n^{2}\Phi(\varphi)&=0\\ \Phi(0)&=\Phi(2\pi)\end{aligned}\right. $$ 

即属此种情况的一个特例.

## 3. 施图姆-刘维尔本征值问题的共同性质

对施图姆-刘维尔方程附加以齐次的第一类、第二类或第三类的边界条件或自然边界条件

$$  \left\{\begin{aligned}&\frac{\mathrm{d}}{\mathrm{d}x}\Big[k(x)\frac{\mathrm{d}y}{\mathrm{d}x}\Big]-q(x)y+\lambda o(x)y=0,\quad a\leqslant x\leqslant b\\ &\Big[\alpha\frac{\mathrm{d}y}{\mathrm{d}x}+\beta y(x)+\gamma k(x)\Big]_{x=a,b}=0\end{aligned}\right.   \tag*{(13.1.4)}$$

就称为施图姆-刘维尔本征值问题. 这类本征值问题具有如下共同性质 $ ^{②} $:

（1）如  $ k(x) $ 及其导数连续， $ q(x) $ 连续或者最多在边界有一阶极点，则存在无限多分立的实本征值

 $$ \lambda_{1}\leqslant\lambda_{2}\leqslant\lambda_{3}\leqslant\cdots $$ 

相应地，有本征函数（可以是 x 的复函数）

 $$ y_{1}(x),y_{2}(x),y_{3}(x),\cdots $$ 

（2）所有本征值  $ \lambda_{m} \geqslant 0 (m = 1, 2, 3, \cdots) $

（3）相应于不同的本征值 $ \lambda_{m} $ 和 $ \lambda_{n} $ 的本征函数 $ y_{m}(x) $ 和 $ y_{n}(x) $，在区间 $ [a,b] $ 上带权重 $ \rho(x) $ 正交归一，即

$$  \int_{a}^{b}\rho(x)y_{m}(x)\bar{y}_{n}(x)\mathrm{d}x=\left\{\begin{aligned}&0,&m\neq n\\ &N_{n}^{2},&m=n\end{aligned}\right.   \tag*{（13.1.5）}$$

其中  $ N_{n} $ 称为  $ y_{n}(x) $ 的模， $ \frac{1}{N_{n}} $ 称为归一化因子， $ \bar{y}_{n}(x) $ 为  $ y_{n}(x) $ 的共轭函数.

（4）本征函数族 $ \left\{y_{m}(x)\right\}:y_{1}(x),y_{2}(x),y_{3}(x),\cdots $是完备的.即，若函数 $ f(x) $具有连续一阶导数和分段连续的二阶导数且满足本征函数族 $ y_{m}(x)(m=1,2,3,\cdots) $所满足的边界条件，则必可展开为绝对且一致收敛的级数

$$  f(x)=\sum_{m=1}^{\infty}c_{m} y_{m}(x)   \tag*{(13.1.6)}$$

其中

$$  c_{m}=\frac{1}{N_{m}^{2}}\int_{a}^{b}\rho(x)f(x)\bar{y}_{m}(x)\mathrm{d}x   \tag*{(13.1.7)}$$

事实上，只要  $ f(x) $ 在  $ [a,b] $ 上平方可积，就能按 (13.1.6) 展开（见参考文献 [7] 15.3 节）

若施图姆-刘维尔方程的解，是不能用初等函数的有限形式表示的函数（如，贝塞尔函数、勒让德多项式等），则称之为特殊函数，故常常将对特殊函数问题的研究，归结为对施图姆-刘维尔问题的研究.

<!-- page: 276 -->

现将两个主要的特殊函数的性质，列入本篇末的表中，作为本篇的小结。读者不妨将本篇各章节和习题中所出现的其他特殊函数，如厄米多项式、拉盖尔多项式，此外还有超几何级数、合流超几何级数 $ ^{③} $等这些物理学中常会遇到的特殊函数的主要性质，自己归纳整理后也列入该表中。

注 ① 见一般高等数学教科书中高阶常微分方程部分.

② 施-刘问题共性证明见二维码.

③ 超几何级数和合流超几何级数分别为高斯方程和库默尔方程的解. 见 13.2 节.

<div style="text-align: center;"><img src="images/p0276_img_in_image_box_761_277_826_342.jpg" alt="Image" width="6%" /></div>


施-刘问题共性证明

#### 习题13.1

1. 厄米多项式的微分表达式为

$$  \mathrm{H}_{n}(x)=(-1)^{n}\mathrm{e}^{x^{2}}\frac{\mathrm{d}^{n}\mathrm{e}^{-x^{2}}}{\mathrm{d}x^{n}}   \tag*{(13.1.8)}$$

试证

（1）其母函数关系式： $ \mathrm{e}^{-t^{2}+2tx}=\sum_{n=0}^{\infty}\frac{\mathrm{H}_{n}(x)}{n!}t^{n}\quad(t>0) $

(2) 其递推公式:  $ \left\{\begin{aligned}H_{n}^{\prime}(x)&=2nH_{n-1}(x)\\ H_{n+1}(x)&-2xH_{n}(x)+2nH_{n-1}(x)\end{aligned}\right.=0 $

$$  \begin{aligned}(3)& 其正交归一性 :\int_{-\infty}^{\infty}e^{-x^{2}}H_{m}(x)H_{n}(x)d x=\begin{cases}0,&m\neq n\\2^{n}n!\sqrt{\pi},&m=n\end{cases}(m,n=0,1,2,\cdots)\end{aligned}   \tag*{(13.1.11)}$$

（芝加哥大学研究生试题）

$$  2.\  拉盖尔多项式的表达式为 L_{n}(x)=\sum_{k=0}^{n}\frac{(-1)^{k}(n!)^{2}}{(k!)^{2}(n-k)!}x^{k}   \tag*{(13.1.12)}$$

$$  \begin{aligned} 试证：(1) 微分表达式为 \quad\mathrm{L}_{n}(x)=e^{x}\frac{\mathrm{d}^{n}}{\mathrm{d}x^{n}}(x^{n}\mathrm{e}^{-x})\end{aligned}   \tag*{（13.1.13）}$$

$$  (2) 母函数展开式为 \quad\frac{\mathrm{e}^{-\frac{xt}{1-t}}}{1-t}=\sum_{n=0}^{\infty}\frac{1}{n!}\mathrm{L}_{n}(x)t^{n}   \tag*{(13.1.14)}$$

$$   正交归一性为 \quad\int_{0}^{\infty}\mathrm{e}^{-x}\mathrm{L}_{m}(x)\mathrm{L}_{n}(x)\mathrm{d}x=\left\{\begin{aligned}&0,&m\neq n\\ &(n!!)^{2},&m=n\end{aligned}\right.   \tag*{(13.1.15)}$$

3. 证明：施-刘方程

 $$ \frac{\mathrm{d}}{\mathrm{d}x}\bigg[k(x)\frac{\mathrm{d}y}{\mathrm{d}x}\bigg]-q(x)y+\lambda\rho(x)y=0,\quad a\leqslant x\leqslant b $$ 

的本征函数  $ y_{m}(x) $ 和  $ y_{n}(x) $ 在区间  $ [a,b] $ 上带权重  $ \rho(x) $ 正交归一

 $$ \int_{a}^{b}\rho(x)y_{m}(x)\bar{y}_{n}(x)\mathrm{d}x=\left\{\begin{aligned}&0,&m\neq n\\ &N_{n}^{2},&m=n\end{aligned}\right. $$ 

 $ ^{*} $4.（1）考虑 $ a \leqslant x \leqslant b $内的微分方程

 $$ \frac{\mathrm{d}y^{2}}{\mathrm{d}x^{2}}+w(x)\big[\lambda-q(x)\big]y=0 $$

<!-- page: 277 -->

$ w(x), q(x) $ 是固定函数，且在  $ a \leqslant x \leqslant b $ 中  $ w(x) \geqslant 0 $，方程的边界条件是

 $$ y(a)=0,\quad y^{^{\prime}}(b)=0 $$ 

解释这个方程的本征值  $ \lambda=\lambda_{n} $ 和本征函数的意义。证明本征值是实的且具有不同本征值的本征函数以一个适当的权函数而正交。叙述一般函数按这些本征函数的展开定理（你不需证明方程总是存在一个或更多个本征函数，假定它们存在而导出这些性质）。

（2）求下列系统的本征值

 $$ \left\{\begin{aligned}&\frac{\mathrm{d}^{2}y}{\mathrm{d}x^{2}}+\lambda y=0,&0\leqslant x\leqslant b\\ &y(0)=0,&y^{\prime}(b)=0\end{aligned}\right. $$ 

5. 量子力学中的薛定谔方程为

 $$ H\psi=E\psi $$ 

其中

 $$ H=-\frac{h^{2}}{2mdx^{2}}+V(x) $$ 

为哈密顿算符， $ \phi $ 和 E 分别是 H 的本征函数和本征值，m 是微观粒子的质量。假定粒子在  $ \delta $ 势阱中运动

 $$ V(x)=-a\delta(x)\quad(a>0) $$ 

对于束缚态情况 $ (E<0) $，求解薛定谔方程.

###  $ ^{*} $13.2 高斯方程和库默尔方程

在前两章中我们着重讨论了贝塞尔方程和勒让德方程，这两个在物理问题中常碰到的施图姆-刘维尔方程。除此以外，高斯方程和库默尔方程也是物理中应用较广的施图姆-刘维尔方程。特别是这两个方程及其解答与其他的斯-刘方程及其解答之间，有着千丝万缕的联系，故本节将对它们及其解答进行简单的介绍。

## 1. 高斯方程和超几何级数

高斯方程

$$  x(x-1)y^{\prime \prime}+\left[(\alpha+\beta+1)x-\gamma\right]y^{\prime}+\alpha\beta y=0   \tag*{(13.2.1)}$$

又称超几何方程. 它有三个正则奇点 x=0,1, $ \infty $. 其中  $ \alpha,\beta $ 和  $ \gamma $ 是实数. 现求其在 x=0 的级数解.

设

$$  y(x)=\sum_{k=0}^{\infty}c_{k}x^{k+\rho},\quad c_{0}\neq0   \tag*{(13.2.2)}$$

则得判定方程的两个根分别为

 $$ \rho=\rho_{1}=0,\quad\rho=\rho_{2}=1-\gamma $$ 

设  $ \gamma \neq $ 整数且  $ \gamma > 1 (\gamma < 1 $ 时结论相同)，则当  $ \rho = \rho_{1} = 0 $ 时将 (13.2.2) 式代入 (13.2.1) 式得到  $ c_{k} $ 的递推公式为

$$  c_{k+1}=\frac{(k+\alpha)(k+\beta)}{(k+\gamma)(k+1)}c_{k},\quad k=0,1,2,\cdots   \tag*{(13.2.3)}$$

<!-- page: 278 -->

故当取 $ c_{0}=1 $时，可得方程(13.2.1)的第一个特解为

$$  \begin{align*}y_{1}(x)&=1+\sum_{k=1}^{\infty}\frac{\alpha(\alpha+1)\cdots(\alpha+k-1)\beta(\beta+1)\cdots(\beta+k-1)}{k!\gamma(\gamma+1)\cdots(\gamma+k-1)}x^{k}\\&=\frac{\Gamma(\gamma)}{\Gamma(\alpha)\Gamma(\beta)}\sum_{k=0}^{\infty}\frac{\Gamma(\alpha+k)\Gamma(\beta+k)}{k!\Gamma(\gamma+k)}x^{k}\end{align*}   \tag*{(13.2.4)}$$

显然该级数解的收敛半径为1. 常将此级数解记为  $ F(\alpha,\beta,\gamma;x) $，即

$$  F(\alpha,\beta,\gamma;x)=\frac{\Gamma(\gamma)}{\Gamma(\alpha)\Gamma(\beta)}\sum_{k=0}^{\infty}\frac{\Gamma(\alpha+k)\Gamma(\beta+k)}{k!\Gamma(\gamma+k)}x^{k},\quad\mid x\mid<1   \tag*{（13.2.5）}$$

称之为超几何级数. 于是, 方程(13.2.1)有一超几何级数解

$$  y_{1}(x)=F(\alpha,\beta,\gamma;x)   \tag*{(13.2.6)}$$

当 $ \left|x\right|=1 $时，由于在k足够大时

 $$ \left|\frac{c_{k}x^{k}}{c_{k+1}x^{k+1}}\right|=1+\frac{\gamma+1-\alpha-\beta}{k}+O\left(\frac{1}{k^{2}}\right) $$ 

故由高斯判别法得知，当  $ \gamma > \alpha + \beta $ 时， $ y_{1}(x) $ 收敛；而当  $ \gamma \leqslant \alpha + \beta $ 时， $ y_{1}(x) $ 发散。

用类似的方法我们可求得:当 $ \rho=\rho_{2}=1-\gamma $ 时方程(13.2.1)的另一超几何级数特解

$$  y_{2}(x)=x^{1-\gamma}F(\alpha-\gamma+1,\beta-\gamma+1,2-\gamma;x)   \tag*{(13.2.7)}$$

由对(13.2.5)式中级数的敛散性讨论立即可知，当 $ |x|=1 $时，亦当 $ \gamma>\alpha+\beta $时收敛， $ \gamma\leqslant\alpha+\beta $时， $ y_{2}(x) $发散.

由上面讨论可知，当  $ \gamma \neq $ 整数时高斯方程（13.2.1）的两个线性独立解为

 $$ \left\{\begin{aligned}y_{1}(x)&=F(\alpha,\beta,\gamma;x)\\ y_{2}(x)&=x^{1-\gamma}F(\alpha-\gamma+1,\beta-\gamma+1,2-\gamma;x)\end{aligned}\right. $$ 

且当  $ \gamma > \alpha + \beta $ 时，它们均在  $ |x| \leqslant 1 $ 上收敛；当  $ \gamma $ 是整数时，方程的一个线性独立解是

 $$ y_{1}(x)=\begin{cases}F(\alpha,\beta,\gamma;x),&\gamma=1,2,3,\cdots\\x^{1-\gamma}F(\alpha-\gamma+1,\beta-\gamma+1,2-\gamma;x),&\gamma=0,-1,-2,\cdots\end{cases} $$ 

而另一个线性独立解则应具有(12.1.18)式的形式. 在此不作详细讨论.

由递推公式(13.2.3)还可看出，当 $ \alpha $或 $ \beta=-l(l=0,1,2,\cdots) $时 $ c_{k}=0(k\geqslant l+1) $，此时 $ F(\alpha,\beta,\gamma;x) $退化为l次多项式.事实上能够证明，勒让德方程是高斯方程的特例 $ ^{①} $，

$$  \mathrm{P}_{l}(x)=F(-l,l+1,1;x)   \tag*{（13.2.8）}$$

## 2. 库默尔(Kummer)方程和合流超几何函数

在高斯方程中，若令  $ x=\frac{X}{\beta} $，则高斯方程化为

 $$ X\Big(\frac{X}{\beta}-1\Big)y^{\prime \prime}(X)+\Big[X+\frac{\alpha+1}{\beta}X-\gamma\Big]y^{\prime}(X)+\alpha y(X)=0 $$

<!-- page: 279 -->

令  $ \beta \to \infty $，仍记 X 为 x，则得

$$  xy^{\prime \prime}+(\gamma-x)y^{\prime}-\alpha y=0   \tag*{(13.2.9)}$$

被称为库默尔方程或合流超几何方程. 它实际上是一个退化了的高斯方程. 其正则奇点为 x=0, $ \infty $. 故当  $ \gamma\neq $ 整数时, 易于得到其两个线性独立的解为

$$  \begin{aligned}y_{1}(x)&=\lim_{\beta\to\infty}F(\alpha,\beta,\gamma;x)=\frac{\Gamma(\gamma)}{\Gamma(\alpha)}\sum_{k=0}^{\infty}\frac{\Gamma(k+\alpha)}{k!\Gamma(k+\gamma)}x^{k}\\&=F(\alpha,\gamma;x)\end{aligned}   \tag*{（13.2.10）}$$

$$  \begin{aligned}y_{2}(x)&=\lim_{\beta\to\infty}x^{1-\gamma}F(\alpha-\gamma+1,\beta-\gamma+1,2-\gamma;x)\\&=x^{1-\gamma}F(\alpha-\gamma+1,2-\gamma;x)\end{aligned}   \tag*{(13.2.11)}$$

其中

$$  F(\alpha,\gamma;x)=\frac{\Gamma(\gamma)}{\Gamma(\alpha)}\sum_{k=0}^{\infty}\frac{\Gamma(k+\alpha)}{k!\Gamma(k+\gamma)}x^{k}   \tag*{（13.2.12）}$$

称为库默尔函数或合流超几何级数. 其收敛半径为∞.

由级数的系数递推公式可知，当  $ \alpha = -n (n = 0, 1, 2, \cdots) $ 时  $ F(\alpha, \gamma; x) $ 退化为 n 次多项式.

许多特殊函数都能用合流超几何函数表示，如

贝塞尔函数

$$  \mathrm{J}_{\nu}(x)=\frac{1}{\Gamma(\nu+1)}\mathrm{e}^{-\mathrm{i}x}\left(\frac{x}{2}\right)^{\nu}F\left(\nu+\frac{1}{2},2\nu+1;2\mathrm{i}x\right)   \tag*{(13.2.13)}$$

厄米函数

$$  \mathrm{H}_{\nu}(x)=\frac{\sqrt{\pi}}{\Gamma\left(\frac{1-\nu}{2}\right)}F\Big(-\frac{\nu}{2},\frac{1}{2};x^{2}\Big)-\frac{\sqrt{2\pi}}{\Gamma\left(\frac{-\nu}{2}\right)}x F\Big(\frac{1-\nu}{2},\frac{3}{2};x^{2}\Big)   \tag*{(13.2.14)}$$

$$  \left\{\mathrm{H}_{2n}(x)=(-1)^{n}\frac{(2n)!}{n!}F\left(-n,\frac{1}{2};x^{2}\right)\right.   \tag*{（13.2.15）}$$

厄米多项式

$$  \mathrm{H}_{2n+1}(x)=(-1)^{n}\frac{(2n+1)!}{n!}2x F\left(-n,\frac{3}{2};x^{2}\right)   \tag*{（13.2.16）}$$

$$  \mathrm{L}_{\nu}^{\mu}(x)=\frac{1}{\Gamma(\nu+1)}F(-\nu,\mu+1,x)   \tag*{(13.2.17)}$$

拉盖尔多项式  $ \mathrm{L}_{n}(x)=F(-n,1;x) $

误差函数  $ \mathrm{erf}(x)=\frac{2x}{\sqrt{\pi}}F\left(\frac{1}{2},\frac{3}{2};-x^{2}\right) $

等等.

注 ① 令  $ x=\frac{1-t}{2},\alpha=-l,\beta=(l+1),\gamma=1 $ ，则方程 (13.2.1) 便化为

 $$ (1-t^{2})y^{\prime \prime}-2ty^{\prime}+l(l+1)y=0 $$

<!-- page: 280 -->

<div style="text-align: center;"><img src="images/p0280_img_in_image_box_100_311_163_378.jpg" alt="本篇主要特殊函数性质小结" width="6%" /></div>


本章授课课件

<div style="text-align: center;"><div style="text-align: center;">本篇主要特殊函数性质小结</div> </div>




<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>名称性质</td><td style='text-align: center; word-wrap: break-word;'>$ P_i(x) $</td><td style='text-align: center; word-wrap: break-word;'>$ P_i^m(x) $</td><td style='text-align: center; word-wrap: break-word;'>$ J_n(x) $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>表达式</td><td style='text-align: center; word-wrap: break-word;'>$ P_i(x) = \begin{cases} \left[\frac{L}{2}\right] &amp; \left(-\frac{1}{2}\right)^n(2l-2n)!x^{l-2n} \\ \sum_{n=0}^{2n-1} \frac{2^n}{n!}(l-n)!(l-2n)! \\ \frac{1}{2^l} \frac{d^l}{dx^l} (x^2-1)^l \\ \frac{1}{2\pi i} \oint_L (\zeta_i-1)^l \int_0 d\zeta_i \\ l=0,1,2,\cdots \end{cases} $\n $ P_i^m(x) = \begin{cases} (1-x^2)^{m_1^2}P_i^{(m)}(x) \\ \frac{1}{2^l!}(1-x^2)^{m_2^2} \frac{d^{l+m}}{dx^{l+m}}(x^2-1)^l \\ \frac{(1-x^2)^{m_2^2}}{2^l} \frac{1}{2\pi i} \frac{(l+m)!}{l!} \\ \cdot \oint_{L^s} (\frac{(\zeta_i-1)^l}{\zeta-x})^{l+m+1} \\ m=0,1,\cdots,l \end{cases} $\n $ P_i^m(x) = \begin{cases} (1-x^2)^{m_1^2}P_i^{(m)}(x) \\ \frac{1}{2^l!}(1-x^2)^{m_2^2} \frac{d^{l+m}}{dx^{l+m}}(x^2-1)^l \\ \frac{(1-x^2)^{m_2^2}}{2^l} \frac{1}{2\pi i} \frac{(l+m)!}{l!} \\ \cdot \oint_{L^s} (\frac{(\zeta_i-1)^l}{\zeta-x})^{l+m+1} \end{cases} $\n $ P_i^m(x) = \sum_{n=-\infty}^{\infty} J_n(x)t^n $</td><td style='text-align: center; word-wrap: break-word;'>$ J_n(x) = \begin{cases} \sum_{k=0}^{\infty} \frac{(-1)k}{k!(n+k)!}\left(\frac{x}{2}\right)^{2k+n} \\ \frac{1}{2\pi i} \int_{-\pi}^{\pi} e^{i(x+h-w\theta)} d\theta \\ \frac{1}{2\pi i} \int_{-\pi}^{\pi} \cos(x\sin\theta-n\theta) d\theta \end{cases} $</td><td style='text-align: center; word-wrap: break-word;'></td></tr><tr><td style='text-align: center; word-wrap: break-word;'>关系母函数</td><td style='text-align: center; word-wrap: break-word;'>$ \frac{1}{\sqrt{1-2xt+t^2}} = \sum_{i=0}^{\infty} P_i(x)t^i $</td><td style='text-align: center; word-wrap: break-word;'>$ \frac{(2m-1)!!(1-x^2)^{m/2}}{(1-2xt+t^2)^{m+1/2}} = \sum_{i=m}^{\infty} P_i^m(x)t^{i-m} $</td><td style='text-align: center; word-wrap: break-word;'>$ e^{\frac{i}{2}(r-\frac{1}{r})} = \sum_{n=-\infty}^{\infty} J_n(x)t^n $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>递推公式</td><td style='text-align: center; word-wrap: break-word;'>$ (l+1)P_{t+1}(x)=(2l+1)xP_t(x)-lP_{t-1}(x) $\n $ P_{t+1}(x)-P_{t-1}^r(x)=(2l+1)P_t(x) $</td><td style='text-align: center; word-wrap: break-word;'>$ (l+1-m)P_{t+1}^m(x)-(2l+1)xP_t^m(x) $\n $ (l+m)P_{t-1}^m(x)=0 $</td><td style='text-align: center; word-wrap: break-word;'>$ \frac{\mathrm{d}}{\mathrm{d}x}\left[x^s J_s(x)\right] = x^s J_{s-1}(x) $\n $ \frac{\mathrm{d}}{\mathrm{d}x}\left[x^{-s} J_s(x)\right] = -x^{-s} J_{s+1}(x) $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>正交性</td><td style='text-align: center; word-wrap: break-word;'>$ \int_{-1}^{t}P_i(x)P_k(x)\mathrm{d}x = \frac{2}{2l+1}\delta_{kl} $</td><td style='text-align: center; word-wrap: break-word;'>$ \int_{-1}^{t}P_i^m(x)P_k^m(x) = \frac{(l+m)!}{(l-m)!} \frac{2\delta_{kl}}{2l+1} $</td><td style='text-align: center; word-wrap: break-word;'>$ \int_0^s J_n(k_m\rho)J_n(k_l\rho)\mathrm{d}\rho = \frac{a^2}{2}\left[J_{n+1}(k_m\rho)\right]^2 \delta_{ml} $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>广义Fourier展开</td><td style='text-align: center; word-wrap: break-word;'>$ f(x) = \sum_{l=0}^{\infty} C_l P_l(x) $\n $ C_l = \frac{2l+1}{2}\int_{-1}^{l}f(x)P_l(x)\mathrm{d}x $</td><td style='text-align: center; word-wrap: break-word;'>$ f(x) = \sum_{l=0}^{\infty} C_l^m P_l^m(x) $\n $ C_l^m = \frac{2l+1}{2}\frac{(l-m)!}{(l+m)!}\int_{-1}^{l}f(x)P_l^m(x)\mathrm{d}x $</td><td style='text-align: center; word-wrap: break-word;'>$ f(\rho) = \sum_{m=1}^{\infty} C_m J_m(k_m\rho) $\n $ C_m = \frac{a^2}{2}\left[J_{m+1}(k_m\rho)\right]^2 \int_0^p f(\rho)J_m(k_m\rho)\mathrm{d}\rho $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>常用值</td><td style='text-align: center; word-wrap: break-word;'>$ P_0(x) = 1, P_1(x) = x $\n $ P_2(x) = \frac{1}{2}(3x^2-1) $\n $ P_1(1) \equiv 1 $,  $ P_i(-x)=(-1)^i P_i(x) $</td><td style='text-align: center; word-wrap: break-word;'>$ P_1^1(x) = (1-x^2)^+  $\n $ P_2^1(x) = 3(1-x^2)^+ x $</td><td style='text-align: center; word-wrap: break-word;'>$ J_0(0) = 1 $,  $ J_n(0) = 0 (n \geq 1) $\n $ J_1(x) = \sqrt{\frac{2}{\pi x}} \sin x $,  $ J_2(x) = \sqrt{\frac{2}{\pi x}} \cos x $,\n $ j_1(x) = \sqrt{\frac{\pi}{2x}} J_{i+1}(x) $,  $ j_0(x) = \frac{\sin x}{x} $,  $ j_1(x) = -\frac{\cos x}{x} $</td></tr></table>

