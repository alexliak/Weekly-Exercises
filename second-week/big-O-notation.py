# Εκτέλεση γραμμικού χρόνου O(n) 
def linearTimeFunction(n):
    sum = 0
    print("Εκτέλεση γραμμικού χρόνου O(n):")
    for i in range(n+1):
        sum += i
        print(f"Προσθέτοντας {i}, άθροισμα: {sum}")
    return sum
print(linearTimeFunction(4))
print("\n------------------------------------\n")

# Εκτέλεση τετραγωνικού χρόνου O(n^2)
def quadraticTimeFunction(n):
    sum = 0
    print("\nΕκτέλεση τετραγωνικού χρόνου O(n^2):")
    for i in range(n+1):
        for j in range(n+1):
            sum += i+j
            print(f"Προσθέτοντας {i}+{j}={i+j}, άθροισμα: {sum}")
    return sum
print(quadraticTimeFunction(4))
print("\n------------------------------------\n")

# Εκτέλεση σταθερού χρόνου O(1)
def constantTimeFunction(n):
    result = n*(n+1)/2
    print("\nΕκτέλεση σταθερού χρόνου O(1):")
    print(f"Υπολογισμός με τη μαθηματική σχέση n*(n+1)/2 για n={n}, αποτέλεσμα: {result}")
    return result
print(constantTimeFunction(4))
print("\n------------------------------------\n")

# Εκτέλεση λογαριθμικού χρόνου O(log n)
def logarithmicTimeFunction(n):
    sum = 0
    i = 1
    print("\nΕκτέλεση λογαριθμικού χρόνου O(log n):")
    while i < n:
        sum += i
        print(f"Προσθέτοντας {i}, άθροισμα: {sum}")
        i *= 2
    return sum
print(logarithmicTimeFunction(4))
print("\n------------------------------------\n")

# Εκτέλεση γραμμικού-λογαριθμικού χρόνου O(n log n)
def linearithmicTimeFunction(n):
    sum = 0
    print("\nΕκτέλεση γραμμικού-λογαριθμικού χρόνου O(n log n):")
    for i in range(n+1):
        j = 1
        while j < n:
            sum += i+j
            print(f"Προσθέτοντας {i}+{j}={i+j}, άθροισμα: {sum}")
            j *= 2
    return sum
print(linearithmicTimeFunction(4))
print("\n------------------------------------\n")

# Εκτέλεση συνάρτησης exponentialTimeFunction - Εκθετικός Χρόνος O(2^n)
def exponentialTimeFunction(n):
    print(f"Είσοδος στην exponentialTimeFunction με n={n}")
    if n <= 0:
        print("Βάση της αναδρομής επειδή n <= 0")
        return 0
    result = exponentialTimeFunction(n-1) + n
    print(f"Επιστροφή από exponentialTimeFunction({n}): {result}")
    return result
print(exponentialTimeFunction(4))
print("\n------------------------------------\n")


# Εκτέλεση συνάρτησης cubicTimeFunction - Κυβικός Χρόνος O(n^3)
def cubicTimeFunction(n):
    sum = 0
    print("\nΕκτέλεση συνάρτησης cubicTimeFunction - Κυβικός Χρόνος O(n^3):")
    for i in range(n+1):
        for j in range(n+1):
            for k in range(n+1):
                sum += i+j+k
                print(f"Προσθήκη {i}+{j}+{k}={i+j+k}, άθροισμα: {sum}")
    return sum
print(cubicTimeFunction(4))
print("\n------------------------------------\n")

# Εκτέλεση συνάρτησης quarticTimeFunction - Τετραγωνικός Χρόνος O(n^4)
def quarticTimeFunction(n):
    sum = 0
    print("\nΕκτέλεση συνάρτησης quarticTimeFunction - Τετραγωνικός Χρόνος O(n^4):")
    for i in range(n+1):
        for j in range(n+1):
            for k in range(n+1):
                for l in range(n+1):
                    sum += i+j+k+l
                    print(f"Προσθήκη {i}+{j}+{k}+{l}={i+j+k+l}, άθροισμα: {sum}")
    return sum
print(quarticTimeFunction(4))
print("\n------------------------------------\n")

# Εκτέλεση συνάρτησης quinticTimeFunction - Πενταγωνικός Χρόνος O(n^5)
def quinticTimeFunction(n):
    sum = 0
    print("\nΕκτέλεση συνάρτησης quinticTimeFunction - Πενταγωνικός Χρόνος O(n^5):")
    for i in range(n+1):
        for j in range(n+1):
            for k in range(n+1):
                for l in range(n+1):
                    for m in range(n+1):
                        sum += i+j+k+l+m
                        print(f"Προσθήκη {i}+{j}+{k}+{l}+{m}={i+j+k+l+m}, άθροισμα: {sum}")
    return sum
print(quinticTimeFunction(4))
print("\n------------------------------------\n")

# Εκτέλεση συνάρτησης sexticTimeFunction - Εξαγωνικός Χρόνος O(n^6)
def sexticTimeFunction(n):
    sum = 0
    print("\nΕκτέλεση συνάρτησης sexticTimeFunction - Εξαγωνικός Χρόνος O(n^6):")
    for i in range(n+1):
        for j in range(n+1):
            for k in range(n+1):
                for l in range(n+1):
                    for m in range(n+1):
                        for o in range(n+1):
                            sum += i+j+k+l+m+o
                            print(f"Προσθήκη {i}+{j}+{k}+{l}+{m}+{o}={i+j+k+l+m+o}, άθροισμα: {sum}")
    return sum
print(sexticTimeFunction(4))

# Εκτέλεση συνάρτησης septicTimeFunction - Επταγωνικός Χρόνος O(n^7)
def septicTimeFunction(n):
    sum = 0
    print("\nΕκτέλεση συνάρτησης septicTimeFunction - Επταγωνικός Χρόνος O(n^7):")
    for i in range(n+1):
        for j in range(n+1):
            for k in range(n+1):
                for l in range(n+1):
                    for m in range(n+1):
                        for o in range(n+1):
                            for p in range(n+1):
                                sum += i+j+k+l+m+o+p
                                print(f"Προσθήκη {i}+{j}+{k}+{l}+{m}+{o}+{p}={i+j+k+l+m+o+p}, άθροισμα: {sum}")
    return sum
print(septicTimeFunction(4))

# Εκτέλεση συνάρτησης octicTimeFunction - Οκταγωνικός Χρόνος O(n^8)
def octicTimeFunction(n):
    sum = 0
    print("\nΕκτέλεση συνάρτησης octicTimeFunction - Οκταγωνικός Χρόνος O(n^8):")
    for i in range(n+1):
        for j in range(n+1):
            for k in range(n+1):
                for l in range(n+1):
                    for m in range(n+1):
                        for o in range(n+1):
                            for p in range(n+1):
                                for q in range(n+1):
                                    sum += i+j+k+l+m+o+p+q
                                    print(f"Προσθήκη {i}+{j}+{k}+{l}+{m}+{o}+{p}+{q}={i+j+k+l+m+o+p+q}, άθροισμα: {sum}")
    return sum
print(octicTimeFunction(4))

# Εκτέλεση συνάρτησης nonicTimeFunction - Εννεαγωνικός Χρόνος O(n^9)
def nonicTimeFunction(n):
    sum = 0
    print("\nΕκτέλεση συνάρτησης nonicTimeFunction - Εννεαγωνικός Χρόνος O(n^9):")
    for i in range(n+1):
        for j in range(n+1):
            for k in range(n+1):
                for l in range(n+1):
                    for m in range(n+1):
                        for o in range(n+1):
                            for p in range(n+1):
                                for q in range(n+1):
                                    for r in range(n+1):
                                        sum += i+j+k+l+m+o+p+q+r
                                        print(f"Προσθήκη {i}+{j}+{k}+{l}+{m}+{o}+{p}+{q}+{r}={i+j+k+l+m+o+p+q+r}, άθροισμα: {sum}")
    return sum
print(nonicTimeFunction(4))

# Εκτέλεση συνάρτησης decicTimeFunction - Δεκαγωνικός Χρόνος O(n^10)
def decicTimeFunction(n):
    sum = 0
    print("\nΕκτέλεση συνάρτησης decicTimeFunction - Δεκαγωνικός Χρόνος O(n^10):")
    for i in range(n+1):
        for j in range(n+1):
            for k in range(n+1):
                for l in range(n+1):
                    for m in range(n+1):
                        for o in range(n+1):
                            for p in range(n+1):
                                for q in range(n+1):
                                    for r in range(n+1):
                                        for s in range(n+1):
                                            sum += i+j+k+l+m+o+p+q+r+s
                                            print(f"Προσθήκη {i}+{j}+{k}+{l}+{m}+{o}+{p}+{q}+{r}+{s}={i+j+k+l+m+o+p+q+r+s}, άθροισμα: {sum}")
    return sum
print(decicTimeFunction(4))