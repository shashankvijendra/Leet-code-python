## Use just for testing purposes 


def sample(input, target):
    for i,j in enumerate(input):
        if target - j in input:
            return [i, input.index(target - j)]

lst = [3,2,4]
target = 9
print(sample(lst, target))