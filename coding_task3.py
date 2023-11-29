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
if np.trace(VV_T) == VV_T.sum():
    # As Q is denominator, if it is zero, no solution.
    Q = np.diag(VV_T)
    flag = True
    for i in Q:
        if i == 0:
            print("NO SOLUTION")
            flag = False
            break
    if flag:
    # To find rational numbers c_i, it is to solve matrix equation: V_T * C = W
    # If V is pairwise orthogonal, we can always find p and q in following way.
    # 1) Muliply V on both side so that the i_th entry of vectors on LHS and RHS is: 
    # LHS = <v_i, v_i> * c_i =  <v_i, W> = RHS
    # Note that p_i = <v_i, W> and q_i = <v_i, v_i> are both integers
    # 2) Solution for c_i = p_i / q_i
        P = V.dot(W)
        gcd = np.gcd(P,Q)
        P = np.floor_divide(P, gcd)
        Q = np.floor_divide(Q, gcd)
        # print output
        for i in range(n):
            print('{} {}'.format(P[i], Q[i]))
else:
    # V is not pairwise orthogonal
    print("NOT ORTHOGONAL")
