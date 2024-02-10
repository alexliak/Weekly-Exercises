def bubble_sort(arr):
    n = len(arr)  # Υπολογίζει το μήκος της λίστας.
    print(f"Αρχική λίστα: {arr}")
    for i in range(n):
        print(f"\nΞεκινά η {i+1}η επανάληψη του εξωτερικού βρόχου")
        swapped = False
        for j in range(0, n-i-1):
            print(f"  Εσωτερικός βρόχος: σύγκριση των στοιχείων στις θέσεις {j} και {j+1} ({arr[j]} > {arr[j+1]})")
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                print(f"    Ανταλλάχθηκαν: {arr[j]} με {arr[j+1]} - Νέα λίστα: {arr}")
        if not swapped:
            print("    Δεν έγινε καμία ανταλλαγή, η λίστα είναι ταξινομημένη.")
            break
        else:
            print(f"  Τέλος της {i+1}ης επανάληψης του εξωτερικού βρόχου, η λίστα τώρα είναι: {arr}")
    print("\nΤελική ταξινομημένη λίστα:", arr)
    return arr


# Παράδειγμα χρήσης
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(arr)
print("Ταξινομημένη λίστα:", sorted_arr)


def bubble_sort(arr):
    n = len(arr)
    print(f"Αρχική λίστα: {arr}")
    for i in range(n-1):
        print(f"\nΕκκίνηση {i+1}ης επανάληψης του εξωτερικού βρόχου.")
        for j in range(n-1-i):
            print(f"  Σύγκριση {arr[j]} με {arr[j+1]}")
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print(f"    Ανταλλαγή {arr[j]} με {arr[j+1]}")
        print(f"  Λίστα μετά από {i+1}η επανάληψη: {arr}")
    print("\nΤελική ταξινομημένη λίστα: ", arr)
    return arr

# Παράδειγμα χρήσης
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(arr)
print("Ταξινομημένη λίστα:", sorted_arr)

def bubble_sort(arr):
    n = len(arr)
    print(f"Αρχική λίστα: {arr}")
    for i in range(n):
        print(f"\nΕκκίνηση της {i+1}ης επανάληψης του εξωτερικού βρόχου")
        for j in range(0, n-i-1):
            print(f"  Σύγκριση των στοιχείων στις θέσεις {j} και {j+1}: {arr[j]} και {arr[j+1]}")
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print(f"    Ανταλλαγή: {arr[j]} με {arr[j+1]} - Νέα λίστα: {arr}")
            else:
                print("    Δεν χρειάστηκε ανταλλαγή")
        print(f"  Η λίστα μετά την {i+1}η επανάληψη: {arr}")
    print("\nΤελική ταξινομημένη λίστα: {arr}")
    return arr

# Παράδειγμα χρήσης
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(arr)
print("Ταξινομημένη λίστα:", sorted_arr)
