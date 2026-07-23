import sqlite3  # noqa: F401

class SkillApp:

    Massage = """
What Do You Want To Do:

1 => Show All Skills
2 => Add New Skill
3 => Delete A Skill
4 => Update Skill Progress
5 => Quit The App

Choose Option: """

    commands_list = [1, 2, 3, 4, 5]


def Read_User_Options():

    while True:
        try:
            user_input = int(input(SkillApp.Massage))

            if user_input in SkillApp.commands_list:

                return user_input
            
            print(f"\n--- Sorry Command {user_input} is Not Found ---")

        except ValueError:

            print("\n--- Invalid Input. Please enter a number ---")

def Performed_User_Options(user_input):

    if user_input in SkillApp.commands_list:
        match user_input:
            case 1:
                Show_Skills(cr)
            case 2:
                Add_Skill(cr)
            case 3:
                Delete_Skill(cr)
            case 4:
                Update_Skill(cr)
            case 5:
                Quit(cr)

def connect_to_database():
    try:

        db = sqlite3.connect("SkillApp.db")
        cr = db.cursor() # noqa: F841

        cr.execute("""
                CREATE TABLE IF NOT EXISTS skills (
                    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT UNIQUE NOT NULL,
                    progress INTEGER CHECK(progress BETWEEN 0 AND 100)
                )
            """)

    except sqlite3.Error as er:
        print(f"Error While Connect To DataBase {er}")

def Show_Skills(cr):
    pass

def Add_Skill(cr):
    print("Add Skill Will Be Here.")

def Delete_Skill(cr):
    print("Delete Skill Will Be Here.")

def Update_Skill(cr):
    print("Update Skill Will Be Here.")

def Quit(cr):
    print("Quit Will Be Here.")

cr = connect_to_database()
option = Read_User_Options()
Performed_User_Options(option)