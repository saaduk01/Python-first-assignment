# Python Strings Assignment

# 1. Creating String Variables
name = "Saad"
city = "Karachi"
sentence = "Python is fun to learn"

print(name)
print(city)
print(sentence)


# 2. Accessing Characters
print(sentence[0])    # First character
print(sentence[-1])   # Last character


# 3. Slicing
print(sentence[0:6])   # Python
print(sentence[7:9])   # is


# 4. String Methods
print(name.upper())
print(name.lower())
print(sentence.replace("fun", "easy"))
print(sentence.split())
print(len(sentence))


# 5. String Formatting
age = 20
print("My name is " + name + " and I am " + str(age) + " years old.")
print(f"My name is {name} and I am {age} years old.")