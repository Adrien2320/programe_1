import random

# variable global
dict_login: dict = {("Adrien", "1234"): 600}
dict_chest: dict = {600:"Biére"}

def get_chest_key(name_and_password_of_user: tuple)-> int:
    """cherche la clé de coffre lier a le typle name_and_password_of_user dans un dictionnaire"""
    # type and assign
    key: int = dict_login[name_and_password_of_user]
    return key

def show_login_menu() -> None:
    """affiche le menu pour se connecter et se connect sur le coffre de l'utilisateur."""
    # type and assign
    answer: tuple
    key: int
    # initiate the login menu
    print("connection a votre coffre".center(100, "_"),
          "\n")
    #
    answer = resquest_name_and_passwords()
    if answer in dict_login:
        key = get_chest_key(answer)
        show_chest_menu(key)
    else:
        print("mot de passe ou nom utilisateur incorrect, veuillez ressayez")
        show_main_menu()

def resquest_name_and_passwords() -> tuple:
    """ Demande à l'utilisateur, un nom et un mot de passe. Et le retourne sour un tuple (name,password)"""
    name: str = input("nom utilisateur:")
    password: str = input("Mot de passe:")
    return name, password


def check_if_exist(name_and_password_user, dict_search: dict) -> bool:
    """Verify si le nom et le mot de passe exist déjà """
    if name_and_password_user in dict_search:
        return True
    else:
        return False


def create_key() -> int:
    """Crée une key aléatoire et unique"""
    key: int = 0
    while check_if_exist(key, dict_chest):
        key = random.randint(1, 1000)
    return key


def show_chest_menu(key: int) -> None:
    pass

# todo créer le menu pour le coffre dans la function show_chest_menu

def show_create_new_user_menu() -> None:
    """ Affiche le menu creation utilisateur et le crée """
    # type and assign
    global dict_login
    name_pass: tuple
    #
    print("création nouvelle utilisateur".center(100, "_"),
          "\n "
          )

    name_pass = resquest_name_and_passwords()
    if check_if_exist(name_pass, dict_login):
        print("\n"
              "nom d'utilisateur existe déjà, Veuillez en trouver un autre!")
        show_create_new_user_menu()
    else:
        key = create_key()
        dict_login = {name_pass: key}
        show_chest_menu(key)


def show_remove_user_menu() -> None:
    """affiche le menu pour supprimer un utilisateur et le supprime"""
    # initiate the remove user menu
    print("suppression de votre compte".center(100,"_"),
          "\n")
    #type and assign
    name_password : tuple = resquest_name_and_passwords()
    key_chest : int = get_chest_key(name_password)
    del dict_login[name_password]
    del dict_chest[key_chest]
    print("votre compte, a bien été supprimer"
          "\n au revoir")
    show_main_menu()

def show_main_menu() -> None:
    """affiche le principale de l'application"""

    # initiate the show of main menu.
    print("enregistrement de mots de passe".center(100, "_"),
          "\n"
          "\n1. connexion"
          "\n2. creation nouvelle utilisateur"
          "\n3. supprimer utilisateur"
          "\n"
          "\n0. quitter"
          )

    # check if user is selected a good button and start the menu selected.
    match number_by_user():
        case 0:
            exit()
            print("Au revoir")
        case 1:
            show_login_menu()
        case 2:
            show_create_new_user_menu()
        case 3:
            show_remove_user_menu()
        case _:
            print("Le nombre entré n'est pas bon, veuillez entré un nombre compris entre 0 et 3.")
            show_main_menu()


def number_by_user() -> int:
    """Demande un nombre à l'utilisateur et return le nombre """
    # type and assign.
    prompt: str = ""
    # check if the enter number is a number or not.
    while not prompt.isdigit():
        prompt = input("choix:")
    # return the select number by user.
    return int(prompt)


if __name__ == '__main__':
    show_main_menu()
