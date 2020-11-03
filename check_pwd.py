def check_pwd(pwd):
    sp_chars = ['~', '`', '!', '@', '#',
                '$', '%', '^', '&', '*',
                '(', ')', '_', '+', '-', '=']
    has_lower = False
    has_upper = False
    has_digit = False
    has_chars = False
    if len(pwd) < 8 or len(pwd) > 20:
        return False
    else:
        for x in pwd:
            if x.islower():
                has_lower = True
            elif x.isupper():
                has_upper = True
            elif x.isdigit():
                has_digit = True
            elif x in sp_chars:
                has_chars = True

    if has_lower and has_upper and has_digit and has_chars:
        return True
    else:
        return False
