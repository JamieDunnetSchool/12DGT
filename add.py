import easygui as eg  

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
