def ngram(n, list):
    r = []
    for i in range(len(list) - n + 1):
        gram = ""
        for j in range(n):
            gram += list[i + j]
        r.append(gram)
    return r

X = set(ngram(2, "paraparaparadise"))
Y = set(ngram(2, "paragraph"))
print(X.union(Y))
print(X.intersection(Y))
print(X.difference(Y))
print(Y.difference(X))
print("se" in X)
print("se" in Y)