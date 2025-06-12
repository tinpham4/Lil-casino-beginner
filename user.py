from slotmachine import playSlot
from roulette import playRoulette


def userMoney():
    user = int(input('Enter in the amount: $'))
    if user >= 1001:
        print("You're not that guy pal. Your budget is $1000.")
        return 1000
    elif user <= 9:
        print("What's the point of coming here, you goof.")
        return 0
    else:
        print(f"Welcome to our Casino fine shy, you have ${user} to gamble.")
        return user

def showMenu():
    print("\n🎰 Casino Menu 🎲")
    print("1. Slot Machine")
    print("2. Blackjack")
    print("3. Roulette")
    print("4. Exit")

bank = userMoney()

while bank >= 10:
    showMenu()
    choice = input("Pick a game (1/2/3): ")
    
    if choice == '1':
        bank = playSlot(bank)
    elif choice == '2':
        print("Sorry, the game is not available at the moment")
    elif choice == '3':
        bank = playRoulette(bank)
    elif choice == '4':
        break
    else:
        print("Invalid choice.")

print("\nThanks for playing!")


