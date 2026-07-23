Massage = """
What Do You Want To Do ? 
1 => Show All Skills
2 => Add New Skill
3 => Delete A Skill
4 => Update Skill Progress
5 => Quit The App
Choose Option: 
"""
commands_list = [1, 2, 3, 4, 5]

user_input = input(Massage).strip().lower()

while user_input not in commands_list:
    print(f"\n---Sorry Command {user_input}  is Not Found---\n---Please, Enter Another Choose----")
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
    if user_input == 1:
        Show_Skills()

    elif user_input == 2:
        Add_Skill()

    elif user_input == 3:
        Delete_Skill()

    elif user_input == 4:
        Update_Skill()

    elif user_input == 5:
        Quit()