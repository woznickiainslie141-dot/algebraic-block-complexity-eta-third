# Block complexity of algebraic numbers: an AI-generated proof idea

This repository shares a **research draft for discussion** concerning the block complexity of base-$b$ expansions of real algebraic irrational numbers. The central proof idea came from GPT. I have read the argument only at a high level and have **not independently verified every step**. Please treat the mathematical claims as unverified and scrutinize the proof before relying on or citing it as an established result.

## Claim in the draft

For a fixed integer base $b\ge 2$, a real algebraic irrational number $\xi$, and the number $p_{\xi,b}(L)$ of distinct length-$L$ blocks in its base-$b$ expansion, the manuscript claims

$$
\limsup_{L\to\infty}\frac{p_{\xi,b}(L)}{L(\log L)^\eta}=+\infty
\qquad\text{for every }\eta<\tfrac13.
$$

It also states a refinement with a $(\log\log L)^\gamma$ factor for $\gamma>1$. It does **not** establish the lossless endpoint $\eta=1/3$, a bound at every sufficiently large $L$, normality, or a claim of priority.

## Materials

- [Read the manuscript (PDF)](paper/block_complexity.pdf) or [LaTeX source](paper/block_complexity.tex).
- [Revision and counter-audit notes](paper/counteraudit_revision_20260914.md), [last internal proof check](paper/final_proof_check_20260913.md), [response on place transport](paper/place_transport_response_20260913.md), and [editorial history](paper/editorial_review_20260912.md).
- [Finite check scripts and outputs](checks/). These test selected finite cases and bookkeeping only; they are not a proof of the asymptotic statement.

The manuscript uses an empty author field. This repository does not attribute the proof to a human mathematician or claim that it has passed peer review.

## AI use and review status

GPT generated the overall proof strategy and was used to draft and internally check the mathematical write-up. My review so far consists of a broad read-through; I have not independently worked through the entire proof in detail. I am publishing this simply to share the idea and invite independent mathematical review. No independent peer review, formal verification, or comprehensive literature priority search has been completed. The internal notes and finite checks should be read with that limitation in mind.

## Build and reproduce

Run `pdflatex` twice in `paper/` to build the PDF from `block_complexity.tex`. The bibliography is included in the source, so BibTeX is not needed. The finite scripts use Python's standard library and can be run as `python checks/verify_R6_paper.py` and `python checks/verify_integer_base_extension.py` from the repository root.

---

## 中文说明

这里公开的是**供讨论的研究草稿**。$\eta<1/3$ 证明的整体思路由 GPT 生成，论文写作和内部检查也使用了 GPT。我目前只是大致通读，还没有逐步独立验证整篇证明；分享的目的是让感兴趣的人检查这个思路，而不是宣称结论已经得到独立确认。有限计算只检查特定情形，不能代替无限情形的证明；稿件也尚未经独立数学审稿或完整的文献首创性调查。

