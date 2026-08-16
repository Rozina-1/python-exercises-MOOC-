while True:
    editor = input("Editor: ")
    
    if editor.lower() == "visual studio code":
        print("an excellent choice!")
        break
    
    # Notice we repeat 'editor.lower() ==' for both!
    elif editor.lower() == "notepad" or editor.lower() == "word":
        print("awful")
        
    else:
        print("not good")