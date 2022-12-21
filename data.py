class Vault:
    """simple vault class"""
    pass


class User:
    """simple user class"""

    def __init__(self, login: str, password: str) -> None:
        """
        Constructor
        :param login: login of user (mus be unique)
        :param password: password of user
        """
        self.login: str = login
        self.password: str = password
        self.vault = Vault()

    def verify_password(self, password: str) -> bool:
        """
        check password
        :param password: password to check
        :return: true if password is valid
        """
        return password == self.password

    def __str__(self) -> str:
        """
        magic method
        :return: string password
        """
        return f"user login = {self.login}, user password = {self.password}"


if __name__ == "__main__":
    user = User("Toto", "1234")

    pwd = input("entrer your password")
    print(user.verify_password(pwd))

    print(user)
