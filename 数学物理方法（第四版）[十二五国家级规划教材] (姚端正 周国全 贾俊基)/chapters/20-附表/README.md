# 20-附表

[返回全书目录](../../README.md)

> PDF 页码：363–367

<!-- page: 363 -->

### Ⅰ．矢量微分算子与拉普拉斯算符

## 1. 矢量微分算符 $ \nabla $

$$  \nabla=\frac{\partial}{\partial x}\boldsymbol{i}+\frac{\partial}{\partial y}\boldsymbol{j}+\frac{\partial}{\partial z}\boldsymbol{k}   \tag*{(Ⅰ.1)}$$

称子

如果函数  $ u(x,y,z) $ 和矢量 A $ (x,y,z) $ 具有连续的一阶偏导数，则定义

（1）函数  $ u(x,y,z) $ 的梯度为

$$  \nabla u=\frac{\partial u}{\partial x}\mathbf{i}+\frac{\partial u}{\partial y}\mathbf{j}+\frac{\partial u}{\partial z}\mathbf{k}   \tag*{(I.2)}$$

(2) 矢量 A(x,y,z) 的散度为

$$  \nabla\cdot\boldsymbol{A}=\left(\frac{\partial}{\partial x}\boldsymbol{i}+\frac{\partial}{\partial y}\boldsymbol{j}+\frac{\partial}{\partial z}\boldsymbol{k}\right)\cdot(\boldsymbol{A}_{x}\boldsymbol{i}+\boldsymbol{A}_{y}\boldsymbol{j}+\boldsymbol{A}_{z}\boldsymbol{k})=\frac{\partial\boldsymbol{A}_{x}}{\partial x}+\frac{\partial\boldsymbol{A}_{y}}{\partial y}+\frac{\partial\boldsymbol{A}_{z}}{\partial z}   \tag*{(I.3)}$$

（3）矢量 $ A(x,y,z) $的旋度为

$$  \begin{aligned}\nabla\times\boldsymbol{A}=&\begin{vmatrix}\boldsymbol{i}&\boldsymbol{j}&\boldsymbol{k}\\\frac{\partial}{\partial x}&\frac{\partial}{\partial y}&\frac{\partial}{\partial z}\\A_{x}&A_{y}&A_{z}\end{vmatrix}=\begin{vmatrix}\frac{\partial}{\partial y}&\frac{\partial}{\partial z}\\A_{y}&A_{z}\end{vmatrix}\boldsymbol{i}-\begin{vmatrix}\frac{\partial}{\partial x}&\frac{\partial}{\partial z}\\A_{x}&A_{z}\end{vmatrix}\boldsymbol{j}+\begin{vmatrix}\frac{\partial}{\partial x}&\frac{\partial}{\partial y}\\A_{x}&A_{y}\end{vmatrix}\boldsymbol{k}\\=&\big(\frac{\partial A_{z}}{\partial y}-\frac{\partial A_{y}}{\partial z}\big)\boldsymbol{i}+\big(\frac{\partial A_{x}}{\partial z}-\frac{\partial A_{z}}{\partial x}\big)\boldsymbol{j}+\big(\frac{\partial A_{y}}{\partial x}-\frac{\partial A_{x}}{\partial y}\big)\boldsymbol{k}\end{aligned}   \tag*{(Ⅰ.4)}$$

2. 拉普拉斯算符  $ \Delta $

$$  \Delta=\nabla^{2}=\frac{\partial^{2}}{\partial x^{2}}+\frac{\partial^{2}}{\partial y^{2}}+\frac{\partial^{2}}{\partial z^{2}}   \tag*{(I.5)}$$

称为拉普拉斯算符，

$$  \Delta u=\nabla\cdot(\nabla u)=\frac{\partial^{2}u}{\partial x^{2}}+\frac{\partial^{2}u}{\partial y^{2}}+\frac{\partial^{2}u}{\partial z^{2}}   \tag*{(Ⅰ.6)}$$

$$  \Delta\mathbf{A}=(\Delta A_{x})\mathbf{i}+(\Delta A_{y})\mathbf{j}+(\Delta A_{z})\mathbf{k}   \tag*{(I.7)}$$

## 3.  $ \nabla $ 和  $ \Delta $ 的运算公式

设函数  $  u(x, y, z)  $,  $  v(x, y, z)  $ 和矢量  $  A(x, y, z)  $,  $  B(x, y, z)  $ 的一阶偏导数存在，则

<!-- page: 364 -->

有

$$  \nabla(u+v)=\nabla u+\nabla v   \tag*{(I.8)}$$

$$  (2)\nabla\cdot(\boldsymbol{A}+\boldsymbol{B})=\nabla\cdot\boldsymbol{A}+\nabla\cdot\boldsymbol{B}   \tag*{(I.9)}$$

$$  (3)\nabla\times(\boldsymbol{A}+\boldsymbol{B})=\nabla\times\boldsymbol{A}+\nabla\times\boldsymbol{B}   \tag*{(Ⅰ.10)}$$

$$  \nabla\cdot(u\mathbf{A})=(\nabla u)\cdot\mathbf{A}+u(\nabla\cdot\mathbf{A})   \tag*{(Ⅰ.11)}$$

$$  \nabla\times(u\mathbf{A})=(\nabla u)\times\mathbf{A}+u(\nabla\times\mathbf{A})   \tag*{(Ⅰ.12)}$$

$$  (6)\nabla\cdot(\mathbf{A}\times\mathbf{B})=\mathbf{B}\cdot(\nabla\times\mathbf{A})-\mathbf{A}\cdot(\nabla\times\mathbf{B})   \tag*{(Ⅰ.13)}$$

$$  \nabla\times(\boldsymbol{A}\times\boldsymbol{B})=(\boldsymbol{B}\cdot\nabla)\boldsymbol{A}-\boldsymbol{B}(\nabla\cdot\boldsymbol{A})-(\boldsymbol{A}\cdot\nabla)\boldsymbol{B}+\boldsymbol{A}(\nabla\cdot\boldsymbol{B})   \tag*{(Ⅰ.14)}$$

$$  \nabla(\boldsymbol{A}\cdot\boldsymbol{B})=(\boldsymbol{B}\cdot\nabla)\boldsymbol{A}+(\boldsymbol{A}\cdot\nabla)\boldsymbol{B}+\boldsymbol{B}\times(\nabla\times\boldsymbol{A})+\boldsymbol{A}\times(\nabla\times\boldsymbol{B})   \tag*{(I.15)}$$

(9) $ \nabla\times(\nabla u)=0 $（当u的二阶偏导连续时）

（10） $ \nabla\cdot(\nabla\times\boldsymbol{A})=0 $（当A的二阶偏导连续时）

$$  (11)\nabla\times(\nabla\times\boldsymbol{A})=\nabla(\nabla\cdot\boldsymbol{A})-\Delta\boldsymbol{A}( 当 \boldsymbol{A} 的二阶偏导连续时 )   \tag*{(Ⅰ.18)}$$

## 4. 常用的矢量定理和矢量公式

（1）高斯定理：对于空间中以s为边界面的任意体积v有

$$  \oint_{s}\boldsymbol{A}\cdot\mathrm{d}\boldsymbol{s}=\oint_{v}\nabla\cdot\boldsymbol{A}\mathrm{d}v   \tag*{(Ⅰ.19)}$$

（2）斯托克斯定理：对于空间中以 l 为边界线的任意曲面积 s 有

$$  \oint_{l}\boldsymbol{A}\cdot\mathrm{d}\boldsymbol{l}=\oint_{s}\nabla\times\boldsymbol{A}\cdot\mathrm{d}s   \tag*{(Ⅰ.20)}$$

（3）格林公式：对于平面上以 l 为边界围线的闭区域  $ \bar{s} $ 中一阶连续可微的标量函数 u, v 有

$$  \oint_{l}u\mathrm{d}x+v\mathrm{d}y=\iint_{\bar{s}}\left(\frac{\partial v}{\partial x}-\frac{\partial u}{\partial y}\right)\mathrm{d}s   \tag*{(Ⅰ.21)}$$

<!-- page: 365 -->

<div style="text-align: center;"><div style="text-align: center;">Ⅱ．傅里叶变换简表</div> </div>




<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>像原函数</td><td style='text-align: center; word-wrap: break-word;'>像函数</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ f(x) = \frac{1}{2\pi}\int_{-\infty}^{\infty} G(\omega) e^{i\omega x} d\omega $</td><td style='text-align: center; word-wrap: break-word;'>$ G(\omega) = \int_{-\infty}^{\infty} f(x) e^{-i\omega x} dx $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \frac{\sin ax}{x} $</td><td style='text-align: center; word-wrap: break-word;'>$ \pi (|\omega| \leq a) $\n $ 0 (|\omega| &gt; a) $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \mathrm{e}^{\mathrm{j}\omega x} (a &lt; x &lt; b) $\n $ 0 (x &lt; a \text{ 或 } x &gt; b) $</td><td style='text-align: center; word-wrap: break-word;'>$ \frac{\mathrm{i}}{\beta - \omega} [\mathrm{e}^{\omega(\beta - \omega)} - \mathrm{e}^{\mathrm{j}\omega(\beta - \omega)}] $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \mathrm{e}^{-cx + \mathrm{j}\omega x} (x &gt; 0) $\n $ 0 (x &lt; 0) $</td><td style='text-align: center; word-wrap: break-word;'>$ \frac{\mathrm{i}}{\beta - \omega + i\bar{c}} $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \mathrm{e}^{-\eta r^2} (\mathrm{Re}\eta &gt; 0) $</td><td style='text-align: center; word-wrap: break-word;'>$ \sqrt{\frac{\pi}{\eta}} \mathrm{e}^{-\frac{\omega^2}{4\eta}} $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \cos\eta x^2 $</td><td style='text-align: center; word-wrap: break-word;'>$ \sqrt{\frac{\pi}{\eta}} \cos\left(\frac{\omega^2}{4\eta} - \frac{\pi}{4}\right) $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \sin\eta x^2 $</td><td style='text-align: center; word-wrap: break-word;'>$ -\sqrt{\frac{\pi}{\eta}} \sin\left(\frac{\omega^2}{4\eta} - \frac{\pi}{4}\right) $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ |x|^{-s} (0 &lt; \mathrm{Re}s &lt; 1) $</td><td style='text-align: center; word-wrap: break-word;'>$ \frac{2}{|\omega|} \Gamma(1 - s) \sin \frac{1}{2} \pi s $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \frac{1}{|x|} $</td><td style='text-align: center; word-wrap: break-word;'>$ \frac{\sqrt{2\pi}}{|\omega|} $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \mathrm{e}^{-a|x|} $</td><td style='text-align: center; word-wrap: break-word;'>$ \frac{2a}{\omega^2 + a^2} $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \frac{1}{x^2 + a^2}, a &gt; 0 $</td><td style='text-align: center; word-wrap: break-word;'>$ \frac{\pi}{a} \mathrm{e}^{-a|x|} $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \left\{\begin{array}{l} \mathrm{e}^{-ax}, \quad x \geq 0, \\ 0, \quad x &lt; 0, \end{array}\right.\ a &gt; 0 $</td><td style='text-align: center; word-wrap: break-word;'>$ \frac{1}{a + i\omega} $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \frac{\mathrm{e}^{\pi x}}{(1 + \mathrm{e}^{\pi x})^2} $</td><td style='text-align: center; word-wrap: break-word;'>$ \pi^2 \frac{\omega}{\sin\omega} $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \ln \frac{x^2 + a^2}{x^2 + b^2}, a, b \geq 0 $</td><td style='text-align: center; word-wrap: break-word;'>$ \frac{2\pi}{|\omega|} (\mathrm{e}^{b|x| - a|x|}) $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \mathrm{e}^{-\frac{x^2}{4a^2}}, a &gt; 0 $</td><td style='text-align: center; word-wrap: break-word;'>$ 2a \sqrt{\pi} \mathrm{e}^{-a^2 \omega^2} $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \arctan \frac{x}{a}, a &gt; 0 $</td><td style='text-align: center; word-wrap: break-word;'>$ \mathrm{i} 2 \frac{\mathrm{e}^{-a|x|}}{\omega} $</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>$ \delta(x - x_0) $</td><td style='text-align: center; word-wrap: break-word;'>$ \mathrm{e}^{-i\omega x_0} $</td></tr></table>

<!-- page: 366 -->

### Ⅲ．拉普拉斯变换简表



<table border="1" style="margin: auto; word-wrap: break-word;"><tr><td style="text-align: center; word-wrap: break-word;">像原函数</td><td style="text-align: center; word-wrap: break-word;">像函数</td></tr><tr><td style="text-align: center; word-wrap: break-word;">$ f(t)=\frac{1}{2\pi i}\int_{p-i\infty}^{p+i\infty}F(p)\mathrm{e}^{pt}\mathrm{d}p $</td><td style="text-align: center; word-wrap: break-word;">$ F(p)=\int_{0}^{+\infty}f(t)\mathrm{e}^{-pt}\mathrm{d}t $</td></tr><tr><td style="text-align: center; word-wrap: break-word;">1或H(t)</td><td style="text-align: center; word-wrap: break-word;">$ \frac{1}{p} $</td></tr><tr><td style="text-align: center; word-wrap: break-word;">$ t^{n},\ n $是正整数</td><td style="text-align: center; word-wrap: break-word;">$ \frac{n!}{p^{n+1}} $</td></tr><tr><td style="text-align: center; word-wrap: break-word;">$ t^{a},\ a&gt;-1 $</td><td style="text-align: center; word-wrap: break-word;">$ \frac{\Gamma(\alpha+1)}{p^{\alpha+1}} $</td></tr><tr><td style="text-align: center; word-wrap: break-word;">$ e^{a t} $</td><td style="text-align: center; word-wrap: break-word;">$ \frac{1}{p-a} $</td></tr><tr><td style="text-align: center; word-wrap: break-word;">sinbt</td><td style="text-align: center; word-wrap: break-word;">$ \frac{b}{p^{2}+b^{2}} $</td></tr><tr><td style="text-align: center; word-wrap: break-word;">cosbt</td><td style="text-align: center; word-wrap: break-word;">$ \frac{p}{p^{2}+b^{2}} $</td></tr><tr><td style="text-align: center; word-wrap: break-word;">shbt</td><td style="text-align: center; word-wrap: break-word;">$ \frac{b}{p^{2}-b^{2}} $</td></tr><tr><td style="text-align: center; word-wrap: break-word;">chbt</td><td style="text-align: center; word-wrap: break-word;">$ \frac{p}{p^{2}-b^{2}} $</td></tr><tr><td style="text-align: center; word-wrap: break-word;">$ t^{a}e^{a t},\ a&gt;-1 $</td><td style="text-align: center; word-wrap: break-word;">$ \frac{\Gamma(\alpha+1)}{(p-c)^{\alpha+1}} $</td></tr><tr><td style="text-align: center; word-wrap: break-word;">$ t^{a}\sin bt,\ a&gt;-1 $</td><td style="text-align: center; word-wrap: break-word;">$ \frac{\Gamma(\alpha+1)[(p+ib)^{\alpha+1}-(p-ib)^{\alpha+1}]}{2i(p^{2}+b^{2})^{\alpha+1}} $</td></tr><tr><td style="text-align: center; word-wrap: break-word;">$ t^{a}\cos bt,\ a&gt;-1 $</td><td style="text-align: center; word-wrap: break-word;">$ \frac{\Gamma(\alpha+1)[(p+ib)^{\alpha+1}+(p-ib)^{\alpha+1}]}{2(p^{2}+b^{2})^{\alpha+1}} $</td></tr><tr><td style="text-align: center; word-wrap: break-word;">$ e^{-a t}\sin bt $</td><td style="text-align: center; word-wrap: break-word;">$ \frac{b}{(p+a)^{2}+b^{2}} $</td></tr><tr><td style="text-align: center; word-wrap: break-word;">$ e^{-a t}\cos bt $</td><td style="text-align: center; word-wrap: break-word;">$ \frac{p+a}{(p+a)^{2}+b^{2}} $</td></tr><tr><td style="text-align: center; word-wrap: break-word;">$ \delta(t) $</td><td style="text-align: center; word-wrap: break-word;">1</td></tr><tr><td style="text-align: center; word-wrap: break-word;">$ \frac{1}{\sqrt{\pi t}}\sin2\sqrt{at} $</td><td style="text-align: center; word-wrap: break-word;">$ \frac{1}{p}\sqrt{p}\mathrm{e}^{-\frac{a}{p}} $</td></tr><tr><td style="text-align: center; word-wrap: break-word;">$ \frac{1}{\sqrt{\pi t}}\cos2\sqrt{at} $</td><td style="text-align: center; word-wrap: break-word;">$ \frac{1}{\sqrt{p}}\mathrm{e}^{-\frac{a}{p}} $</td></tr><tr><td style="text-align: center; word-wrap: break-word;">$ \frac{1}{\sqrt{\pi t}}\mathrm{e}^{-\frac{a^{2}}{4t}} $</td><td style="text-align: center; word-wrap: break-word;">$ \frac{1}{\sqrt{p}}\mathrm{e}^{p/p} $</td></tr><tr><td style="text-align: center; word-wrap: break-word;">$ \frac{1}{\sqrt{\pi t}}\mathrm{e}^{-2a\sqrt{t}} $</td><td style="text-align: center; word-wrap: break-word;">$ \frac{1}{\sqrt{p}}\mathrm{e}^{\frac{a^{2}}{p}}\mathrm{erfc}\left(\frac{\alpha}{\sqrt{p}}\right) $</td></tr><tr><td style="text-align: center; word-wrap: break-word;">erf( $ \sqrt{at} $)</td><td style="text-align: center; word-wrap: break-word;">$ \frac{\sqrt{a}}{p}\sqrt{p+a} $</td></tr><tr><td style="text-align: center; word-wrap: break-word;">erf $ \left(\frac{a}{2\sqrt{t}}\right) $</td><td style="text-align: center; word-wrap: break-word;">$ \frac{1}{p}\mathrm{e}^{-a\sqrt{p}}(a\geq0) $</td></tr><tr><td colspan="2">续表</td></tr><tr><td style="text-align: center; word-wrap: break-word;">像原函数</td><td style="text-align: center; word-wrap: break-word;">像函数</td></tr><tr><td style="text-align: center; word-wrap: break-word;">$ e^{t}erf(\sqrt{t}) $</td><td style="text-align: center; word-wrap: break-word;">$ \frac{1}{p+\sqrt{p}} $</td></tr><tr><td style="text-align: center; word-wrap: break-word;">$ J_{n}(t),\ n&gt;-1 $</td><td style="text-align: center; word-wrap: break-word;">$ \frac{(\sqrt{p^{2}+1}-p)^{2}}{\sqrt{p^{2}+1}} $</td></tr><tr><td style="text-align: center; word-wrap: break-word;">$ t^{2}J_{v}(t),\ \nu&gt;-\frac{1}{2} $</td><td style="text-align: center; word-wrap: break-word;">$ \frac{2^{2}\Gamma\left(\nu+\frac{1}{2}\right)}{\sqrt{\pi}}\frac{1}{(p^{2}+1)^{\nu+\frac{1}{2}}} $</td></tr><tr><td style="text-align: center; word-wrap: break-word;">$ t^{\frac{4}{2}}J_{n}(2\sqrt{t}) $</td><td style="text-align: center; word-wrap: break-word;">$ \frac{1}{p^{n+1}}e^{-\frac{1}{p}} $</td></tr><tr><td style="text-align: center; word-wrap: break-word;">$ \frac{e^{bt}-e^{at}}{t} $</td><td style="text-align: center; word-wrap: break-word;">$ \ln\frac{p-a}{p-b} $</td></tr><tr><td style="text-align: center; word-wrap: break-word;">$ \frac{1}{\sqrt{\pi}t}\sin\frac{1}{2t} $</td><td style="text-align: center; word-wrap: break-word;">$ \frac{1}{\sqrt{p}}e^{-\sqrt{p}}\sin\sqrt{p} $</td></tr><tr><td style="text-align: center; word-wrap: break-word;">$ \frac{1}{\sqrt{\pi}t}\cos\frac{1}{2t} $</td><td style="text-align: center; word-wrap: break-word;">$ \frac{1}{\sqrt{p}}e^{-\sqrt{p}}\cos\sqrt{p} $</td></tr><tr><td style="text-align: center; word-wrap: break-word;">$ \int_{0}^{t}\frac{\sin\xi}{\sqrt{2\pi\xi}}d\xi $</td><td style="text-align: center; word-wrap: break-word;">$ \frac{1}{2\sqrt{2}pi}\frac{\sqrt{p+i}-\sqrt{p-i}}{\sqrt{p^{2}+1}} $</td></tr><tr><td style="text-align: center; word-wrap: break-word;">$ \int_{0}^{t}\frac{\cos\xi}{\sqrt{2\pi\xi}}d\xi $</td><td style="text-align: center; word-wrap: break-word;">$ \frac{1}{2\sqrt{2}p}\frac{\sqrt{p+i}+\sqrt{p-i}}{\sqrt{p^{2}+1}} $</td></tr></table>

<!-- page: 367 -->

