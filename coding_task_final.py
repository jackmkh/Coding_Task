#!/usr/bin/env python3
import numpy as np

n = int(input())
V = []
for i in range(n):
    V.append(list(map(int, input().split(' '))))
V = np.array(V, dtype = 'object')
W = list(map(int, input().split(' ')))
W = np.array(W, dtype = 'object')

# If the vectors are pairwise orthogonal, 
# then only diagnals of matrix VV_T are non-zero values while others are zero
VV_T = V.dot(V.T)
if np.trace(abs(VV_T)) == abs(VV_T).sum():
    # If W is zero vector, C_i = 0 must be a solution
    if abs(W).sum() == 0:
        for i in range(n):
            print(0, 1, sep = " ")
    # If Rank(V) < Rank(V|W), then there is no solution
    # By removing projection of W on each component v_i, we should get a zero vector if W is in span(V)
    else:
        res = np.zeros((n,2), dtype = 'object')
        for idx, vec in enumerate(V):
            if sum(abs(vec)) == 0:
                res[idx] = [0, 1]
            else:
                p_i = vec.dot(W)
                q_i = vec.dot(vec)
                gcd = np.gcd(p_i, q_i)
                p_i = np.floor_divide(p_i, gcd)
                q_i = np.floor_divide(q_i, gcd)
                res[idx] = [p_i, q_i]
        for idx, c_i in enumerate(res):
            W = W - V[idx]*c_i[0]/c_i[1]
        if sum(abs(W)) < 1e-9:
            for i in range(n):
                print(res[i][0], res[i][1], sep = ' ')
        else:
            print("NO SOLUTION")
else:
    # V is not pairwise orthogonal
    print("NOT ORTHOGONAL")