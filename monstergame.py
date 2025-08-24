import easygui as eg
Monsters = {
"Stoneling": {"Strength": 7, "Speed": 1, "Stealth": 25, "Cunning": 15}, 
"Vexscream": {"Strength": 1, "Speed": 6, "Stealth": 21, "Cunning": 19}, 
"Dawnmirage": {"Strength": 5, "Speed": 15, "Stealth": 18, "Cunning": 22}, 
"Blazegolem": {"Strength": 15, "Speed": 20, "Stealth": 23, "Cunning": 6}, 
"Websnake": {"Strength": 7, "Speed": 15, "Stealth": 10, "Cunning": 5}, 
"Moldvine": {"Strength": 21, "Speed": 18, "Stealth": 14, "Cunning": 5}, 
"Vortexwing": {"Strength": 19, "Speed": 13, "Stealth": 19, "Cunning":2}, 
"Rotthing": {"Strength": 16, "Speed": 7, "Stealth": 4, "Cunning":12}, 
"Froststep": {"Strength": 14, "Speed": 14, "Stealth": 17, "Cunning":4}, 
"Wispghoul": {"Strength": 17, "Speed": 19, "Stealth": 3, "Cunning":2}
}

while True:

    choice = eg.buttonbox("Welcome to the Monster game what would you like to do.", "Selection", 
                          choices=["View Cards", "Add Card", "Search/Change", "Delete Card", "Exit"])
    
    if choice == "View Cards":

        output = ""
        for monster_id, info in Monsters.items():
            output += (
                f"\nName: {monster_id} \n"
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
         
        delete = eg.enterbox("Enter the name of the Monster you want to delete:", title="Delete")
        if delete in Monsters:
            if eg.ynbox(f"Are you sure you want to delete '{delete}'?", "Confirm Delete"):
                del Monsters[delete]
                eg.msgbox(f"'{delete}' monster deleted.")
        else:
            eg.msgbox("Monster not found.")

    elif choice == "Exit":

         break   
