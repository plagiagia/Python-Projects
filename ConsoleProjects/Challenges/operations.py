class Operations:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        self.operations = 0
        self.results = [self.n1]
        self.next_step = []

    def reached(self):
        if self.n2 in self.results:
            return -1
        else:
            return 0

    def step(self, num):
        subtract = num - 1
        mul = num * 2
        temp = []

        if self.n2 >= subtract >= 0:
            temp.append(subtract)

        if self.n2 >= mul >= 0:
            temp.append(mul)

        return temp

    def calculate_operations(self):
        while self.reached() == 0:
            self.operations += 1
            for each in self.results:
                self.next_step.extend(self.step(each))

            self.results = self.next_step
            self.next_step = []
        return self.operations


a = Operations(6, 20)
calc = a.calculate_operations()
print(f"Number of calculations to go from {a.n1} to {a.n2} are {calc}")
