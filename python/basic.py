
import random
import os
 
choices = ['A', 'B', 'C']
numbers = [ 0, 1, 2]
dictionary = {
    "message": "Hello World"
}

print('Random choice: ' , random.choice(choices))

# Destruct
a, b, c = choices
print(a , b, c)

# Try-with
with open(os.path.dirname(__file__) + '/test.txt') as file:
    lines = file.readlines()
    print(lines[0])

# Loop array
for c in choices + numbers:
    print(c)

# Loop object
for k in dictionary:
    print(k + ":" + dictionary[k])

html = f"""
    <!doctype html>
        <title>Hello</title>
        <bod>
            <pre>
                First 1 element: {choices[0:1]}
                First 2 elements: {choices[:-1]}
            </pre>
        </body>
    </html>
"""

print(html)