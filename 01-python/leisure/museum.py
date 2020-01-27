

artists=["Rodin", "Van Gogh", "Pollack", "Miró "]

def draw_museum():
    print("Welcome to the Boston University Computer Science Museum")
    
    print("\n\n")
    for artist in artists:
        printFrame();
        print(artist)
        print()
    print("\n\n")

    return



def printFrame(width=10, height=10):
    for i in range(width):
        print("=",end="")
    print()
    middleString = "|"
    for i in range(width - 1):
        middleString=middleString + " "
    middleString+= "|"
    for i in range(height):
        print(middleString)
    for i in range(width):
        print("=",end="")
    print()
    return