key = input()
count = int(input())
guesses = []


guessed = False
for i in range(count):
    guesses.append(input())


def compare(guess: str, target: str):
    output = ["-"] * len(target)

    for index, (guess_letter, target_letter) in enumerate(zip(guess, target)):
        if guess_letter == target_letter:
            output[index] = "G"
            target = target.replace(guess_letter, "-", 1)

    for index, (guess_letter, target_letter) in enumerate(zip(guess, target)):
        if guess_letter in target and output[index] == "-":
            output[index] = "Y"
            target = target.replace(guess_letter, "-", 1)

    return "".join(output).replace("-", "R")


for guess in guesses:
    if guessed:
        print("Game Over")
        continue

    if guess == key:
        guessed = True

    if len(guess) != len(key):
        print("Invalid Length")
        continue

    print(compare(guess, key))
