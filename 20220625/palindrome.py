def is_palindrom(text: str) -> bool:

    text = text.replace(" ", "").lower()
    palindrom = text[::-1]
    if text == palindrom:
        return True


print(is_palindrom('Kobyła ma mały bok'))