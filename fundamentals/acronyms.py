def find_acronym():
    lookup = input(f"Enter a software acronym to look up:\n")

    found = False
    try:
        with open("acronyms.txt") as file:
            for line in file:
                if lookup in line:
                    print(line)
                    found = True
                    break
    except FileNotFoundError as e:
        print("File not found")
        return
    if not found:
        print("The acronym does not exist.")


def add_acronym():
    acronym = input(f"Enter an acronym to add.\n")
    definition = input(f"Enter a definition to add.\n")

    with open("acronyms.txt", "a") as file:
        file.write(acronym + " - " + definition + "\n")


def main():
    choice = input(f"Do you want to find(F) or add(A) an acronym?\n")
    if choice == "F":
        find_acronym()
    elif choice == "A":
        add_acronym()


main()
