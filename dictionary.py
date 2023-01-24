number_tostring = {
    0: "Zero",
    1: "One",
    2: "Two",
    3: "Three"
}

string_toNumber = {
    "One": 1,
    "Two": 2,
    "Three": 3
}

print(number_tostring[1])
# or
print(number_tostring.get(1))
print(number_tostring.get(8, "Not available"))
print(string_toNumber.get("m", "Not a valid number"))
