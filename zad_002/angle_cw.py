import numpy as np
from orient import orient

# zwraca kąt między wektorami -ab-> i -bc-> zgodnie z wskazówkami zegara
def angle_cw(a, b, c):
    if c == a or c == b or a == b:
        return 0

    vec1 = [b[0] - a[0], b[1] - a[1]]
    vec2 = [c[0] - b[0], c[1] - b[1]]
    unit_vec1 = vec1 / np.linalg.norm(vec1)
    unit_vec2 = vec2 / np.linalg.norm(vec2)

    angle = np.arccos(np.dot(unit_vec1, unit_vec2))
    o = orient(a, b, c)

    if o < 0:
        angle = 2*np.pi - angle
    
    return angle