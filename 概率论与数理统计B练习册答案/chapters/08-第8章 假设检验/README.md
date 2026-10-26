# 08-第8章 假设检验

[返回全书目录](../../README.md)

> PDF 页码：101–105

<!-- page: 101 -->

<div style="text-align: center;"><div style="text-align: center;">习题 8 假设检验</div> </div>


1.某种零件的长度服从正态分布，方差 $ \sigma^2=1.21 $，现从零件堆中随机抽取6件，测得长度(单位：mm)为:32.46,31.54,30.10,29.76,31.67,31.23。问当显著性水平为 $ \alpha=0.05 $时，能否认为这批零件的平均长度为32.50mm？

解：设假设检验： $ H_0 $： $ \mu = 32.50 $； $ H_1 $： $ \mu \ne 32.50 $，由于方差已知，故用 $ U $检验法，检验统计量 $ U = \frac{\overline{X} - \mu}{\sigma / \sqrt{n}} \sim N(0,1) $分布，

则拒绝域为： $ |U| > u_{\frac{\alpha}{2}} $，查表得， $ u_{0.025} = 1.96 $，

计算得 $ \overline{X}=31.13,U=\frac{31.13-32.50}{1.1/\sqrt{6}}=-3.05 $,

统计判决:  $ |U| = |-3.05| > 1.96 $，统计量落入拒绝域内，故拒绝原假设，即不认为这批零件的平均长度为32.50mm.

<!-- page: 102 -->

2.有一批枪弹，出厂时测得枪弹射出枪口的初速度V服从 $ N(950,\sigma^{2}) $(单位： $ m/s $).在储存较长时间后取出9发进行测试，得样本值：914,920,910,934,953,945,912,924,940.

假设储存后的枪弹射出枪口的初速度仍服从正态分布，可否认为储存后的枪弹射出枪口的平均初速度已经显著降低(取 $ \alpha=0.05 $)？

解：设假设检验为： $ H_0 $： $ \mu = 950 $， $ H_1 $： $ \mu < 950 $，因为 $ \sigma^2 $未知，故用 $ T $检验法。

检验统计量为 $ T = \frac{\overline{X} - \mu}{s / \sqrt{n}} \sim t(n-1) $,

则有拒绝域为： $ T < -t_{\alpha}(n-1) $，查表有， $ t_{0.05}(8) = 1.86 $，

根据已知数据，计算得 $ \overline{x}=928 $， $ s=15.6 $， $ t=\frac{928-950}{15.6/\sqrt{9}}=-4.23 $，

统计判决：T = -4.23 < -1.86, 统计量落入拒绝域内，故拒绝原假设，即认为平均初速度已经显著降低。

<!-- page: 103 -->

3.某种产品在处理前后的含脂率分别为X和Y，且 $ X \sim N(\mu_1, \sigma^2) $， $ Y \sim N(\mu_2, \sigma^2) $。从产品中任取10件，测得它们处理前后的含脂率（质量分数，%）如下：









<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>前</td><td style='text-align: center; word-wrap: break-word;'>0.19</td><td style='text-align: center; word-wrap: break-word;'>0.18</td><td style='text-align: center; word-wrap: break-word;'>0.21</td><td style='text-align: center; word-wrap: break-word;'>0.30</td><td style='text-align: center; word-wrap: break-word;'>0.66</td><td style='text-align: center; word-wrap: break-word;'>0.42</td><td style='text-align: center; word-wrap: break-word;'>0.08</td><td style='text-align: center; word-wrap: break-word;'>0.12</td><td style='text-align: center; word-wrap: break-word;'>0.30</td><td style='text-align: center; word-wrap: break-word;'>0.27</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>后</td><td style='text-align: center; word-wrap: break-word;'>0.19</td><td style='text-align: center; word-wrap: break-word;'>0.24</td><td style='text-align: center; word-wrap: break-word;'>1.04</td><td style='text-align: center; word-wrap: break-word;'>0.08</td><td style='text-align: center; word-wrap: break-word;'>0.20</td><td style='text-align: center; word-wrap: break-word;'>0.12</td><td style='text-align: center; word-wrap: break-word;'>0.31</td><td style='text-align: center; word-wrap: break-word;'>0.29</td><td style='text-align: center; word-wrap: break-word;'>0.13</td><td style='text-align: center; word-wrap: break-word;'>0.07</td></tr></table>

试在显著性水平 $ \alpha=0.05 $下，检验该产品处理前后的含脂率有无显著变化？

解：这是 $ \sigma_{1}^{2}=\sigma_{2}^{2}=\sigma^{2} $，但未知，两个正态总体的均值差的检验。

设假设检验为： $ H_0 $： $ \mu_1 = \mu_2 $， $ H_1 $： $ \mu_1 \ne \mu_2 $，

检验统计量为： $ T = \frac{\overline{X} - \overline{Y}}{S_w \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}} \sim t(n_1 + n_2 - 2) $分布，

则有拒绝域为 $ \left|T\right|\geq t_{\frac{\alpha}{2}}(n_1+n_2-2) $，查表 $ t_{0.025}(18)=2.1 $，

根据已知数据计算得  $ \overline{x} = 0.273 $， $ \overline{y} = 0.267 $， $ s_1 = 0.167 $， $ s_2 = 0.283 $， $ S_w^2 = \frac{9 \times 0.167^2 + 9 \times 0.283^2}{18} = 0.054 $， $ s_w = 0.232 $， $ T = \frac{\overline{X} - \overline{Y}}{S_w \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}} = \frac{0.273 - 0.267}{0.232 \times \sqrt{\frac{1}{10} + \frac{1}{10}}} = 0.058 $，

统计判决： $ T=0.058<t_{0.025}(18)=2.1 $，统计量没有落入拒绝域内，故接受原假设，即认为该产品处理前后的含脂率无显著变化

<!-- page: 104 -->

4.已知某厂生产的维尼纶纤度 $ X \sim N(\mu,\sigma^2) $，其方差 $ \sigma^2 $按往常资料确定为0.048.某日抽取5根纤维，测得其纤度如下:1.32,1.55,1.36,1.40,1.44,

试问该日厂里生产的维尼纶纤度的方差有无显著变化(取 $ \alpha=0.1 $?

解：设假设检验为： $ H_{0} $： $ \sigma^{2}=0.048 $， $ H_{1} $： $ \sigma^{2}\neq0.048 $，

检验统计量为： $ \chi^{2}=\frac{(n-1)S^{2}}{\sigma^{2}}\sim\chi^{2}(n-1) $分布，

则有拒绝域： $ \chi^{2}<\chi_{1-\frac{\alpha}{2}}^{2}(n-1) $，或 $ \chi^{2}>\chi_{\frac{\alpha}{2}}^{2}(n-1) $，

查表得： $ \chi_{1-\frac{\alpha}{2}}^{2}(n-1)=\chi_{0.95}^{2}(4)=0.711,\chi_{0.05}^{2}(4)=9.488 $

根据已知数据计算得 $ \overline{x}=1.414 $， $ s^{2}=0.031 $， $ \chi^{2}=\frac{4\times0.031}{0.048}=2.583 $，

统计判决： $ 0.711<\chi^{2}=2.583<9.488 $，没有落入拒绝域内，

故接受原假设，即该日厂里生产的维尼纶纤度的方差无显著变化。

<!-- page: 105 -->

5. 对两批同型号的电子元件各抽取6件进行测试，得电阻(单位：Ω)数据如下：









<table border=1 style='margin: auto; word-wrap: break-word;'><tr><td style='text-align: center; word-wrap: break-word;'>1批</td><td style='text-align: center; word-wrap: break-word;'>0.140</td><td style='text-align: center; word-wrap: break-word;'>0.138</td><td style='text-align: center; word-wrap: break-word;'>0.143</td><td style='text-align: center; word-wrap: break-word;'>0.141</td><td style='text-align: center; word-wrap: break-word;'>0.144</td><td style='text-align: center; word-wrap: break-word;'>0.137</td></tr><tr><td style='text-align: center; word-wrap: break-word;'>11批</td><td style='text-align: center; word-wrap: break-word;'>0.135</td><td style='text-align: center; word-wrap: break-word;'>0.140</td><td style='text-align: center; word-wrap: break-word;'>0.142</td><td style='text-align: center; word-wrap: break-word;'>0.136</td><td style='text-align: center; word-wrap: break-word;'>0.138</td><td style='text-align: center; word-wrap: break-word;'>0.141</td></tr></table>

设这两批元件的电阻总体服从 $ N(\mu_1, \sigma_1^2) $和 $ N(\mu_2, \sigma_2^2) $，且相互独立。试问这两批元件的电阻的方差有无显著差异？( $ \alpha = 0.05 $)

解：设假设检验为： $ H_0 $： $ \sigma_1^2 = \sigma_2^2 $， $ H_1 $： $ \sigma_1^2 \neq \sigma_2^2 $，

检验统计量为： $ F = \frac{S_1^2}{S_2^2} \sim F(n_1 - 1, n_2 - 1) $分布，

则有拒绝域： $ F < F_{1-\frac{\alpha}{2}}(n_1 - 1, n_2 - 1) $，或 $ F > F_{\frac{\alpha}{2}}(n_1 - 1, n_2 - 1) $，

查表得： $ F_{\frac{\alpha}{2}}(n_1 - 1, n_2 - 1) = F_{0.025}(5, 5) = 7.15 $， $ F_{1-\frac{\alpha}{2}}(n_1 - 1, n_2 - 1) = F_{0.975}(5, 5) = \frac{1}{F_{0.025}(5, 5)} = 0.1399 $。

根据已知数据，计算得 $ \overline{x} = 0.1405 $， $ \overline{y} = 0.13867 $， $ s_1^2 = 0.0000075 $， $ s_2^2 = 0.000006 $， $ F = \frac{S_1^2}{S_2^2} = 1.25 $，

统计判决： $ 0.1399 < F = 1.25 < 7.15 $，没有落入拒绝域内，故接受原假设，

即认为这两批元件的电阻的方差没有显著差异。
