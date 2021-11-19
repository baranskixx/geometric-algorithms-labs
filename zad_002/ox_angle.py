import numpy as np

# zwraca kąt między osią OX a wektorem -ab-> wyznaczony przez łuk idący 
# odwrotnie do wskazówek zegara od OX do -ab->
def ox_angle(a, b):
    if a == b:
        return 0
    
    unit_vec1 = (1, 0)
    vec2 = (b[0] - a[0], b[1] - a[1])
    unit_vec2 = vec2 / np.linalg.norm(vec2)

    angle = np.arccos(np.dot(unit_vec1, unit_vec2))

    return angle