adj = input("Adjective : ")
Verb1 = input("Verb 1 : ")
Verb2= input("Verb 2 : ")
Famouschar = input("Famous Charecter : ")
Madlip = f"I think of myself as a {adj} person. I like to {Verb1} because it's funny. It also motivates me to {Verb2}. I'm also blood related to {Famouschar}."
Madlip2 = f"I think of my father as a {adj} person. I hate to {Verb1} because it's stupid. It kills my desire to  me to {Verb2}. I also envy {Famouschar}."
Madlip3 = f"Your first grade teacher is a {adj} person. She likes to {Verb1} because she's smart. she also {Verb2} every weekend. thinking she's {Famouschar}."

def Madlip(i):

    if i == 1 :
        return Madlip
    if i == 2 :
        return Madlip2
    if i == 3 :
        return Madlip3 
    if i > 3 or i< 0 :
        return "This is not a valid number we only have 3 Madlips!"
i = int(input("enter 1 for 1st Madlip. 2 for the second Madlip. 3 for the third Madlip : "))        
print(Madlip(i) )               