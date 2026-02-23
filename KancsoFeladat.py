class KancsoFeladat:
    def __int__(self, ke, c, max):
        self.kezdo = ke
        self.cel = c
        self.MAX = max

    def celteszt(self, a): #a=(a1,a2,a3) allapot
        return a[0] == self.cel or a[1] == self.cel or a[2] == self.cel

    def rakovetkezo(self, a): #a=(a1,a2,a3) allapot
        gyereke = []
        a1,a2,a3 = a
        max1,max2,max3 = self.max
        tomb_a=[a1,a2,a3]
        tomb_max=[max1,max2,max3]
        for i in range(3):
            for j in range(3):
                if i == j:
                    continue
                if tomb_a[i] != 0 and tomb_a[j] != tomb_max[j]:
                    T = min(tomb_a[i], tomb_max[j]-tomb_a[j])
                    tmp=tomb_a
                    tomb_a[i] = tomb_a[i] - T
                    tomb_a[j] = tomb_a[j] + T
                    gyereke.append((f"tolt {i+1}->{j+1}",(tomb_a[0], tomb_a[1], tomb_a[2])))
                    tomb_a=tmp



        # tolt 1,2 operator alkalmazasi elofeltetele
        if a1 != 0 and a2 != max2:
            T = min(a1, max2-a2)
            gyereke.append(("tolt 1->2", (a1-T, a2+T,a3)))

        # tolt 1,3 operator alkalmazasi elofeltetele
        if a1 != 0 and a3 != max3:
            T = min(a1, max3 - a3)
            gyereke.append(("tolt 1->3", (a1 - T, a2, a3 + T)))

        # tolt 2,1 operator alkalmazasi elofeltetele
        if a2 != 0 and a1 != max1:
            T = min(a2, max1 - a1)
            gyereke.append(("tolt 2->1", (a1 + T, a2 - T, a3)))

        # tolt 2,3 operator alkalmazasi elofeltetele
        if a2 != 0 and a3 != max3:
            T = min(a2, max3 - a3)
            gyereke.append(("tolt 2->3", (a1, a2 - T, a3 + T)))


if __name__ == '__main__':
    feladat = KancsoFeladat((0,0,8), 4, (3,5,8))
