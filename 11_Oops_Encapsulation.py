class person:
    def __hello(self):
        print("I am showing")

    def welcome(self):
        self.__hello()


p1 = person()
print(p1.welcome())
