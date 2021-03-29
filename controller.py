# TODO pour la semaine prochaine faire les liens entre la game loop et le front

from models import McGyver
from view import View
from extract_map import read_map
from constants import X_SIZE, Y_SIZE


class Controller:
    def __init__(self):
        self.view = View()
        self.mcGyver = McGyver(map=self.extract_map())
        self.items = []
        self.game_loop()

        # calls and initiates classes and methods

    def extract_map(self):
        map = read_map()
        self.view.map = map

        return map

        # use the map extraction method here

    def game_loop(self):

        self.items = self.view.display(self.mcGyver)

        while True:
            input = self.view.play_game()

            # a = self.mcGyver.move()
            if input:

                x = self.mcGyver.position.x
                y = self.mcGyver.position.y

                # self.view.display_remove(x, y)

                if self.mcGyver.move(input):
                    self.view.display_hero(self.mcGyver)
                    self.view.display_remove(x, y)

                for item in self.items:

                    if item == [self.mcGyver.position.x*X_SIZE,
                                self.mcGyver.position.y*Y_SIZE]:

                        self.mcGyver.items += 1
                        self.items.remove(item)

                if self.end_conditions(self.mcGyver):
                    self.view.stop_game()
                    break

    # make the calls to the view for display ex : self.view.display()
    # get the inputs self.view.handle_input()
    # collection of items
    # check the end condition

    def end_conditions(self, mcGyver):

        if (mcGyver.items == 3 and
            mcGyver.position.x == 13 and
                mcGyver.position.y == 1):
            print("you win")
            return True
        elif mcGyver.position.x == 13 and mcGyver.position.y == 1:
            print("you lose")
            return True

        else:
            return False

        # check the end condition


c = Controller()

c.game_loop()
