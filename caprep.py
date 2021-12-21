from abc import ABC, abstractmethod

job_title = ""


class Job(ABC):
    global job_title
    job_title = input("what is the users job title: ")


class User(Job):
    def __init__(self):
        self.first_name = input("\nWhat is the users first name: ")
        self.second_name = input("\nWhat is the users second name: ")

    def make_email(self):
        email = self.first_name + self.second_name + "@gmail.com"
        print("email is: ", email)


user = User()
user.make_email()
