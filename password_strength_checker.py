def check_password(password):
    length = False
    if len(password) >= 8:
        length = True

    has_upper = False
    for char in password:
        if char.isupper():
            has_upper = True
            break

    has_lower = False
    for char in password:
        if char.islower():
            has_lower = True
            break

    has_digit = False
    for char in password:
        if char.isdigit():
            has_digit = True
            break

    has_special = False
    special_chars = "!@#$%^&*()-_+=[]{}|;:,'.<>?/"
    for char in password:
        if char in special_chars:
            has_special = True
            break


    score = 0
    if length:
        score += 1
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_special:
        score += 1

    if score <= 2:
        print("Weak Password")
    elif score <=4:
        print("Medium Password")
    else:
        print("Strong Password")

    print("\nSuggestions")

    if not length:
        print("Make Password at least 8 Characters long")
    if not has_upper:
        print("Add a UpperCase Character")
    if not has_lower:
        print("Add a LowerCase Character")
    if not has_digit:
        print("Add a Number")
    if not has_special:
        print("Add a Special Character")

password = input("Enter your password: ")
check_password(password)

