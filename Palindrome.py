#create a variable to store the string
word = str(input("Enter the word:"))

#creating a function for string reversal
def reverse(word):
    return word[::-1]

#palindrome function
def palindrome(word):
    reversal = reverse(word)
    
    if (word == reversal):
        return True
    return False

answer = palindrome(word)

#result
if answer == 1:
    print("The given word is a palindrome")
else:
    print("The given word is not a palindrome")
    