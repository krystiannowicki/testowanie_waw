def dziel(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        print("Nie można dzielić przez zero")

def dziel_b(a, b):
    assert b != 0, "Nie można dzielić przez zero."
    return a/b



# if dziel(20, 10) == 2:
#     print("PASSED")
# else:
#     raise Exception("FAILD")
#
# if dziel(20, 5) == 2:
#     print("PASSED")
# else:
#     raise Exception("FAILD")

# assert dziel(20,10) == 2, "Faild"
# assert dziel(150,10) == 2, "Faild"


def kwadrat_sumy(a, b):
    return (a+b)**2


# assert kwadrat_sumy(0,0) == 0, "Failed"
# assert kwadrat_sumy(1,1) == 4, "Failed"

# Asercje nie służa tylko do testowania!!

# dziel(5, 0)

def konkatnacja_str(a, b):
    return a+b

assert konkatnacja_str("kot","2") == "kot2", "Failed"
assert konkatnacja_str("","") == "", "Faild"