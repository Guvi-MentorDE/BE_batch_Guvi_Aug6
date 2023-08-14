def annagram(loc_str1, loc_str2):
    if sorted(loc_str1) == sorted(loc_str2):
        return "yes"
    else:
        return "no"

def palindrome(loc_str1):
    if loc_str1 == loc_str1[::-1]:
        return 'yes'
    else:
        return 'no'

if __name__ == "__main__":

    str1= "madam"
    if_palindrome= palindrome(str1)

    str2= "save"
    str3= "vase"

    if_annagram= annagram(str2, str3)

    print("Is the string palindrome?" + ' ' + if_palindrome)

    print("Is the string annagram?" + ' ' + if_annagram)