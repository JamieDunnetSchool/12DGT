import easygui as eg
Monsters = {
    "1": {"Name": "Stoneling", "Strength": 7, "Speed": 1, "Stealth": 25, "Cunning": 15},
    "2": {"Name": "Vexscream", "Strength": 1, "Speed": 6, "Stealth": 21, "Cunning": 19},
    "3": {"Name": "Dawnmirage", "Strength": 5, "Speed": 15, "Stealth": 18, "Cunning": 22},
    "4": {"Name": "Blazegolem", "Strength": 15, "Speed": 20, "Stealth": 23, "Cunning": 6},
    "5": {"Name": "Websnake", "Strength": 7, "Speed": 15, "Stealth": 10, "Cunning": 5},
    "6": {"Name": "Moldvine", "Strength": 21, "Speed": 18, "Stealth": 14, "Cunning": 5},
    "7": {"Name": "Vortexwing", "Strength": 19, "Speed": 13, "Stealth": 19, "Cunning": 2},
    "8": {"Name": "Rotthing", "Strength": 16, "Speed": 7, "Stealth": 4, "Cunning": 12},
    "9": {"Name": "Froststep", "Strength": 14, "Speed": 14, "Stealth": 17, "Cunning": 4},
    "10": {"Name": "Wispghoul", "Strength": 17, "Speed": 19, "Stealth": 3, "Cunning": 2}
}

while True:

    choice = eg.buttonbox("Welcome to the Monster game what would you like to do.", "Selection", 
                          choices=["View Cards", "Add Card", "Search/Change", "Delete Card", "Exit"])
    
    if choice == "View Cards":

        output = ""
        for monster_id, info in Monsters.items():
            output += (
                f"\n#{monster_id} — {info['Name']}\n"
                f"  Strength: {info['Strength']}\n"
                f"  Speed:    {info['Speed']}\n"
                f"  Stealth:  {info['Stealth']}\n"
                f"  Cunning:  {info['Cunning']}\n"
            )
        eg.msgbox(output or "No monsters yet.", "Monster Cards")

    elif choice == "Add Card":


        print("Add Card")


    elif choice == "Search/Change":

        print("Search/Change")

    elif choice == "Delete Card":
         
         print("viewcards")

    elif choice == "Exit":

         break   
