def jarvis_scenes(S):
    # sortowanie punktów (stabilne) najpierw
    # po x, potem po y

    S = sorted(S, key = lambda x : x[0])
    S = sorted(S, key = lambda x : x[1])

    # p1 jest punktem o najmniejszej współrzędnej x wśród punktów
    # o najmniejszej współrzędnej y - ten punkt na pewno znajdzie się w otoczce
    p1 = S[0]
    prev = None
    current = p1
    scenes = [[[p1], []]]
    back_in_p1 = False
    A = [None]*len(S)
    
    # pętle wykonuję do momentu, aż powrócę do punktu p1
    while not back_in_p1:
        # jeśli prev (przedostatni punkt dodany do otoczki) nie istnieje (bo w otoczce mamy tylko p0)
        # obliczam kąt między każdym punktem a osią OX
        if prev is None:
            for i in range(len(A)):
                A[i] = [ox_angle(p1, S[i]), dist(S[i], current), i]
        # w.p.p obliczam kąt między wektorami -a-S[i]-> i -a-b-> gdzie a i b to 
        # odpowiednio ostatni i przedostatni punkt dodany do otoczki
        else:
            for i in range(len(A)):
                A[i] = [angle_cw(prev, current, S[i]), dist(current, S[i]), i]
        
        A = sorted(A, key= lambda x: x[1], reverse= True)
        A = sorted(A, key= lambda x: x[0], reverse= True)


        prev = current
        current = S[A[0][2]]
        new_scene = deepcopy(scenes[len(scenes) - 1])


        if p1 != current:
            new_scene[0].append(current)
        else:
            back_in_p1 = True

        new_scene[1].append([prev, current])
        scenes.append(new_scene)
    
    return scenes