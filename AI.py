import random

class Vacuum:

    def __init__(self, row, column):
        
        self.row = row
        self.column = column
        self.matrix = [[random.randrange(0,2) for _ in range(self.column)] for _ in range(self.row)]
        self.location = [random.randrange(0, self.row), random.randrange(0, self.column)]
        self.end1 = self.location[0]
        self.end2 = self.location[1] - 1
        if self.end2 < 0:
            print("enB < 0!!!!")
            if self.end1 == 0:
                self.end1 = len(self.matrix) - 1
                self.end2 = len(self.matrix[0]) - 1
            else:
                self.end1 = self.location[0] - 1
                self.end2 = len(self.matrix[0]) - 1

    def status(self, mat, location):
        if mat[location[0]][location[1]] == 1:
            return False
        elif mat[location[0]][location[1]] == 0:
            return True

    
    def action(self):
        if self.location[0] == self.end1 and self.location[1] == self.end2:
            if not self.status(mat=self.matrix, location=self.location): #Dirty
                print('Dirty')
                self.matrix[self.location[0]][self.location[1]] = 0
                print(self.matrix)
                print(self.matrix)
                print("DONE !!!!")
        elif self.location[0] == 0 and self.location == 0:
            print(self.matrix)
            print("DOne!")

        else:
            if not self.status(mat=self.matrix, location=self.location): #Dirty
                print('Dirty')
                self.matrix[self.location[0]][self.location[1]] = 0
                print(self.matrix)
                print(40*"#")
                if self.location[1] < len(self.matrix[0]) - 1:
                    self.location[1] += 1
                    print('vacuum location >> ' + str(self.location[0]))
                    print('vacuum location >> ' + str(self.location[1]))

                    self.action()

                elif self.location[1] == len(self.matrix[0]) - 1:
                    if self.location[0] < len(self.matrix) - 1:
                        self.location[0] += 1
                        self.location[1] = 0
                        print('vacuum location >> ' + str(self.location[0]))
                        print('vacuum location >> ' + str(self.location[1]))
                        self.action()

                    elif self.location[0] == len(self.matrix) - 1:
                        self.location[0] = 0
                        self.location[1] = 0
                        print('vacuum location >> ' + str(self.location[0]))
                        print('vacuum location >> ' + str(self.location[1]))
                        self.action()

            elif self.status(mat=self.matrix, location=self.location):   #Clean
                print("Clean")
                print(self.matrix)
                print(40*"#")
                if self.location[1] < len(self.matrix[0]) - 1:
                    self.location[1] += 1
                    print('vacuum location >> ' + str(self.location[0]))
                    print('vacuum location >> ' + str(self.location[1]))
                    self.action()

                elif self.location[1] == len(self.matrix[0]) - 1:
                    if self.location[0] < len(self.matrix) - 1:
                        self.location[0] += 1
                        self.location[1] = 0
                        print('vacuum location >> ' + str(self.location[0]))
                        print('vacuum location >> ' + str(self.location[1]))
                        self.action()

                    elif self.location[0] == len(self.matrix) - 1:
                        self.location[0] = 0
                        self.location[1] = 0
                        print('vacuum location >> ' + str(self.location[0]))
                        print('vacuum location >> ' + str(self.location[1]))
                        self.action()


if __name__ == "__main__":
    print('Hi, I am a smart vacuum cleaner')
    print(40*' # ')
    row = int(input('Please enter the number of rows >> >>  '))
    column = int(input('Please enter the number of columns >> >>  '))
    print(40*' # ')
    vacuum = Vacuum(row = row, column = column)
    print('Matrix >> ' + str(vacuum.matrix))
    print(40*' # ')
    print('Location >> ' + str(vacuum.location))
    print(40*' # ')

    vacuum.status(mat=vacuum.matrix, location=vacuum.location)

    vacuum.action()