# funkcja orienta zwraca wyznacznik macierzy postaci
#  | ax, ay, 1 |
#  | bx, by, 1 |
#  | cx, cy, 1 |
# wyznacznik ten definiuje po jakiej stronie (lewo / prawo)
# znajduje się punkt c względem wektora -ab->
def orient(a, b, c):
    return a[0]*b[1] + a[1]*c[0] + b[0]*c[1] - b[1]*c[0] - a[1]*b[0] - a[0]*c[1]


a = (3, 1)
b = (2, 2)
c = (1, 2)
d = (4, 3/2)
e = (3, 7/4)
f = (5, 2)
print(orient((0, 0), (4, 1), (2, 2)))
