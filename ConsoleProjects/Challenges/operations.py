class Operations:
    """
    A class that calculates the operations needed to reach from a specific number to another,
    doing only two operations: multiplication with 2 or subtraction with 1.
    """

    def __init__(self, n1: int, n2: int):
        """
        :param n1: A random integer number to begin with
        :param n2: A random integer number to end with.

        operations: A placeholder to save the number of operations to perform.
        results: A list to save the results of the operations and look for the n2
        next_step: A temporary list to save the next branch of operations
        """
        self.n1 = n1
        self.n2 = n2
        self.operations = 0
        self.results = [self.n1]
        self.next_step = []

    def reached(self):
        """
        Checks if we reach the number we have as target
        :return: -1 if we reached the target, else 0
        """
        if self.n2 in self.results:
            return -1
        else:
            return 0

    def step(self, num: int):
        """
        :param num: An integer number
        :return: A list with the results of the operations on num
        """
        subtract = num - 1
        mul = num * 2
        temp = []

        if subtract >= 0:
            # Don't save in the list numbers smaller than 0
            temp.append(subtract)

        temp.append(mul)

        return temp

    def calculate_operations(self):
        """
        Here we calculate the number of operations needed to reach the target number.
        :return: The number of operations
        """
        while self.reached() == 0:
            self.operations += 1

            for each in self.results:
                # for each number in results
                for i in self.step(each):
                    # for each result from the previous numbers
                    # calculate the next step and append it to the list
                    self.next_step.append(i)
            # Change the lists
            self.results = self.next_step
            # Reset the temp list
            self.next_step = []
        return self.operations


a = Operations(6, 7)
calc = a.calculate_operations()
print(f"Number of calculations to go from {a.n1} to {a.n2} are {calc}")

