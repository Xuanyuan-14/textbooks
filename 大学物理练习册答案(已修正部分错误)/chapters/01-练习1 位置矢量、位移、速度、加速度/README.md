# 01-练习1 位置矢量、位移、速度、加速度

[返回全书目录](../../README.md)

> PDF 页码：1–6

<!-- page: 1 -->

##### 练习1 位置矢量、位移、速度、加速度

1. 一物体在某瞬时以初速度  $ \vec{v}_{0} $ 从某点开始运动，在  $ \Delta t $ 时间内，经一长度为  $ \Delta s $ 的曲线路径后，又回到出发点，此时速度为  $ -\vec{v}_{0} $，则在这段时间内物体的平均速率为  $ \underline{\Delta S / \Delta t} $，物体的平均加速度为  $ -2\vec{v}_{0} / \Delta t $

解：根据平均速率公式可知 $ \bar{v}=\frac{\Delta S}{\Delta t} $

根据平均加速度公式可知 $ \overline{a}=\frac{\Delta\overrightarrow{v}}{\Delta t}=\frac{-\overrightarrow{v}_{0}-\overrightarrow{v}_{0}}{\Delta t}=-\frac{2\overrightarrow{v}_{0}}{\Delta t} $

<!-- page: 2 -->

2. 一质点在平面内运动，已知质点位置矢量表示为  $ \vec{r} = at^{2}\vec{i} +bt^{2}\vec{j} $，其中 a, b 为常量，则质点作  $ \underline{\text{匀变速直线}} $ 运动。

解：

依题意 $ \overrightarrow{r}=at^{2}\overrightarrow{i}+bt^{2}\overrightarrow{j} $

速度 $ \overrightarrow{v}=\frac{d\overrightarrow{r}}{dt}=2at\overrightarrow{i}+2bt\overrightarrow{j} $

加速度 $ \overrightarrow{a}=\frac{d\overrightarrow{v}}{dt}=2a\overrightarrow{i}+2b\overrightarrow{j} $是常量，所以质点作匀变速运动

又由 $ \begin{aligned}x&=at^{2}\\ y&=bt^{2}\end{aligned} $  $ \Rightarrow $  $ y=\frac{b}{a}x\Rightarrow $ 质点作直线运动

质点作匀变速直线运动

<!-- page: 3 -->

3. 一质点的运动方程为  $ x = 6t - t^{2}(SI) $，则在  $ 0 \sim 4s $ 的时间间隔内，质点的位移大小为  $ \underline{8m} $，在  $ 0 \sim 4s $ 的时间间隔内质点走过的路程为  $ \underline{10m} $。

解：依题意，质点作一维运动， $ x=6t-t^{2} $

由0~4s的时间间隔内，质点位移大小 $ \Delta x=6\times4-4^{2}=8m $

 $ v=\frac{dx}{dt}=6-2t\Rightarrow a=\frac{dv}{dt}=-2m/s^{2} $

加速度小于零，质点先作匀减速直线运动，后作反方向的匀加速直线运动

当t=3时，速度为零。0~3s内质点所走路程 $ \Delta s=(6\times3-3^{2})-0=9m $

 $ 3s \sim 4s $ 内，质点所走路程  $ \Delta s' = \left|(6 \times 4 - 4^{2}) - (6 \times 3 - 3^{2})\right| = 1m $

0s ~ 4s内，质点所走总路程 $ \Delta s'=9m+1m=10m $

<!-- page: 4 -->

4. 已知质点的运动方程： $ \overrightarrow{r}(t)=3t\overrightarrow{i}+(5-t^{2})\overrightarrow{j}-t^{3}\overrightarrow{k}(m) $。则：(1)  $ t=3s $ 时的速度；(2)  $ 1s \sim 4s $ 内的平均速度。

解：（1）依题意 $ \vec{r}=3t\vec{i}+(5-t^2)\vec{j}-t^3\vec{k} $ m

速度 $ \vec{v}=\frac{d\vec{r}}{dt}=3\vec{i}-2t\vec{j}-3t^2\vec{k} $ m/s

当t=3s时，速度 $ \vec{v}=3\vec{i}-6\vec{j}-27\vec{k} $ m/s

(2) t=1s时， $ \overrightarrow{r}(1)=3\overrightarrow{i}+4\overrightarrow{j}-1\overrightarrow{k} $ m

t=4s时， $ \overrightarrow{r}(4)=12\overrightarrow{i}-11\overrightarrow{j}-64\overrightarrow{k} $ m

1s~4s的平均速度 $ \overrightarrow{v}=\frac{\Delta\overrightarrow{r}}{\Delta t}=\frac{\overrightarrow{r}(4)-\overrightarrow{r}(1)}{4-1}=3\overrightarrow{i}-5\overrightarrow{j}-21\overrightarrow{k} $ m/s

<!-- page: 5 -->

5. 一质点在 xoy 平面内运动:  $ x = -t^{2} $， $ y = -t^{4} + 2t^{2} $

求： x = -4m (t > 0) 时质点的速度、速率及加速度。

解：（1）依题意 $ \overrightarrow{r}=(-\mathrm{t}^{2})\overrightarrow{i}+(-\mathrm{t}^{4}+2\mathrm{t}^{2})\overrightarrow{j} $ m

 $$ \begin{aligned}\Rightarrow\left\{\begin{aligned}\vec{v}&=\frac{d\vec{r}}{dt}=-2t\vec{i}+(-4\mathrm{t}^{3}+4\mathrm{t})\vec{j}\\v&=\sqrt{4t^{2}+(4\mathrm{t}-4\mathrm{t}^{3})^{2}}\\\vec{a}&=\frac{d\vec{v}}{dt}=-2\vec{i}+(-12\mathrm{t}^{2}+4)\vec{j}\end{aligned}\right.\end{aligned} $$ 

 $$ \overrightarrow{v}=-4\overrightarrow{i}-24\overrightarrow{j}m/s $$ 

当 $ x=-4m $时, $ -t^{2}=-4\Rightarrow t=2s\Rightarrow\begin{cases}v=4\sqrt{37}m/s\\\vec{a}=-2\vec{i}-44\vec{j}m/s^{2}\end{cases} $

<!-- page: 6 -->

6. 已知质点运动的加速度为： $ \vec{a}=6\vec{i}+4\vec{j} $， $ t=0 $时 $ v_{0}=0 $， $ \vec{r}_{0}=10\vec{i} $，求：任一时刻质点的位置（即运动方程）。

解：依题意 $ \overrightarrow{a}=6\overrightarrow{i}+4\overrightarrow{j}\Rightarrow\overrightarrow{v}=6t\overrightarrow{i}+4t\overrightarrow{j} $

$\because t=0$时，$v_{0}=0,\vec{r}_{0}=10\vec{i}\quad\vec{v}=\frac{d\vec{r}}{dt}\Rightarrow d\vec{r}=\vec{v}dt=(6t\vec{i}+4t\vec{j})$ dt上式两边积分$\int_{\vec{r}_{0}}^{\vec{r}}d\vec{r}=\int_{0}^{t}(6t\vec{i}+4t\vec{j})$ dt

 $$ \vec{r}=(10+3t^{2})\overrightarrow{i}+2t^{2}\overrightarrow{j} $$

