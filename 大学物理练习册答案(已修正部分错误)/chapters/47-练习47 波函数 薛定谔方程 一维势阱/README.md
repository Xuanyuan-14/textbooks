# 47-练习47 波函数 薛定谔方程 一维势阱

[返回全书目录](../../README.md)

> PDF 页码：349–355

<!-- page: 349 -->

### 练习47 波函数 薛定谔方程 一维势阱

1. 设描述微观粒子运动的波函数为  $ \psi(\vec{r},t) $，则  $ \psi\psi^{*} $ 表示  $ \underline{\quad\vec{r}处t时刻的概率密度\quad} $； $ \psi(\vec{r},t) $ 须满足的条件是  $ \underline{\quad\text{单值，连续，有限}} $；其归一化条件是  $ \underline{\quad\int_{-\infty}^{+\infty}\psi\psi^{*}\mathrm{d}v=1} $。

解：根据概率密度的定义： $ \psi\psi^{*} $表示 $ \vec{r} $处t时刻的概率密度描述微观粒子的波函数 $ \psi(\vec{r},t) $必须满足三个标准条件：

单值，连续，有限

在整个空间找到粒子的概率为100%，故有归一化条件

 $$ \int_{-\infty}^{+\infty}\psi\psi^{*}dv=1 $$

<!-- page: 350 -->

2. 一维谐振动处在  $ \psi(x)=\sqrt{\frac{\alpha}{\pi^{1/2}}}e^{-\frac{1}{2}\alpha^2x^2-\frac{1}{2}i\omega t} $ 的状态。式中  $ \alpha,\omega $ 均为常数， $ i=\sqrt{-1} $，则  $ \int_{-\infty}^{\infty}\psi\psi^*dx=\underline{1} $。

解：根据归一化条件

 $$ \int_{-\infty}^{+\infty}\psi\psi^{*}d x=\int_{-\infty}^{+\infty}\sqrt{\frac{a}{\pi^{1/2}}}e^{-\frac{1}{2}a^{2}x^{2}-\frac{1}{2}i\omega t}\sqrt{\frac{a}{\pi^{1/2}}}e^{-\frac{1}{2}a^{2}x^{2}+\frac{1}{2}i\omega t}d x=1 $$

<!-- page: 351 -->

3. 宽度为 a 的一维无限深势阱中的基态粒子在 0.25 a

0.75 a 之间出现的概率为  $ \underline{0.818} $。

解： 宽度为a的一维无限深势阱在基态的波函数为

 $$ \psi(x)=\sqrt{\frac{2}{a}}\sin\frac{\pi x}{a}\quad(0\prec x\prec a) $$ 

在0.25a到0.75a之间出现的概率为

 $$ \int_{0.25a}^{0.75a}\psi\psi^{*}d x=\int_{0.25a}^{0.75a}\sqrt{\frac{2}{a}}\sin\frac{\pi x}{a}\times\sqrt{\frac{2}{a}}\sin\frac{\pi x}{a}d x=0.818 $$

<!-- page: 352 -->

4. 试用不确定关系估算：在宽度为 $a$ 的一维无限深势阱中，质量为 $m$ 的粒子的最低能量。（不确定关系式 $P_{x} = \Delta P_{x}$，$\Delta x \cdot \Delta P_{x} \geq h$）

解：粒子位置的不确定量  $ \Delta x = a $，由  $ \Delta x \Delta P_{x} \geq h $ 可得： $ \Delta P_{x} \geq \frac{h}{a} $

粒子的最低能量： $ E_{1}=\frac{P_{x}^{2}}{2m}=\frac{\Delta P_{x}^{2}}{2m}=\frac{\left(\frac{h}{a}\right)^{2}}{2m}=\frac{h^{2}}{2ma^{2}} $

<!-- page: 353 -->

5. 一维运动的粒子处在  $ \psi(x)=\left\{\begin{aligned}&0&(x<0)\\ &Axe^{-\lambda x&(x\geq0)\end{aligned}\right. $ 描写的状态中，其中  $ \lambda $ 是正常数。（1）将  $ \psi(x) $ 归一化；（2）求粒子概率密度分布函数；（3）在什么位置找到粒子的概率最大。（提示：积分公式  $ \int_{0}^{\infty}x^{2}e^{-ax}dx=\frac{2}{a^{3}} $）

解：① 由波函数的归一化条件可得：

 $ \int_{0}^{\infty}A^{2}x^{2}e^{-2\lambda x}dx = 1 $

用部分积分法，可得： $ \int_{0}^{\infty}A^{2}x^{2}e^{-2\lambda x}dx = -\frac{A^{2}}{4\lambda^{3}}e^{-2\lambda x}\bigg|_{0}^{\infty} = \frac{A^{2}}{4\lambda^{3}} = 1 $

所以  $ A = 2\lambda^{\frac{3}{2}} $，归一化波函数为：

 $$ \Psi(x)=\left\{\begin{matrix}\mathbf{0}&{(x<0)}\\ {2\lambda^{3/2}x e^{-\lambda x}}&{(x\geq0)}\\ \end{matrix}\right. $$

<!-- page: 354 -->

5. 一维运动的粒子处在  $ \psi(x)=\left\{\begin{array}{ll}0 & (x<0) \\ Axe^{-\lambda x} & (x\geq0)\end{array}\right. $ 描写的状态中，其中  $ \lambda $ 是正常数。（1）将  $ \psi(x) $ 归一化；（2）求粒子概率密度分布函数；（3）在什么位置找到粒子的概率最大。（提示：积分公式  $ \int_{0}^{\infty}x^{2}e^{-ax}dx=\frac{2}{a^{3}} $）

②粒子概率密度发布函数为 $ P(x)=\left|\psi(x)\right|^2 $，所以：

 $$ P(x)=\left\{\begin{array}{cc}\mathbf{0}&(x<O)\\4\lambda^{3}x^{2}e^{-2\lambda x}&(x\geq O)\end{array}\right. $$ 

③ 令  $ \frac{dP(x)}{dx}\bigg|_{x=x_0}=0 $，有

 $ 4\lambda^{3}(2x_{0}e^{-2\lambda x_{0}}-2\lambda x_{0}^{2}e^{-2\lambda x_{0}})=0 $ 所以  $ x_{0}=\frac{1}{\lambda} $

<!-- page: 355 -->

6. 设质量 m 的微观粒子在宽度为 a 的一维无限深方势阱中运动，其波函数为  $ \psi(x) = \sqrt{\frac{2}{a}} \sin \frac{3\pi}{a} x $，求：

（1）粒子的能量和动量；（2）概率密度最大的位置

(1)  $ \mathrm{E}=\frac{\hbar^{2}k^{2}}{2m}=\frac{n^{2}\hbar^{2}k^{2}}{2ma^{2}}=\frac{9\hbar^{2}k^{2}}{2ma^{2}} $

又 $ \mathrm{E}=\frac{P^{2}}{2m}\Rightarrow P=\pm\sqrt{2mE}=\pm\sqrt{\frac{9\hbar^{2}\pi^{2}}{a^{2}}}=\pm\frac{3\hbar\pi}{a} $

(2)  $ \frac{\partial P(x)}{\partial x}=0 $  $ \Rightarrow x=\frac{a}{6},\frac{a}{2},\frac{5a}{6} $

