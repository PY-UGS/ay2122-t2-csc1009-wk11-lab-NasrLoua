class Calculator:

    def adder(self, x, y):
        print(x + y)

    def subtractor(self, x, y):
        print(x - y)

    def multiplier(self, x, y):
        print(x * y)

    def divider(self, x, y):
        print(x / y)

    def clear(self):
        return print(0)


obj = Calculator()
x = input("Please enter the first value: ")
y = input("\nPlease enter the second value: ")

obj.adder(int(x), int(y))
obj.subtractor(int(x), int(y))
obj.multiplier(int(x), int(y))
obj.divider(int(x), int(y))
obj.clear()
