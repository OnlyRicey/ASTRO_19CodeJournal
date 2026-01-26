


class favorite_animal():

    def __init__(self, a_length, l_length, num_eyes, has_tail, is_furry):
        self.a_length = float(a_length)
        self.l_length = float(l_length)
        self.num_eyes = int(num_eyes)
        self.has_tail = bool(has_tail)
        self.is_furry = bool(is_furry)

    def traits_show(self):
        print("Arm Length:", self.a_length)
        print("Leg Length:", self.l_length)
        print("Number of Eyes:", self.num_eyes)
        print("Has a Tail:", 'yes ' if self.has_tail else 'no')
        print("Is Furry:", 'yes ' if self.is_furry else 'no')

my_favorite = favorite_animal(1.5, 2.0, 2, True, True)
my_favorite.traits_show()