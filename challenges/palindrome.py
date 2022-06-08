# function which return reverse of a string

def isPalindrome(x):
	return x == x[::-1]

choice=input("choose number or word ")
if choice in ('number','word'):
    if choice == 'number':
        x = str(input("enter number to check if it is palindrome "))
        ans = isPalindrome(x)
        if ans:
            print("the number "+ x + " is palindrome")
        else:
            print("the number " + x + " is not palindrome")
    elif choice == 'word':
        x = str(input("enter word to check if it is palindrome"))
        ans = isPalindrome(x)
        if ans:
            print("the word "+ x + " is palindrome")
        else:
            print("the word " + x + " is not palindrome")
else:
    print("invalid choice") 
    
