# MODEL
#############################################################################################################
class Place:

    def __init__(self, place, activity) -> None:
        self.place = place
        self.activity = activity


# CONTROLLER
#############################################################################################################
class TravelManager:

    def __init__(self, place1: Place, place2: Place, place3: Place) -> None:
        self.places = [place1, place2, place3]

    def choice(self):
        while True:
            try:
                print(f'\033[45m{"OPT":<5}{"PLACE":<30}{"ACTIVITY":<30}\033[m')
                print(f'{"1":<5}{self.places[0].place:<30}{self.places[0].activity:<30}')
                print(f'{"2":<5}{self.places[1].place:<30}{self.places[1].activity:<30}')
                print(f'{"3":<5}{self.places[2].place:<30}{self.places[2].activity:<30}')
                opt = int(input('Choose your option: '))
                assert opt >= 1 and opt <= 3
            except:
                print('\033[31mINVALID OPTION\033[m')
            else:
                return opt

    def chosen_activity(self):
        esc = self.choice()
        if esc == 1:
            print(f'Congratulations. You have chosen \033[32m{self.places[0].activity.lower()} in {self.places[0].place}\033[m')
        elif esc == 2:
            print(f'Congratulations. You have chosen \033[32m{self.places[1].activity.lower()} in {self.places[1].place}\033[m')
        elif esc == 3:
            print(f'Congratulations. You have chosen \033[32m{self.places[2].activity.lower()} in {self.places[2].place}\033[m')


# VIEW
#############################################################################################################
pe = Place('Pernambuco', 'To go to the beach')
rj = Place('Rio de Janeiro', 'To visit Cristo Redentor')
pr = Place('Parana', 'To climb mountains')
travel_manager = TravelManager(pe, rj, pr)
print(travel_manager.chosen_activity())