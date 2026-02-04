# Regular expressions (regex) in Python are primarily handled via the built-in re module to search, match, and manipulate strings based on specific patterns.
import re

s = "ujj-awal@gmail.com ujjawal.patidar@gammaedge.com is the email of ujjawal.patidar"

# print(re.search(r'[\w\.-]+@[\w\.]+', s))
print(re.findall(r'[\w\.-]+@[\w\.]+', s))

# print(re.match(r'[@.]+', s))
# print(re.search(r'@', s))

# change = re.sub(r'[\w\.-]+@[\w\.]+', 'changed', s)
# print(change)

print(re.findall(r'^u', s))



# . (Dot): Matches any character except newline.
# \w, \d, \s: Matches alphanumeric, digits, and whitespace, respectively.
# +, *, ?: Matches one or more, zero or more, or zero or one repetition.
# ^, $: Anchors that match the start or end of a string, respectively.
# [...]]: Matches any character inside the brackets. 
