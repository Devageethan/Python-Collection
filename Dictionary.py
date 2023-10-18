a={
    1:10,
    2:20,
    3:30
}
print(a.keys())
print(a.values())
a.pop(1)
print(a)
a.clear()
print(a)

d={
    "name":"deva",
    "age":23,
    "clg":"tpgit"
}
d.update({"age":22})
d["degree"]="mechanical"
print(d.values())
print(d.keys())
del d ["clg"]
print(d)