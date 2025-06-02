# n=input("Enter a alphabatic character: ")
# def vowels(n):
#     vowels="aeiouAEIOU"
#     count=0
#     # for i in range

def vowel(text):
    vowels = "aeiouAEIOU"
    count = 0
    for i in text:
        if i in vowels:
            count += 1
    return count


input_string = input("Enter a string: ")
vowel_count = vowel(input_string)
print("Number of vowels:", vowel_count)

