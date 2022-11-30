def menu() -> None:

    # déclaration and assign
    flag: bool = False
    answer: int

    # initialise the terminal
    print(f"1. Login:")
    print(f"2. New Login:")
    print(f"3. Delete Login:")
    print(f"0. Close")

    # check if user is insert a good values
    while not flag:
        answer = input(":")
        if answer in [1,2,3,0]:
        #if answer == "1" or answer == "2" or answer == "3" or answer == "0":
            flag = True
        print(flag)

    # start the function depending on the answer of the user.
    match answer:
        case "1":
# function qui se connect sur un login
        case "2":
# function qui créer un nouvel utilisateur.
        case "3":
# function qui supprime un utilisateur.
        case _:
            exit()