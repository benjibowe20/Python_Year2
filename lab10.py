
#   LAB 10 -> FIBONACCI GAME

#   KEY CONTENTS:
#   -ABSTRACT CLASSES
#   -TRY EXCEPT STATEMENTS
#   -GLOBAL VARIABLES


from abc import ABC, abstractmethod

wins = 0


class Game(ABC):

    def __init__(self):
        while True:
            try:
                self.userinput = int(input("\nPick any number: "))
                break
            except ValueError:
                print("\nPlease enter a whole number.")

        pass

    @abstractmethod
    def fibonacci_calculation(self):
        pass

    @abstractmethod
    def guess_number(self):
        pass


# noinspection PyGlobalUndefined
class Fibonacci_Game(Game):
    def fibonacci_calculation(self):
        num = 1
        count = 0
        a = 0
        b = 0
        global c
        c = 0
        for count in range(self.userinput):
            if count > 0:
                if c == 0:
                    c = 1
            print(num, " = ", c)
            a = b
            b = c
            c = a + b
            num = num + 1

    def guess_number(self):
        guess = int(input("\nWhat is the next number in the sequence: "))
        if guess == c:
            print("\nCongratulations you answered correctly.")
            global wins
            wins = wins + 1
        else:
            print("\nIncorrect answer, the correct answer was: ", c)


loop = True
while loop:
    run = Fibonacci_Game()
    run.fibonacci_calculation()
    run.guess_number()
    play = input("\nIf you would like to play again press 'y' if you would like to quit press 'n': ")
    if play == "n":
        print("\nYou have won", wins, "times.")
        loop = False
