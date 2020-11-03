def check_pwd(pwd):
    has_lower = False
    if len(pwd) < 8 or len(pwd) > 20:
        return False
    else:
        for x in pwd:
            if x.islower():
                has_lower = True

    if has_lower:
        return True
    else:
        return False

