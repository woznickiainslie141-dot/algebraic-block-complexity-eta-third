# Window bounds for algebraic block complexity

**Latest public update: 7 October 2026; selected manuscript: 30 September 2026.** 本仓库以最新窗口加强版替换原 η<1/3 首页，分享 GPT 生成的证明思路与研究稿，供讨论和独立审查。

Let ξ be a real algebraic irrational number and b >= 2 a fixed integer base. Write p_{ξ,b}(L) for the number of distinct length-L blocks in its fractional expansion, and R(L) for the shortest prefix containing two occurrences of some length-L word.

## Current manuscript

For every fixed θ>1, the draft asserts that c=c(ξ,b,θ)>0 exists such that **every sufficiently large interval [X,X^θ] contains an integer L** satisfying

$$
R(L)>cL\sqrt{\frac{\log L}{\log\log L}},
\qquad
p_{\xi,b}(L)>\frac c2L\sqrt{\frac{\log L}{\log\log L}}.
$$

For each g in {R,p}, it asserts

$$
\limsup_{L\to\infty}\frac{g(L)\sqrt{\log\log L}}{L\sqrt{\log L}}>0,
$$

and the consequences

$$
\limsup_{L\to\infty}\frac{g(L)(\log\log L)^\gamma}{L\sqrt{\log L}}=\infty
\quad(\gamma>1/2),\qquad
\limsup_{L\to\infty}\frac{g(L)}{L(\log L)^\eta}=\infty
\quad(\eta<1/2).
$$

Near windows [X,X exp{A F(X)^2 log(2F(X))}]=[X,X^{1+o(1)}] are also given for F(x)=(log x)^u/(log log x)^γ, with 0<u<1/2, γ>=0, or u=1/2, γ>1/2.

The scope includes arbitrary algebraic degree and composite integer bases. Constants depend on the fixed data. The draft does not assert this size at every sufficiently large L, a lossless η=1/2 endpoint, normality, or an effective numerical starting length. The γ=1/2 statement is a **positive limsup**, not an infinite limsup.

## Materials

- **Current main manuscript:** [17-page window PDF](paper/window/window_half_exponent.pdf), [standalone LaTeX](paper/window/window_half_exponent.tex).
- [Version and verification notes](paper/window/window_version_notes_20260930_zh.md), [dyadic-layer audit](paper/window/collision_energy_audit_20260929_zh.md), [general-degree/base audit](paper/window/generalization_proof_zh.md).
- Earlier [half-exponent PDF](paper/window/half_exponent.pdf) and [source](paper/window/half_exponent.tex), whose weighted limsup required γ>1, are retained.
- [Finite algebra checks](paper/window/checks/verify_general_weights.py) verify selected identities, not the infinite theorem. [Publication checks](PUBLICATION_CHECKS.json) record integrity and document checks.
- The original [η<1/3 PDF](paper/block_complexity.pdf), [source](paper/block_complexity.tex), audits and original checks directory remain historical.

The draft's arithmetic core is its **fixed-support moving-weight sparse-parameter theorem**, proved internally by adapting Evertse–Ferretti's auxiliary-polynomial argument. It is not a published fixed-weight theorem that can simply be quoted for varying weights. The window argument retains all dyadic prefix scales: repeated approximation scales strengthen quality, and fixed-quality bounds are summed.

## AI use and review status

GPT generated the strategies and mathematical write-up and assisted with internal audits. Cheng Huang distributes and maintains the materials; the manuscripts have empty personal author fields. These are **AI-generated research drafts for discussion**, without independent peer review or completed formal verification. A separate partial Lean effort has not proved the final theorem and is not represented here as verification. Finite checks and internal audit labels do not change that status. No comprehensive priority search or confirmed global optimality is claimed.

## Build and checks

Run pdflatex twice on window_half_exponent.tex in paper/window. It is standalone, with bibliography in the source. For finite algebra checks:

~~~text
python -m pip install -r paper/window/checks/requirements.txt
python paper/window/checks/verify_general_weights.py
python paper/window/checks/verify_weights.py
~~~

Earlier η<1/3 checks remain runnable as python checks/verify_R6_paper.py and python checks/verify_integer_base_extension.py.

## Public version record

- **v2026.10.07-window-draft:** the 30 September window manuscript becomes the main public version. The historical eta-third repository name is retained for link continuity.
- [v0.1-preliminary](https://github.com/woznickiainslie141-dot/algebraic-block-complexity-eta-third/releases/tag/v0.1-preliminary): original η<1/3 version made public on 23 September 2026.
- [Zenodo DOI 10.5281/zenodo.22961670](https://doi.org/10.5281/zenodo.22961670) archives **earlier v0.1 files only**, not this window version. Cheng Huang is listed as Distributor; manuscripts have no personal author attribution.

Version dates document public sharing, not priority over independent work. This update changes GitHub only; the existing DOI record is not overwritten.
