class Kiralyno:

    def __init__(self, k,s, c):
        self.kezdo = k
        self.sor=s
        self.cel = c
        self.N = c-1


    def celteszt(self, a):
        return self.sor == self.cel





    def rakovetkezo(self, a):
        gyerekek = []
        s = self.sor  # A következő sor indexe (0-tól indulva)
        for i in range(self.N):
            elofeltetel = True
            for m in range(s):
                if a[m] == i or abs(m - s) == abs(a[m] - i):
                    elofeltetel = False
                    break

            if elofeltetel:
                uj_allapot = a + [i]
                gyerekek.append(uj_allapot)

        return gyerekek


if __name__ == '__main__':
    feladat = Kiralyno([[1,0],[2,0],[3,0],[4,0]],1,5)