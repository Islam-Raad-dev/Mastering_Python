# ----------------
# -- User Input --
# ----------------

FirstName = input("What's Is Your First Name: ")
MiddleName = input("What's Is Your Middle Name: ")
LastName = input("What's Is Your Last Name: ")

FirstName = FirstName.strip().capitalize()
MiddleName = MiddleName.strip().capitalize()
LastName = LastName.strip().capitalize()

print(f"Hello {FirstName} {MiddleName:.1s} {LastName} Happy To See You.")
