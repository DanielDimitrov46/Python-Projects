def isPalindrome(str):
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True


s = input("Enter something: ")
result = isPalindrome(s)

if (result):
    print("Yes")
else:
    print("No")