# d1={}
# print(type(d1))

d2={"Ankit":"Begusarai" ,"Harsh":"Bhagalpur","Raja":{"s1":"gopalganj","s2":"gorakhpur"}}
# print(d2["Raja"]["s1"])
d2["Ankita"]="Siwan"
d2[123] ="USA"
# del d2["Harsh"]
print(d2)

#function


# print(d2.copy())

d3=d2.copy()

del d3["Ankit"]


print(d3.update({"Leena":"Delhi"}))
print(d2.items())
# print(d3)
