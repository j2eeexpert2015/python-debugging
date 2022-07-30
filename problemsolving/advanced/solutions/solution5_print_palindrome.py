#https://stackoverflow.com/questions/19365008/wheres-the-bug-in-this-function-to-check-for-palindrome

# function to check string is
# palindrome or not
def is_palindrome(number):
    i = 0
    print("Input number is ",number)
    for i in range(len(number)):
        if number[i] != number[-1 - i]:
            print('It is not a palindrome')
            break
        else:
            print('It is a palindrome')
            break

ans = is_palindrome('983389')
