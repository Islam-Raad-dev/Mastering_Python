# -----------------------------------
# --------- Modules 2 -------------
# -----------------------------------

import sys

sys.path.append(r"D:\Games")
print(sys.path)

import ISLAM

print(dir(ISLAM))

ISLAM.sayHello("Ahmed")
ISLAM.sayHello("Islam")
ISLAM.sayHello("Mohamed")

ISLAM.sayHowAreYou("Ahmed")
ISLAM.sayHowAreYou("Islam")
ISLAM.sayHowAreYou("Mohamed")

# Alias

import ISLAM as ee

ee.sayHello("Ahmed")
ee.sayHello("Islam")
ee.sayHello("Mohamed")

ee.sayHowAreYou("Ahmed")
ee.sayHowAreYou("Islam")
ee.sayHowAreYou("Mohamed")

from ISLAM import sayHello

sayHello("Islam")

from ISLAM import sayHello as ss

ss("Islam")
