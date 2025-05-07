word =["palindrome", "banana", "Orange"]
for i in word:
    vowels = set('aeiouAEIOU')
    count = 0
    for letter in i:
        if letter in vowels:
            count += 1
    print(f"Number of vowels in {i} is {count}")