Massage = """
What Do You Want To Do ? 
"s" => Show All Skills
"a" => Add New Skill
"d" => Delete A Skill
"u" => Update Skill Progress
"q" => Quit The App
Choose Option: 
"""
commands_list = ["s", "a", "d", "u", "q"]

user_input = input(Massage).strip().lower()

while user_input not in commands_list:
    print(f"Sorry Command {user_input}  is Not Found\n Enter Another Choose:")
    user_input = input(Massage).strip().lower()


def Show_Skills():
    print("Show Skill Will Be Here.")


def Add_Skill():
    print("Add Skill Will Be Here.")


def Delete_Skill():
    print("Delete Skill Will Be Here.")


def Update_Skill():
    print("Update Skill Will Be Here.")


def Quit():
    print("Quit Will Be Here.")

#____________________________________________________________________________



if user_input in commands_list:
    if user_input == "s":
        Show_Skills()

    elif user_input == "a":
        Add_Skill()

    elif user_input == "d":
        Delete_Skill()

    elif user_input == "u":
        Update_Skill()

    elif user_input == "q":
        Quit()