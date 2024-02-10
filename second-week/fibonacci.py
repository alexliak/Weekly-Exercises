def fibonacci(n, depth=0):
    indent = "  " * depth  # Δημιουργεί ένα indent για κάθε επίπεδο αναδρομής
    print(f"{indent}fibonacci({n}) called")

    # Βασικές περιπτώσεις
    if n <= 0:
        print(f"{indent}Επιστροφή: 'Η είσοδος πρέπει να είναι θετικός αριθμός!'")
        return "Η είσοδος πρέπει να είναι θετικός αριθμός!"
    elif n == 1:
        print(f"{indent}Επιστροφή: 0")
        return 0
    elif n == 2:
        print(f"{indent}Επιστροφή: 1")
        return 1
    else:
        # Αναδρομική κλήση για τον υπολογισμό των προηγούμενων δύο όρων
        result = fibonacci(n-1, depth+1) + fibonacci(n-2, depth+1)
        print(f"{indent}Επιστροφή: {result}")
        return result

# Παράδειγμα κλήσης της συνάρτησης
n = 5
print(f"Υπολογισμός του {n}ου αριθμού Fibonacci:")
fibonacci(n)
