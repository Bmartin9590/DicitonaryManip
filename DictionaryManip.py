## WAP that manipulates the given dictionary. Use the necessary functions to complete the tasks.
## 1. Add a key "pocket" (When you want to add a key to a dictionary, you mention the variable put the key in [] and then enter the value(s))
## 2. Set the value of pocket to be "sea shells", and "candies"
## 3. Sort the backpack items (use .sort function)
## 4. remove "dagger" from backpack (use .remove function)
## 5. Add 50 to the gold value
## 6. Print the new dictionary

## When you want to manipulate a key in a dictionary you must refer to the dictionary first and use [] to refer to the specific [key]

inventory = {"gold" : 500, "pouch" : ["mint", "twine", "gemstone"], "backpack" : ["flute", "dagger", "bread loaf", "jelly"]}
inventory["pocket"] = ("sea shells", "candies")
inventory["backpack"].sort()
inventory["backpack"].remove("dagger")
inventory["gold"] = inventory["gold"] + 50
print(inventory)