# --------------------------------------------------------------------
# -- Object Oriented Programming => Instance Attributes and Methods --
# --------------------------------------------------------------------
# Self: Point To Instance Created From Class
# Instance Attributes: Instance Attributes Defined Inside The Constructor
# -----------------------------------------------------------------------
# Instance Methods: Take Self Parameter Which Point To Instance Created From Class
# Instance Methods Can Have More Than One Parameter Like Any Function
# Instance Methods Can Freely Access Attributes And Methods On The Same Object
# Instance Methods Can Access The Class Itself
# -----------------------------------------------------------

class Member : 
    def __init__(self, First_Name, Mid_Name,  Last_Name, Age):

        self.FName = First_Name
        self.MName = Mid_Name
        self.LName = Last_Name
        self.Age = Age


Member_One   = Member("Islam", "Raad", "Fathi", 20)
Member_Two   = Member("Ahmad", "Ali", "Salah", 19)
Member_Three = Member("Omar", "Raad", "Abd", 22)

print(Member_One.FName + " " + Member_One.MName+ " " + Member_One.LName + ", Age = ", Member_One.Age)