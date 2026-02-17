# ask users for their input:
name = input("what is your name ?: ")
print("hello", name)
# print using the fstrings:
print(f"Hello {name}")
# ask for users age and store it:
age = int(input("what is your age: "))
print(f"you are {age} years old")
# print both your name and your age in one sentence:
print(f"your name is {name.upper()} and you are {age} years old")

# taking the argument of end= "\n":
name = input("what is your name: ")
print("How was your night in this new place mr.", end= " ")
print(name)

# formatting strings
print(f"Hello, '{name}'")

# removing whitespaces:
print(f"Hello, {name.strip()}")
name = name.strip()
# making first letter uppercase:
name = name.title()
# making the whole word into uppercase:
name = name.upper()


print(name)


town = input("Where do you comes from:")
print(town,"is a very nice place")

