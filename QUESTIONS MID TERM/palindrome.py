print("--- Palindrome Checker ---")
user_input = input("Enter a word, phrase, or sentence to check: ")

cleaned_string = "".join(char for char in user_input if char.isalnum()).lower()

if cleaned_string == cleaned_string[::-1]:
    print(f"\n Yes, '{user_input}' is a palindrome!")
else:
    print(f"\n No, '{user_input}' is not a palindrome.")