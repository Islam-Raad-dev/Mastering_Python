# --------------------
# --  Control Flow  --
# -- If, Elif, Else --
# -- Make Decisions --
# --------------------

uName = "Islam"
uCountry = "Iraq"
cName = "Python Course"
cPrice = 210

if uCountry == "Egypt":
    print(f"Hello {uName} Because You Are From {uCountry}")
    print(f'The Course "{cName}" Price Is: ${cPrice - 80}')

elif uCountry == "KSA":
    print(f"Hello {uName} Because You Are From {uCountry}")
    print(f'The Course "{cName}" Price Is: ${cPrice - 60}')

elif uCountry == "Kuwait":
    print(f"Hello {uName} Because You Are From {uCountry}")
    print(f'The Course "{cName}" Price Is: ${cPrice - 50}')

else:
    print(f"Hello {uName} Because You Are From {uCountry}")
    print(f'The Course "{cName}" Price Is: ${cPrice - 30}')
