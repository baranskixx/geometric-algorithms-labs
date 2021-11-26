from angle_cw import angle_cw
from dist import dist
from ox_angle import ox_angle


def jarvis(S):
    # sortowanie punktów (stabilne) po x -> po y
    S = sorted(S, key= lambda x : x[0])
    S = sorted(S, key= lambda x : x[1])

    p1 = S[0]
    convex_hull = [p1]
    
    current = p1
    prev = None
    back_in_p1 = True
    A = [None]*len(S)

    while not back_in_p1:
        if prev is None:
            for i in range(len(A)):
                A[i] = [ox_angle(p1, S[i]), dist(p1, S[i]), i]
        else:
            for i in range(len(A)):
                A[i] = [angle_cw(prev, current, S[i]), dist(current, S[i]), i]
        
        A = sorted(A, key= lambda x: x[1], reverse= True)
        A = sorted(A, key= lambda x: x[0], reverse= True)

        prev = current
        current = S[A[0][2]]

        if p1 == current:
            back_in_p1 = True
        
        convex_hull.append(current)
    
    return convex_hull
        



