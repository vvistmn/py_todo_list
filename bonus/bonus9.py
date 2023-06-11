password = input('Enter new password: ')
validate_password = {}

if len(password) >= 8:
    validate_password['is_length'] = True
else:
    validate_password['is_length'] = False

is_digit = False
is_lower = False
is_upper = False

for i in password:
    if i.isdigit():
        is_digit = True

    if i.islower():
        is_lower = True

    if i.isupper():
        is_upper = True

validate_password['is_digit'] = is_digit
validate_password['is_lower'] = is_lower
validate_password['is_upper'] = is_upper

print(validate_password)

if all(validate_password.values()):
    print('Strong Password')
else:
    print('Weak password')



