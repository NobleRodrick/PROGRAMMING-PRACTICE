import random


class Hat:

    houses = ["Gryffindor", "hufflepuff", "Ravenclaw", "Slytherine"]

    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))


Hat.sort("Harry")