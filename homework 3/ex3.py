def is_palindrome(text: str) -> bool:
    """Return True if English letters (a-z, A-Z) in text form a palindrome."""
    cleaned = "".join(
        ch.lower() for ch in text if "a" <= ch <= "z" or "A" <= ch <= "Z"
    )
    return cleaned == cleaned[::-1]


user_input = input("Enter a string: ")
if is_palindrome(user_input):
    print("Is palindrome")
else:
    print("Is not palindrome")
