# MODEL
#############################################################################################################
class Player:

    def __init__(self, name: str) -> None:
        self.name = name
        self.__pts = 0

    def set_pts(self, pts: int) -> None:
        self.__pts += pts

    def get_pts(self) -> int:
        return self.__pts


# CONTROLLER
#############################################################################################################
class Game:

    def __init__(self, p1: Player, p2: Player) -> None:
        self.players = [p1, p2]

    def choose(self):
        from random import choice
        options = ['Rock', 'Scissor', 'Paper']
        return choice(options)
    
    def play(self):
        play1 = self.choose()
        play2 = self.choose()
        if play1 == 'Rock' and play2 == 'Scissor' or play1 == 'Scissor' and play2 == 'Paper' or play1 == 'Paper' and play2 == 'Rock':
            self.players[0].set_pts(1)
            print(f'{self.players[0].name} chose \033[32m{play1}\033[m x {self.players[1].name} chose \033[31m{play2}\033[m')
            print(f'\033[32m{self.players[0].name} vwon.\033[m')
        elif play2 == 'Rock' and play1 == 'Scissor' or play2 == 'Scissor' and play1 == 'Paper' or play2 == 'Paper' and play1 == 'Rock':
            self.players[1].set_pts(1)
            print(f'{self.players[1].name} chose \033[32m{play1}\033[m x {self.players[0].name} chose \033[31m{play2}\033[m')
            print(f'\033[32m{self.players[1].name} won.\033[m')
        else:
            print(f'{self.players[0].name} chose \033[32m{play1}\033[m x {self.players[1].name} chose \033[32m{play2}\033[m')
            print('It is a tie.')

    def pts_balance_0(self) -> int:
        return self.players[0].get_pts()

    def pts_balance_1(self) -> int:
        return self.players[1].get_pts()


def name():
    while True:
        try:
            smth = str(input('Choose the first name: ')).strip().title()
            for letter in smth:
                if not letter.isalpha() and not letter.isspace():
                    raise ValueError
        except:
            print('Only letters are accepted.')
        else:
            return smth
    

# VIEW
#############################################################################################################
from time import sleep

player1 = Player(name())
player2 = Player(name())
game = Game(player1, player2)
while game.pts_balance_0() < 5 and game.pts_balance_1() < 5:
    game.play()
    sleep(2)
print(f'\033[43m{"FINAL SCORE":^50}\033[m')
print(f'{"PLAYER":<33}{"POINTS":<15}')
print(f'{player1.name:<35}{game.pts_balance_0():<15}')
print(f'{player2.name:<35}{game.pts_balance_1():<15}')