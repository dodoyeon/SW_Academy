# 분수의 덧셈
from math import gcd
def solution(numer1, denom1, numer2, denom2):
    d = gcd(denom1, denom2)
    denom = denom1*denom2//d
    numer = numer1*(denom//denom1) + numer2*(denom//denom2)
    d = gcd(numer, denom)
    return numer//d, denom//d

def answersheet(numer1, denom1, numer2, denom2):
    denom = denom1*denom2
    numer = numer1*denom2+numer2*denom1
    d = gcd(numer, denom)
    return numer//d, denom//d