import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = high

        feedback = input(f"Is the number {guess}, too high(H), too low(L) or correct(C)?").lower()

        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1

    print(f"Congrats, the number {guess} is the correct number!")

computer_guess(1000)