def fibonacci_sequence(n: int) -> list[int]:
    """Return a list containing the first n terms of the Fibonacci sequence."""
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence


try:
    n = int(input("Enter number: "))
except ValueError:
    print("Please enter a valid natural number.")
else:
    if 1 <= n <= 100:
        print(fibonacci_sequence(n))
    else:
        print("Number must be a natural number not exceeding 100.")
