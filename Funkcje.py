def add(x, y):
    return x + y


def product(x, y):
    return x*y


def polidrom(wyraz):
    return list(str(wyraz).lower().replace(" ","")) == list(str(wyraz).lower().replace(" ",""))[::-1]
