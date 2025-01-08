# Write a program to verify whether an email address is valid or not

import re

email_input = input("Enter email address: ")

email_pattern = r"[\w.-]+@\w+\.\w+"
check = re.match(email_pattern, email_input)

print(check)