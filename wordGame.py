import math
def wordGame():
    print("We will now play WordGame.")
    print("Please do not use this game to make fun of anyone for any reason.")
    
    userInput = input("Enter a word (or phrase): ")

    inputLen = len(userInput)
    centerIndex = math.floor(inputLen/2)
    oneFourthIndex = 0
    threeFourthIndex = 0

    print("For the word",userInput, "here are some other words:")

    print("Reverse:")
    print(userInput[::-1])

    print("Switching the front half and back half of the word:")
    frontHalf = userInput[0:centerIndex]
    backHalf = userInput[centerIndex:inputLen]
    newWord = backHalf + frontHalf
    print(newWord)
    print("")

    if(inputLen >= 4):
        print("We detected your word has a length of at least 4")
        print("Here's another word for you:")
        oneFourthIndex = math.floor(inputLen/4)
        threeFourthIndex = math.floor(inputLen/4*3)
        
        firstFourth = newWord[0:oneFourthIndex]
        secondFourth = newWord[oneFourthIndex:centerIndex]
        threeFourth = newWord[centerIndex:threeFourthIndex]
        fourFourth = newWord[threeFourthIndex:inputLen]

        newWord4 = secondFourth + fourFourth + firstFourth + threeFourth
        print(newWord4)
    
    print("Thank you for playing WordGame!")
    

    
    
