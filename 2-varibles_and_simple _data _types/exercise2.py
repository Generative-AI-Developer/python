'''2-8. File Extensions: Python has a removesuffix() method that works exactly
like removeprefix(). Assign the value 'python_notes.txt' to a variable called
filename. Then use the removesuffix() method to display the filename without
the file extension, like some file browsers do.
'''
text = "hello.txt"
print(text)
result = text.removesuffix(".txt")
print(result)

text = "hello.txt"
print(text)
result = text.removeprefix("he")
print(result)


text = "hello.txt"
print(text)
result = text.removesuffix("xt")
print(result)


