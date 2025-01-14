# using random
import random


def testing_random():
    values = [1, 2, 3, 4]
    print(random.choice(values))
    print(random.choice(values))
    print(random.choice(values))
    print(random.sample(values, 2))
    print(random.sample(values, 3))

    # shuffle the list randomly
    random.shuffle(values)
    print(values)

    # generate random number ranging (0, 10)
    print(random.randint(0, 10))
    print(random.randint(0, 10))


if __name__ == "__main__":
    testing_random()
