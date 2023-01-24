characters = ["Kendall", "Logan", "Shiv", "Roman"]
                # 0          # 1      # 2      # 3
                # -4         # -3     # -2     # -1
print(characters[-4:])
characters.insert(1, "Marie")
print(characters)
characters.pop()  # Removes last value
print(characters)
characters.remove("Logan")
print(characters)
characters.append("Tom")  # Adds value at the last
print(characters)
print(characters.index("Shiv"))
print(characters.count("Tom"))
characters.sort()
print(characters)
