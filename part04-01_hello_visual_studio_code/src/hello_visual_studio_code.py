while True:
    # Demander l'éditeur à l'utilisateur
    editor = input("Editor: ")
    
    # Convertir en minuscules pour ignorer la casse (majuscules/minuscules)
    editor_lower = editor.lower()
    
    if editor_lower == "visual studio code":
        print("an excellent choice!")
        break # Arrête la boucle
    elif editor_lower == "word" or editor_lower == "notepad":
        print("awful")
    else:
        print("not good")
# Write your solution here