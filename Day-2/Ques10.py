# Create a dictionary that groups anagrams together from a list of words.

d = {}

l = ["naman", "tea", "ate", "manan", "ujjawal"]

for i in l:
    hash = "".join(sorted(i))

    if not d.get(hash):
        d[hash] = []
    d[hash].append(i)

print(d)