# PYTHON - INPUT, OUTPUT

## CONTENTS

- [ABOUT](#about)
- [SOME KEYPOINTS](#some keypoints)
- [OTHER CONCEPTS](#other concepts)

## ABOUT

In `Python`, input/output refers to the process of taking data from external sources (like a user via the keyboard, files, or other programs) and sending data to external destinations (like displaying output to the screen or writing to files).

## SOME KEYPOINTS

- INPUT: to do this the `input()` function is used to take input from a user through the keyboard. it prompts the user to enter data and awaits input. an example is:
	> name = input("Enter your name: ")

- OUTPUT: the output in python is done using the `print()` function, it displays the result on a screen or console, it can output strings, variables and so much more. an example is:
	> print("i am janice, nice to meet you.")

##### NOTE:
*python also provides functions to read data from files*. (`open()`, `read()`, `readline()`, `readlines()`). You can also write to files using `open()` with `"w"` or `"a"` mode to write or append content to a file.

## OTHER CONCEPTS

- `JSON`(Javascript Object Notation):
it is a lightweight, human-readable data interchange format. It's used for transmitting data between a server and a web application as text.
- `SERIALIZATION`:
the process of converting a data structure or object into a format (like JSON) that can be easily stored, transmitted, or reconstructed later. It's useful for saving the state of an object or transmitting it across different systems.
- `DESERIALIZATION`:
the opposite process of serialization.
- `Converting a Python Data Structure to a JSON String`:
Python provides the json module, which includes methods to work with JSON data. The json.dumps() function is used to convert a Python data structure (such as a dictionary or list) into a JSON string.
a code example is:
```
import json

data = {'name': 'John', 'age': 30}
json_string = json.dumps(data)
print(json_string)
```
