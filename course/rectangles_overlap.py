def solve(A, B, C, D, E, F, G, H):
        if A >= E or D <=E:
            return 0
        if A >= G or A >=H:
            return 0
        return 1

A = 6
B = 8
C = 10
D = 9
E = 6
F = 1
G = 9
H = 6
A = 60
B = 65
C = 99
D = 84
E = 85
F = 24
G = 99
H = 84
print(solve(A,B,C,D,E,F,G,H))