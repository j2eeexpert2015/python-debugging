#https://stackoverflow.com/questions/19365008/wheres-the-bug-in-this-function-to-check-for-palindrome
number=input("Enter any number :")
i=0
for i in range(len(number)):
    if number[i]!=number[-1-i]:
        print('It is not a palindrome')
        break
    else:
        print('It is a palindrome')
        break