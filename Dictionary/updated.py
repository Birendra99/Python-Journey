
names={
    1:"Biren",
    2:"Sita",
    3:"Ram"
}
names[1]="Birendra"
print(names[1])
print(names.keys())
print(names.values())

citys={
    1:"Rajkot",
    2:"Diu",
    3:"Kathmandu",
    4:"Delhi"
}
citys.update({1:"Dehardun"})
print(citys)
citys.update({3:"Tikapur"})
citys.update({5:"Butwal"})
print(citys)