# ---------------------------
# -- Dictionary --
# ----------------
# [1] Dict Items Are Enclosed in Curly Braces
# [2] Dict Items Are Contains Key : Value
# [3] Dict Key Need To Be Immutable => (Number, String, Tuple) List Not Allowed
# [4] Dict Value Can Have Any Data Types
# [5] Dict Key Need To Be Unique
# [6] Dict Is Not Ordered You Access Its Element With Key
# ----------------------------

# Dictionary

user = {
    "name": "Islam",
    "age": 20,
    "country": "Iraq",
    "skills": ["Html", "Css", "JS"],
    "rating": 10.5,
}

print(user)
print(user["country"])
print(user.get("country"))

print(user.keys())
print(user.values())

# Two-Dimensional Dictionary

languages = {
    "One": {"name": "Html", "progress": "80%"},
    "Two": {"name": "Css", "progress": "90%"},
    "Three": {"name": "Js", "progress": "90%"},
}

print(languages)
print(languages["One"])
print(languages["Three"]["name"])

# Dictionary Length

print(len(languages))
print(len(languages["Two"]))

# Create Dictionary From Variables

frameworkOne = {"name": "Vuejs", "progress": "80%"}

frameworkTwo = {"name": "ReactJs", "progress": "80%"}

frameworkThree = {"name": "Angular", "progress": "80%"}

allFramework = {"one": frameworkOne, "two": frameworkTwo, "three": frameworkThree}

print(allFramework)

# clear()

user = {"name": "Osama"}
print(user)
user.clear()
print(user)

print("=" * 50)

# update()

member = {"name": "Osama"}
print(member)
member["age"] = 36
print(member)
member.update({"country": "Egypt"})
print(member)

print("=" * 50)

#-----------------------------------------------------------------------
# Dictionary Methods


# copy()

main = {"name": "Osama"}

b = main.copy()
print(b)
main.update({"skills": "Fighting"})
print(main)
print(b)

# keys() + values()

print(main.keys())
print(main.values())