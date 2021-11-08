import cur as cur
import length as length
import switch as switch
from numpy import double

import programming_language
import procedural
import object_oriented
import functional
import random


class Container:
    length = 0
    cont = []

    def __init__(self):
        length = 0
        cont = list[length]

    def file_input(self, filename):
        with open(filename) as f:
            data = f.readlines()
            for i in range(len(data)):
                curr_data = data[i].split(' ')
                if curr_data[0] == "1":
                    procedural_language = procedural.Procedural()
                    curr_data.pop(0)
                    procedural_language.in_from_file(curr_data)
                    self.cont.append(procedural_language)
                    self.length += 1
                elif curr_data[0] == "2":
                    object_oriented_language = object_oriented.ObjectOriented()
                    curr_data.pop(0)
                    object_oriented_language.in_from_file(curr_data)
                    self.cont.append(object_oriented_language)
                    self.length += 1
                elif curr_data[0] == "3":
                    functional_language = functional.Functional()
                    curr_data.pop(0)
                    functional_language.in_from_file(curr_data)
                    self.cont.append(functional_language)
                    self.length += 1
        f.close()

    def rnd_input(self, number):
        for i in range(number):
            k = random.randrange(3)
            if k == 0:
                procedural_language = procedural.Procedural()
                procedural_language.in_rnd()
                self.cont.append(procedural_language)
                self.length += 1
            elif k == 1:
                object_oriented_language = object_oriented.ObjectOriented()
                object_oriented_language.in_rnd()
                self.cont.append(object_oriented_language)
                self.length += 1
            elif k == 2:
                functional_language = functional.Functional()
                functional_language.in_rnd()
                self.cont.append(functional_language)
                self.length += 1

    def delete_elements_lower_than_average(self) -> float:
        sum_of_elements = 0
        for i in range(len(self.cont)):
            sum_of_elements += (self.cont[i]).quotient()
        average_quotient = sum_of_elements / len(self.cont)
        new_cont = []
        for i in range(len(self.cont)):
            if self.cont[i].quotient() >= average_quotient:
                new_cont.append(self.cont[i])
        self.cont = new_cont
        return average_quotient
    
    def out_in_file(self, filename, average_quotient):
        with open(filename, "w+") as f:
            f.write("Filled container:\n")
            if average_quotient != 0:
                f.write("Average Quotient: " + str(average_quotient) + "\n")
            f.write("Container has " + str(len(self.cont)) + "elements\n")
            for i in range(len(self.cont)):
                f.write(str(self.cont[i]))
            f.close()









