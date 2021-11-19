from math import sqrt

# zwraca odległość między punktami p1 i p2 w metryce euklidesowej
def dist(p1, p2):
    return sqrt(((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2))
