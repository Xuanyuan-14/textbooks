# 03-第3章 多维随机变量及其分布

[返回全书目录](../../README.md)

> PDF 页码：35–56

<!-- page: 35 -->

<div style="text-align: center;"><div style="text-align: center;">习题3-1 二维随机变量</div> </div>


1. 一箱子装有100件产品，其中一、二、三等品分别为80件、10件、10件。现从中随机抽取一件，记  $ X_1 = \begin{cases} 1, & 抽到一等品 \\ 0, & 其他 \end{cases} $， $ X_2 = \begin{cases} 1, & 抽到二等品 \\ 0, & 其他 \end{cases} $ 求随机变量 $ (X_1, X_2) $的分布律。

解： $ (X_1, X_2) $的可能取值只有4对： $ (0,0) $， $ (0,1) $， $ (1,0) $， $ (1,1) $，根据乘法公式，可得  $ P\{X_1 = 0, X_2 = 0\} = P\{X_1 = 0\} \cdot P\{X_2 = 0 \mid X_1 = 0\} = \frac{20}{100} \times \frac{10}{20} = 0.1 $， $ P\{X_1 = 0, X_2 = 1\} = P\{X_1 = 0\} \cdot P\{X_2 = 1 \mid X_1 = 0\} = \frac{20}{100} \times \frac{10}{20} = 0.1 $， $ P\{X_1 = 1, X_2 = 0\} = P\{X_1 = 1\} \cdot P\{X_2 = 0 \mid X_1 = 1\} = \frac{80}{100} \times 1 = 0.8 $， $ P\{X_1 = 1, X_2 = 1\} = P\{X_1 = 1\} \cdot P\{X_2 = 1 \mid X_1 = 1\} = \frac{20}{100} \times 0 = 0 $，即 $ (X_1, X_2) $的分布律为： $ \frac{X_2 \setminus X_1}{0} \begin{vmatrix} 0 & 1 \\ 0.1 & 0.1 \\ 1 & 0.8 \end{vmatrix} $

<!-- page: 36 -->

2. 袋中有1个红色球，2个黑色球与3个白色球，现有放回地从袋中取两次，每次取1球，以X、Y、Z分别表示两次取球所取得的红球，黑球与白球的个数，求：

(1)  $ P\{X=1 \mid Z=0\} $; (2) 二维随机变量  $ (X,Y) $ 的分布律。

解: (1) 题意表示在两次没有取白球的情况下，取了1个红球, 1个黑球, 即  $ P\{X=1 \mid Z=0\} = \frac{P\{X=1,Z=0\}}{P\{Z=0\}} = \frac{\frac{1}{6} \times \frac{2}{6} \times 2}{\frac{3}{6} \times \frac{3}{6}} = \frac{4}{9} $.

而  $ P\{X=1 \mid Z=0\} = \frac{P\{X=1,Z=0\}}{P\{Z=0\}} = \frac{\frac{1}{6} \times \frac{3}{6}}{\frac{3}{6}} = \frac{1}{6} $ 这个解法, 表示的是在第一次没有取白球的情况下, 第二次取红球的概率, 这个解法不符合题目所问.

(2)  $ P\{X=0,Y=0\} $ 表示两次有放回取球中, 没有取红球和黑球, 即两次都是取白球, 故  $ P\{X=0,Y=0\} = \frac{3}{6} \times \frac{3}{6} = \frac{1}{4} $;

 $ P\{X=0,Y=1\} $ 表示两次有放回取球中, 没有取红球, 有一次取黑球, 即另一次取白球, 故  $ P\{X=0,Y=1\} = \frac{2}{6} \times \frac{3}{6} \times 2 = \frac{1}{3} $;

 $ P\{X=0,Y=2\} $ 表示两次有放回取球中, 没有取红球, 两次都是取黑球, 故  $ P\{X=0,Y=2\} = \frac{2}{6} \times \frac{2}{6} = \frac{1}{9} $;

 $ P\{X=1,Y=0\} $ 表示两次有放回取球中, 一次取红球, 没有取黑球, 即另一次取白球, 故  $ P\{X=1,Y=0\} = \frac{1}{6} \times \frac{3}{6} \times 2 = \frac{1}{6} $;

 $ P\{X=1,Y=1\} $ 表示两次有放回取球中, 一次取红球, 一次取黑球, 故  $ P\{X=1,Y=1\} = \frac{1}{6} \times \frac{2}{6} \times 2 = \frac{1}{9} $;

 $ P\{X=2,Y=0\} $ 表示两次有放回取球中, 两次取红球, 没有取黑球, 故  $ P\{X=2,Y=0\} = \frac{1}{6} \times \frac{1}{6} = \frac{1}{36} $;

<!-- page: 37 -->

即有分布律  $ \begin{array}{c} Y \backslash X \\ 0 \quad \frac{1}{4} \quad \frac{1}{6} \quad \frac{2}{36} \\ 1 \quad \frac{1}{3} \quad \frac{1}{9} \quad 0 \cdot \\ 2 \quad \frac{1}{9} \quad 0 \quad 0 \end{array} $





3. 袋中装有标号为1、2、2的3个球，从中任取一个且不放回，然后再从袋中任取一个，用X、Y分别表示第一次、第二次取到的球的号码数，求(X,Y)的分布律。

解：X和Y的取值都是1,2，且有 $ P\{X=1,Y=1\}=0 $,

 $ P\{X=1,Y=2\}=P\{X=1\}\cdot P\{Y=2\mid X=1\}=\frac{1}{3}\times1=\frac{1}{3}; $

 $ P\{X=2,Y=1\}=P\{X=2\}\cdot P\{Y=1\mid X=2\}=\frac{2}{3}\times\frac{1}{2}=\frac{1}{3}; $

 $ P\{X=2,Y=2\}=P\{X=2\}\cdot P\{Y=2\mid X=2\}=\frac{2}{3}\times\frac{1}{2}=\frac{1}{3}; $

即有分布律：1  $ \quad 0 \quad \frac{1}{3} $.

2  $ \quad \frac{1}{3} \quad \frac{1}{3} $

37/105

<!-- page: 38 -->

4. 设随机变量  $ (X, Y) $ 的概率密度为  $ f(x, y) = \left\{ \begin{aligned} & A e^{-(2x + 3y)}, x > 0, y > 0, \\ & 0, \quad \text{其他} \end{aligned} \right. $，

求 (1) 常数  $ A $; \quad (2)  $ (X, Y) $ 的分布函数  $ F(x, y) $; \quad (3)  $ P\{Y \leq X\} $.

解: (1)  $ \int_{-\infty}^{+\infty} \int_{-\infty}^{+\infty} f(x, y) \, dx \, dy = \int_{-\infty}^{+\infty} dy \int_{-\infty}^{+\infty} A e^{-(2x+3y)} \, dx = A \int_{0}^{+\infty} e^{-3y} dy \int_{0}^{+\infty} e^{-2x} dx = \frac{1}{2} A \int_{0}^{+\infty} e^{-3y} dy = \frac{1}{6} A $, 故  $ A = 6 $.

(2)当 $ x \leq 0 $或 $ y \leq 0 $时，有 $ F(x, y) = 0 $;

当x>0, y>0时， $ F(x,y)=\int_{0}^{x}\mathrm{d}u\int_{0}^{y}6e^{-(2u+3v)}\mathrm{d}v=\left(1-e^{-2x}\right)\left(1-e^{-3y}\right) $,

即有 $ F(x,y)=\left\{\begin{aligned}&\left(1-e^{-2x}\right)\left(1-e^{-3y}\right),x>0,y>0\\&0,\quad 其他\end{aligned}\right. $

 $$ )P\big\{Y\leq X\big\}=6\int_{0}^{+\infty}e^{-3y}\mathrm{d}y\int_{y}^{+\infty}e^{-2x}\mathrm{d}x=3\int_{0}^{+\infty}e^{-3y}\big(e^{-2y}\big)\mathrm{d}y=3\int_{0}^{+\infty}e^{-5y}\mathrm{d}y=\frac{3}{5}. $$ 

如果写成 $ P\{Y \leq X\} = 6\int_{0}^{+\infty} e^{-2x} \, \mathrm{d}x \int_{0}^{y} e^{-3y} \, \mathrm{d}y $，还计算不出来。

<!-- page: 39 -->

<div style="text-align: center;"><div style="text-align: center;">习题3-2 边缘分布</div> </div>






1. 完成下列表格：

     $ X|Y $  $ \quad y_1 \quad $  $ \quad y_2 \quad $  $ \quad y_3 \quad $  $ \quad p_{i\bullet} $

     $ x_1 $  $ \quad 0.1 $  $ \quad 0.2 $  $ \quad 0.4 $

     $ x_2 $  $ \quad 0.2 $  $ \quad 0.2 $  $ \quad 0.4 $

     $ p_{\bullet j} $  $ \quad 1 $

解：由第一行，得 $ p_{12}=0.1 $，由最后一列，得 $ p_{2}=0.6 $，故 $ p_{23}=0.2 $，

所以表格如下： $ \begin{array}{ccccc}X|Y&y_{1}&y_{2}&y_{3}&p_{i\bullet}\\x_{1}&0.1&0.1&0.2&0.4\\x_{2}&0.2&0.2&0.2&0.6\\\end{array} $

 $ p_{\bullet j} $ 0.3 0.3 0.4 1

<!-- page: 40 -->

2. 设随机变量X在1,2,3,4四个整数中等可能地取值,另一随机变量X请切牟利

1~X中等可能地取值,试求(X,Y)的联合分布律及边缘分布律。

 $$ \begin{aligned}& 解：P\left\{X=1,Y=1\right\}=\frac{1}{4}\times1=\frac{1}{4},\\&P\left\{X=1,Y=2\right\}=P\left\{X=1,Y=3\right\}=P\left\{X=1,Y=4\right\}=0,\\&P\left\{X=2,Y=1\right\}=P\left\{X=2,Y=2\right\}=\frac{1}{4}\times\frac{1}{2}=\frac{1}{8},\\&P\left\{X=2,Y=3\right\}=P\left\{X=2,Y=4\right\}=0,\\&P\left\{X=3,Y=1\right\}=P\left\{X=3,Y=2\right\}=P\left\{X=3,Y=3\right\}\\&=\frac{1}{4}\times\frac{1}{3}=\frac{1}{12},\quad P\left\{X=3,Y=4\right\}=0,\\&P\left\{X=4,Y=1\right\}=P\left\{X=4,Y=2\right\}=P\left\{X=4,Y=3\right\}\\&=P\left\{X=4,Y=4\right\}=\frac{1}{4}\times\frac{1}{4}=\frac{1}{16}.\end{aligned} $$

<!-- page: 41 -->

故 $ (X,Y) $的联合分布律与边缘分布律如下表：









<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Y</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>3</td><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>p.j</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>1/4</td><td style='text-align: center; word-wrap: break-word;'>1/8</td><td style='text-align: center; word-wrap: break-word;'>1/12</td><td style='text-align: center; word-wrap: break-word;'>1/16</td><td style='text-align: center; word-wrap: break-word;'>25/48</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>2</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>1/8</td><td style='text-align: center; word-wrap: break-word;'>1/12</td><td style='text-align: center; word-wrap: break-word;'>1/16</td><td style='text-align: center; word-wrap: break-word;'>13/48</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>3</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>1/12</td><td style='text-align: center; word-wrap: break-word;'>1/16</td><td style='text-align: center; word-wrap: break-word;'>7/48</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>4</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>1/16</td><td style='text-align: center; word-wrap: break-word;'>1/16</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>Pi.</td><td style='text-align: center; word-wrap: break-word;'>1/4</td><td style='text-align: center; word-wrap: break-word;'>1/4</td><td style='text-align: center; word-wrap: break-word;'>1/4</td><td style='text-align: center; word-wrap: break-word;'>1/4</td><td style='text-align: center; word-wrap: break-word;'>1</td></tr></table>

<!-- page: 42 -->

3. 已知随机变量 X 和 Y 的概率分布如下：





X -1 0 1 Y 0 1

p  $ \frac{1}{4} $  $ \frac{1}{2} $  $ \frac{1}{4} $, p  $ \frac{1}{2} $  $ \frac{1}{2} $, 且 $ P\{XY=0\}=1 $.

求X和Y的联合分布律。

解: (1) 由已知  $ P\{XY = \mathbf{0}\} = 1 $，知  $ P\{XY \neq \mathbf{0}\} = \mathbf{0} $，即

 $ P\{X = -1, Y = 1\} = P\{X = 1, Y = 1\} = 0 $，从而有

 $$ P\left\{X=-\mathbf{1},Y=\mathbf{0}\right\}=P\left\{X=-\mathbf{1}\right\}=\frac{\mathbf{1}}{4},\ P\left\{X=\mathbf{1},Y=\mathbf{0}\right\}=P\left\{X=\mathbf{1}\right\}=\frac{\mathbf{1}}{4}, $$ 

 $ P\{X=0,Y=1\}=P\{Y=1\}=\frac{1}{2},\quad P\{X=0,Y=0\}=0, $

于是X和Y的联合分布律为



<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>Y|X</td><td style='text-align: center; word-wrap: break-word;'>-1</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>p_{j}</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>1/4</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>1/4</td><td style='text-align: center; word-wrap: break-word;'>1/2</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>1</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>1/2</td><td style='text-align: center; word-wrap: break-word;'>0</td><td style='text-align: center; word-wrap: break-word;'>1/2</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>p_{i.}</td><td style='text-align: center; word-wrap: break-word;'>1/4</td><td style='text-align: center; word-wrap: break-word;'>1/2</td><td style='text-align: center; word-wrap: break-word;'>1/4</td><td style='text-align: center; word-wrap: break-word;'>42/105</td></tr></table>

<!-- page: 43 -->

4. 二维随机变量  $ (X, Y) $ 的概率密度为

 $ f(x,y)=\left\{\begin{aligned}&\frac{(1+2x)(1+2y)}{4},0\leq x\leq1,0\leq y\leq1,\\&0,\quad 其他\end{aligned}\right. $，求X和Y的边缘概率密度。

 $$ \begin{aligned}& 解：f_{_{X}}\left(x\right)=\int_{-\infty}^{+\infty}f\left(x,y\right)\mathrm{d}y=\left\{\begin{aligned}&\int_{0}^{1}\frac{\left(1+2x\right)\left(1+2y\right)}{4}\mathrm{d}y,0\leq x\leq1\\&0,\quad 其他 \end{aligned}\right.=\left\{\begin{aligned}&\frac{\left(1+2x\right)}{2},0\leq x\leq1\\&0,\quad 其他 \end{aligned}\right.\end{aligned} $$ 

 $$ f_{Y}\left(y\right)=\int_{-\infty}^{+\infty}f\left(x,y\right)\mathrm{d}x=\left\{\begin{aligned}&\int_{0}^{1}\frac{\left(1+2x\right)\left(1+2y\right)}{4}\mathrm{d}x,0\leq y\leq1\\&0,\quad 其他 \end{aligned}\right.=\left\{\begin{aligned}&\frac{\left(1+2y\right)}{2},0\leq y\leq1\\&0,\quad 其他 \end{aligned}\right. $$

<!-- page: 44 -->

5.二维随机变量(X,Y)在以原点为圆心，R为半径的圆内服从均匀分布，试求X,Y的联合概率密度和边缘概率密度。







解：半径为 $ R $的圆的面积为 $ \pi R^2 $，故 $ (X,Y) $的联合概率密度为 $ f(x,y)=\left\{\begin{aligned}&\frac{1}{\pi R^2},x^2+y^2\leq R^2\\&0,\quad 其他\end{aligned}\right. $。

$$f_{X}(x)=\left\{\begin{array}{ll}\displaystyle\int_{-\sqrt{R^{2}-x^{2}}}^{\sqrt{R^{2}-x^{2}}}\frac{1}{\pi R^{2}}\mathrm{d}y=\frac{2}{\pi R^{2}}\sqrt{R^{2}-x^{2}},-R\leq x\leq R,&\text{ 同理，可求得 }\\0,&\text{ 其他 }\end{array}\right.$$

$$f_{Y}(y)=\left\{\begin{array}{ll}\displaystyle\frac{2}{\pi R^{2}}\sqrt{R^{2}-y^{2}},-R\leq y\leq R\\0,&\text{ 其他 }\end{array}\right.$$

<!-- page: 45 -->

<div style="text-align: center;"><div style="text-align: center;">习题3-3 条件分布 习题3-4 随机变量的独立性</div> </div>


习题3-3 条件分布 习题3-4 随机变量的独立性

1. 设二维随机变量(X,Y)的分布律为  $ \begin{bmatrix} Y \mid X & 0 & 1 \\ 0 & 0.3 & 0.2 \\ 1 & 0.4 & 0.1 \end{bmatrix} $ 试求在Y=1的条件下X的条件分布律。







解：根据公式 $ P\left\{X=x_{i}\mid Y=y_{j}\right\}=\frac{P\left\{X=x_{i},Y=y_{j}\right\}}{P\left\{Y=y_{j}\right\}}=\frac{p_{ij}}{p_{\bullet j}} $

所以有 $ P\{X=0|Y=1\}=\frac{P\{X=0,Y=1\}}{P\{Y=1\}}=\frac{0.4}{0.5}=\frac{4}{5} $，

 $ P\left\{X=1\mid Y=1\right\}=\frac{P\left\{X=1,Y=1\right\}}{P\left\{Y=1\right\}}=\frac{0.1}{0.5}=\frac{1}{5} $，即

 $$ \begin{array}{r}{x_{i}\quad0\quad1}\\ {P\left\{X=x_{i}\left|Y=1\right.\right\}\quad4/5\quad1/5}\end{array} $$

<!-- page: 46 -->

2. 设随机变量  $ (X, Y) $ 的概率密度为  $ f(x, y) = \begin{cases} e^{-x - y}, & x > 0, y > 0 \\ 0, & \text{其他} \end{cases} $.

(1) 求条件概率密度  $ f_{Y|X}(y|x) $ 和  $ f_{X|Y}(x|y) $;

(2) 说明 X 与 Y 的独立性。

解: $ (\mathbf{1})\because f_{Y}(y)=\left\{\begin{aligned}&\int_{0}^{+\infty}e^{-x-y}\mathrm{d}x=e^{-y},y>0,\\&0,\quad 其他\end{aligned}\right.,\quad f_{X}(x)=\left\{\begin{aligned}&\int_{0}^{+\infty}e^{-x-y}\mathrm{d}y=e^{-x},x>0,\\&0,\quad 其他\end{aligned}\right., $

 $$ \displaystyle\;\bullet\;\bullet $$ 

 $$ f_{_{Y\mid X}}\left(y\left|x\right.\right)=\left\{\begin{aligned}&\frac{f\left(x,y\right)}{f_{_{X}}\left(x\right)}=\frac{e^{-x-y}}{e^{-x}}=e^{-y},y>0\\&\quad0,\quad 其他 \end{aligned}\right.,\quad f_{_{X\mid Y}}\left(x\left|y\right.\right)=\left\{\begin{aligned}&\frac{f\left(x,y\right)}{f_{_{Y}}\left(y\right)}=e^{-x},x>0\\&\quad0,\quad 其他 \end{aligned}\right.. $$ 

(2)  $ \because f_{X}(x)f_{Y}(y)=f(x,y) $，所以，X与Y相互独立。

<!-- page: 47 -->

3. 设随机变量  $ X $ 与  $ Y $ 相互独立，试完成下表：

 $ X \mid Y $ \quad  $ y_1 $ \quad  $ y_2 $ \quad  $ y_3 $ \quad  $ p_i $。

 $ x_1 $ \quad 1/8

 $ x_2 $ \quad 1/8

 $ p_{\bullet i} $ \quad 1/6







解：显然， $ p_{11}=\frac{1}{6}-\frac{1}{8}=\frac{1}{24} $，这样就有 $ \frac{1}{6}\times p_{1\bullet}=\frac{1}{24} $，即 $ p_{1\bullet}=\frac{1}{4} $， $ p_{2\bullet}=\frac{3}{4} $；又由 $ p_{\bullet2}\times p_{1\bullet}=p_{12}=\frac{1}{8}\Rightarrow p_{\bullet2}=\frac{1}{8}/p_{1\bullet}=\frac{1}{2} $，故 $ p_{22}=\frac{1}{2}-\frac{1}{8}=\frac{3}{8} $；所以有， $ p_{13}=p_{1\bullet}-p_{11}-p_{12}=\frac{1}{4}-\frac{1}{24}-\frac{1}{8}=\frac{1}{12} $， $ p_{\bullet3}=p_{13}/p_{1\bullet}=\frac{1}{12}/\frac{1}{4}=\frac{1}{3} $， $ p_{23}=p_{\bullet3}-p_{13}=\frac{1}{3}-\frac{1}{12}=\frac{1}{4} $。即有 $ \begin{array}{r}X\mid Y\\x_{1}\\x_{2}\end{array} $  $ \begin{array}{r}y_{1}\\x_{1}\\x_{2}\end{array} $  $ \begin{array}{r}y_{2}\\x_{1}\\y_{1}\\y_{2}\\y_{3}\end{array} $  $ \begin{array}{r}y_{3}\\x_{1}\\y_{1}\\y_{2}\\y_{3}\end{array} $  $ \begin{array}{r}p_{1\bullet}\\x_{1}\\y_{1}\\y_{2}\\y_{3}\end{array} $  $ \begin{array}{r}p_{2\bullet}\\x_{1}\\y_{1}\\y_{2}\\y_{3}\end{array} $  $ \begin{array}{r}p_{1\bullet}\\x_{1}\\y_{1}\\y_{2}\\y_{3}\end{array} $  $ \begin{array}{r}p_{2\bullet}\\x_{1}\\y_{1}\\y_{2}\\y_{3}\end{array} $  $ \begin{array}{r}p_{1\bullet}\\x_{1}\\y_{1}\\y_{2}\\y_{3}\end{array} $  $ \begin{array}{r}p_{2\bullet}\\x_{

<!-- page: 48 -->

4.设X和Y是两个相互独立的随机变量，X在(0,1)内服从均匀分布，Y的概率密度为 $ f_{Y}(y)=\left\{\begin{aligned}&\frac{1}{2}e^{-\frac{y}{2}},y>0.\\&0,\quad 其他\end{aligned}\right. $



(1)求X与Y的联合概率密度；

(2)设关于a的二次方程为 $ a^{2}+2Xa+Y=0 $，求此方程有实根的概率。

解: (1) 由已知有,  $ f_{X}(x)=\left\{\begin{aligned}&1,0<x<1\\&0,\quad \text{其他}\end{aligned}\right. $,  $ f(x,y)=f_{X}(x)f_{Y}(y)=\left\{\begin{aligned}&\frac{1}{2}e^{-\frac{y}{2}},0<x<1,y>0\\&0,\quad \text{其他}\end{aligned}\right. $

(2)方程有实根为 $ \Delta \geq 0 $，即 $ 4X^2 - 4Y \geq 0 \Rightarrow Y \leq X^2 $，故有

 $$ \begin{aligned}&P\left\{Y\leq X^{2}\right\}=\iint\limits_{G}f(x,y)\mathrm{d}x\mathrm{d}y=\int_{0}^{1}\mathrm{d}x\int_{0}^{x^{2}}\frac{1}{2}e^{-\frac{y}{2}}\mathrm{d}y=\int_{0}^{1}\left(1-e^{-\frac{x^{2}}{2}}\right)\mathrm{d}x=1-\int_{0}^{1}e^{-\frac{x^{2}}{2}}\mathrm{d}x\\ &=1-\sqrt{2\pi}\int_{0}^{1}\varphi(x)\mathrm{d}x=1-\sqrt{2\pi}\big(\Phi\big(1\big)-\Phi\big(0\big)\big)=1-\sqrt{2\pi}\times0.34=0.1445.\\ \end{aligned} $$

<!-- page: 49 -->

5.一电子仪器由两部件构成，以X和Y分别表示这两个部件的寿命（单位：kh）。已知X和Y的联合分布函数为

 $$ F(x,y)=\left\{\begin{aligned}1&-e^{-0.5x}-e^{-0.5y}+e^{-0.5(x+y)},x\geq0,y\geq0\\ 0,& 其他 \end{aligned}\right.. $$ 

(1)判断X和Y是否相互独立；

(2)求两个部件的寿命都超过100h的概率 $ \alpha $.

解: $ (1)\because F_{X}(x)=F(x,+\infty)=1-e^{-0.5x},F_{Y}(y)=F(+\infty,y)=1-e^{-0.5y} $,

且 $ F_{X}(x)F_{Y}(y)=\left(1-e^{-0.5x}\right)\left(1-e^{-0.5y}\right)=F(x,y), $

所以X和Y是相互独立的。

(2)又因为， $ P\{X \geq 0.1\} = 1 - P\{X < 0.1\} = 1 - F_X(0.1) = e^{-0.05} $，同理 $ P\{Y \geq 0.1\} = e^{-0.05} $，由(1)的结论，有

 $$ P\bigl\{X\ge0.1,Y\ge0.1\bigr\}=P\bigl\{X\ge0.1\bigr\}P\bigl\{Y\ge0.1\bigr\}=e^{-0.05}\times e^{-0.05}=e^{-0.1}. $$

<!-- page: 50 -->

<div style="text-align: center;"><div style="text-align: center;">习题3-5 两个随机变量的函数的分布</div> </div>


1. 设  $ (X, Y) $ 的分布律为：0 \quad 0.25 \quad 0.1 \quad 0.3，求  $ (1) Z = X + Y $ 的分布律； $ (2) V = \min\{X, Y\} $ 的分布律。

1 \quad 0.15 \quad 0.15 \quad 0.05

解:(1)根据X、Y的取值，得Z的可能取值为0,1,2,3，即

$$P\{Z=0\}=P\{X=0,Y=0\}=0.25,P\{Z=1\}=P\{X=0,Y=1\}+P\{X=1,Y=0\}=0.25,$$

$$P\{Z=2\}=P\{X=0,Y=2\}+P\{X=1,Y=1\}=0.45,P\{Z=3\}=P\{X=1,Y=2\}=0.05,$$

所以$Z$的分布律为：

$$p_{i}\begin{array}{c}Z\\0\\0.25\end{array}\begin{array}{c}1\\0.25\\0.45\end{array}\begin{array}{c}2\\0.45\\0.05\end{array}.$$

(2) $ V = \min\{X, Y\} $的可能取值为0,1，即

 $ P\{V=0\}=P\{X=0,Y=0\}+P\{X=0,Y=1\}+P\{X=0,Y=2\}+P\{X=1,Y=0\}=0.8, $

 $ P\{V=1\}=P\{X=1,Y=1\}+P\{X=1,Y=2\}=0.2, $

所以 $ V=\min\{X,Y\} $的分布律为： $ \begin{array}{ccc}V&0&1\\p_{i}&0.8&0.2\end{array} $

<!-- page: 51 -->

2.设随机变量(X,Y)的概率密度为： $ f(x,y)=\begin{cases}6x,0\leq x\leq1,y\geq0,x+y\leq1\\0,\end{cases} $ 其他。

试求 $ Z=X+Y $的概率密度。

解：当 $ z<0,z>1 $时， $ f(x,y)=0 $;

当 $ 0\leq z\leq1 $时， $ f_{Z}(z)=\int_{-\infty}^{+\infty}f(x,z-x)dx=\int_{0}^{z}6x dx=3x^{2}\big|_{0}^{z}=3z^{2} $，

所以， $ f_{Z}(z)=\begin{cases}3z^{2},0\leq z\leq1\\0,\end{cases} $ 其他。

<!-- page: 52 -->

3.设X,Y是相互独立的随机变量, $ X\sim\pi(\lambda_{1}) $

 $ Y\sim\pi(\lambda_{2}). $证明： $ Z=X+Y\sim\pi(\lambda_{1}+\lambda_{2}). $





解：由于 $ X\sim\pi(\lambda_1) $， $ Y\sim\pi(\lambda_2) $，故有 $ P\{X=k\}=\frac{\lambda_1^k}{k!}e^{-\lambda_1} $， $ P\{Y=k\}=\frac{\lambda_2^k}{k!}e^{-\lambda_2} $， $ k=0,1,2,\cdots $。又 $ X,Y $相互独立，因此， $ P\{Z=n\}=\sum_{k=0}^{n}P\{X=k,Y=n-k\}=\sum_{k=0}^{n}P\{X=k\}=\sum_{k=0}^{n}\frac{\lambda_1^k}{k!}e^{-\lambda_1}\cdot\frac{\lambda_2^{n-k}}{(n-k)!}e^{-\lambda_2}=e^{-\left(\lambda_1+\lambda_2\right)}\sum_{k=0}^{n}\frac{\lambda_1^k\cdot\lambda_2^{n-k}}{k!\left(n-k\right)!}=e^{-\left(\lambda_1+\lambda_2\right)}\cdot\frac{1}{n!}\sum_{k=0}^{n}C_n^k\lambda_1^k\cdot\lambda_2^{n-k}=\frac{\left(\lambda_1+\lambda_2\right)^n}{n!}e^{-\left(\lambda_1+\lambda_2\right)} $， $ n=0,1,2,\cdots $。即 $ Z=X+Y\sim\pi(\lambda_1+\lambda_2) $

<!-- page: 53 -->

4.设随机变量$(X,Y)$的概率密度为$f(x,y)=\begin{cases}\dfrac{e}{e-1}e^{-(x+y)},0<x<1,y>0,\\0,\quad\text{其他}\end{cases}$

求$U=\max\{X,Y\}$的分布函数。

解：当 $ u \leq 0 $时， $ F_U(u) = 0 $;

当$0 < u \leq 1$时，$F_U(u) = \int_0^u \mathrm{d}y \int_0^u \frac{e}{e-1} e^{-(x+y)} \mathrm{d}x = \frac{e}{e-1} \int_0^u e^{-x} \mathrm{d}x \int_0^u e^{-y} \mathrm{d}y = \frac{e}{e-1} (1 - e^{-u})^2$，

当$u > 1$时，$F_U(u) = \int_0^1 \mathrm{d}x \int_0^u \frac{e}{e-1} e^{-(x+y)} \mathrm{d}y = \frac{e}{e-1} \int_0^1 e^{-x} \mathrm{d}x \int_0^u e^{-y} \mathrm{d}y = \frac{e}{e-1} \times (1 - e^{-1}) \times (1 - e^{-u}) = 1 - e^{-u}$，

所以，$U = \max\{X, Y\}$的分布函数为$F_U(u) = \begin{cases} 0, & u < 0 \\ \frac{e}{e-1} (1 - e^{-u})^2, & 0 < u \leq 1. \\ 1 - e^{-u}, & u > 1 \end{cases}$

<!-- page: 54 -->

5. 设随机变量 $ X $和 $ Y $相互独立， $ Z = X + Y $，

且 $ X $的概率分布为 $ P\{X = i\} = \frac{1}{3}(i = -1,0,1) $，

 $ Y $的概率密度为 $ f_Y(y) = \left\{ \begin{array}{ll} 1, & 0 \leq y \leq 1 \\ 0, & \text{其它} \end{array} \right. $，

(1)求 $ P\left\{Z\leq\frac{1}{2}\mid X=0\right\};(2) $求Z的概率密度。

解: (1) 由已知 X 和 Y 相互独立, 有

 $$ \begin{aligned}&P\left\{\mathbf{Z}\leq\frac{\mathbf{1}}{2}\middle|X=\mathbf{0}\right\}=P\left\{X+Y\leq\frac{\mathbf{1}}{2}\middle|X=\mathbf{0}\right\}=P\left\{Y\leq\frac{\mathbf{1}}{2}\middle|X=\mathbf{0}\right\}\\&\frac{P\left\{Y\leq\frac{\mathbf{1}}{2},X=\mathbf{0}\right\}}{P\left\{X=\mathbf{0}\right\}}=\frac{P\left\{Y\leq\frac{\mathbf{1}}{2}\right\}P\left\{X=\mathbf{0}\right\}}{P\left\{X=\mathbf{0}\right\}}=P\left\{Y\leq\frac{\mathbf{1}}{2}\right\}\\&=\int_{0}^{\frac{1}{2}}f_{Y}\left(y\right)\mathrm{d}y=\frac{\mathbf{1}}{2}.\\ \end{aligned} $$

<!-- page: 55 -->

$$ \begin{aligned}&\left(2\right) 先求 \mathbb{Z} 的分布函数 F_{z}\left(z\right),\  由全概率公式可得：P\left\{\mathbb{Z}\leq z\right\}\\&=P\left\{X+Y\leq z\right\}=P\left\{Y\leq z-X\right\}=\sum_{i=-1,0,1}P\left\{Y\leq\mathbb{Z}-i,X=i\right\}\\&=P\left\{Y\leq z+1,X=-1\right\}+P\left\{Y\leq z,X=0\right\}+P\left\{Y\leq z-1,X=1\right\}\\&=\sum_{i=-1,0,1}P\left\{Y\leq\mathbb{Z}-i\left|X=i\right.\right\}P\left\{X=i\right\}\\&=\frac{1}{3}\Big(P\left\{Y\leq z+1\right\}+P\left\{Y\leq z\right\}+P\left\{Y\leq z-1\right\}\Big)\\&=\frac{1}{3}\Big(F_{Y}\left(z+1\right)+F_{Y}\left(z\right)+F_{Y}\left(z-1\right)\Big)\\&\therefore f_{z}\left(z\right)=F_{z}^{\prime}\left(z\right)=\frac{1}{3}\Big(F_{Y}^{\prime}\left(z+1\right)+F_{Y}^{\prime}\left(z\right)+F_{Y}^{\prime}\left(z-1\right)\Big)\\&=\frac{1}{3}\Big(f_{Y}\left(z+1\right)+f_{Y}\left(z\right)+f_{Y}\left(z-1\right)\Big),\end{aligned} $$

<!-- page: 56 -->

$$\because \left\{ \begin{array} { l } { Z = X + Y , } \\ { X = -1 , 0 , 1 , } \end{array} \right. \Rightarrow \left\{ \begin{array} { l } { Z \text { 是连续型随机变量，且 } } \\ { 0 \leq Z - X \leq 1 , \left( Y = Z - X \right) } \end{array} \right. \Rightarrow \left\{ \begin{array} { l } { 0 \leq Z + 1 \leq 1 } \\ { 0 \leq Z \leq 1 } \\ { 0 \leq Z - 1 \leq 1 } \end{array} \right.$$

$$ \mathbf { 0 } \leq y \leq 1 , \quad \text { 将 } X \text { 的三个值分别代入，有 } \left\{ \begin{array} { l } { - 1 \leq Z \leq 0 , } \\ { 0 \leq Z \leq 1 , } \\ { 1 \leq Z \leq 2 } \end{array} \right. \text { 此时 } f _ { Y } ( z ) , f _ { Y } ( z - 1 ) \text { 都为 } 0 ,$$

$$ \Rightarrow \left\{ \begin{array} { l } { - 1 \leq Z \leq 0 , } \\ { 0 \leq Z \leq 1 , } \\ { 1 \leq Z \leq 2 } \end{array} \right. \text { 此时 } f _ { Y } ( z + 1 ) , f _ { Y } ( z - 1 ) \text { 都为 } 0 , \quad \text {   } . \)



 $$ \therefore f_{z}\left(z\right)=\left\{\begin{aligned}&\frac{1}{3}f_{Y}\left(z+1\right)=\frac{1}{3},-1\leq z\leq0\\&\frac{1}{3}f_{Y}\left(z\right)=\frac{1}{3},0\leq z\leq1\\&\frac{1}{3}f_{Y}\left(z-1\right)=\frac{1}{3},1\leq z\leq2\\&0,\quad\  其它 \ \end{aligned}\right.\Rightarrow f_{z}\left(z\right)=\left\{\begin{aligned}&\frac{1}{3},-1\leq z\leq2\\&0,\quad 其它 \end{aligned}\right. $$

