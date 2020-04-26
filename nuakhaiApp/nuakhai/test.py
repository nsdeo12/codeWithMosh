from itertools import combinations


def commonPrefix(inputs):
    # Write your code here
    print("start")
    originalString = input("Enter a string:")
    substrings = [originalString[x:y] for x, y in combinations(
        range(len(originalString)+1, r=2)
    )]
    print(substrings)
