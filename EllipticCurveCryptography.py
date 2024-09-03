from sage.all import *

def double_and_add(l, P):
    l_binary = bin(l)[2:]
    i_initial = l_binary[-1]
    
    A = P
    if i_initial == '0':
        B = P.order() * P
    else:
        B = P
    for i in reversed(l_binary[:-1]):
        A = A + A
        if i == '1':
            B = B + A
    return B


def shanks_algorithm(E, P, Q):
    n = E.cardinality()
    m = ceil(sqrt(n))
    
    T = {}
    R = P.curve()(0)
    
    for r in range(m):
        T[R] = r
        R = R + P
    
    mP = double_and_add(m, P)
    
    for q in range(m):
        R = Q - q * mP
        if R in T:
            r = T[R]
            return q * m + r
    
    return None  



prime = 31
a = 12
b = 17


elliptic_curve = EllipticCurve(GF(prime), [1, 0, 0, a, b])


generator_point = elliptic_curve.random_point()
scalar = 10  
target_point = double_and_add(scalar, generator_point)


found_k = shanks_algorithm(elliptic_curve, generator_point, target_point)

print(f"Elliptic Curve: {elliptic_curve}")
print(f"Generator Point: {generator_point}")
print(f"Q = kP, scalar = {scalar}: {target_point}")
print(f"Found k: {found_k}")