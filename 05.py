def ngram(n, list):
    r = []
    for i in range(len(list) - n + 1):
        gram = []
        for j in range(n):
            gram.append(list[i + j])
        r.append(gram)
    return r

print(ngram(2, str.split("I am an NLPer")))
print(ngram(2, "I am an NLPer"))