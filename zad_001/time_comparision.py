import numpy as np
from random import uniform
from datetime import datetime

# det_2_x_2 przyjmuje jako argument macierz o wymiarach 2x2
def det_2_x_2(M):
    return M[0][0]*M[1][1] - M[1][0]*M[0][1]

# analogicznie det_3_x_3 przyjmuje jako argument macierz o wymiarach 3x3
def det_3_x_3(M):
    return (M[0][0]*M[1][1]*M[2][2] +
            M[1][0]*M[2][1]*M[0][2] +
            M[2][0]*M[0][1]*M[1][2] -
            M[0][2]*M[1][1]*M[2][0] -
            M[0][1]*M[1][0]*M[2][0] -
            M[0][0]*M[1][2]*M[2][1])    

def calculate_time(method, method_name, A):
    start = datetime.now()

    for matrix in A:
        ans = method(matrix)

    end = datetime.now()

    print('Czas obliczen dla sposobu liczenia wyznacznika macierzy metoda ' + method_name.upper() + ': ' + str(end-start))

if __name__ == '__main__':
    N = int(1e7)

    T1 = [None]*N
    T2 = [None]*N

    for i in range(N):
        T1[i] = np.array([[uniform(0, 1000), uniform(0, 1000), uniform(0, 1000)],
                        [uniform(0, 1000), uniform(0, 1000), uniform(0, 1000)],
                        [uniform(0, 1000), uniform(0, 1000), uniform(0, 1000)]])
        T2[i] = np.array([[uniform(0, 1000), uniform(0, 1000)],
                        [uniform(0, 1000), uniform(0, 1000)]])

    methods = ['2x2 własnej implementacji', '2x2 NumPy', '3x3 własnej implementacji', '3x3 NumPy']

    # Obliczenie 100000 wyznaczników macierzy 2x2 z użyciem biblioteki NumPy

    calculate_time(det_2_x_2, '2x2 wlasny', T2)
    calculate_time(det_3_x_3, '3x3 wlasny', T1)
    calculate_time(np.linalg.det, '2x2 numpy', T2)
    calculate_time(np.linalg.det, '3x3 numpy', T1)
