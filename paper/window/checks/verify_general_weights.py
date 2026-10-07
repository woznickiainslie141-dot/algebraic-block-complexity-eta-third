"""Finite exact checks of the general formulas; see the manuscript for proofs."""
from itertools import combinations, permutations
from pathlib import Path
from collections import Counter
import json
import sympy as S

root = Path(__file__).resolve().parent
eps, rho = S.symbols('epsilon rho', real=True)
X1, X2, X3 = [S.eye(3)[:,i] for i in range(3)]
report = {'scope':'Finite algebra and coset checks, not a proof of the asymptotic theorem.',
          'arrangements':[], 'coset_cases':[], 'base_cases':[]}

def check_arrangement(name, betas):
    degree = len(betas)
    mass = S.Rational(1,degree)
    forms = [-b*X1+b*X2+X3 for b in betas]
    systems = [[X1,X2,f] for f in forms] + [[X1,X2,X3]]
    weights = [[mass,mass*rho,-mass*eps] for _ in forms] + [[-1,-rho,0]]
    orders = [[2,1,0] for _ in forms] + [[0,1,2]]
    def weight(vector, dimension):
        total = S.Integer(0)
        for system,w,order in zip(systems,weights,orders):
            found=False
            for indices in combinations(order,dimension):
                if dimension == 1:
                    determinant=system[indices[0]].dot(vector)
                else:
                    determinant=S.Matrix.hstack(*(system[i] for i in indices),vector).det()
                if S.simplify(determinant) != 0:
                    total += sum(w[i] for i in indices)
                    found=True
                    break
            assert found
        return S.simplify(total)
    plane_cases=[('generic',X3,-1-eps), ('B_generic',X1+X2,rho-1-eps),
                 ('X1',X1,-eps),('X2',X2,-eps)]
    for i,f in enumerate(forms):
        plane_cases += [(f'A_{i}',f+X2,-1-eps+(1-rho)*mass),
                        (f'L_{i}',f,-(1-mass)*(1+eps))]
    line_cases=[('no_vanishing',X3,-eps),('all_vanishing',X1+X2,rho-1)]
    for i,b in enumerate(betas):
        line_cases += [(f'one_X2_zero_{i}',X1+b*X3,-(1-mass)*(1+eps)),
                       (f'one_X1_zero_{i}',X2-b*X3,-(1-mass)*(rho+eps))]
    for dim,cases in [(2,plane_cases),(1,line_cases)]:
        for label,v,expected in cases:
            actual=weight(v,dim)
            assert S.simplify(actual-expected)==0,(name,label,actual,expected)
    report['arrangements'].append({'name':name,'degree':degree,
                                  'plane_checks':len(plane_cases),'line_checks':len(line_cases)})

check_arrangement('quadratic_real',[S.sqrt(2)-1,-S.sqrt(2)-1])
root3=S.real_root(2,3)
zeta=(-1+S.sqrt(3)*S.I)/2
check_arrangement('cubic_one_real_two_nonreal',[root3,root3*zeta,root3*S.conjugate(zeta)])
check_arrangement('quartic_two_real_two_nonreal',[S.sqrt(S.sqrt(2)),-S.sqrt(S.sqrt(2)),
                                               S.I*S.sqrt(S.sqrt(2)),-S.I*S.sqrt(S.sqrt(2))])
check_arrangement('five_distinct_form_parameters',[1,2,3,4,5])

for degree,complex_place in [(2,False),(3,False),(3,True),(4,True),(5,True)]:
    group=list(permutations(range(degree)))
    conjugation=list(range(degree))
    if complex_place:
        conjugation[1],conjugation[2]=conjugation[2],conjugation[1]
    unseen=set(group)
    masses=Counter()
    h=2 if complex_place else 1
    while unseen:
        sigma=next(iter(unseen))
        left=tuple(conjugation[i] for i in sigma)
        coset={sigma,left}
        assert len(coset)==h
        beta_index=sigma.index(0)
        assert all(g.index(0)==beta_index for g in coset)
        masses[beta_index] += S.Rational(h,len(group))
        unseen-=coset
    assert all(masses[i]==S.Rational(1,degree) for i in range(degree))
    report['coset_cases'].append({'degree':degree,'complex_places':complex_place,
                                 'group_order':len(group),'mass_per_conjugate':str(masses[0])})

for base in [2,4,6,10,12,30,72,210]:
    factors=S.factorint(base)
    numerator=sum(int(a)*S.log(int(p)) for p,a in factors.items())
    assert S.logcombine(numerator,force=True)==S.log(S.Integer(base))
    report['base_cases'].append({'base':base,'factorization':{str(p):int(a) for p,a in factors.items()},
                                 'normalized_prime_weight_sum':1})
report['checks_passed']=True
(root/'general_weights_verified.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(report,ensure_ascii=False,indent=2))
