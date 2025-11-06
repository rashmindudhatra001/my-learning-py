class MathOperation:
    def add(self, *args):
        total = 0
        for num in args:
            total += num
        print("Sum is:", total)

obj = MathOperation()
obj.add(5)
obj.add(5, 10)
obj.add(5, 10, 15)
obj.add(1, 2, 3, 4, 5)
