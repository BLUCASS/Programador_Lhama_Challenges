# CONTROLLER
#############################################################################################################
class EmailSystem:

    def __init__(self, name, email) -> None:
        self.name = name.title().strip()
        self.email = email.lower().strip()

    def title(self):
        while True:
            try:
                title = str(input('Choose the subject: ')).strip().capitalize()
                for letter in title:
                    if not letter.isalpha() and not letter.isspace():
                        raise ValueError
            except:
                print('\033[31mONLY TYPE LETTERS (A-Z)\033[m')
            else:
                self.title = title
                break

    def text(self):
        text = str(input('Write the email: '))
        self.text = text
    
    def recipients(self):
        destiny = []
        while True:
            filter = str(input('Type a new destiny: ')).lower().strip()
            if not '@' in filter: filter += '@gmail.com'
            destiny.append(filter)
            resp = str(input('D you want to add a new destiny [Y/N]? ')).upper()[0]
            if resp != 'Y':
                self.recipients = destiny
                break

    def compose(self):
        for destiny in self.recipients:
            print(f'''\033[34m{"-="*30}\n\033[44m{"AUTOMATIC EMAIL SENDER":^60}\033[m\n\033[34m{"-="*30}\033[m\n
From: \033[34m{self.email}\033[m
To: \033[34m{destiny}\033[m
Subject: {self.title}\n
Text: {self.text}\n
Kind regards, 
{self.name}\n\n''')


# VIEW
#############################################################################################################
company = EmailSystem('test company', 'tests@gmail.com')
company.title()
company.recipients()
company.text()
company.compose()