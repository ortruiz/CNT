class Assignment2:

    age = 0

    # Task 1 (Constructor)
    def __init__(self, age):
        self.age = age

    # Task 2 (Welcome)
    def sayWelcome(self, name):
        print("Welcome to the assignment,",name,"!   Haven't seen you for",self.age,"years!")

    # Task 3(List)
    def doubleList (self, input):
        for i,item in enumerate(input):
            input[i] += item
        return input







