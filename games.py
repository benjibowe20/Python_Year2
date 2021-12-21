import sys


class fibonacci:
    def __init__(self):
        self.userinput = int(input("\nHow many numbers would you like to print: "))
        self.stored_num = 0
        self.count = 0

    def count(self):
        self.count = 0

    def calculate_fibonacci(self):
        a = 0
        b = 0
        c = 1
        for i in range(self.userinput):
            print(c, "\n")
            a = b
            b = c
            c = a + b
        self.stored_num = c

    def guess_number(self):
        guess = int(input("\nWhat is the next number in the sequence: "))
        if guess == self.stored_num:
            print("\nCorrect answer well done!")
            self.count = self.count + 1
        else:
            print("\nIncorrect answer, the correct answer was: ", self.stored_num)
        print("\nCorrect answers: ", self.count)


while 1:
    game = fibonacci()
    game.calculate_fibonacci()
    game.guess_number()
