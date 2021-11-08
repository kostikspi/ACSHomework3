class ProgrammingLanguage:
    name = ""
    index_tiobe = 0
    year_of_creation = 0

    def __init__(self):
        self.name = ""

    def __init__(self, index_tiobe, name, year_of_creation):
        self.index_tiobe = index_tiobe
        self.name = name
        self.year_of_creation = year_of_creation

    def quotient(self):
        return self.index_tiobe / len(self.name)
