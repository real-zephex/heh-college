# Regex
# Sequence of characters which are used to search for specific pattern in an another string

"""
Special Sequence : predefined patterns
  E.g.: \d : match integer values 
        \w : match alphanumerical values
        \s : match whitespace characters

Character Classes : specify a set of characters to match
  E.g.: [abc] : match any of abc
        [a-z] : match for anything between a to z
        [A-Z] : match for anything between A to Z
        [0-9] : match for anything between 0 to 9

Quantifiers : specify how many times a character or group should be matched
  E.g.: * : zero or more occurences
        + : one or more occurences
        ? : zero or one occurence
        {n} : matches exactly n occurences
        {n, } : matches n or more occurences
        {n, m} : matches between n and m occurences

Greedy Matching : matches as much as possible
Non greedy matching : matches as little text as possible. You can make a non greedy quantifier using `?`

Regx Flags : modify the behaviour of regex matching.
E.g.: re.I : ignore case

"""

import re

# Basic pattern matching examples
def regex_examples():
    # Search for digits
    text = "My phone number is 123-456-7890"
    pattern = r"\d{3}-\d{3}-\d{4}"
    match = re.search(pattern, text)
    print(f"Phone number found: {match.group() if match else 'Not found'}")

    # Email validation
    email = "user@example.com"
    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    is_valid = re.match(email_pattern, email)
    print(f"Email is valid: {bool(is_valid)}")

    # Split example
    text = "apple,banana;orange:grape"
    split_result = re.split(r'[,;:]', text)
    print(f"Split result: {split_result}")

    # Substitution example
    text = "Replace all numbers 123 and 456"
    new_text = re.sub(r'\d+', 'X', text)
    print(f"After substitution: {new_text}")

if __name__ == "__main__":
    regex_examples()

