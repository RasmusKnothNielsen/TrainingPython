def isPalindrome(string):
    if len(string) <= 1:
        return True

    else:
        return string[0] == string[-1] and isPalindrome(string[1:-1])


userInput = input("Please enter a sequence to check if it is an palindrome: ")
answer = isPalindrome(userInput)
print("Is '" + userInput + "' an palindrome? " + str(answer))