l = [[1,2,3,4],[5,6,7,8]]
# max = [4,8]

# o = []
# for i in l:
#     o.append(max(i))
# print(o)

# o = []
# for i in l:
#     # i.sort(reverse=True)
#     # o.append(i[0])
#     i.sort()
#     o.append(i[-1])
# print(o)

o = []
max = 0
for i in l:
    for j in i:
        if j > max:
            max = j
    o.append(max)
print(o)