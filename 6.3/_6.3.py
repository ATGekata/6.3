def print_even_numbers_in_range(A, B):
    for num in range(A, B + 1):
        if num % 2 == 0:
            print(num, end=" ")

A = int(input("Enter the integer A: "))
B = int(input("Enter the integer B (A <= B): "))

print("Even numbers between", A, "and", B, "are:")
print_even_numbers_in_range(A, B)
