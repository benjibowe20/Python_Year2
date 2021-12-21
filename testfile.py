import unittest

class checkfile(unittest.TestCase):
    def test_int_test_float(self):
        self.userinput = input("What is the file name you wish to check: ")

    def openfile(self):
        self.testingfile = open(self.userinput, 'r')

    def test_mean(self):
        self.stats.append(4)

    def closefile(self):
        self.testingfile.close()


if __name__ == "__main__":
    unittest.main()



