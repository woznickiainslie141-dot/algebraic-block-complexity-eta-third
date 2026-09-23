"""Extended exact checks for the paper on binary block complexity of algebraic irrationals.

Scope: finite consistency checks with exact integers / rationals only.
They support, but never replace, the proofs in the paper.

Sections
  1. exhaustive binary words: maximal-repeat decomposition, parity of a, primitivity,
     range of a  (rule: maximise |V|, then minimise |U|, among A(n) = U V W V X)
  2. actual binary expansion of sqrt(2)-1: every structural claim on real data,
     including |q xi - a| <= 2^{-|V|} verified by exact integer squaring
  3. overlap reduction: the factor 1/3 and the periodicity of the reduced block
  4. end-to-end construction on a Sturmian (Fibonacci) word of low complexity:
     pigeonhole repeat, overlap reduction, extraction with s_{j+1} > 2 t_j, growth bounds
  5. uniform occupancy of rational planes on admissible point sets
  6. subspace-theorem bookkeeping: the six local inequalities, bin by bin
  7. sparse heights in multiplicative intervals [A, A^omega)
  8. the exponent 1/3 in the final counting inequality
"""
from itertools import product
from fractions import Fraction
from math import gcd, isqrt, log, ceil
from pathlib import Path
import json
import random
import time

report = {}
random.seed(20260912)
T0 = time.time()


# ----------------------------------------------------------------------------
# helpers
# ----------------------------------------------------------------------------
def prefix_value(word, j):
    a = 0
    for bit in word[:j]:
        a = 2 * a + bit
    return a


def decompose_max(w, v_start=None):
    """Maximal decomposition w = U V W V X (so |V W| >= |V|).

    Returns (r, s, v), r = |U|, s = |V W|, v = |V|, with v maximal, then r
    minimal, then s minimal; None if w has no repeated block.
    """
    n = len(w)
    if v_start is None:
        v_start = n // 2
    for v in range(min(v_start, n // 2), 0, -1):
        for r in range(0, n - 2 * v + 1):
            for s in range(v, n - r - v + 1):
                if w[r:r + v] == w[r + s:r + s + v]:
                    return (r, s, v)
    return None


def check_point_claims(w, r, s, v):
    """Structural claims for the point attached to one decomposition of the prefix w."""
    t = r + s
    a = prefix_value(w, t) - prefix_value(w, r)
    q = 2 ** t - 2 ** r
    assert 0 <= a <= q < 2 ** t, (r, s, v, a, q)
    assert gcd(gcd(2 ** t, 2 ** r), a) == 1
    if r > 0:
        assert w[r - 1] != w[t - 1]      # shortest preperiod
        assert a % 2 == 1
    return t, a, q


# ----------------------------------------------------------------------------
# 1. exhaustive binary words
# ----------------------------------------------------------------------------
words_checked = 0
parity_checks = 0
for n in range(2, 13):
    for bits in product((0, 1), repeat=n):
        w = list(bits)
        words_checked += 1
        d = decompose_max(w)
        if d is None:
            continue
        r, s, v = d
        check_point_claims(w, r, s, v)
        if r:
            parity_checks += 1
for _ in range(1200):
    n = random.randint(13, 80)
    w = [random.randint(0, 1) for _ in range(n)]
    words_checked += 1
    d = decompose_max(w, v_start=min(n // 2, 40))
    if d is None:
        continue
    r, s, v = d
    check_point_claims(w, r, s, v)
    if r:
        parity_checks += 1
report['words_checked'] = words_checked
report['positive_preperiod_parity_checks'] = parity_checks


# ----------------------------------------------------------------------------
# 2. the actual binary expansion of sqrt(2)-1
# ----------------------------------------------------------------------------
M = 4000
A = isqrt(2 * 4 ** M)                 # A/2^M <= sqrt(2) < (A+1)/2^M
bits = bin(A)[2:]
assert bits[0] == '1' and len(bits) == M + 1
w_sqrt2 = [int(c) for c in bits[1:]]  # digits of sqrt(2)-1

sqrt2_checks = 0
sqrt2_approx_checks = 0
reps = []
for n in [60, 150, 400, 1000, 2500, 4000]:
    pref = w_sqrt2[:n]
    d = decompose_max(pref, v_start=80)
    assert d is not None, n
    r, s, v = d
    t, a, q = check_point_claims(pref, r, s, v)
    reps.append((n, r, s, v))
    sqrt2_checks += 1
    # |q(sqrt(2)-1) - a| <= 2^{-v}  <=>  (2^v(a+q)-1)^2 < 2 q^2 4^v < (2^v(a+q)+1)^2
    L = (2 ** v * (a + q) - 1) ** 2
    R = (2 ** v * (a + q) + 1) ** 2
    assert L < 2 * q * q * 4 ** v < R
    sqrt2_approx_checks += 1
report['sqrt2_prefixes_checked'] = sqrt2_checks
report['sqrt2_approximation_checks'] = sqrt2_approx_checks
report['sqrt2_repeat_lengths'] = reps


# ----------------------------------------------------------------------------
# 3. overlap reduction: v = d*floor((k+d)/(2d)) >= k/3, and the two v-blocks agree
# ----------------------------------------------------------------------------
overlap_checks = 0
for k in range(2, 400):
    for d in range(1, k):
        v = d * ((k + d) // (2 * d))
        assert 3 * v >= k and 2 * v <= k + d and v % d == 0
        base = [random.randint(0, 1) for _ in range(d)]
        win = [base[i % d] for i in range(k + d)]
        assert win[:v] == win[v:2 * v]
        overlap_checks += 1
report['overlap_reduction_checks'] = overlap_checks


# ----------------------------------------------------------------------------
# 4. end-to-end construction on the Fibonacci word (Sturmian: p(k) = k+1)
# ----------------------------------------------------------------------------
def fibonacci_word(length):
    a, b = [0], [0, 1]
    while len(b) < length:
        a, b = b, b + a
    return b[:length]


FW_LEN = 30000
FW = ''.join(str(b) for b in fibonacci_word(FW_LEN))

# 4a. low complexity of the test word: p(k) = k+1 for a Sturmian word
compl = {}
for k in [5, 10, 20, 40, 80]:
    compl[k] = len({FW[i:i + k] for i in range(2000)})
report['fibonacci_complexity'] = compl
assert all(compl[k] == k + 1 for k in compl)

C_CONST = 1.0
U_EXP = 1 / 3


def k_of(ell):
    return max(1, int(ell / (4 * C_CONST * log(ell) ** U_EXP)))


def constructive_decomposition(s, k):
    """Two equal k-blocks (pigeonhole) + overlap reduction -> (r, s, v), v >= k/3."""
    seen = {}
    for i in range(len(s) - k + 1):
        blk = s[i:i + k]
        if blk in seen:
            u, u2 = seen[blk], i
            d = u2 - u
            if d >= k:
                return (u, d, k)
            v = d * ((k + d) // (2 * d))
            return (u, v, v)
        seen[blk] = i
    return None


# grid of prefixes on which the construction is run
grid = []
ell, step = 200, 1.02
while ell < 12000:
    grid.append(int(ell))
    ell *= step
grid = sorted(set(grid))

decs = {}
for ell in grid:
    k = k_of(ell)
    if 2 * k + 2 >= ell:
        continue
    d = constructive_decomposition(FW[:ell], k)
    if d is None:
        continue
    r, s, v = d
    assert 3 * v >= k, (ell, k, v)
    assert r + s + v <= ell
    decs[ell] = (r, s, v, k)
report['sturmian_decompositions'] = len(decs)
_min_ratio = min(v / (ell / (12.0 * log(ell) ** U_EXP)) for (ell, (r, s, v, k)) in decs.items())
assert _min_ratio > 0.85
report['sturmian_min_v_over_a_ell_log'] = round(_min_ratio, 3)

# 4b. extraction with s_{j+1} > 2 t_j, the growth bounds, and log t_j <= A j log(2j)
ell_seq = []
ell_cur, t_prev, s_prev = 200, None, None
while True:
    for e in grid:
        if e <= ell_cur:
            continue
        r, s, v, k = decs[e]
        if t_prev is None or s > 2 * t_prev:
            t = r + s
            if t_prev is not None:
                assert t > 2 * t_prev            # t doubles
                assert s > 2 * t_prev            # defining property of the extraction
                assert s > s_prev                # s strictly increasing
            ell_seq.append((e, r, s, t, v))
            ell_cur, t_prev, s_prev = e, t, s
            break
    else:
        break

assert len(ell_seq) >= 5, len(ell_seq)
ratios = []
for (e1, r1, s1, t1, v1), (e2, r2, s2, t2, v2) in zip(ell_seq, ell_seq[1:]):
    ratios.append(e2 / (e1 * log(e1) ** U_EXP))
As = [log(t) / (j * log(2 * j)) for j, (e, r, s, t, v) in enumerate(ell_seq, start=1)]
assert max(ratios) < 50                                     # (7) with a fixed C1
report['sturmian_extraction'] = [(e, r, s, t, v) for (e, r, s, t, v) in ell_seq]
report['sturmian_extraction_points'] = len(ell_seq)
report['sturmian_max_ell_ratio_over_ell_logu'] = round(max(ratios), 3)
report['sturmian_max_log_t_over_jlog2j'] = round(max(As), 4)

# 4c. structural hypotheses of the plane-occupancy lemma on this real sequence
sturmian_pts = []
for (e, r, s, t, v) in ell_seq:
    dec = FW[:e]
    a = int(dec[:t], 2) - int(dec[:r], 2) if r else int(dec[:t], 2)
    q = 2 ** t - 2 ** r
    assert 0 <= a <= q
    assert gcd(gcd(2 ** t, 2 ** r), a) == 1
    if r > 0:
        assert dec[r - 1] != dec[t - 1]
        assert a % 2 == 1
    sturmian_pts.append((2 ** t, 2 ** r, a))
s_vals = [s for (e, r, s, t, v) in ell_seq]
assert len(set(s_vals)) == len(s_vals)
assert all(t2 > 2 * t1 for (_, _, _, t1, _), (_, _, _, t2, _) in zip(ell_seq, ell_seq[1:]))


# ----------------------------------------------------------------------------
# 5. uniform occupancy of rational planes
# ----------------------------------------------------------------------------
def cross(x, y):
    z = (x[1] * y[2] - x[2] * y[1], x[2] * y[0] - x[0] * y[2],
         x[0] * y[1] - x[1] * y[0])
    g = gcd(gcd(abs(z[0]), abs(z[1])), abs(z[2]))
    assert g
    return tuple(u // g for u in z)


def v2(m):
    assert m > 0
    k = 0
    while m % 2 == 0:
        m //= 2
        k += 1
    return k


def plane_occupancy(points):
    """points: (2^t, 2^r, a) with t increasing and t_{j+1} > 2 t_j, a odd when r > 0,
    s = t - r pairwise distinct.  Verifies the Liouville mechanism and the bound <= 4."""
    occupied_max = 0
    pairs = 0
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            pairs += 1
            z = cross(points[i], points[j])
            Z = max(abs(c) for c in z)
            ti, tj = v2(points[i][0]), v2(points[j][0])
            assert Z <= 2 ** (ti + tj + 1)
            occ = [x for x in points if sum(c * y for c, y in zip(z, x)) == 0]
            if z[2]:
                for x in occ:
                    t, r = v2(x[0]), v2(x[1])
                    assert r <= v2(abs(z[2]))          # 2^r | z_3 a with a odd
                    assert 2 ** (t - r) < 16 * Z * Z    # Liouville, xi = sqrt(2)-1
                    assert 2 ** t < 16 * Z ** 3
                assert len(occ) <= 4
            else:
                ss = [v2(x[0]) - v2(x[1]) for x in occ]
                assert len(set(ss)) == len(ss)
                assert len(occ) <= 1
            occupied_max = max(occupied_max, len(occ))
    return occupied_max, pairs


# 5a. admissible points with r = 0 killed / r > 0 odd, heights doubling
M5 = 6000
A5 = isqrt(2 * 4 ** M5)                 # sqrt(2) ~ A5/2^M5
adm = []
t = 2
for j in range(14):
    t = 2 * t + 1
    r = int(t * (0.3 + 0.6 * ((j * 7919) % 100) / 100.0)) % t
    q = 2 ** t - 2 ** r
    m = isqrt(2 * q * q) - q              # floor(q(sqrt(2)-1))
    a = m if m % 2 == 1 else m + 1        # nearest odd integer to q(sqrt(2)-1)
    # |q(sqrt(2)-1) - a| <= 1, exactly:  (a+q-1)^2 <= 2q^2 <= (a+q+1)^2
    assert (a + q - 1) ** 2 <= 2 * q * q <= (a + q + 1) ** 2
    adm.append((2 ** t, 2 ** r, a))
assert len({v2(x[0]) - v2(x[1]) for x in adm}) == len(adm)   # distinct s = t - r
occ_adm, pairs_adm = plane_occupancy(adm)
report['admissible_points'] = len(adm)
report['admissible_plane_pairs'] = pairs_adm
report['admissible_max_points_in_a_plane'] = occ_adm

# 5b. the real points produced by the Sturmian construction
occ_st, pairs_st = plane_occupancy(sturmian_pts)
report['sturmian_points'] = len(sturmian_pts)
report['sturmian_plane_pairs'] = pairs_st
report['sturmian_max_points_in_a_plane'] = occ_st


# ----------------------------------------------------------------------------
# 6. subspace-theorem bookkeeping on the real points of the Sturmian construction
# ----------------------------------------------------------------------------
eps = Fraction(1, 100)
k_bins = ceil(2 / eps)
delta = eps - Fraction(1, k_bins)
assert 0 < delta <= 1
weight_checks = 0
point_checks = 0
for (e, r, s, t, v) in ell_seq:
    dec = FW[:e]
    a = int(dec[:t], 2) - int(dec[:r], 2) if r else int(dec[:t], 2)
    q = 2 ** t - 2 ** r
    rho = Fraction(r, t)
    l = min(int(rho * k_bins), k_bins - 1)
    assert Fraction(l, k_bins) <= rho < Fraction(l + 1, k_bins)
    w = [0, Fraction(l + 1, k_bins) - 1, -1 - eps, -1, -Fraction(l, k_bins), 0]
    assert all(x <= 0 for x in w)                      # (3.5): exponents <= 0
    assert sum(w) == -3 - delta                        # (3.4): sum = -n - delta
    weight_checks += 1
    # normalized, pointwise:  max_sigma |L(sigma x)|_v / |sigma x|_v <= A_v H(x)^{d}
    assert Fraction(l, k_bins) <= Fraction(r, t) < Fraction(l + 1, k_bins)
    assert Fraction(r, t) <= Fraction(l + 1, k_bins)       # 2^{r-t} <= 2^{t((l+1)/k-1)}
    assert k_bins * r >= t * l                             # 2^{-r} <= 2^{-t l / k} at 2
    # |e| = |q xi - a| <= 2^{-eps t}, xi = value of the Fibonacci word
    xi_e = Fraction(int(dec, 2), 2 ** e)
    err = abs(q * xi_e - a) + Fraction(q, 2 ** e)
    assert err ** int(1 / eps) <= Fraction(1, 2 ** t)
    assert 2 ** r < 2 ** t and 0 <= a < 2 ** t         # H(x) = max = 2^t
    point_checks += 1
report['weight_bins_checked'] = weight_checks
report['pointwise_local_inequalities'] = point_checks


# ----------------------------------------------------------------------------
# 7. sparse heights in multiplicative intervals [A, A^omega)
# ----------------------------------------------------------------------------
height_checks = 0
for omega in [2, 3, 5, 10, 100, 1000, 10 ** 6]:
    ell = 0
    while 2 ** ell < omega:
        ell += 1
    ts, t = [], 3
    while t < 10 ** 7:
        ts.append(t)
        t = 2 * t + 1
    for log2A in [1, 2, 5, 17, 22]:
        cnt = sum(log2A <= u < omega * log2A for u in ts)
        assert cnt <= 1 + ell
        height_checks += 1
report['sparse_height_interval_checks'] = height_checks


# ----------------------------------------------------------------------------
# 8. the exponent 1/3 in the final counting step
# ----------------------------------------------------------------------------
def threshold_logN(u, x_max=20000.0):
    """x = log N such that N/2 <= N^{3u}(log N)^{3u+2} fails for all larger x.

    The inequality is log(N/2) <= 3u log N + (3u+2) log log N, i.e., asymptotically
    (1-3u) log N - o(log N) >= 0.  So for u < 1/3 it holds only below a finite threshold
    (giving the contradiction), while for u > 1/3 it holds for all large N.
    Returns (largest x with the inequality true, True if it is true for all large x).
    """
    best, fails_late = None, False
    x = 1.0
    while x < x_max:
        if x - log(2) <= 3 * u * x + (3 * u + 2) * log(x):
            if best is None or fails_late:
                best, fails_late = x, False
            else:
                best = x
        else:
            if best is not None:
                fails_late = True
        x += 0.01
    return best, not fails_late


report['final_threshold_logN_u_lt_third'] = {str(u): threshold_logN(u)[0]
                                             for u in [0.2, 0.30, 0.32]}
report['final_threshold_u_0.34_holds_for_large_N'] = threshold_logN(0.34)[1]

report['seconds'] = round(time.time() - T0, 1)
report['passed'] = True
out = Path(__file__).with_name('R6_paper_verification.json')
out.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
print(json.dumps(report, indent=2))
