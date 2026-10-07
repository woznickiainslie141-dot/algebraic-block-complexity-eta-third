# Collision–energy 审计与二进尺度分层补充证明

日期：2026-09-29。

对象：[half_exponent.tex](half_exponent.tex) 与 [第二轮展望](review_outlook_20260929_zh.md)。

## 0. 本轮结论与证明边界

**第 4 项的组合步骤可以闭合，而且不需要逐点 δ_h 版 Theorem 5.1。** 只用现稿已有的固定 δ、变动权重 Theorem 5.1 / Corollary 5.6，按逼近质量分层计数，即可推出

\[
\exists c=c(\xi,b)>0\quad\forall X\text{ 充分大}\quad
\exists L\in[X,X^{3/2}]:\quad
r(L)>cL\sqrt{\frac{\log L}{\log\log L}}.
\tag{0.1}
\]

于是同一窗口内存在 L 满足

\[
p(L)>\frac c2L\sqrt{\frac{\log L}{\log\log L}}.
\tag{0.2}
\]

这里 r 是 Bugeaud–Kim 的最短重复前缀长度。以下用 R 表示它，避免与逼近中的前周期长度 r 混淆。

**依赖范围：** 本文给出从现稿第 5 节算术输入到 (0.1)–(0.2) 的完整补充论证。第 5 节本身是未发表稿中的新算术引理，不能冒充 EF2013 的现成定理；本轮核对了所用计数接口、Hoeffding 步骤和 Roth 非消失条件，没有将本文称为对原稿全部外部依赖的独立同行审稿。

能兑现的改进来自：保留多个前缀尺度落入同一逼近尺度时的质量收益。尚未得到针对所有重复词对的算术 energy 上界。

## 1. Collision 改写：什么信息进入了旧证明

在长度 H 的数字前缀中，固定词长 k，令

\[
M=H-k+1,\qquad f_w=\#\{\text{该前缀中词 }w\text{ 的起点}\},
\qquad E(k,H)=\sum_w f_w^2.
\]

由 Cauchy–Schwarz，

\[
E(k,H)\ge\frac{M^2}{p(k)},\qquad
\#\{\text{有序、不同起点的相等词对}\}
=E(k,H)-M\ge\frac{M^2}{p(k)}-M.
\tag{1.1}
\]

现稿 Lemma 2.1 取 k 约为 H/(CF(H))，使 p(k)≤H/4。对充分大的 H，k≤H/2，(1.1) 至少给出 H/2 个有序碰撞。

但后续只选其中一个碰撞。若发生重叠，用周期性改造成两个不重叠的相等块，长度 v≥k/3。得到

\[
0\le r<t\le H,\quad t-r\ge v,\quad
0\le a\le b^t-b^r,\quad
|(b^t-b^r)\xi-a|\le b^{-v}.
\tag{1.2}
\]

因此，旧证明的实际结构是

\[
\text{低复杂度}\Rightarrow\text{有碰撞}
\Rightarrow\text{每个前缀尺度一个逼近}
\Rightarrow\text{分离逼近的质量计数}.
\tag{1.3}
\]

(1.1) 中全部碰撞对的重数没有被带入算术步骤。不同碰撞可能给出同一尺度、相同或高度相关的逼近；重叠消除也不是单射。现有定理控制的是分离的参数，不是 E(k,H)。

**故仅把最后的计数改称 energy bound，并没有获得所有碰撞对的算术控制。** 下面的改进利用的是“前缀尺度的重数”，须与“同一前缀中的词对重数”区分。

## 2. 固定 δ 算术输入的准确形式

固定 ξ,b，以及现稿第 3–4 节的形式、域和位支撑。将 Corollary 5.6 的隐含常数明确记为 K_c，将阈值常数记为 K_t。

对 0<δ≤1，有阈值 C_*(δ)，满足

\[
\log\log C_*(\delta)\le K_t\delta^{-2}\log(2/\delta).
\tag{2.1}
\]

如果一列 admissible 点具有共同 δ，满足

\[
Q_{j+1}>Q_j^2,\qquad Q_j\ge C_*(\delta),\qquad
H_{\mathcal L,c^{(j)},Q_j}(x_j)\le Q_j^{-\delta},
\]

则其长度至多

\[
K_c\delta^{-2}\log(2/\delta).
\tag{2.2}
\]

常数与各点的 ρ=r/t 无关。

对满足 (1.2) 的逼近，只要选共同的

\[
0<\varepsilon\le\min(v/t,1/2),\qquad
\delta=\frac\varepsilon{3+\varepsilon},\quad
Q=b^{(1+\varepsilon/3)t},
\tag{2.3}
\]

原稿第 3–4 节便提供上述 admissibility 与小高度条件。这是在每一质量层中重新使用一个共同 ε；没有逐点 δ 的扩展。

## 3. 核心覆盖引理：同尺度重数带来指数级质量收益

### 引理

存在 K_0,K_1>0，只依赖 ξ,b，具有如下性质。令 B≥2，I 是有限整数集合。对每个 i∈I，有一个满足 (1.2) 的逼近，且

\[
H_i=2^i,\qquad t_i\ge T,\qquad
v_i\ge 2^i/B,\qquad v_i\le t_i\le2^i.
\tag{3.1}
\]

如果

\[
\log T\ge K_0B^2\log(2B),
\tag{3.2}
\]

则

\[
\boxed{|I|\le K_1B^2\log(2B).}
\tag{3.3}
\]

### 证明

置

\[
\tau_i=\lfloor\log_2t_i\rfloor,\qquad
\mu_\tau=\#\{i\in I:\tau_i=\tau\}.
\]

对每个非空的 τ 类，保留其中最大的 i，记作 i_τ，并保留其逼近。

由于 τ_i≤i，μ_τ 个不同整数 i 都不小于 τ，所以

\[
i_\tau\ge\tau+\mu_\tau-1.
\]

再由 t_{i_τ}<2^{τ+1}，得到

\[
\frac{v_{i_\tau}}{t_{i_\tau}}
>\frac{2^{i_\tau-\tau-1}}B
\ge\frac{2^{\mu_\tau-2}}B.
\tag{3.4}
\]

这就是保留重数的收益。原稿的贪心稀疏抽取没有使用 (3.4)。

对每个整数 j≥1，令

\[
\mathcal T_j=\{\tau:\mu_\tau\ge j\},\qquad N_j=|\mathcal T_j|,
\quad \varepsilon_j=\frac{2^{j-3}}B,\quad
\delta_j=\frac{\varepsilon_j}{3+\varepsilon_j}.
\tag{3.5}
\]

仅考虑 N_j>0 的层。因 v/t≤1，(3.4) 蕴含 2^{j-2}/B<1，所以 ε_j<1/2。层内所有保留的逼近都满足 v/t>2ε_j，故可使用 (2.3)。这样处理避免了直接截断质量后丢失重数收益的问题。

将 τ 按奇偶分成两类。每一类中，相邻 τ 至少相差 2，因而

\[
t_{\mathrm{next}}\ge2^{\tau+2}>2t_{\mathrm{previous}}.
\]

该层 ε_j 共同，故相应 Q 满足 Q_next>Q_previous²。

**统一阈值。** 由于 δ_j≥δ_1=1/(12B+1)，且 δ^{-2}log(2/δ) 在 (0,1] 上递减，(2.1) 对所有非空质量层都被常数倍的 B²log(2B) 控制。同时

\[
\log\log Q\ge\log T+\log\log b.
\]

增大 K_0 后，(3.2) 保证所有层、所有保留点都超过各自阈值。不需要 C_*(δ) 本身单调，只用其统一上界。

于是对两种奇偶分别调用 (2.2)，得到

\[
N_j\le 2K_c\delta_j^{-2}\log(2/\delta_j)
\le K_2 B^2\,4^{-j}\log(2B).
\tag{3.6}
\]

这里使用 ε_j≤1/2，故 δ_j≥2ε_j/7；常数 K_2 与 B,j 无关。

最后按重数求和：

\[
|I|=\sum_\tau\mu_\tau
=\sum_{j\ge1}N_j
\le K_2B^2\log(2B)\sum_{j\ge1}4^{-j}
=\frac{K_2}{3}B^2\log(2B).
\]

引理得证。

**这一证明不需要选取共同等待时间，也没有 q 与未知平均 δ 相互依赖的问题。** Ω 分离的代价已包含在逐层调用的 Corollary 5.6 中。

## 4. 从重复函数推出窗口版 √(log/loglog) 下界

令

\[
F(x)=\sqrt{\frac{\log x}{\log\log x}},\qquad Y=X^{3/2}.
\]

假设窗口内所有整数 k 都满足

\[
R(k)\le CkF(k)\qquad(X\le k\le Y),
\tag{4.1}
\]

其中 C>0 是稍后选取的固定小常数。记 F_Y=F(Y)，B=24CF_Y。对充分大的 X，B≥2，且 F 在所用区间递增。

取全部满足

\[
8CF_YX\le2^i\le Y
\tag{4.2}
\]

的整数 i，令 ℓ_i=2^i，并置

\[
k_i=\left\lfloor\frac{\ell_i}{4CF_Y}\right\rfloor.
\]

由下端的缓冲因子，k_i≥2X−1≥X；由 CF_Y→∞，亦有 k_i≤Y。故 (4.1) 给出

\[
R(k_i)\le Ck_iF(k_i)\le CF_Yk_i\le\ell_i/4.
\]

因此前缀中有两次长 k_i 的相等词。使用现稿 Lemma 2.1 中的重叠消除部分，得到 (1.2)，其中

\[
v_i\ge k_i/3\ge\frac{\ell_i}{24CF_Y}=\frac{2^i}B,
\qquad t_i\ge v_i\ge X/3.
\tag{4.3}
\]

没有调用窗口左端之外的复杂度假设。尺度数为

\[
|I|=\frac{\log(Y/X)}{\log2}-O(\log F_Y+|\log C|+1)
=\left(\frac1{2\log2}+o(1)\right)\log X.
\tag{4.4}
\]

另一方面，C 固定时

\[
B^2\log(2B)
=(288C^2+o(1))\log Y
=(432C^2+o(1))\log X.
\tag{4.5}
\]

选 C 足够小，使

\[
432K_0C^2<1/2,\qquad
432K_1C^2<1/(4\log2).
\]

于是充分大的 X 满足 (3.2)，取 T=X/3。引理给出的 (3.3) 与 (4.4)–(4.5) 矛盾。

因此每个充分大的窗口 [X,X^{3/2}] 都有整数 L 使

\[
R(L)>CLF(L).
\tag{4.6}
\]

由于 R(L)≤L+p(L)，且 F(L)→∞，同一个 L 满足

\[
p(L)\ge R(L)-L>(C/2)LF(L)
\]

（X 充分大）。这证明 (0.1)–(0.2)。

### 逻辑方向

R(L)≤L+p(L) 只能把 R 的下界传给 p；不能从 p 的下界推出 R 的下界。本节直接以 (4.1) 为反证假设，因而证明了更强的 R 版本。

### 直接后果

对 R 与 p 都有

\[
\limsup_{L\to\infty}
\frac{p(L)\sqrt{\log\log L}}{L\sqrt{\log L}}>0,
\]

并且

\[
\limsup_{L\to\infty}
\frac{p(L)(\log\log L)^\gamma}{L\sqrt{\log L}}=\infty
\qquad(\gamma>1/2).
\tag{4.7}
\]

所以，在相同的第 5 节算术输入下，先前 γ=1 的正 limsup 还可加强为无穷。

同样的证明可将 3/2 替换为任意固定 β>1；常数 C 允许依赖 β。窗口左端缓冲仍为 O(log F_Y)，不会改变主项。

## 5. 接近 X 的窗口：明确写出 o(1)

更一般地，设

\[
F(x)=(\log x)^u(\log\log x)^{-\gamma},\qquad F(x)\to\infty,
\quad F(X)^2\log(2F(X))=o(\log X).
\tag{5.1}
\]

例如 0<u<1/2、γ=0，或 u=1/2、γ>1/2。

固定任意 C>0，取足够大的常数 A=A(ξ,b,C,u,γ)，置

\[
Y=X\exp\{A F(X)^2\log(2F(X))\}.
\tag{5.2}
\]

于是 Y=X^{1+o(1)}，且 F(Y)/F(X)→1。若整个 [X,Y] 都满足 R(k)≤CkF(k)，重复第 4 节构造：

\[
|I|=\left(\frac A{\log2}+o(1)\right)F(X)^2\log(2F(X)),
\]

而 B²log(2B)=(576C²+o(1))F(X)²log(2F(X))。阈值条件因 (5.1) 自动满足。取 A 大于计数上界中的相应常数，得到矛盾。

因此每个充分大的上述窗口内都有 R(L)>CLF(L)。对 p 的任意指定常数，先将 R 的指定常数增大一倍再减去 L 即可。

在 u=1/2、γ=1/2 端点，F(X)²log F(X) 与 log X 同阶，本证明只给固定幂次窗口及固定正下界常数；不能据此宣称该端点也有 X^{1+o(1)} 窗口。

## 6. 临界项逐项定位

### 6.1 二分之一指数来自辅助多项式的概率计数

现稿 §5 的随机变量是随机选取单项式后的块贡献，不是数字序列中的随机变量；这里没有使用数字独立性假设。

Hoeffding 给出坏单项式比例

\[
\exp(-m\alpha^2/2).
\]

为了在 s+1 个位上同时保留足够多的自由系数，需要

\[
m>2\alpha^{-2}\log(2s+2).
\tag{6.1}
\]

产品公式中的指数则要求

\[
-\delta/9+15(s+1)\alpha<0,
\quad\text{故当前取法为 }\alpha\asymp\delta.
\tag{6.2}
\]

合并得到 m≈δ^{-2}。形式上可以将 mδ² 称为统一质量的平方预算；这是当前 1/2 指数的具体来源。仅重新命名原始词对计数，不会改变 (6.1)。

### 6.2 两个剩余对数是两个独立约束

令 y=log L、δ≈1/(CF(L))。

| 环节 | 原稿中的量 | 在窗口计数中的要求 |
|---|---|---|
| Roth 非消失的高度阈值 | E_m=2(3m²/α)^m；log log C_*≪m log(m/α) | C²F²log F 必须足够小于 y，才能使用计数定理 |
| Ω 分离转成普通倍增分离 | Ω=4m²/α≈δ^{-5}；q≈log(1/δ) | 可用点数上界为 O(C²F²log F)，需要尺度质量超过它 |

二者在当前参数下都落在 F²log F 这一量级。它们是要同时满足的两个条件，**不能再将它们相乘，额外计入一次 log**。

旧证明还有一处组合损失：贪心序列只提供约 y/log F 个尺度。它与 (2.2) 的 log 相乘，产生 F²(log F)²≲y，对应 γ=1。

第 3 节利用同尺度质量增长，恢复了约 y 个前缀尺度的总量，使计数条件变成 F²log F≲y，对应 γ=1/2。统一高度阈值也恰好适配这个量级。

### 6.3 固定质量计数不等于所有质量的强二次 energy 界

对任意给定质量 u，(2.2) 控制的是

\[
\#\{\text{分离逼近：质量}\ge u\}
\ll u^{-2}\log(2/u),
\tag{6.3}
\]

前提是这些点都超过 u 对应的高度阈值。这是一个质量分布的尾计数界。

即使已有更好的尾界 N(u)≤Ku^{-2}，也不能直接推得 Σ_hδ_h²≤K'。抽象反例是：第 j 层有 4^j 个数，质量都为 2^{-j}。各阈值的尾计数满足 N(u)≲u^{-2}，但每层对 Σδ² 的贡献为 1，总能量随层数增长。此例只否定计数之间的逻辑推断，不声称它能由实际代数逼近实现。

若尝试逐点 δ_h 的 Hoeffding 步骤，负均值主项是 Σ_hδ_h，波动规模由点数 m 控制，自然出现的量是

\[
\frac{(\sum_h\delta_h)^2}{m},
\]

而非自动出现 Σ_hδ_h²。完整扩展还需核对共同外积类型的抽取、δ_min 对高度阈值的影响及分离参数。第 3 节绕过这些新增接口，所以本轮无需把展望稿中的“例行改写”升级成独立定理。

## 7. 对用户列出五项的结论

| 项目 | 本轮核验结果 |
|---|---|
| 1. γ=1 正 limsup | 与小常数反证一致；由本轮补充证明还可升级为 γ=1 的 limsup=∞ |
| 2. 重复函数版本 | 成立；须从 R 的低上界重新运行重复词构造，不能倒用 R≤L+p |
| 3. 近幂窗口 | 第 5 节给出明确窗口；对 u<1/2 及 u=1/2、γ>1/2 均适用 |
| 4. √(log/loglog) | 从现稿固定 δ 算术输入可推出；第 3–4 节补全组合证明，不需逐点 δ_h 扩展 |
| 5. 剩余 √loglog 损失 | 当前证明中确有高度阈值与 Ω 分离两个障碍；不能据此证明所有其他技术都无法改进 |

对于 η>1/2，“改进三维或特殊族上的算术计数”是一个充分的研究方向；把它与“必须解决某个通用公开难题”说成严格等价，超出了本次审计能证明的范围。同样，当前每尺度取点方法的局限不是对所有能量方法的排除定理。

## 8. 后续停止准则

本轮有一个可以兑现的组合改进，应先将它独立核验并整理进论文。下一步若只把 (2.2) 改名为 energy estimate，而没有改变其 δ^{-2}、阈值或分离代价，就不应继续声称突破了算术瓶颈。

真正新增的 collision-energy 工作必须补出至少一个现有证明没有的接口，例如：保留同一高度区间内大量碰撞对，并证明在剔除明确的退化簇后，其算术总贡献受控。第 5 节现有输入尚不提供这一接口；这比笼统要求“更强 energy bound”具体，但本轮没有证明它。

## 来源与核对位置

- [现稿 Lemma 2.1](half_exponent.tex#L114)：重复词及重叠消除。
- [现稿 Theorem 5.1](half_exponent.tex#L380)、[Corollary 5.6](half_exponent.tex#L666)：本补充证明的算术输入。
- [原稿 Hoeffding 条件](half_exponent.tex#L503)、[参数选择](half_exponent.tex#L568)、[非消失高度条件](half_exponent.tex#L604)、[旧最终预算](half_exponent.tex#L691)。
- [Evertse–Ferretti 2013 正式版](https://annals.math.princeton.edu/wp-content/uploads/annals-v177-n2-p04-p.pdf)：Proposition 12.1 的次数比与高度条件；Lemma 13.3 允许不同块系数的概率计数。现稿的新变动权重定理与这些已发表输入应分开标注。
- [Bugeaud–Kim](https://irma.math.unistra.fr/~bugeaud/travaux/complsturm3ndRev1.pdf)：重复函数定义及 Lemma 2.2 的 R(n)≤n+p(n)。

本轮没有以有限数字实验支持任何无限命题；分层和窗口结论均由上述不等式推导。未作完整的文献优先权调查，也未宣称已经完成独立同行审稿或形式化证明。
