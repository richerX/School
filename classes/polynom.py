from fractions import Fraction
from fractions import gcd

Upper_num = {"0": 8304, "1": 185, "2": 178, "3": 179, "4": 8308, 
             "5": 8309, "6": 8310, "7": 8311, "8": 8312, "9": 8313}


class Poly():
    
    @staticmethod
    def MonoPoly(deg, poly):      
        str_ans = ""
        
        # определяет знак перед мономом (отбрасывает случай, когда коэффицент = 0)
        if poly[deg] > 0:
            str_ans = "+"
        elif poly[deg] == 0:
            return ""
        elif poly[deg] < 0:
            str_ans = "-"
        
        # определяет коэффицент монома
        str_ans += " "
        if type(poly[deg]) == Fraction and poly[deg] % 1 != 0:
            if deg == (len(poly) - 1) and poly[deg] < 0:
                str_ans += "-(" + str(abs(poly[deg])) + ")"
            else:
                str_ans += "(" + str(abs(poly[deg])) + ")"
        elif poly[deg] == 1 and deg != 0:
            pass
        elif deg == len(poly) - 1:
            if poly[deg] == -1:
                str_ans += "-"
            else:
                str_ans += str(round(poly[deg], 3))
        elif poly[deg] == -1 and deg != 0:
            pass
        else:
            str_ans += str(abs(round(poly[deg], 3)))
        
        # ставит x после коэффицента, кроме последнего
        if deg != 0:
            str_ans += "x"
        
        # определяет степень x
        str_deg = ""
        for j in str(deg):
            str_deg += chr(Upper_num[j])
        if deg != 1 and deg != 0:
            str_ans += str_deg
        
        str_ans += " "        
            
        return(str_ans)
    
    @staticmethod
    def integer_poly(A):
        A = Poly(A)
        lcm = 1
        for i in A._coeff:
            if i != 0 and type(i) == Fraction:
                lcm = (lcm * i.denominator) // (gcd(lcm, i.denominator))
        for i in range(len(A._coeff)):
            A._coeff[i] *= int(lcm)
        return A
    
    @staticmethod
    def rationalization(n):
        ans = []
        for i in range(1, int((abs(n) ** (1 / 2)) + 1)):
            if n % i == 0:
                ans.append(i)
                ans.append(-i)
        for i in range(len(ans)):
            if (n // ans[i]) not in ans:
                ans.append(n // ans[i])
                ans.append(-n // ans[i])
        return ans
    
    def rational_roots(self):
        for i in self._coeff:
            if type(i) not in (int, Fraction):
                raise TypeError
        ans = []
        A = Poly(self)
        while len(A._coeff) > 1 and A._coeff[0] == 0:
            A //= Poly((0, 1))
            ans.append(0)
        while len(A._coeff) != 1:
            while len(A._coeff) > 1 and A._coeff[0] == 0:
                A //= Poly((0, 1))
                ans.append(0)            
            A = Poly.integer_poly(A)
            mas_p = Poly.rationalization(A._coeff[0])
            mas_q = Poly.rationalization(A._coeff[-1])
            flag = False
            for p in mas_p:
                if flag:
                    break
                for q in mas_q:
                    if flag:
                        break
                    while (A | Fraction(p, q)) == 0:
                        flag = True
                        A //= Poly((-Fraction(p, q), 1))
                        if Fraction(p, q) % 1 == 0:
                            ans.append(p // q)
                        else:
                            ans.append(Fraction(p, q))
            if not flag:
                break
        ans.sort()
        return ans
                    
    def __init__(self, *args):
        if len(args) == 0:
            self._coeff = [0]
            
        elif type(args[0]) == int:
            self._coeff = [args[0]]
            
        elif type(args[0]) == float:
            self._coeff = [args[0]]
            
        elif type(args[0]) == list:
            self._coeff = args[0]
            
        elif type(args[0]) == tuple:
            self._coeff = list(args[0])
            
        elif type(args[0]) == str:
            self._coeff = list(map(float, args[0].split()))            
            for i in range(len(self._coeff)):
                if self._coeff[i] == int(self._coeff[i]):
                    self._coeff[i] = int(self._coeff[i])
            
        elif type(args[0]) == Poly:
            self._coeff = []
            for i in args[0]._coeff:
                self._coeff.append(i)
        
        elif type(args[0]) == Fraction:
            self._coeff = []
            self._coeff.append(args[0])        
            
        elif hasattr(args, "__iter__"):
            self._coeff = []
            for i in args[0]:
                self._coeff.append(i)
                
        for i in range(len(self._coeff) - 1, -1, -1):
            if self._coeff[i] != 0 or i == 0:
                self._coeff = self._coeff[:i + 1]
                break
                   
    def __repr__(self):
        str_ans = "Poly((" 
        for i in range(len(self._coeff)):
            if type(self._coeff[i]) == Fraction:
                str_ans += "Fraction" + "(" + str(self._coeff[i].numerator) + ", " + str(self._coeff[i].denominator) + ")" + ", "
            else:
                str_ans += str(self._coeff[i]) + ", "
        str_ans = str_ans[:-2]
        str_ans += "))"
        return str_ans
    
    def __str__(self):
        str_answer = ""
        for i in range(len(self._coeff) - 1, -1, -1):
            str_answer += self.MonoPoly(i, self._coeff)
        str_answer = str_answer[2:len(str_answer) - 1]
        if str_answer == "":
            str_answer = "0"
        return str_answer
    
    def __eq__(self, A):
        A = Poly(A)
        if len(self._coeff) == len(A._coeff):
            for i in range(len(self._coeff)):
                if self._coeff[i] != A._coeff[i]:
                    return False
            return True
        return False
    
    def __ne__(self, A):
        if self == A:
            return False
        return True
    
    def __neg__(self):
        ans = []
        for i in self._coeff:
            ans.append(-i)
        return Poly(ans)
    
    def __pos__(self):
        return self
    
    def __bool__(self):
        if str(self) == "0":
            return False
        return True
    
    def __add__(self, A):
        A = Poly(A)
        ans = []
        for i in range(max(len(self._coeff), len(A._coeff))):
            try:
                a = self._coeff[i]
            except:
                a = 0
            try:
                b = A._coeff[i]
            except:
                b = 0
            ans.append(a + b)
        return Poly(ans)
                     
    def __radd__(self, A):
        return self + A
    
    def __iadd__(self, A):
        A = Poly(A)
        for i in range(max(len(self._coeff), len(A._coeff))):
            try:
                self._coeff[i] += A._coeff[i]
            except:
                if i >= len(self._coeff):
                    self._coeff.append(A._coeff[i])
                elif i >= len(A._coeff):
                    pass
        for i in range(len(self._coeff) - 1, 0, -1):
            if self._coeff[i] != 0:
                self._coeff = self._coeff[:i + 1]
                break         
        return self
    
    def __sub__(self, A):
        A = Poly(A)
        ans = []
        for i in range(max(len(self._coeff), len(A._coeff))):
            try:
                a = self._coeff[i]
            except:
                a = 0
            try:
                b = A._coeff[i]
            except:
                b = 0
            ans.append(a - b)
        return Poly(ans)
                     
    def __rsub__(self, A):
        return Poly(A) - self
    
    def __isub__(self, A):
        A = Poly(A)
        for i in range(max(len(self._coeff), len(A._coeff))):
            try:
                self._coeff[i] -= A._coeff[i]
            except:
                if i >= len(self._coeff):
                    self._coeff.append(-A._coeff[i])
                elif i >= len(A._coeff):
                    pass
        for i in range(len(self._coeff) - 1, 0, -1):
            if self._coeff[i] != 0 or i == 0:
                self._coeff = self._coeff[:i + 1]
                break         
        return self  
    
    def __mul__(self, A):
        A = Poly(A)
        ans = []
        for i in range(len(self._coeff)):
            for j in range(len(A._coeff)):
                while True:
                    try:
                        ans[i + j] += self._coeff[i] * A._coeff[j]
                        break
                    except:
                        ans.append(0)
        return Poly(ans)
                     
    def __rmul__(self, A):
        return self * A
    
    def __imul__(self, A):
        A = Poly(A)
        ans = []
        for i in range(len(self._coeff)):
            for j in range(len(A._coeff)):
                while True:
                    try:
                        ans[i + j] += self._coeff[i] * A._coeff[j]
                        break
                    except:
                        ans.append(0) 
        for i in range(len(ans)):
            while True:
                try:
                    self._coeff[i] = ans[i]
                    break
                except:
                    self._coeff.append(0)            
        return self   
    
    def __pow__(self, A):
        ans = Poly(self)
        if A == 0:
            ans._coeff = [1]
        elif A == 1:
            pass
        else:
            dop = 1
            while A != 1:
                if A % 2 == 0:
                    ans *= ans
                    A /= 2
                else:
                    dop *= ans
                    A -= 1
            ans *= dop
        return ans
        
    def __ipow__(self, A):
        ans = Poly(self)
        if A == 0:
            self._coeff = [1]
        elif A == 1:
            pass
        else:
            dop = 1
            while A != 1:
                if A % 2 == 0:
                    ans *= ans
                    A /= 2
                else:
                    dop *= ans
                    A -= 1
            ans *= dop
            for i in range(len(ans._coeff)):
                while True:
                    try:
                        self._coeff[i] = ans._coeff[i]
                        break
                    except:
                        self._coeff.append(0)              
        return self
    
    def __or__(self, A):
        ans = 0
        for i in range(len(self._coeff) - 1, 0, -1):
            ans += self._coeff[i]
            ans *= A
        ans += self._coeff[0]
        return ans
    
    def __iter__(self):
        for i in self._coeff:
            yield i
    
    def __divmod__(self, B):  # A = B * Q + R;
        if type(B) in (int, float, Fraction):
            Q = Poly(self)
            for i in range(len(self._coeff)):
                Q._coeff[i] = Fraction(Q._coeff[i], B)
            R = Poly(0)
        elif type(B) == Poly:
            A = Poly(self) 
            Q = Poly()
            Q._coeff.clear()            
            while len(A._coeff) >= len(B._coeff):
                nowAns = Fraction(A._coeff[-1], B._coeff[-1])
                Q._coeff.insert(0, nowAns)
                for i in range(1, len(B._coeff) + 1):
                    A._coeff[-i] -= B._coeff[-i] * nowAns
                A._coeff.pop()
            if len(A._coeff) < len(B._coeff):
                Q._coeff.append(0)                
            if len(A._coeff) == 0:
                A._coeff.append(0)                
            for i in range(len(A._coeff) - 1, -1, -1):
                if A._coeff[i] != 0 or i == 0:
                    A._coeff = A._coeff[:i + 1]
                    break
            for i in range(len(Q._coeff) - 1, -1, -1):
                if Q._coeff[i] != 0 or i == 0:
                    Q._coeff = Q._coeff[:i + 1]
                    break
            R = Poly(A)
        return (Q, R)
    
    def __rdivmod__(self, A):
        Q, R = divmod(Poly(A), self)
        return Q, R
    
    def __floordiv__(self, A):
        Q, R = divmod(self, A)
        return Q
    
    def __rfloordiv__(self, A):
        Q, R = divmod(A, self)
        return Q
    
    def __ifloordiv__(self, A):
        Q, R = divmod(self, A)
        self._coeff.clear()
        for i in Q._coeff:
            self._coeff.append(i)
        return self   
    
    def __mod__(self, A):
        Q, R = divmod(self, A)
        return R
    
    def __rmod__(self, A):
        Q, R = divmod(A, self)
        return R
    
    def __imod__(self, A):
        Q, R = divmod(self, A)
        self._coeff.clear()
        for i in R._coeff:
            self._coeff.append(i)
        return self
    
    def __len__(self):
        return len(self._coeff)
    
    def __getitem__(self, i):
        if i % 1 != 0 or i < 0:
            raise IndexError()
        elif i >= len(self):
            return 0
        else:
            return self._coeff[i]
    
    def __setitem__(self, i, val):
        if i % 1 != 0 or i < 0:
            raise IndexError()
        elif i >= len(self):
            self._coeff += [0] * (i - len(self) + 1)
            self._coeff[i] = val
        else:
            self._coeff[i] = val
    
    def __call__(self, x):
        if type(x) in (int, float, Fraction):
            return (self | x)
        else:
            ans = Poly()
            for i in range(len(self._coeff)):
                ans += (x ** i) * self._coeff[i]
            return ans


def pgcd(a, b):
    if a == b:
        return a
    elif b == 0:
        factor = a._coeff[-1]
        for i in range(len(a._coeff)):
            dividend = a._coeff[i]
            
            if type(factor) == Fraction:
                if type(dividend) == Fraction:
                    a._coeff[i] = Fraction(dividend.numerator * factor.denominator, dividend.denominator * factor.numerator)
                elif type(dividend) == int:
                    a._coeff[i] = Fraction(dividend * factor.denominator, factor.numerator)
                    
            elif type(factor) == int:
                if type(dividend) == Fraction:
                    a._coeff[i] = Fraction(dividend.numerator, dividend.denominator * factor)
                elif type(dividend) == int:
                    a._coeff[i] = Fraction(dividend, factor)                
        return a
    else:
        return pgcd(b, a % b)
                 
X = Poly((0, 1))
exec(open("input.txt").read())