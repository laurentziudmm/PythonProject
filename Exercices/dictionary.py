# name: John Smith
# email: john
# phone:


# customer = {
#     "name":"John Smith",
#     "age": 30,
#     "is_verified":True
# }
# customer["name"] = "Jack Smith"
# customer["birthdate"] = "Yan 1 1980"


# # print(customer["name"])

# # print(customer.get("birthdate", "yan 1 1980"))

# print(customer["birthdate"])
# print(customer["name"])



#exercitiu

phone = input('Phone: ')

# "1" -> "One"
# "2" -> "Two"

digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "For",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight"
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "
print(output)
