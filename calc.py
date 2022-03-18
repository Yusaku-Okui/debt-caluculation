#利回り
import numpy_financial as npf
class YieldRatio:
    def __init__(self, price, interest, term):
        self.price = price
        self.interest = interest
        self.term = term

    def y_content(self):
        l = [self.interest for i in range(self.term-1)]
        l2 = [-self.price,100+self.interest]
        l2[1:1] = l
        yr = round(npf.irr(l2), 4)
        return yr

#購入価格
import numpy as np
import numpy.polynomial.polynomial as pol
class P_Func(YieldRatio):
    def p_content(self):
        l = np.geomspace(self.interest/(1+self.y_content()), self.interest/((1+self.y_content())**(self.term-1)), num=self.term-1).sum()
        lt = (self.interest + 100) / ((1 + self.y_content()) ** self.term)
        pr = round(l + lt,4)
        return pr

# 金額デュレーション
import sympy as sym
from sympy import  Symbol, diff
class D_Dur(P_Func):
    def d_content(self):
        cf = np.r_[np.tile(self.interest, int(self.term)-1), self.interest + 100]
        coef = np.linspace(1, self.term, self.term) * cf
        seq = pol.polyval(1 / (1 + self.y_content()), np.r_[0, coef])
        dollar_dur = round((1 / (1 + self.y_content()) * seq), 4)
        dollar_dur = abs(dollar_dur)
        return dollar_dur

# 修正デュレーション
class M_Dur(D_Dur):
    def m_content(self):
        m = round(self.d_content() / self.p_content(), 4)
        return m

# マコーレのデュレーション
class D_Mac(M_Dur):
    def dmac_content(self):
        d_mac = round(self.m_content() * (1 + self.y_content()), 4)
        return d_mac
