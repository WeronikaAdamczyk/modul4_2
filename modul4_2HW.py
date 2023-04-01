def is_palindrom(text):
    if text == text[::-1]:
        return True
    return False
print(is_palindrom("kajak"))
