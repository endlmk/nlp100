import random

def shuffle_word(s:str):
    rand = s[1:-1]
    res = (random.sample(rand, len(rand)))
    res.insert(0, s[0])
    res.append(s[-1])
    return "".join(res)

def shuffle(s:str):
    return " ".join([shuffle_word(w) if len(w) > 4 else w for w in s.split()])

print(shuffle("I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."))