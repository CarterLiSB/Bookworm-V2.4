string = "banana"
s = dict()
for i in string:
    if i not in s:
        s[i] = 1
    else:
        s[i] += 1

max = float("-inf")
c = ''
for i in s:
    if max < s[i]:
        max = s[i]
        c=i

print(c + "," + str(max))
