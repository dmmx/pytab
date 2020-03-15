"""Dice Frequency. Returns frequency counts and total."""

import sys

def roll(ndice):
    freq = {}
    dice = [1 for i in range(ndice)]
    counter = 0
    score = 0
    print(f"dice = {dice}")

    while score < 6*ndice:

        counter += 1
        score = sum(dice)
        print(counter, score, dice)    
        
        if score in freq:
            freq[score] = freq[score] + 1
        else:
            freq[score] = 1

        for d in range(ndice):
            if dice[d] < 6:
                dice[d] += 1
                break
            else:
                dice[d] = 1

    return freq, counter


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Enter the number of dice you would like to roll")
        print("This program will return the frequency of the sum")
        print("of the dice rolled.")
        print()
        print("I.e., How often will you roll on 10 on three dice?")
        print()
        print("WARNING: This program can take a long time to run")
        print("for dice counts greater than 7.")
    else:
        dice_count = int(sys.argv[1])
        f, n = roll(dice_count)
        print(f"n = {n}")
        print(f"Frequencies = {f}")

