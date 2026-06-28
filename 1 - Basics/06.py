# ---------------------
# -- Strings Methods 1 --
# ---------------------
   
# split() rsplit()

a = "I Love Python and C++ and PostrgreSQL"
print(a.split())

b = "I-Love-Python-and-C++-and-PostrgreSQL"
print(b.split("-"))

c = "I-Love-Python-and-C++-and-PostrgreSQL"
print(c.split("-", 3))

d = "I-Love-Python-and-C++-and-PostrgreSQL"
print(d.rsplit("-", 3))

# center()

e = "Islam"
print(e.center(9))  # Spaces
print(e.center(9, "#"))  # Hashes
print(e.center(15, "@"))  # @

# count()

f = "I Love Python and C++ Because C++ is Easy"
print(f.count("C++"))  # 2 C++ Words
print(f.count("C++", 0, 25))  # Only One C++ Word

# swapcase()

g = "I Love Python"
h = "i lOVE pYTHON"

print(g.swapcase())
print(h.swapcase())

# startswith()

i = "I Love Python"
print(i.startswith("I"))
print(i.startswith("S"))
print(i.startswith("P", 7, 12))

# endswith()

j = "I Love Python"
print(j.endswith("n"))
print(j.endswith("S"))
print(j.endswith("e", 2, 6))
