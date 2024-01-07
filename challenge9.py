# MODEL
#############################################################################################################
class User:

    def register_user(self) -> list:
        print('\033[34mREGISTER YOUR DATA INTO THE SYSTEM IN ORDER TO ACCESS THE MESSAGE: \033[m')
        email = str(input('Email address: ')).lower().strip()
        if not '@' in email: email += '@gmail.com'
        password = str(input('Password: '))
        data = [email, password]
        self._email = email
        self._password = password


# CONTROLLER
#############################################################################################################
class SecretText:

    def __init__(self) -> None:
        self._user = []

    def set_user(self, user: User) -> None:
        self._user.append(user)

    def text(self) -> str:
        if self.authenticator() == True:
            return f'\033[32mYOU HAVE WON ACCESS TO THE SECRET MESSAGE.\033[m'
        else:
            return f'\033[31mAUTHORIZATION DENIED.\033[m'

    def authenticator(self) -> bool:
        print('\033[34mNOW INSERT YOUR DATA IN ORDER TO ACCESS THE MESSAGE: \033[m')
        email = str(input('Email address: ')).lower().strip()
        if not '@' in email: email += '@gmail.com'
        password = str(input('Password: '))
        for user in self._user:
            if user._email == email and user._password == password:
                return True
        return False
    

# VIEW
#############################################################################################################
user1 = User()
user1.register_user()
secret_text = SecretText()
secret_text.set_user(user1)
message = secret_text.text()
print(message)