from sympy import mod_inverse

# Given data
n1, a1 = 5, 2
n2, a2 = 11, 3
n3, a3 = 17, 5

# Compute N
N = n1 * n2 * n3

# Compute partial products
N1 = N // n1
N2 = N // n2
N3 = N // n3

# Compute modular inverses
y1 = mod_inverse(N1, n1)
y2 = mod_inverse(N2, n2)
y3 = mod_inverse(N3, n3)

# Calculate the solution using CRT formula
x = (a1 * N1 * y1 + a2 * N2 * y2 + a3 * N3 * y3) % N

# Print the result
print("The integer x such that x ≡ a mod 935 is:", x)
