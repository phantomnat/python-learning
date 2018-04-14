C = 'C'
S = 'S'


class Beam():
    def __init__(self, p):
        self.p = p
    
    @property
    def damage(self):
        d = 0  # damage
        s = 1  # strength
        for c in self.p:
            if c == 'C':
                s *= 2
            else:
                d += s

        return d
    
    def swap(self, i, j):
        if i == j:
            return self.p
        elif i > j:
            i, j = j, i

        ci, cj = self.p[i], self.p[j]
        swapped = self.p[:i] + cj + self.p[i+1:j] + ci + self.p[j+1:]
        self.p = swapped
    
        return self.p
    
    def fswap(self, i):
        """Swap forward"""
        return self.swap(i, i+1)
    
    def bswap(self, i):
        """Swap backward"""
        return self.swap(i-1, i)
    
    @property
    def min_damage(self):
        return self.p.count(S)
    
    def __str__(self):
        return self.p


if __name__ == '__main__':
    T = int(input())
    for i, t in enumerate(range(T)):
        D, P = input().split()
        D = int(D)
        
        b = Beam(P)
        hack = 0

        if b.min_damage > D:
            print('Case #{i}: IMPOSSIBLE'.format(i=i+1))
            continue
        
        while (b.damage > D):
            ls = b.p.rfind(S)
            lc = b.p.rfind(C, 0, ls)
            b.fswap(lc)
            hack += 1
        
        print('Case #{i}: {hack}'.format(i=i+1, hack=hack))