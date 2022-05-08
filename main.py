restarts = 0
petCoin = 0
pet_keyword = "pet"
petcoins_keyword = ("petcoins" or "petcoin")
exit_keyword = ("exit" or "leave")
commands_keywords = (pet_keyword or petcoins_keyword or exit_keyword)


class user:
    @staticmethod
    def checkPetCoin():
        print("You have", petCoin, "PetCoins")


class dog:
    @staticmethod
    def pet():
        global petCoin
        print("You petted your dog. +1 PetCoin.")
        petCoin = petCoin + 1


def exitProcess():
    global petCoin
    with open("PetCoins.txt", "w") as f:
        f.write(str(petCoin))
        f.close()


def entranceProcess():
    global petCoin

    with open("PetCoins.txt", "w") as f:
        text_petCoins = int(f.self())
        f.close()
    petCoin = int(text_petCoins)
    print(petCoin)


def main():
    global restarts, commands_keywords, pet_keyword, petcoins_keyword, exit_keyword
    entranceProcess()
    if restarts == 0:
        print("""Write "pet" to pet your dog. If you would like to view your PetCoins (you gain a petCoin each 
        time you pet your dog) write "petcoin" or "petcoins", if you would like to leave write "exit".""")
    if restarts > 0:
        print("What would you like to do?")
    if restarts >= 100:
        print("""Please consider taking a break. You can use the exit command by responding with "exit" to save and 
        "quit", "leave" or "exit". What would you like to do?""")
    choice = input("You: ")
    if commands_keywords not in choice.lower():
        print("That's not a command")
        restarts = restarts + 1
        main()
    for commands_keywords in choice.lower():
        for pet_keyword in choice.lower():
            if "petcoin" not in choice.lower():
                dog.pet()
                restarts = restarts + 1
                main()
            else:
                user.checkPetCoin()
                restarts = restarts + 1
                main()
        for petcoins_keyword in choice.lower():
            user.checkPetCoin()
            restarts = restarts + 1
            main()
        for exit_keyword in choice.lower():
            if pet_keyword or petcoins_keyword in choice:
                print("Only use the exit command on its own. Don't use it alongside or in combination with other "
                      "commands.")
                restarts = restarts + 1
                main()
            else:
                exitProcess()


if __name__ == '__main__':
    main()
