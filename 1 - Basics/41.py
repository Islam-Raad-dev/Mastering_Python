# -----------------------------------
# --------- Modules 2 -------------
# -----------------------------------

import sys

sys.path.append(r"D:\Games")
print(sys.path)

import ISLAM # type: ignore  # noqa: E402

print(dir(ISLAM))

ISLAM.sayHello("Ahmed")
ISLAM.sayHello("Islam")
ISLAM.sayHello("Mohamed")

ISLAM.sayHowAreYou("Ahmed")
ISLAM.sayHowAreYou("Islam")
ISLAM.sayHowAreYou("Mohamed")

# Alias

import ISLAM as ee  # type: ignore  # noqa: E402

ee.sayHello("Ahmed")
ee.sayHello("Islam")
ee.sayHello("Mohamed")

ee.sayHowAreYou("Ahmed")
ee.sayHowAreYou("Islam")
ee.sayHowAreYou("Mohamed")

from ISLAM import sayHello  # type: ignore  # noqa: E402

sayHello("Islam")

from ISLAM import sayHello as ss  # type: ignore  # noqa: E402

ss("Islam")
