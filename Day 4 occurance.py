#occurance of a character
string = input("Enter ant string :  ")
c = input("Enter character to check its occurrence :   ")
count = 0
for i in string:
    if i == c:
        count += 1
        print(c, "occurs", count, "time ()s .")