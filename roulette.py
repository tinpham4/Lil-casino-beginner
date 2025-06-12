import random

def playRoulette(bank):
    print("\n🎡 Roulette - Red or Black (-$10)")
    bank -= 10

    userChoice = input("Pick a color (Red or Black): ")

    spinResult = random.choice(['red', 'black']).lower()

    print(f"The wheel spins... It's {spinResult.capitalize()}!")

    if userChoice == spinResult:
        print("🎉 You won! +$20")
        bank += 20
    else:
        print("Nice tried lil bro 🫵🏼🤡")
    
    print(f"💰 Balance: ${bank}")
    return bank

