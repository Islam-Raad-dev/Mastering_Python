# -------------
# -- Boolean Methods --
# -------------
# [1] In Programming You Need to Known Your If Your Code Output 
# is True Or False
# [2] Boolean Values Are The Two Constant Objects False + True.
# ---------------------------------------------------------------

name = " "
print(name.isspace())

print("=" * 50)

print(100 > 200)
print(100 > 100)
print(100 > 90)

print("=" * 50)

# True Values

print(bool("Islam"))
print(bool(100))
print(bool(100.95))
print(bool(True))
print(bool([1, 2, 3, 4, 5]))

print("=" * 50)

# False Values

print(bool(0))
print(bool(""))
print(bool(""))
print(bool([]))
print(bool(False))
print(bool(()))
print(bool({}))
print(bool(None))


# -----------------------
# -- Boolean Operators --
# -----------------------
# and
# or
# not
# -----------------------

age = 36
country = "IRAQ"
rank = 10

print(age > 16 and country == "IRAQ" and rank > 0)  # True
print(age > 16 and country == "KSA" and rank > 0)  # False

print(age > 40 or country == "KSA" or rank > 20)  # False
print(age > 40 or country == "IRAQ" or rank > 20)  # True

print(age > 16)  # True
print(not age > 16)  # Not True = False