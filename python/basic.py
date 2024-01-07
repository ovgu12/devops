
import random
import os
import advance
import json

choices = ['A', 'B', 'C']
numbers = [ 0, 1, 2]
dictionary = {
    "message": "Hello World"
}

# JSON
jsonizedDict = json.dumps(dictionary)
dict = json.loads(jsonizedDict)
print(dict == dictionary)

# Randojmize
print('Random choice: ' , random.choice(choices))

# Destruct
a, b, c = choices
print(a , b, c)

# Try-with
with open(os.path.dirname(__file__) + '/test.txt') as file:
    lines = file.readlines()

# Loop array
for c in choices + numbers:
    print(c)

# Loop object
for k,v in dictionary.items():
    print(k + ":" + v)

html = f"""
    <!doctype html>
        <title>Hello</title>
        <bod>
            <pre>
                First 1 element: {choices[0:1]}
                First 2 elements: {choices[:-1]}
                {advance.hello("World")}
            </pre>
        </body>
    </html>
"""

print(html)