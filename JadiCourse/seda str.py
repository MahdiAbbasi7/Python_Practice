seda_dar = ['a','e','i','o','u']
my_input = [char.lower() for char in input()]
output = ''
for char in my_input:
 if char not in seda_dar:
    output = (output + '.' + char.lower())
print(output)
