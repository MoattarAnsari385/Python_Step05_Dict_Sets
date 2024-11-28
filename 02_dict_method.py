marks = {
    "English": 85,
    "Mathematics": 90,
    "Physics": 78,
    "Chemistry": 88,
    "Biology": 92
}

# Print all items (key-value pairs) in the dictionary
print(marks.items())
print(" ")

# Print only the keys
print(marks.keys())
print(" ")

# Print only the values
print(marks.values())
print(" ")

# Update the dictionary: change Biology's marks and add a new subject (Computer)
marks.update({"Biology" : 90, "Computer" : 100})
print(marks)
print(" ")

# Remove the key 'Chemistry' from the dictionary
marks.pop('Chemistry')
print(marks)
print(" ")

# Access values using get() and direct indexing
print(marks.get("English")) 
print(marks["English"]) 

# Demonstrating behavior of get() vs direct indexing when key doesn't exist
print(marks.get("English2")) # Prints None
# print(marks["English2"]) # Return Error

# Remove the last inserted item (key-value pair) from the dictionary
marks.popitem()  
print(marks)

# Set a default value for a key if it doesn't exist
marks.setdefault("Physics", 75)
print(marks)  

# Create a copy of the dictionary
new_marks = marks.copy()
print(new_marks)

# Clear all items from the dictionary
marks.clear()
print(marks)  

new_dict = dict.fromkeys(["a", "b", "c", "d", "e"], 0)
print(new_dict)