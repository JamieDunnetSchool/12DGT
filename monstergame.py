"""This program lets the user look and edit the monster cards cataloge."""

import easygui as eg
Monsters = {
    "Stoneling": {"Strength": 7, "Speed": 1, "Stealth": 25, "Cunning": 15},
    "Vexscream": {"Strength": 1, "Speed": 6, "Stealth": 21, "Cunning": 19},
    "Dawnmirage": {"Strength": 5, "Speed": 15, "Stealth": 18, "Cunning": 22},
    "Blazegolem": {"Strength": 15, "Speed": 20, "Stealth": 23, "Cunning": 6},
    "Websnake": {"Strength": 7, "Speed": 15, "Stealth": 10, "Cunning": 5},
    "Moldvine": {"Strength": 21, "Speed": 18, "Stealth": 14, "Cunning": 5},
    "Vortexwing": {"Strength": 19, "Speed": 13, "Stealth": 19, "Cunning": 2},
    "Rotthing": {"Strength": 16, "Speed": 7, "Stealth": 4, "Cunning": 12},
    "Froststep": {"Strength": 14, "Speed": 14, "Stealth": 17, "Cunning": 4},
    "Wispghoul": {"Strength": 17, "Speed": 19, "Stealth": 3, "Cunning": 2}
}
while True:
    choice = eg.buttonbox(
        "Welcome to the Monster game what would you like to do.", "Selection",
        choices=["View Cards", "Add Card", "Search/Change",
                 "Delete Card", "Exit"])

    # View cards
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
        eg.msgbox(output or "No monsters yet.", "View Cataloge")

# Add cards
    elif choice == "Add Card":
        name = eg.enterbox("Enter the name of the new Monster:",
                           "Add Monster Card")
        while True:
            strength = int(eg.enterbox(f"Enter {name}'s Strength 0-25:"))
            if 0 <= strength <= 25:
                break
            else:
                eg.msgbox("Strength must be between 0 and 25.")
        while True:
            speed = int(eg.enterbox(f"Enter {name}'s Speed 0-25:"))
            if 0 <= speed <= 25:
                break
            else:
                eg.msgbox("Strength must be between 0 and 25.")
        while True:
            stealth = int(eg.enterbox(f"Enter {name}'s Stealth 0-25:"))
            if 0 <= stealth <= 25:
                break
            else:
                eg.msgbox("Strength must be between 0 and 25.")
        while True:
            cunning = int(eg.enterbox(f"Enter {name}'s Cunning 0-25:"))
            if 0 <= cunning <= 25:
                break
            else:
                eg.msgbox("Strength must be between 0 and 25.")
        verify = (
                f"Are you sure you want to add this monster?\n\n"
                f"Name: {name}\n"
                f"  Strength: {strength}\n"
                f"  Speed:    {speed}\n"
                f"  Stealth:  {stealth}\n"
                f"  Cunning:  {cunning}"
            )
            
        if eg.ynbox(verify, "Verify Monster"):
                Monsters[name] = {"Strength": strength, "Speed": speed, "Stealth": stealth, "Cunning": cunning}
                eg.msgbox(f"Monster '{name}' added successfully!")
        else:
                eg.msgbox("Monster not added.")

#Search and Edit cards
    elif choice == "Search/Change":
           
            output2 = ""
            for monster_id, info in Monsters.items():
                    output2 += f"Name: {monster_id}\n"
            search = eg.enterbox("Enter the name of the monster to search:\n\n" + output2, title="Search/Edit" )

            if search in Monsters:
                monster = Monsters[search]
                message = (
                    f"Name: {search}\n"
                    f"  Strength: {monster['Strength']}\n"
                    f"  Speed:    {monster['Speed']}\n"
                    f"  Stealth:  {monster['Stealth']}\n"
                    f"  Cunning:  {monster['Cunning']}\n"
                )
                eg.msgbox(message, "Monster Details")

                if eg.ynbox("Do you want to change this monster?", "Edit Monster"):
                    try:
                        # Strength Checking 
                        while True:
                            strength = int(eg.enterbox("Enter new Strength (0-25):", default=str(monster["Strength"])))
                            if 0 <= strength <= 25:
                                break
                            else:
                                eg.msgbox("Strength must be between 0 and 25.")

                        # Speed Checking
                        while True:
                            speed = int(eg.enterbox("Enter new Speed (0-25):", default=str(monster["Speed"])))
                            if 0 <= speed <= 25:
                                break
                            else:
                                eg.msgbox("Speed must be between 0 and 25.")

                        # Stealth Checking
                        while True:
                            stealth = int(eg.enterbox("Enter new Stealth (0-25):", default=str(monster["Stealth"])))
                            if 0 <= stealth <= 25:
                                break
                            else:
                                eg.msgbox("Stealth must be between 0 and 25.")

                        # Cunning Checking
                        while True:
                            cunning = int(eg.enterbox("Enter new Cunning (0-25):", default=str(monster["Cunning"])))
                            if 0 <= cunning <= 25:
                                break
                            else:
                                eg.msgbox("Cunning must be between 0 and 25.")

                        # save the monster 
                        Monsters[search] = {
                            "Strength": strength,
                            "Speed": speed,
                            "Stealth": stealth,
                            "Cunning": cunning
                        }
                        eg.msgbox("Monster updated successfully.", "Success")

                    except Exception:
                        eg.msgbox("Invalid input. Update cancelled.", "Error")
            else:
                eg.msgbox("Monster not found.")
# Delete Card
    elif choice == "Delete Card":
                
                output2 = ""
                for monster_id, info in Monsters.items():
                    output2 += f"Name: {monster_id}\n"

                delete = eg.enterbox(
                    "Enter the name of the Monster you want to delete:\n\n" + output2,
                    title="Delete"
                )

                if delete in Monsters:
                        if eg.ynbox(f"Are you sure you want to delete '{delete}'?", "Confirm Delete"):
                            del Monsters[delete]
                            eg.msgbox(f"'{delete}' monster deleted.")
                else:
                    eg.msgbox("Monster not found.")
# Exit 
    elif choice == "Exit":

         break
