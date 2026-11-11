def can_form_string(first: str, second: str) -> bool:
    """Check case-insensitively whether second uses the exact characters of first."""
    return sorted(first.lower()) == sorted(second.lower())


first_str = input("Enter first string: ")
second_str = input("Enter second string: ")

if can_form_string(first_str, second_str):
    print("YES")
else:
    print("NO")
