person = {
  "name":"Anag",
  "age":15,
  "hobby":"dancing"
}
print(person["name"])
for i in person:
  print(person[i])


for i in person.values():
  print(i)

person["age"]=90
person["dob"]="17th of October"
print("person")