print([len(w.translate(str.maketrans("", "", ",."))) for w in str.split("Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.")])
