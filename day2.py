## part 1
def numberTwins(min, max):
    evenLength = [ str(n) for n in range(min, max+1) if len(str(n)) % 2 == 0 ]
    twins = [ n for n in evenLength if n[:len(n)//2] == n[len(n)//2:] ]
    return twins

## part 2 :(
def factors(n):
    return [ f for f in range(1,n) if n % f == 0 ]

# to check if a bunch of substrings (split up into factor pieces) are equal
def subStringsEqual(s, factor):
    chunks = []
    for i in range(0, len(s), factor):
        chunks.append(s[i:i+factor])
    boolList = [x == chunks[0] for x in chunks]
    f = lambda acc, x: acc & x
    acc = True; [acc := acc & x for x in boolList]
    return acc

def numberQuinzuplets(min, max):
    twins = []
    for n in range(len(str(min)), len(str(max))+1):
        rightLength = [str(x) for x in range(min,max+1) if len(str(x)) == n ]
        for f in factors(n):
            twins += [ x for x in rightLength if subStringsEqual(x, f)]
    return twins

with open('day2-input.txt', 'r') as input:
    for line in input:
        # so legible
        idRanges = [ list(map(lambda a: int(a), x)) for x in  list(map(lambda a: a.split('-'), line.split(','))) ]

invalidIDs = [ numberQuinzuplets(l[0], l[1]) for l in idRanges ]
# squishing a list of lists!!
invalidIDs = [ int(x) for xs in invalidIDs for x in xs ]
print(f"the sum is {sum(set(invalidIDs))}")