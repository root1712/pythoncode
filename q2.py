l = [1,2,3,1,2,1,2,5,6,8,9,5,6,4,3]
# o = 1:3,2:3,3:2....

# d = {}
# for i in l:
#     d[i] = d.get(i,0) + 1
# print(d)

d = {}
for i in l:
    if i in d.keys():
        d[i] = d[i] + 1
    else:
        d[i] = 1
# print(d)
for k,v in d.items():
    print(f"{k} occure {v} times in l")