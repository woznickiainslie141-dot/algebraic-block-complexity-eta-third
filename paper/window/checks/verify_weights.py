"""Finite exact algebra checks; the manuscript supplies the general proofs."""
from pathlib import Path
from itertools import combinations
import json
import sympy as S

ROOT = Path(__file__).resolve().parent
e, r = S.symbols('epsilon rho', real=True)
xi, xip = S.sqrt(2)-1, -S.sqrt(2)-1
X1, X2, X3 = [S.Matrix([int(i == j) for i in range(3)]) for j in range(3)]
Lp, Lm = -xi*X1+xi*X2+X3, -xip*X1+xip*X2+X3
systems = [[X1, X2, Lp], [X1, X2, Lm], [X1, X2, X3]]
weights = [[S.Rational(1,2), r/2, -e/2]]*2 + [[-1, -r, S.Integer(0)]]
# The order of weights is constant on 0 <= rho <= 1-epsilon.
orders = [[2,1,0], [2,1,0], [0,1,2]]

def plane_weight(normal):
    total = 0
    for forms, w, order in zip(systems, weights, orders):
        for i,j in combinations(order, 2):
            if S.simplify(S.Matrix.hstack(forms[i],forms[j],normal).det()) != 0:
                total += w[i] + w[j]
                break
        else:
            raise AssertionError('No independent pair')
    return S.simplify(total)

def line_weight(vector):
    total = 0
    for forms, w, order in zip(systems, weights, orders):
        for i in order:
            if S.simplify(forms[i].dot(vector)) != 0:
                total += w[i]
                break
        else:
            raise AssertionError('All forms vanish')
    return S.simplify(total)

plane_cases = [
    ('generic', X3, -1-e),
    ('A_plus_generic', Lp+X2, -(1+r)/2-e),
    ('A_minus_generic', Lm+X2, -(1+r)/2-e),
    ('L_plus', Lp, -(1+e)/2),
    ('L_minus', Lm, -(1+e)/2),
    ('B_generic', X1+X2, r-1-e),
    ('X1', X1, -e), ('X2', X2, -e),
]
results = {'plane_cases': [], 'line_cases': [], 'scope': 'Finite exact algebra checks, not a proof of the asymptotic theorem.'}
for name, normal, expected in plane_cases:
    actual = plane_weight(normal)
    assert S.simplify(actual-expected) == 0, (name, actual, expected)
    results['plane_cases'].append({'name': name, 'raw_weight': str(actual)})

line_cases = [
    ('neither_L_zero', X3, -e),
    ('one_L_zero_X2_zero', X1+xi*X3, -(1+e)/2),
    ('one_L_zero_X1_zero', X2-xi*X3, -(r+e)/2),
    ('both_L_zero', X1+X2, r-1),
]
for name, vector, expected in line_cases:
    actual = line_weight(vector)
    assert S.simplify(actual-expected) == 0, (name, actual, expected)
    results['line_cases'].append({'name': name, 'raw_weight': str(actual)})

means = [sum(w)/3 for w in weights]
assert S.simplify(sum(means)+e/3) == 0
max_indices = [0,0,2]
max_sum = sum((w[i]-mean)/(1+e/3) for w,mean,i in zip(weights,means,max_indices))
assert S.simplify(max_sum-1) == 0
delta = S.symbols('delta', positive=True)
slack = S.simplify(-delta/9+15*delta/1000+delta/12)
assert slack == -S.Rational(23,1800)*delta
results.update(normalization=True, product_exponent_below_minus_delta_over_12_by=str(-slack), checks_passed=True)
(ROOT/'weights_verified.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(results,ensure_ascii=False,indent=2))
