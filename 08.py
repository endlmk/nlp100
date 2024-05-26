def cipher(s: str):
    return "".join([chr(219 - ord(c)) if str.isalpha(c) and str.islower(c) else c for c in s])


print(cipher("abcde"))
print(cipher(cipher("abcde")))
