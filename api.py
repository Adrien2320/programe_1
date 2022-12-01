
def login():
    pass


def create_new_user():
    pass


def remove_user():
    pass




def show_main_menu() -> None:
    """affiche le principale de l'application"""

    print("Login and Password".center(100, "_"),
          "\n1. login:"
          "\n2. create new user:"
          "\n3. remove user:"
          "\n0. exit:"
          )
    
    match number_by_user():
        case 0:                                                                                   
            exit()                                                                                
            print("Au revoir")                                                                    
        case 1:                                                                                   
            login()                                                                               
        case 2:                                                                                   
            create_new_user()                                                                    
        case 3:                                                                                  
            remove_user()                                                                         
        case _:                                                                                   
            print("Le nombre entré n'est pas bon, veuillez entré un nombre compris entre 0 et 3.")
            show_main_menu()


def number_by_user() -> int:
    """Demande un nombre à l'utilisateur et return le nombre """
    prompt:str=""
    while not prompt.isdigit():
        prompt = input("choix:")

    return int(prompt)

if __name__ == '__main__':
    show_main_menu()



















