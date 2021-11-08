import string
import random

import programming_language


class Procedural(programming_language.ProgrammingLanguage):
    def __init__(self, presence_of_adt, index_tiobe, name, year_of_creation):
        super().__init__(index_tiobe, name, year_of_creation)
        self.presence_of_adt = presence_of_adt

    def __init__(self):
        self.name = ""

    def in_from_file(self, data):
        self.name = data[0]
        self.year_of_creation = int(data[1])
        self.index_tiobe = int(data[2])
        self.presence_of_adt = bool(data[3])

    def in_rnd(self):
        k = random.randrange(1, 15)
        self.name = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(k))
        self.year_of_creation = random.randrange(1950, 2021)
        self.index_tiobe = random.randrange(99)
        self.presence_of_adt = bool(random.randrange(1))

    def __str__(self):
        return "Procedural Programming Language: name = " + str(self.name) + ", yearOfCreation = " \
               + str(self.year_of_creation) + \
               ", indexTIOBE = " + str(self.index_tiobe) + ", presenceOfADT = " + str(self.presence_of_adt) + "\n"
