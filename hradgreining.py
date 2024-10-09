letter = input()

if __name__ == "__main__":
    l = len(letter)
    yes = 0
    for i in range(0,l-2):
        if letter[i] == "C" and letter[i+1] == "O" and letter[i+2] == "V":
            yes += 1

    if yes != 0:
        print("Veikur!")
    else:
        print("Ekki veikur!")
