
def show_main_menu() -> None:
    """affiche le menu principale de l'application """

    # initialise the terminal
    print(f"1. Login:")
    print(f"2. New user:")
    print(f"3. Delete user:")
    print(f"0. Close")

def check_user_anwser():
    """vérifie si l'utilisateur a entrer un bon bouton"""
    # déclaration and assign
    flag: bool = False
    answer: int

    # check if user is insert a good values
    while not flag:
        answer = input(":")
        if answer in [1, 2, 3, 0]:
            # if answer == "1" or answer == "2" or answer == "3" or answer == "0":
            flag = True
        print(flag)

def select_menu_selected_by_user():
    """ selectionne la demande de l'utilisateur"""
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