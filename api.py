import random

def get_chest_key(name_and_password_of_user: tuple) -> int:
    """cherche la clé de coffre lier au tuple name_and_password_of_user dans un dictionnaire"""
    # type and assign
    key: int = dict_login[name_and_password_of_user]
    # return of the chest key
    return key


def show_login_menu() -> None:
    """affiche le menu pour se connecter ."""
    # type and assign
    answer: tuple
    key: int
    # initiate the login menu
    print("connection a votre coffre".center(100, "_"),
          "\n")
    # assign answer with the select of the user
    answer = resquest_name_and_passwords()
    # check if the user's answer is found in the dict_login
    if answer in dict_login:
        #  get the chest key link with the user answer and start the chest menu
        key = get_chest_key(answer)
        show_chest_menu(key)
    else:
        #  show that the user answer is incorrect and return in the main menu
        print("mot de passe ou nom utilisateur incorrect, veuillez ressayez")
        show_main_menu()


def resquest_name_and_passwords() -> tuple:
    """ Demande à l'utilisateur, un nom et un mot de passe. Et le retourne sous un tuple (name,password)"""
    # type and assign
    name: str = input("nom utilisateur:")
    password: str = input("Mot de passe:")
    # return the user's answers into a tuple
    return name, password


def check_if_exist(name_and_password_user, dict_search: dict) -> bool:
    """Verify si le nom et le mot de passe exist déjà """
    # check if the user's answer exist in the dict_search
    if name_and_password_user in dict_search.keys():
        # the user's answer not exist in dict_search and return true
        return True
    else:
        # the user's answer exist in dict_search and return False
        return False


def create_key() -> int:
    """Créer une key aléatoire et unique"""
    # type and assign
    key: int = 0
    # check if the key exist in dict_chest and if yes new create
    while check_if_exist(key, dict_chest):
        key = random.randint(1, 1000)
    return key


def get_value()-> tuple :
    """demande a l'utilisateur un nom, login et un mot de passe. le return sous un tuple"""
    # initiate show
    print("ajout des données".center(100,"_"),
          "\n")
    # type and assign
    name : str = input("Nom:")
    login : str = input("speudo:")
    password : str = input("Mot de passe:")

    # return the values
    return name,login,password



def add_item_in_chest(key)->None:
    """ajoute une valeur dans le coffre de l'utilisateur"""
    # assign and type
    message : tuple = get_value()
    name : str = message[0]
    login : str = message[1]
    password : str = message[2]

    # add the datas in dict_chest
    dict_chest[key] = {name:(login,password)}
    print("enregistrement réussi")
    show_chest_menu(key)


def change_item_in_chest(key):
    """change une donnée dans le dict_chest"""
    # assign and type

    # initiate show
    print("modification des données".center(100,"_"),
          "\n")
    #
    show_the_data_names()





def show_chest_menu(key: int) -> None:
    """affiche le menu du coffre"""
    # type and assign

    # initiate the chest menu
    print("Coffre personnel".center(100,"_"),
          "\n"
          "\n 1.ajouter"
          "\n 2.modifier"
          "\n 3.supprimer"
          "\n 4.chercher"
          "\n"
          "\n 0.revenir en arrière"
          "\n")
    # start the sub menu select by user
    match number_by_user():
        case 0:
            show_main_menu()
        case 1:
            add_item_in_chest(key)
        case 2:
            change_item_in_chest(key)
        case 3:
            delete_item_in_chest(key)
        case 4:
            search_item_in_chest(key)
        case _:
            print("Le nombre entré n'est pas bon, veuillez entré un nombre compris entre 0 et 5.")
            show_chest_menu()



def show_create_new_user_menu() -> None:
    """ Affiche le menu creation utilisateur et le créer """
    # type and assign
    global dict_login
    global dict_chest
    name_pass: tuple
    # initiate the create new user menu
    print("création nouvelle utilisateur".center(100, "_"),
          "\n "
          )
    # assign name_password with the user's answer
    name_password = resquest_name_and_passwords()
    # check if the user's answer exist in dict_login
    if check_if_exist(name_password, dict_login):
        #  show that the name and password exist in dict_login and restart the create new user menu
        print("\n"
              "nom d'utilisateur existe déjà, Veuillez en trouver un autre!")
        show_create_new_user_menu()
    else:
        # type and assign key, create the new user and start the chest menu
        key = create_key()
        dict_login = {name_pass: key}
        dict_chest = {key : ""}
        show_chest_menu(key)


def show_remove_user_menu() -> None:
    """affiche le menu pour supprimer un utilisateur et le supprime"""
    # initiate the remove user menu
    print("suppression utilisateur".center(100, "_"),
          "\n")
    # type and assign
    name_password: tuple = resquest_name_and_passwords()
    key_chest: int = get_chest_key(name_password)
    # delete user in the dict_login
    del dict_login[name_password]
    del dict_chest[key_chest]
    # show that the account has been successfully delete and start the main menu
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
    # assign and type
    dict_login: dict = {('Adrien','1234'):999}
    dict_chest: dict = {}
    show_main_menu()
