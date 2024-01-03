# TO CREATE A PROGRAM WHERE YOU HAVE AN ELEVATOR TO MOVE PEOPLE INSIDE A BUILDING

# MODEL
###############################################################################################################################
class Elevator:

    def __init__(self) -> None:
        self.__floor = 1

    def change_floor(self, floor: int) -> None: 
        if floor < 1 or floor > 15: return self.__error_message()
        self.__floor = floor
        return f'Elevator going to the {floor} floor'
    
    def __error_message(self) -> str:
        return f'\033[31mPLEASE, INSERT A VALID FLOOR\033[m'


# VIEW
###############################################################################################################################
try:
    elevator = Elevator()
    print(f'''\033[32;44m{"ELEVATOR PANEL":^32}\033[m
[01]   [02]   [03]   [04]   [05]
[06]   [07]   [08]   [09]   [10]
[11]   [12]   [13]   [14]   [15]''')
    floor = int(input('Choose your floor: '))
    print(elevator.change_floor(floor))
except:
    print('\033[31mPLEASE, INSERT A NUMBER.\033[m')