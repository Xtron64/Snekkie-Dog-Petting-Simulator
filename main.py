restarts = 0
petCoin = 0


class user:
    @staticmethod
    def checkPetCoin():
        print("You have", petCoin, "PetCoins")


class dog:
    @staticmethod
    def pet():
        global petCoin
        print("You petted your dog. +1 petCoin")
        petCoin = petCoin + 1


def main():
    global restarts
    if restarts == 0:
        print("""Write "pet" to pet your dog. If you would like to view your PetCoins (you gain a petCoin each 
        time you pet your dog) write "petcoin" or "petcoins".""")
    else:
        print("What would you like to do?")
    choice = input("You: ")
    if choice.lower() == "pet" or "pet the dog" or "pet dog":
        dog.pet()
        restarts = restarts + 1
        main()
    elif choice.lower() == "petcoins" or "petcoins" or "check petcoin" or "check my petcoin":
        user.checkPetCoin()
        restarts = restarts + 1
        main()
    else:
        restarts = restarts + 1
        main()


if __name__ == '__main__':
    main()
