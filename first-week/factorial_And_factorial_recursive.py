# Προσθήκη
sum = 1 + 2  # Αποτέλεσμα: 3

# Παραγοντικό συνάρτηση (μη αναδρομική προσέγγιση)
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(3))  # Αποτέλεσμα: 24

# Αναδρομική συνάρτηση για τον υπολογισμό του παραγοντικού
def factorial_recursive(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

print(factorial_recursive(6))  # Αποτέλεσμα: 24

# Αναδρομική συνάρτηση για την ακολουθία Fibonacci
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(5))  # Αποτέλεσμα: 5
