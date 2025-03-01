class Player:
    def __init__(self, name, token):
        self.validate_input(name,token)
        self.__name = name
        self.__token = token

    def validate_input(self, name, token):
        if not name:
            raise ValueError("Wrong input, Please enter your name🌚🌚🌚: ")

        if not token:
            raise ValueError("Please Enter your Token🌚🌚🌚: ")

    def get_name(self):
        return self.__name

    def get_token(self):
        return self.__token

    def __str__(self):
        return f" Name = {self.__name}\n Token = {self.__token}"