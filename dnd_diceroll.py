import random

print(' ')
print('Welcome to DnD Diceroller')
print(' ')
print('Instructions:')
print('Enter a d4,d6,d8,d10,d12,d100,or d20 plus/minus any modifier (example: d20+4)')
print('To roll multiple dice, add the number before the dice (ex. 2d20)')
print("To roll with advantage or disadvantage start roll with 'adv' or 'dis'")
print("For example: 'adv2d20+4'")
print("Enter 'x' to exit the diceroller")
print(' ')

def roll_dice(num,type):
    roll_dice.rolls = []

    for x in range(0,num):
        if type not in [4,6,8,10,12,20,100]:
            print('Not valid. Dice must be a d4,d6,d8,d10,d12,d100,or d20')
            break

        else:
            roll_dice.rolls.append(random.randint(1,type))


def main():
    while True:

        roll_input = input("Enter roll: ")


        if roll_input.lower() == "x":
            print('Thank you for using DnD diceroller! Goodbye.')
            break

        else:

            mod = 0
            dice = roll_input
            result = 0

            for x in roll_input:
                if x == "+":
                    mod += int(roll_input.split("+")[1])
                    dice = roll_input.split("+")[0]

                elif x == "-":
                    mod -= int(roll_input.split("-")[1])
                    dice = roll_input.split("-")[0]
                else:
                    pass

            if dice[0].isnumeric() == False:
                if dice[0:3].lower() == "dis":
                    dice = dice.split("dis")[1]

                    roll_dice(int(dice.split("d")[0]),int(dice.split("d")[1]))
                    rolls = roll_dice.rolls
                    result = min(rolls)

                elif dice[0:3].lower() == "adv":
                    dice = dice.split("adv")[1]

                    roll_dice(int(dice.split("d")[0]),int(dice.split("d")[1]))
                    rolls = roll_dice.rolls
                    result = max(rolls)

                else:
                    roll_dice(1,int(dice.split("d")[1]))
                    rolls = roll_dice.rolls
                    result = rolls[0]

            else:
                roll_dice(int(dice.split("d")[0]),int(dice.split("d")[1]))
                rolls = roll_dice.rolls
                result = sum(rolls)

            total = result+mod

            print("{rolls}+{mod}={total}".format(rolls=rolls,mod=mod,total=total))

            continue



if __name__ == "__main__":
    main()
