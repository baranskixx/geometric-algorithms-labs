import numpy as np
from queue import LifoQueue
from math import sqrt
from random import uniform, seed, randint

def orient(a, b, c):
    return np.linalg.det(np.array([[a[0], a[1], 1],
                                    [b[0], b[1], 1],
                                    [c[0], c[1], 1]])) > 0

def dist(p1, p2):
    return sqrt(((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2))

def graham(S, eps):
    # sortuję najpierw po współrzędnej x, potem po y
    # sortowanie jest stabilne
    S = sorted(S, key = lambda a : a[0])
    S = sorted(S, key = lambda a : a[1])

    x0, y0 = S.pop(0)
    unit_axis_x = [1, 0]
    scenes = []

    n = len(S)

    # każdy punkt po wykonaniu tej pętli wygląda tak: (x, y, ang), gdzie ang = kąt między wersorem [1, 0] a wersorem 
    # współliniowym z prostą przechodzącą przez dany punkt oraz punkt p0
    for i in range(n):
        vec = [S[i][0] - x0, S[i][1] - y0]
        unit_vec = vec / np.linalg.norm(vec)
        
        angle = np.arccos(np.dot(unit_vec, unit_axis_x))
        if orient((x0, y0), (x0, y0 + 1), S[i]) < 0:
            angle = 2*np.pi - angle
        
        S[i] = [S[i], angle]

    # sortowanie punktów po ang
    S = sorted(S, key = lambda x : x[1])
    
    # jeśli na prostej p0-a między punktami a i p0 leży punkt b to go usuwamy
    i = 0
    while i < len(S)-1:
        if S[i][1] == S[i+1][1]:
            if dist((x0, y0), S[i][0]) < dist((x0, y0), S[i+1][0]):
                S.pop(i)
            else:
                S.pop(i+1)
        else:
            i += 1
    
    # utworzenie stosu, dodanie do niego p0 oraz dwóch punktów,
    # których wartość ang jest najmniejsza
    stack = LifoQueue()
    n = len(S)

    stack.put((x0, y0))
    stack.put(S[0][0])
    stack.put(S[1][0])
    
    # sprawdzanie, czy każdy z pozostałych punktów należy do otoczki
    for i in range(2, n):
        # ściągnięcie dwóch punktów z góry stosu
        p2 = stack.get()
        p1 = stack.get()

        # tak długo, jak punkt nie leży po lewo względem prostej przechodzącej przez dwa 
        # punkty z góry stosu usuwaj ze stosu
        while orient(p1, p2, S[i][0]) <= 0:
            p2 = p1
            p1 = stack.get()
        
        stack.put(p1)
        stack.put(p2)
        stack.put(S[i][0])

    ans = []
    while not stack.empty():
        ans.append(stack.get())
    ans.reverse()

    return ans
    
if __name__ == '__main__':
    seed(44)

    graham([(0, 0), (5, 0), (2, 2), (4, 1), (4, 3), (5, 4), (-4, 1), (-2, 2), (-3, 4)], 1e-5)
    graham([(0, 0), (5, 0), (2, 4)], 1e-5)
    graham([(0, 0), (4, -2), (8, -1), (10, 3), (8, 7), (5, 7), (6, 3)], 1e-5)
    graham([[0, 0], [1, 0], [1, 0.5], [1, 1], [0, 1]], 1e-5)

