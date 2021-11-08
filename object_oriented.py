import random
import string

import programming_language
from enum import Enum


class InheritanceType(Enum):
    SINGLE = 1,
    MULTIPLE = 2,
    INTERFACE = 3


class ObjectOriented(programming_language.ProgrammingLanguage):
    def __init__(self):
        self.name = ""

    def in_from_file(self, data):
        self.name = data[0]
        self.year_of_creation = int(data[1])
        self.index_tiobe = int(data[2])
        if data[3] == "Single":
            self.inheritance_type = InheritanceType.SINGLE
        elif data[3] == "Multiple":
            self.inheritance_type = InheritanceType.MULTIPLE
        else:
            self.inheritance_type = InheritanceType.INTERFACE

    def in_rnd(self):
        k = random.randrange(1, 15)
        self.name = ''.join(
            random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(k))
        self.year_of_creation = random.randrange(1950, 2021)
        self.index_tiobe = random.randrange(99)
        k = random.randrange(1, 3)
        if k == 1:
            self.inheritance_type = InheritanceType.SINGLE
        elif k == 2:
            self.inheritance_type = InheritanceType.MULTIPLE
        else:
            self.inheritance_type = InheritanceType.INTERFACE

    def __str__(self):
        return "Object-Oriented Programming Language: name = " + str(self.name) + ", yearOfCreation = " \
                 + str(self.year_of_creation) + \
                 ", indexTIOBE = " + str(self.index_tiobe) + ", inheritance_type = " + str(self.inheritance_type) + "\n"
