import re


def check_email(email):
    email_regexp = r"^[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\.[a-zA-Z0-9-.]+$"
    email_check_pattern = re.compile(email_regexp)
    validation_result = "valid" if email_check_pattern.fullmatch(
        email) else "not valid"
    return (email, validation_result)

# Символ + - обозначает повторение предыдущего элемента один или более раз.


# Valid
print(check_email('bs@gmail.com'))
print(check_email('b_s@gmail.com'))
print(check_email('b.s@gmail.com'))
print(check_email('b.s@sub.gmail.com'))
# Invalid
print(check_email('bsgmail.com'))
print(check_email('bs@gmailcom'))
print(check_email('@gmail.com'))
print(check_email('bs@'))
