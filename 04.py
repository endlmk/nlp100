sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
l = [w[0:1] if index + 1 in [1, 5, 6, 7, 8, 9, 15, 16] else w[0:2] for index, w in enumerate(str.split(sentence))]
print({w: index + 1 for index, w in enumerate(l)})
