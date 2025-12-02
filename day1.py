# Let's remember class syntax ;w;
class Dial:
    # init: the dial's value (what it's pointing at)
    #       the overflows (how many time it's passed 0)
    def __init__(self, startingValue):
        self.value = startingValue
        self.overflows = 0
    # method to rotate dial
    # this would be way tidier if I got rid of the counter logic from below
    # oh well
    def rotate(self, input):
        if input[0] is 'L':
            rotation = -int(input[1:])
        elif input[0] is 'R':
            rotation = int(input[1:])
        else:
            return TypeError
        self.value += rotation
        if self.value > 100:
            self.overflows += abs(self.value // 100) 
            if self.value % 100 == 0:
                self.overflows -= 1
        if self.value < 0:
            self.overflows += abs(self.value // 100) 
            if self.value - rotation == 0:
                self.overflows -= 1
        self.value = self.value % 100

northPoleDial = Dial(50)
counter = 0
with open('day1-input.csv', 'r') as inputData:
    for line in inputData:
        northPoleDial.rotate(line)
        print(northPoleDial.value)
        if northPoleDial.value == 0:
            counter += 1
print(f"The original password is {counter}")
print(f"and the new method has password {northPoleDial.overflows+counter}")