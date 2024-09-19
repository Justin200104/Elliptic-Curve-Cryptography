# Elliptic-Curve-Cryptography



This algorithm solves the Elliptic Curve Discrete Logarithm Problem (ECDLP). Given points \( P \) and \( Q = kP \) on the elliptic curve, Shanks' algorithm finds the scalar \( k \).  
The algorithm works by precomputing "baby steps" and using a giant-step technique to find the matching \( k \).

```python
def shanks_algorithm(E, P, Q):
    # Solves for k in Q = kP using the Baby-Step Giant-Step algorithm
```
# Testing the Algorithm

The elliptic curve is initialized with a randomly generated point \( P \).

The Double-and-Add algorithm is used to compute \( Q = kP \) for a known scalar \( k \).

Shanks' Algorithm is then applied to retrieve the original scalar \( k \).

## Example Output

### Elliptic Curve:
Elliptic Curve defined by \( y^2 = x^3 + 12x + 17 \) over GF(31)

### Generator Point:
A random point on the curve.

### \( Q = kP \):
The resulting point after multiplying the generator point by the scalar \( k = 10 \).

### Found \( k \):
Shanks' Algorithm successfully retrieves the scalar \( k \) used in the multiplication.

## Conclusion
This project illustrates the use of Double-and-Add for scalar multiplication and Shanks' Algorithm to solve the elliptic curve discrete logarithm problem. These concepts are essential for secure cryptographic systems, including ECC-based encryption and digital signatures.
