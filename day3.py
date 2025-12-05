from typing import Any
def max(l: list) -> int:
    if len(l) == 1: 
        return (l[0])
    else:
        if l[0] >= l[1]:
            return max( [l[0]]+l[2:] )
        else:
            return max( l[1:] ) 
# I am too tired to explain any of this
def calculateJoltage(numberList: list[int], maxLength: int) -> int:
    output = []
    firstDigit = max(numberList[:-(maxLength-1)])
    firstIndex = numberList[:-(maxLength-1)].index(firstDigit)
    output.append((firstDigit, firstIndex))
    counter = 0
    for i in range(maxLength-1,0,-1):
        print(f"index is {i}")
        if i == 1:
            digit = max(numberList[output[counter][1]+1:])
            digitIndex = numberList[output[counter][1]+1:].index(digit)+output[counter][1]+1
        else:
            print(f"start searching from {output[counter][1]}")
            print(f"{numberList[output[counter][1]+1:-(i-1)]}")
            digit = max(numberList[output[counter][1]+1:-(i-1)])
            digitIndex = numberList[output[counter][1]+1:].index(digit)+output[counter][1]+1
        output.append((digit, digitIndex))
        counter += 1
        print(f"output is {output}")
    finalNumber = ''.join([str(x[0]) for x in output])
    return int(finalNumber)

with open('day3-input.txt', 'r') as file:
    finalJoltage = []
    for line in file:
        numberList = [ int(x) for x in list(line.strip()) ]
        finalJoltage.append(calculateJoltage(numberList,12))
    print(finalJoltage)
    print(sum(finalJoltage))
       
