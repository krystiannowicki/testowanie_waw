from math import pi

# def circle_area(r):
#     if type(r) not in [int, float]:
#         return "Podałeś nie prawidłowy typ. Podaj liczbe."
#     elif r < 0:
#         return "Koło o taki promieniu nie istnieje."
#     else:
#         return pi*r**2

def circle_area(r):
    if r < 0:
        raise Exception("Promień nie może być ujemny.")
    try:
        return pi*r**2
    except:
        return "Coś poszło nie tak"

print(circle_area(1))
print(circle_area(0))
print(circle_area(-1))
print(circle_area(2+5j))
print(circle_area(True))
print(circle_area("asd"))
