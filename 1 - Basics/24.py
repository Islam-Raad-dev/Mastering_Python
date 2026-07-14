# -----------------
# ---- For Loop ----
# -----------------
# for item in iterable_object :
# -----------------------------
# item Is A Vairable You Create and Call Whenever You Want
# item refer to the current position and will run and visit all items.
# iterable_object => Sequence [ list, tuples, set, dict, string]
# ---------------------------------------------------------------

myNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in myNumbers:
    # print(number * 17)

    if number % 2 == 0:  # Even
        print(f"The Number {number} Is Even.")

    else:
        print(f"The Number {number} Is Odd.")

else:
    print("The Loop Is Finished")

myName = "Osama"

for letter in myName:
    print(f" [ {letter.upper()} ] ")
