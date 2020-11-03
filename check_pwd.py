def check_pwd(pwd):
    has_lower = False
    has_upper = False
    if len(pwd) < 8 or len(pwd) > 20:
        return False
    else:
        for x in pwd:
            if x.islower():
                has_lower = True
            elif x.isupper():
                has_upper = True

    if has_lower and has_upper:
        return True
    else:
        return False

