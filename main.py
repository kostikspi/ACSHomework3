import programming_language
import container
import sys


def print_error_message1():
    print("incorrect command line!\n"
          "  Waited:\n"
          "     command -f infile outfile01 outfile02\n"
          "  Or:\n"
          "     command -n number outfile01 outfile02\n")


def print_error_message2():
    print("incorrect qualifier value!\n"
          "  Waited:\n"
          "     command -f infile outfile01 outfile02\n"
          "  Or:\n"
          "     command -n number outfile01 outfile02\n")


def print_error_message3():
    print("incorrect number of languages. Set 0 < number <= 10000\n")


if len(sys.argv) != 5:
    print_error_message1()
    quit()
else:
    print("Start")
    container = container.Container()
    if sys.argv[1] == "-f":
        container.file_input(sys.argv[2])
    elif sys.argv[1] == "-n":
        if int(sys.argv[2]) < 1 | int(sys.argv[2]) > 10000:
            print_error_message3()
            quit()
        container.rnd_input(int(sys.argv[2]))
    else:
        print_error_message2()
        quit()
    container.out_in_file(sys.argv[3], 0)
    average_quotient = container.delete_elements_lower_than_average()
    container.out_in_file(sys.argv[4], average_quotient)
