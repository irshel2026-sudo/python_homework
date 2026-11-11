import random

numbers = [random.randint(1, 4) for _ in range(5)]
expanded = []

for num in numbers:
    expanded.extend([num] * num)

print(f"List - {expanded}")
print(f"Length - {len(expanded)}")
