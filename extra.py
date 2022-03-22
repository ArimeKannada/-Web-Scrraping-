import os
os.system('cls||clear')

with open("extra.txt", "r", encoding="utf8") as data:
    data = data.read()
    # print(data)
    code = []
    name = []
    v = data.split('\n')
    # print(v)
    for n in v:
        x = n.split(" = ")
        # print(x[0])
        code.append(x[0])
        name.append(x[1])

print(code)
print(name)