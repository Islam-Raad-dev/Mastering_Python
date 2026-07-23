import sqlite3  # noqa: F401
import os
class SkillApp:

    Message = """
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
            user_input = int(input(SkillApp.Message))

            if user_input in SkillApp.commands_list:

                return user_input
            
            print(f"\n--- Sorry Command {user_input} is Not Found ---")

        except ValueError:

            print("\n--- Invalid Input. Please enter a number ---")

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
        db.commit()
        return db, cr
    except sqlite3.Error as er:
            print(f"Error While Connecting To DataBase: {er}")
            return None, None

def Show_Skills(cr):

    os.system("cls" if os.name == "nt" else "clear")

    print("\n---------------Show Skills Screen---------------\n")

    cr.execute("select * from skills")

    results = cr.fetchall()

    if not results:
        print("No Skills Found")

    for id, name, prog in results:

        print(f"User ID [{id}], Skill Name [{name}], Progress is [{prog}]")

    db.commit()

def Add_Skill(cr):

    os.system("cls" if os.name == "nt" else "clear")

    print("\n----------------Add Skill Screen----------------\n")

    SkillName = input("Enter Skill Name: ")
    Progress = input("Enter Skill Progress: ")

    db.execute(f"INSERT INTO skills (name, progress) VALUES ('{SkillName}', '{Progress}')")
    db.commit()

def Delete_Skill(cr):
    os.system("cls" if os.name == "nt" else "clear")

    print("\n----------------Delete Skill Screen----------------\n")

    deleted_skill = input("Enter Skill ID: ")

    db.execute(f"delete from skills where user_id = {deleted_skill}")

    db.commit()

def Update_Skill(cr):
        os.system("cls" if os.name == "nt" else "clear")

        print("\n----------------Update Skill Screen----------------\n")

        skill_id = input("Enter The Skill ID: ")
        updated_skill = input("Enter The New Skill: ")
        updated_progress = input("Enter The New Progress: ")

        db.execute(f"update skills set name = '{updated_skill}' , progress = '{updated_progress}' where user_id = {skill_id}")

        db.commit()

def Quit(cr):
    db.close()
    exit()

def Performed_User_Options(user_input, db, cr):

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

db, cr = connect_to_database()
if db:
    option = Read_User_Options()
    Performed_User_Options(option, db, cr)