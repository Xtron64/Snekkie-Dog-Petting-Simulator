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
    # Find a way to store the amount of petcoins the player has as an integer


def entranceProcess():
    global petCoin
    # I don't know


def main():
    global restarts, commands_keywords, pet_keyword, petcoins_keyword, exit_keyword
    entranceProcess()
    if restarts == 0:
        print("""Write "pet" to pet your dog. If you would like to view your PetCoins (you gain a petCoin each 
        time you pet your dog) write "petcoin" or "petcoins", if you would like to leave write "exit".""")
    if restarts > 0:
        print("What would you like to do?")
    choice = input("You: ")
    if commands_keywords not in choice.lower():
        print("That's not a command")
        restarts = restarts + 1
        main()
    else:
        for pet_keyword in choice.lower():
            if "petcoins" and "petcoin" and petcoins_keyword not in choice.lower():
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


if __name__ == '__main__':
    main()
