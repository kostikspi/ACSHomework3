import random
import string
from enum import Enum
import programming_language


class Typing(Enum):
    PRINCIPAL = 1,
    DYNAMIC = 2


class Functional(programming_language.ProgrammingLanguage):
    def __init__(self):
        self.name = ""

    ##def __init__(self, index_tiobe, name, year_of_creation, typing_scheme, support_of_lazy_computations):
    ##    super().__init__(index_tiobe, name, year_of_creation)
    ##    self.typing_scheme = typing_scheme;
    ##    self.support_of_lazy_computations = support_of_lazy_computations;

    def in_from_file(self, data):
        self.name = data[0]
        self.year_of_creation = int(data[1])
        self.index_tiobe = int(data[2])
        if data[3] == "Principal":
            self.typing_scheme = Typing.PRINCIPAL
        else:
            self.typing_scheme = Typing.DYNAMIC
        self.support_of_lazy_computations = bool(data[4])

    def in_rnd(self):
        k = random.randrange(1, 15)
        self.name = ''.join(
            random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(k))
        self.year_of_creation = random.randrange(1950, 2021)
        self.index_tiobe = random.randrange(99)
        k = random.randrange(1, 2)
        if k == 1:
            self.typing_scheme = Typing.PRINCIPAL
        else:
            self.typing_scheme = Typing.DYNAMIC
        self.support_of_lazy_computations = bool(random.randrange(1))

    def __str__(self):
        return "Functional Programming Language: name = " + str(self.name) + ", yearOfCreation = " \
               + str(self.year_of_creation) + \
               ", indexTIOBE = " + str(self.index_tiobe) + ", typing scheme = " + str(self.typing_scheme) + \
               ", support of lazy computations = " + str(self.support_of_lazy_computations) + "\n"
