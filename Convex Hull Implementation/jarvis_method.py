import numpy as np
from math import sqrt
from random import uniform, seed, randint

INF = 1e9

def orient(a, b, c):
    return np.linalg.det(np.array([[a[0], a[1], 1],
                                    [b[0], b[1], 1],
                                    [c[0], c[1], 1]]))

def dist(p1, p2):
    return sqrt(((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2))

def find_min_angle_ccw(a, b, S, eps):
    vec1 = [b[0] - a[0], b[1] - a[1]]
    unit_vec1 = vec1 / np.linalg.norm(vec1)
    n = len(S)

    for i in range(n):
        vec2 = [S[i][0][0] - b[0], S[i][0][1] - b[1]]

        if vec2 == [0, 0] or vec1 == vec2:
            S[i][1] = [2*np.pi, INF]
        else:
            unit_vec2 = vec2 / np.linalg.norm(vec2)
            angle = np.arccos(np.dot(unit_vec1, unit_vec2))

            if orient(a, b, S[i][0]) < 0:
                angle = 2*np.pi - angle
            S[i][1] = [angle, -dist(b, S[i][0])]
    
    return min(S, key = lambda x : x[1])[0]
    

def jarvis(S, eps):
    # sortuję najpierw po współrzędnej x, potem po y
    # sortowanie jest stabilne
    S = sorted(S, key = lambda a : a[0])
    S = sorted(S, key = lambda a : a[1])

    for i in range(len(S)):
        S[i] = [S[i], [2*np.pi, INF]]

    ans = [S[0][0]]

    x, y = ans[0]
    ans.append(find_min_angle_ccw((x-1, y), (x, y), S, eps))

    next = None
    while next != ans[0]:
        m = len(ans)
        next = find_min_angle_ccw(ans[m-2], ans[m-1], S, eps)

        ans.append(next)
    
    return ans[:-1]


if __name__ == '__main__':
    seed(44)

    jarvis([(0, 0), (5, 0), (2, 2), (4, 1), (4, 3), (5, 4), (-4, 1), (-2, 2), (-3, 4)], 1e-5)
    jarvis([(0, 0), (5, 0), (2, 4)], 1e-5)
    jarvis([(0, 0), (4, -2), (8, -1), (10, 3), (8, 7), (5, 7), (6, 3)], 1e-5)
    jarvis([[0, 0], [1, 0], [1, 0.5], [1, 1], [0, 1]], 1e-5)
