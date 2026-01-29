# Check if two strings are anagrams of each other.

substr = "lawajju"
string = "ujjawal"

substr = list(substr)
string = list(string)

substr = sorted(substr)
string = sorted(string)

print(substr, string)

if(substr == string):
    print("yes they are Anagram")
else:
    print("No they are not Anagram")