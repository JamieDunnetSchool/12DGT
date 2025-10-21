"""Dose the let user look and edit the monster cards cataloge."""
import easygui as eg

Serch_Editing_Title = "Search/Edit"
Del_Titile = "Delete"
Add_Title = "Add Monster Card"
Selection_Titile = "Main Menu"
Edit_title = "Edit Cards"
Error_title = "Error"
View_Title = "View Catalouge"
Error_Mesage = "Input Error"
min = 1
max = 25

# Monsters Dictornary
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


def main_menu():
    """Return the Allows the user to pick what they want to do."""
    choice = eg.buttonbox(
        "Welcome to the Monster game what would you like to do.",
        Selection_Titile, choices=["View Cards", "Print Cards", "Add Card",
                                   "Search/Change", "Delete Card", "Exit"])
    # Funtions to go to the part of code we need.
    if choice == "View Cards":
        view()
    elif choice == "Print Cards":
        print_monsters()
    elif choice == "Add Card":
        add()
    elif choice == "Search/Change":
        search_edit()
    elif choice == "Delete Card":
        delete()
    elif choice == "Exit":
        exit()


def print_monsters():
    """Print all monstrs to the terainal."""
    output = ""
    for monster_id, info in Monsters.items():
        output += (
            f"\nName: {monster_id}\n"
            f"  Strength: {info['Strength']}\n"
            f"  Speed:    {info['Speed']}\n"
            f"  Stealth:  {info['Stealth']}\n"
            f"  Cunning:  {info['Cunning']}\n"
        )
    print(output)
    main_menu()


def view():
    """Return the allows the users to view the cards in a easy gui box."""
    output = ""
    # For how much mosters we have it will print the each one till finshed.
    for monster_id, info in Monsters.items():
        output += (
            f"\nName: {monster_id} \n"
            f"  Strength: {info['Strength']}\n"
            f"  Speed:    {info['Speed']}\n"
            f"  Stealth:  {info['Stealth']}\n"
            f"  Cunning:  {info['Cunning']}\n"
        )
    eg.msgbox(output or "No monsters yet.", View_Title)
    main_menu()


def add():
    """Return the allows the user add cards to the dictornary."""
    while True:
        name = eg.enterbox("Enter the name of the new Monster:", Add_Title)
        
        # If user cancels or closes
        if name is None:
            main_menu()
            return
        # If user enters nothing
        if name.strip() == "":
            eg.msgbox("You must enter a monster name.", Error_Mesage)
            continue
        # If the name already is in the dictionary
        if name in Monsters:
            eg.msgbox("That name is already taken. Please pick a new one.",
                      Error_Mesage)
            continue
        
        # Valid name
        break
    try:
        while True:
            # Chose all the stats for the monster
            strength = eg.integerbox(f"Enter {name}'s Strength between "
                                    + str(min) + " and " + str(max) + ".")
            # Limitng inbetween the max and the min
            if min <= strength <= max:
                break
            else:
                eg.msgbox("Strength must be between " + str(min)
                        + " and " + str(max) + ".", Error_Mesage)
        while True:
            speed = eg.integerbox(f"Enter {name}'s Speed between "
                                + str(min) + " and " + str(max) + ".")
            # Limitng inbetween the max and the min
            if min <= speed <= max:
                break
            else:
                eg.msgbox("Speed must be between " + str(min)
                        + " and " + str(max) + ".", Error_Mesage)
        while True:
            stealth = eg.integerbox(f"Enter {name}'s Stealth between "
                                    + str(min) + " and " + str(max) + ".")
            # Limitng inbetween the max and the min
            if min <= stealth <= max:
                break
            else:
                eg.msgbox("Stelth must be between " + str(min)
                        + " and " + str(max) + ".", Error_Mesage)
        while True:
            cunning = eg.integerbox(f"Enter {name}'s Cunning between "
                                    + str(min) + " and " + str(max) + ".")
            # Limitng inbetween the max and the min
            if min <= cunning <= max:
                break
            else:
                eg.msgbox("Cunning  must be between " + str(min)
                        + " and " + str(max) + ".", Error_Mesage)
                # Verifying id the user wants to put them info in
    except Exception:
        eg.msgbox("Invalid input. Update cancelled.", Error_title)
    verify = (
            f"Are you sure you want to add this monster?\n\n"
            f"Name: {name}\n"
            f"  Strength: {strength}\n"
            f"  Speed:    {speed}\n"
            f"  Stealth:  {stealth}\n"
            f"  Cunning:  {cunning}"
        )

    if eg.ynbox(verify, "Verify Monster"):
        Monsters[name] = {"Strength": strength, "Speed": speed,
                          "Stealth": stealth, "Cunning": cunning}
        eg.msgbox(f"Monster '{name}' added successfully!")
    else:
        eg.msgbox("Monster not added.")
    main_menu()


def search_edit():
    """Return the allows the user to edit and search cards."""
    output2 = ""
    for monster_id, info in Monsters.items():
        output2 += f"Name: {monster_id}\n"
    search = eg.enterbox("Enter the name of the monster to search:\n\n"
                         + output2, Serch_Editing_Title)
        # If user enters nothing
    if search.strip() == "":
        eg.msgbox("You must enter a monster name.", Error_Mesage)
    
    # Checking if the moster they searched is in the dictorneary.
    elif search in Monsters:
        monster = Monsters[search]
        message = (
            f"Name: {search}\n"
            f"  Strength: {monster['Strength']}\n"
            f"  Speed:    {monster['Speed']}\n"
            f"  Stealth:  {monster['Stealth']}\n"
            f"  Cunning:  {monster['Cunning']}\n"
        )
        # Askeing if they want to edit the monster
        if eg.ynbox(message + "\n Do you want to change this monster?",
                    Edit_title):
            try:
                # Strength Checking
                while True:
                    strength = eg.integerbox("Enter new Strength between " +
                                             str(min) + " and " + str(max)
                                             + ".",
                                             default=str(monster["Strength"]))
                    # Limitng inbetween the max and the min
                    if min <= strength <= max:
                        break
                    else:
                        eg.msgbox("Strength must be between " + str(min)
                                  + " and " + str(max) + ".", Error_Mesage)

                # Speed Checking
                while True:
                    speed = eg.integerbox("Enter new Speed between " + str(min)
                                          + " and " + str(max) + ".",
                                            default=str(monster["Speed"]))
                    # Limitng inbetween the max and the min
                    if min <= speed <= max:
                        break
                    else:
                        eg.msgbox("Speed must be between " + str(min)
                                  + " and " + str(max) + ".", Error_Mesage)

                # Stealth Checking
                while True:
                    stealth = eg.integerbox("Enter new Stealth between "
                                            + str(min)
                                            + " and " + str(max) + ".",
                                            default=str(monster["Stealth"]))
                    # Limitng inbetween the max and the min
                    if min <= stealth <= max:
                        break
                    else:
                        eg.msgbox("Stealth must be between " + str(min)
                                  + " and " + str(max) + ".", Error_Mesage)

                # Cunning Checking
                while True:
                    cunning = eg.integerbox("Enter new Cunning between "
                                            + str(min)
                                            + " and " + str(max) + ".",
                                            default=str(monster["Cunning"]))
                    # Limitng inbetween the max and the min
                    if min <= cunning <= max:
                        break
                    else:
                        eg.msgbox("Cunning must be between " + str(min)
                                  + " and " + str(max) + ".", Error_Mesage)

                # Save the monster
                Monsters[search] = {
                    "Strength": strength,
                    "Speed": speed,
                    "Stealth": stealth,
                    "Cunning": cunning
                }
                eg.msgbox("Monster updated successfully.", "Success")

            except Exception:
                eg.msgbox("Invalid input. Update cancelled.", Error_title)
    else:
        eg.msgbox("Monster not found.")
    main_menu()


def delete():
    """Return the allows the user to delete cards from the ditronery."""
    output2 = ""
    for monster_id, info in Monsters.items():
        output2 += f"Name: {monster_id}\n"
    
    while True: 
        delete = eg.enterbox(
            "Enter the name of the Monster you want to delete:\n\n"
            + output2, Del_Titile
        )
        # Confrimation if they would like to deleat the monster
    
        if delete in Monsters:
            if eg.ynbox(f"Are you sure you want to delete '{delete}'?",
                        Del_Titile):
                del Monsters[delete]
                eg.msgbox(f"'{delete}' monster deleted.")
        elif delete is None:
            main_menu()
            return
        elif delete.strip() == "":
                eg.msgbox("You must enter a monster name.", Error_Mesage)
                continue
        else:
            eg.msgbox("Monster not found.")

        main_menu()


def exit():
    """Return the user to Exit the program."""
    eg.msgbox("Have a good day.")
    quit


main_menu()
