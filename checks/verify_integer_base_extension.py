"""Small exact consistency checks; not an independent proof or distribution experiment."""
from fractions import Fraction as F
from itertools import product, combinations
from math import gcd, isqrt
from pathlib import Path
import json

def factor(b):
    out = {}
    p = 2
    while p*p <= b:
        while b % p == 0:
            out[p] = out.get(p, 0) + 1
            b //= p
        p += 1
    if b > 1:
        out[b] = 1
    return out

def val(a, p):
    assert a
    a = abs(a)
    v = 0
    while a % p == 0:
        a //= p
        v += 1
    return v

def prefix(w, b, n):
    z = 0
    for x in w[:n]:
        z = b*z+x
    return z

def repeat(w):
    n = len(w)
    for v in range(n//2, 0, -1):
        for r in range(n-2*v+1):
            for s in range(v, n-r-v+1):
                if w[r:r+v] == w[r+s:r+s+v]:
                    return r, s, v

report = {"scope": "Exact finite consistency only; no statistical or formal-proof claim."}
words = valid = positive = nonprimitive = 0
for b in (2, 3, 4, 6, 10):
    for n in (3, 4):
        for w in product(range(b), repeat=n):
            words += 1
            z = repeat(w)
            if z is None:
                continue
            valid += 1
            r, s, v = z
            t = r+s
            a = prefix(w, b, t)-prefix(w, b, r)
            q = b**t-b**r
            g = gcd(b**r, a)
            assert 0 <= a <= q < b**t
            assert gcd(gcd(b**t//g, b**r//g), a//g) == 1
            assert b**t//g >= b**s
            A = prefix(w, b, t+v)
            assert F(A, b**(t+v)) <= F(a, q) <= F(A+1, b**(t+v))
            if r:
                positive += 1
                assert w[r-1] != w[t-1] and a % b
                ps = [(p,e) for p,e in factor(b).items() if val(a,p) < e]
                assert ps
                for p,e in ps:
                    assert g*p**(e*r) <= b**r*p**(e-1)
                nonprimitive += g > 1
report.update(words=words, repeat_candidates=valid,
              positive_preperiods=positive, nonprimitive_candidates=nonprimitive)

plane_checks = point_checks = 0
for b in (2, 3, 4, 6, 10, 12):
    pts = []
    t = 2
    for j in range(6):
        t = 2*t+1
        r = j % 3
        q = b**t-b**r
        a = isqrt(2*q*q)-q
        if r and a % b == 0:
            a += 1
        assert (a+q-1)**2 < 2*q*q < (a+q+1)**2
        assert 0 <= a < b**t
        pts.append((t,r,a))
    for i,j in combinations(range(len(pts)),2):
        t,r,a = pts[i]
        T,R,A = pts[j]
        x,y = (b**t,b**r,a),(b**T,b**R,A)
        z = (x[1]*y[2]-x[2]*y[1], x[2]*y[0]-x[0]*y[2],
             x[0]*y[1]-x[1]*y[0])
        g = gcd(gcd(abs(z[0]),abs(z[1])),abs(z[2]))
        assert g
        z = tuple(c//g for c in z)
        Z = max(map(abs,z))
        assert Z <= 2*b**(t+T)
        for tt,rr,aa in pts:
            if z[0]*b**tt+z[1]*b**rr+z[2]*aa:
                continue
            point_checks += 1
            if z[2]:
                assert z[2]*aa % b**rr == 0
                if rr:
                    for p,e in factor(b).items():
                        if val(aa,p) < e:
                            assert e*rr <= val(z[2],p)+e-1
                assert b**(tt-rr) < 16*Z*Z
        plane_checks += 1
report.update(plane_checks=plane_checks, plane_point_checks=point_checks)

# The identities are algebraic in positive weights whose sum is one.
# Rational partitions test those identities exactly, not log(p)/log(b) numerically.
weight_checks = 0
for ws in ((F(1),),(F(1,3),F(2,3)),(F(1,6),F(1,3),F(1,2))):
    for eps in (F(1,2),F(1,8),F(1,31)):
        k = (2*eps.denominator+eps.numerator-1)//eps.numerator
        delta = eps-F(1,k)
        alpha = 1+delta/3
        theta = delta/(3+delta)
        for l in range(k):
            raw = [(F(1),F(l+1,k),-eps)]
            raw += [(-w,-w*F(l,k),F(0)) for w in ws]
            assert sum(map(sum,raw)) == -delta
            assert sum(max(e) for e in raw) == 1
            for split in ((F(1),),(F(1,2),F(1,2))):
                lifted = [tuple(d*x for x in e) for e in raw for d in split]
                cs = [tuple((x-sum(e)/3)/alpha for x in e) for e in lifted]
                assert all(sum(c)==0 for c in cs)
                assert sum(max(c) for c in cs)==1
                assert sum(sum(e)/3 for e in lifted)==-delta/3
                assert alpha*theta==delta/3
                for e,c in zip(lifted,cs):
                    assert all(x-alpha*y == sum(e)/3 for x,y in zip(e,c))
                weight_checks += 1
report["centered_weight_systems"] = weight_checks

# A concrete algebraic normalization counterexample: size is not projective height.
b,t,r,a = 6,4,2,2
g = gcd(b**r,a)
assert g == 2 and b**t//g == 648 != b**t
report["normalization_example"] = {"b":b,"t":t,"r":r,"a":a,"g":g,"H":648,"Psi":1296}
report["passed"] = True
Path(__file__).with_name("integer_base_extension_verification.json").write_text(
    json.dumps(report,indent=2)+"\n",encoding="utf-8")
print(json.dumps(report,indent=2))
