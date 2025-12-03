# Fibonacci series of 8 terms
fib = [1, 1]

for i in range(2, 8):
    fib.append(fib[i-1] + fib[i-2])

print("Fibonacci series (8 terms):", fib)
