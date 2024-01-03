# TO ADD A NEW ELEVATOR TO THE CHALLENGE 1

# MODEL
###############################################################################################################################
class Elevator:

    def __init__(self, id) -> None:
        self.__id = id
        self.__floor = 1

    def set_floor(self, floor):
        self.__floor = floor

    def get_floor(self):
        return self.__floor

    def check_id(self, id):
        return self.__id == id

    def get_id(self) -> int:
        return self.__id


# CONTROLLER
###############################################################################################################################
class ElevatorManager:

    def __init__(self, el1: Elevator, el2: Elevator) -> None:
        self.__elevators = [el1, el2]
        self.__floor = 1

    def filtering_floor(self, id: int, floor: int) -> None:
        if floor < 1 or floor > 15:
            return self.__error_message_floor()
        else:
            return self.__filtering_elevator(id, floor)
        
    def __filtering_elevator(self, id: int, floor: int) -> None:
        for elevator in self.__elevators:
            if elevator.check_id(id):
                return self.__change_floor(elevator, floor)
        return self.__error_message_elevator()

    def __change_floor(self, elevator, floor):
        elevator.set_floor(floor)
        return f'Elevator {elevator.get_id()} going to the {floor}° floor'
    
    def __error_message_elevator(self):
        return f'\033[31mPLEASE, INSERT A VALID ELEVATOR\033[m'

    def __error_message_floor(self) -> str:
        return f'\033[31mPLEASE, INSERT A VALID FLOOR\033[m'


# VIEW
###############################################################################################################################
try:
    print(f'\033[32;44m{"CUSTOMER PANEL":^32}\033[m\n[1] ELEVATOR 1\n[2] ELEVATOR 2')
    elevator = int(input('Choose your elevator: '))
    print(f'''\033[32;44m{"ELEVATOR PANEL":^32}\033[m
[01]   [02]   [03]   [04]   [05]
[06]   [07]   [08]   [09]   [10]
[11]   [12]   [13]   [14]   [15]''')
    floor = int(input('Choose your floor: '))
except:
    print('\033[31mPLEASE, INSERT A NUMBER.\033[m')
else:
    elevator1 = Elevator(1)
    elevator2 = Elevator(2)
    elevatorManager = ElevatorManager(elevator1, elevator2)
    answer = elevatorManager.filtering_floor(elevator, floor)
    print(answer)
