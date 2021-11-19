from angle_cw import angle_cw
from dist import dist
from ox_angle import ox_angle
from orient import orient
from queue import Queue

EPS = 1e-10


def graham(S):
    S = sorted(S, key = lambda v : v[0])
    S = sorted(S, key = lambda v : v[1])

    p0 = S.pop(0)

    A = [None]*len(S)

    for i in range(len(A)):
        angle = ox_angle(p0, S[i])
        A[i] = [i, dist(p0, S[i]), angle]
    
    A = sorted(A, key = lambda v : v[1], reverse = True)
    A = sorted(A, key = lambda v : v[2])

    while i < len(A)-1:
        if abs(A[i][2] - A[i+1][2]) < EPS:
            if A[i][1] < A[i+1][1]:
                A.pop(i)
            else:
                A.pop(i+1)
    
    stack = Queue()

    stack.put(p0)
    stack.put(S[A[0][0]])
    stack.put(S[A[1][0]])

    for i in range(2, len(A)):
        b = stack.get()
        a = stack.get()
        c = S[A[i][0]]

        while stack.qisze() > 1 and orient(a, b, c) < EPS:
            a, b = stack.get(), a
        
        stack.put(a)
        stack.put(b)
        stack.put(c)
    
    return stack






    


