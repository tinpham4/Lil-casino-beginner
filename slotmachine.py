import random

symbols = ['🍒', '🍇', '🍉', '💎', '7️⃣']

def playSlot(bank):
    print("\nSpinning the slot... (-$10)")
    bank -= 10

    a1 = random.choice(symbols)
    a2 = random.choice(symbols)
    a3 = random.choice(symbols)

    print(f"{a1} | {a2} | {a3}")

    if a1 == a2 == a3 == '7️⃣':
        print("🎉 JACKPOT! +$1000")
        bank += 1000
    elif a1 == a2 == a3:
        print("✨ Nice! Small prize! +$50")
        bank += 50
    else:
        print("Better luck next time!")

    print(f"💰 Current Balance: ${bank}")
    return bank
    
