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
     
        name = eg.enterbox("Enter the name of the new Monster:")
        if name:
                strength = int(eg.enterbox(f"Enter {name}'s Strength 0-25:"))
                speed = int(eg.enterbox(f"Enter {name}'s Speed 0-25:"))
                stealth = int(eg.enterbox(f"Enter {name}'s Stealth 0-25:"))
                cunning = int(eg.enterbox(f"Enter {name}'s Cunning 0-25:"))

                Monsters[name] = {
                    "Strength": strength,
                    "Speed": speed,
                    "Stealth": stealth,
                    "Cunning": cunning
                }

                eg.msgbox(f"Monster '{name}' added successfully!")

    elif choice == "Search/Change":
        search = eg.enterbox("Enter the name of the combo to search:")
        if search in Monsters:
            combo = menu[search]
            message = f"Combo Name: {search}\n"
            for item, price in zip(combo["items"], combo["prices"]):
                message += f"  - {item}: ${price:.2f}\n"
            eg.msgbox(message, "Combo Details")
            if eg.ynbox("Do you want to change this combo?", "Edit Combo"):
                items = []
                prices = []
                for i in range(3):
                    item = eg.enterbox(f"Enter new item {i+1} name:", default=combo["items"][i])
                    price = eg.enterbox(f"Enter new price for {item}:", default=str(combo["prices"][i]))
                    try:
                        price = float(price)
                        items.append(item)
                        prices.append(price)
                    except:
                        eg.msgbox("Invalid price. Cancelling update.")
                        break
                else:
                    menu[search] = {"items": items, "prices": prices}
                    eg.msgbox("Combo updated successfully.")
        else:
            eg.msgbox("Monster not found.")

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
