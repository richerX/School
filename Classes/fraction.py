class Fraction(): 
    
    @staticmethod
    def Nod(a, b):
        while True:
            if b == 0:
                break
            else:
                a, b = b, a % b
        return a
    
    @staticmethod
    def Lcm(a, b):
        m = a * b
        while a != 0 and b != 0:
            if a > b:
                a %= b
            else:
                b %= a
        return m // (a + b)    
        
    def __init__(self, *args):        
        if len(args) == 0:
            self.nom = 0
            self.denom = 1
        elif len(args) == 1:
            self.nom = args[0]
            self.denom = 1
        elif len(args) == 2:
            nod = self.Nod(args[0], args[1])
            self.nom = args[0] // nod
            self.denom = args[1] // nod    
            
    def __str__(self):
        if self.nom == 0:
            return("0")
        elif self.denom == 1:
            return(str(self.nom))
        else:
            return("{0}/{1}".format(self.nom, self.denom))
        
    def __add__(self, A):
        if type(A) == int:
            nom = self.nom + self.denom * A
            denom = self.denom
        else:
            lcm = self.Lcm(self.denom, A.denom)
            nom = (lcm // self.denom) * self.nom + (lcm // A.denom) * A.nom
            denom = lcm
        nod = self.Nod(nom, denom)
        return Fraction(nom // nod, denom // nod)
        
    def __radd__(self, A):
        return self + A
    
    def __sub__(self, A):
        if type(A) == int:
            nom = self.nom - self.denom * A
            denom = self.denom
        else:
            lcm = self.Lcm(self.denom, A.denom)
            nom = (lcm // self.denom) * self.nom - (lcm // A.denom) * A.nom
            denom = lcm
        nod = self.Nod(nom, denom)
        return Fraction(nom // nod, denom // nod)
    
    def __rsub__(self, A):
        if type(A) == int:
            nom = self.nom - self.denom * A
            denom = self.denom
        else:
            lcm = self.Lcm(self.denom, A.denom)
            nom = (lcm // self.denom) * self.nom - (lcm // A.denom) * A.nom
            denom = lcm
        nod = self.Nod(nom, denom)
        return Fraction(-nom // nod, denom // nod)
    
    def __neg__(self):
        return Fraction(-self.nom, self.denom)
    
    def __mul__(self, A):
        if type(A) == int:
            nom = self.nom * A
            denom = self.denom
        else:
            nom = self.nom * A.nom
            denom = self.denom * A.denom
        nod = self.Nod(nom, denom)
        return Fraction(nom // nod, denom // nod)
    
    def __rmul__(self, A):
        return self * A
    
    def __floordiv__(self, A):
        if type(A) == int:
            nom = self.nom
            denom = self.denom * A
        else:
            nom = self.nom * A.denom
            denom = self.denom * A.nom
        nod = self.Nod(nom, denom)
        return Fraction(nom // nod, denom // nod)
    
    def __rfloordiv__(self, A):
        if type(A) == int:
            nom = self.denom * A
            denom = self.nom
        else:
            nom = self.nom * A.denom
            denom = self.denom * A.nom
        nod = self.Nod(nom, denom)
        return Fraction(nom // nod, denom // nod)
    
    def __lt__(self, A):  # x < y
        return A - self > 0
    
    def __le__(self, A):  # x <= y       
        return A - self >= 0
        
    def __eq__(self, A):  # x == y
        if A == 0:
            return self.nom == 0        
        return self - A == 0
        
    def __ne__(self, A):  # x != y
        if A == 0:
            return self.nom != 0        
        return self - A != 0
        
    def __gt__(self, A):  # x > y
        if A == 0:
            return self.nom > 0        
        return self - A > 0
    
    def __ge__(self, A):  # x >= y
        if A == 0:
            return self.nom >= 0        
        return self - A >= 0
    
    def __abs__(self):
        if self.nom >= 0:
            return self
        else:
            return -self
        
    def denom_change(self, x):
        self.denom += x    
      

m, n = map(int, input().split("/"))
Frac = Fraction(m, n)
print(Frac)