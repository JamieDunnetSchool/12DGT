import easygui as eg



search = eg.enterbox("Enter the name of the monster to search:", "Search/Edit")
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
