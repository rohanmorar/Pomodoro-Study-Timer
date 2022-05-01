blocks = [
    {
    "gym":False,
    "school":True,
    "store":False,
    },
    {
    "gym":True,
    "school":False,
    "store":False,
    },
    {
    "gym":True,
    "school":True,
    "store":True,
    },
    {
    "gym":False,
    "school":True,
    "store":False,
    },
    {
    "gym":False,
    "school":True,
    "store":True,
    }
]

Reqs = ["gym", "school", "store"]
v_list = [v for v in blocks[2].values()]
v = set(v_list)
print(v)

# for i in range (1,len(blocks)-1):
#     if set(blocks[0].values) == {True}:





