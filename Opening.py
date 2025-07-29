import easygui as eg

choice = eg.buttonbox("Welcome to the Monster game.", "Selection", 
                          choices=["View Cards", "Add Card", "Search/Change", "Delete Card", "Exit"])