name = "Byron"
last_name = "Cueva"
print(name)
print(last_name)

# Concatenation
full_name = name + " " + last_name
print(full_name)

quote = "I' am Byron"
print(quote)

quote2 = 'She said "Hello"'
print(quote2)

# Format
## Concatenation form
template = "Hi, my name is " + name + " and my last name is " + last_name
print('v1', template)

## Use the format function
template = "Hi, my name is {} and my last name is {}".format(name, last_name)
print('v2', template)

# This is the most form use
template = f"Hi, my name is {name} and my last name is {last_name}"
print('v3', template)