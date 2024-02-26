# Example 1
raw_data = "Yossi,30,Eilat"

split_data = raw_data.split(",")
print(split_data)

name = split_data[0]
age = split_data[1]
city = split_data[2]

print(name)
print(city)
print(age)

# Example 2
text = "HelloWorld"
parts = text.split(',')
print(parts)


# Example 3
text = """Line one
Line two
Line three"""
# Split the string into lines
lines = text.split('\n')
print(lines)
# Output: ['Line one', 'Line two', 'Line three']


# Example 4
text = "one:two:three:four:five"
# Split the string on colon, but only the first two occurrences
parts = text.split(':', 2)
print(parts)
# Output: ['one', 'two', 'three:four:five']

# Extra
print(parts[:2])
