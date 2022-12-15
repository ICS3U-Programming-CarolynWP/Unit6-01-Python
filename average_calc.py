# !/usr/bin/env python3
# Created by: Carolyn Webster Pless
# Created on: 2022/12/14
# Generates 9 random numbers then uses a for loop to calculate
# the average. Uses arrays.

# To be able to generate random numbers
import random


def main():
    # Variables
    sum = 0
    counter = 0
    average = 0
    number_list = []
    MAX_NUM = 100
    MIN_NUM = 0
    MAX = 10

    # For loop to generate random numbers and add them to the list
    for counter in range(0, MAX):
        random_number = random.randint(MIN_NUM, MAX_NUM)
        print("Adding {} to the list".format(random_number))
        number_list.append(random_number)
    # Resetting the counter back to 0
    counter = 0
    map(int, number_list)
    # For loop to calculate the average
    for counter in range(0, MAX):
        sum += number_list[counter]
    average = sum / 10
    # Displaying the average to the user
    print("The average of all numbers is {}".format(average))


if __name__ == "__main__":
    main()
