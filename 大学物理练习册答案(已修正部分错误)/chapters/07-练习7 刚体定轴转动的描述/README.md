# 07-练习7 刚体定轴转动的描述

[返回全书目录](../../README.md)

> PDF 页码：49–54

<!-- page: 49 -->

### 练习7 刚体定轴转动的描述

1. 半径为  $ r=1.5 \, m $ 的飞轮，初角速度  $ \omega_{0}=10 \, rad \cdot s^{-1} $，角加速度  $ \beta=-5 \, rad \cdot s^{-2} $，则在  $ t= $  $ \underline{4s} $时角位移为零，而此时边缘上点的线速度大小  $ v=\underline{15 m/s} $

解： $ \beta = -5 rad / s^{2} \Rightarrow d\omega = -5dt $

两边积分得 $ \int_{\omega_{0}}^{\omega}d\omega=\int_{0}^{t}-5dt\Rightarrow\omega=\omega_{0}-5t $

即： $ \frac{d\theta}{dt}=\omega_{0}-5t\Rightarrow\Delta\theta=\omega_{0}t-\frac{5}{2}t^{2} $

若 $ \Delta\theta=0 $，则 $ \omega_{0}t=\frac{5}{2}t^{2}\Rightarrow t=\frac{2\omega_{0}}{5}=4s $

 $ v = \omega r = (\omega_{0} - 5 \, \text{t}) \, r \Rightarrow v = 15 \, \text{m/s} $

<!-- page: 50 -->

2. 一作匀变速转动的飞轮在 10s 内转了 16 圈，其末角速度为 15 rad/s，它的角加速度的大小为  $ \underline{0.99 rad/s^{2}} $。

解：根据运动学公式  $ \omega = \omega_{0} + \beta t $

 $$ \Delta\theta\;=\;\omega_{0}t\;+\frac{1}{2}\;\beta t^{2} $$ 

 $$ \therefore\ \beta=2(\omega\ t-\Delta\theta)/\ t^{2} $$ 

将 $ \omega=15\ rad/s $， $ t=10\ s $， $ \Delta\theta=32\pi rad $代入上式得

 $$ \beta=0.99rad/s^{2} $$

<!-- page: 51 -->

3. 半径为 30 cm 的飞轮，从静止开始以  $ 0.50 \, rad \cdot s^{-2} $ 的匀角加速度转动，则飞轮边缘上一点在飞轮转过  $ 240^{\circ} $ 时的切向加速度大小  $ a_{\tau} = \underline{0.15 \, m/s^{2}} $，法向加速度大小  $ a_{n} = \underline{0.4\pi \, m/s^{2}} $。

解：依题意，从静止开始转动有 $ \omega = \beta t \Rightarrow \Delta \theta = 0.25 t^{2} $

 $$ \begin{array}{c} v=\omega r=r\beta t=0.3\times0.5t=0.15t\\ \Rightarrow\ a_{_{\tau}}=\frac{d v}{d t}=0.15m/s^{2};\ a_{_{n}}=\frac{v^{2}}{R}=\frac{(0.15t)^{2}}{0.3}\end{array} $$ 

当 $ \Delta\theta = 240^\circ $时，即： $ 0.25t^2 = \frac{4}{3}\pi \Rightarrow t^2 = \frac{16}{3}\pi $

 $$ \Rightarrow a_{n}=0.4\pi m/s^{2} $$

<!-- page: 52 -->

4. 一飞轮以等角加速度 2 rad /s $ ^{2} $转动，在某时刻以后的 5s 内飞轮转过了 100 rad. 若此飞轮是由静止开始转动的，问在上述的某时刻以前飞轮转动了多少时间?

解：设在某时刻之前，飞轮已转动了 $ t_{1} $时间，由于初角速度  $ \omega_{0}=0 $

 $$ \omega_{1}\;=\;\beta t_{1} $$ 

而在某时刻后 $ t_{2}=5 $ s时间内，转过的角位移为

$$  \theta~=~\omega_{1}t_{2}~+~\frac{1}{2}~\beta t_{2}^{2}   \tag*{(2)}$$

将已知量 $ \theta = 100rad, t_{2} = \overline{5}s, \beta = 2rad / s^{2} $代入式（2）得

 $$ \omega_{1}=15r a d/s $$ 

从而， $ t_{1} = \omega_{1} / \beta = 7.5s $

即在某时刻之前，飞轮已经转动了7.5 s

<!-- page: 53 -->

5. 已知一定轴转动体系，在各个时间间隔内的角速度如下：

$$  \omega=3+3t\quad0\leqslant t\leqslant8   \tag*{(SI)}$$

 $$ \omega=51-3t\quad t\geqslant8\quad(SI) $$ 

若 t=0 时， $ \theta_{0}=0 $，求当体系角速度变为零时角位移的大小。

解：体系所做的运动是先做匀加速转动，后做匀减速转动.

其中  $ \omega = 3 + 3t $ （ $ 0 \leq t \leq 8 $）为匀加速阶段

其中  $ \omega = 51 - 3t $ （ $ t \geq 8 $）为匀减速阶段

当系统角速度变为时，有

 $$ 51-3\mathrm{t}=0\Rightarrow\mathrm{t}=17\mathrm{s} $$ 

若t = 0时， $ \theta_{0} = 0 $，则

 $$ \Delta\theta=\int_{0}^{8}\left(3+3\mathrm{t}\right)\mathrm{~d}\mathrm{t}+\int_{8}^{17}\left(51-3\mathrm{t}\right)\mathrm{d}\mathrm{t}=241.5\mathrm{rad} $$

<!-- page: 54 -->

6. 半径为 20 cm 的主动轮，通过皮带拖动半径为 50 cm 的从动轮转动，皮带与轮之间无相对滑动。主动轮从静止开始作匀角加速转动。在 4 s 内从动轮的角速度达到  $ 8\pi \, rad \cdot s^{-1} $，则主动轮在这段时间内转过了多少圈？

解：依题意，主动轮从静止开始转动有$\omega_{主} = \beta t \Rightarrow \Delta\theta_{主} = \frac{1}{2}\beta t^{2}$

主动轮与从动轮不打滑，有：$v_{主} = v_{从}$，即$\omega_{主}R_{主} = \omega_{从}R_{从}$

$\omega_{从} = \frac{R_{主}}{R_{从}} \omega_{主} = \frac{R_{主}}{R_{从}} \beta t = 0.4\beta t$

$t = 4s$时，$\omega_{从} = 0.4\beta t = 8\pi rad / s \Rightarrow \beta = 5\pi rad / s^{2}$

$\therefore t = 4s$时，$\Delta\theta_{主} = \frac{1}{2}\beta t^{2} = \frac{1}{2} \times 5\pi \times 4^{2} = 40\pi r a a$

主动轮转过的圈数$n = \Delta\theta / 2\pi = 40\pi / 2\pi = 20$圈

