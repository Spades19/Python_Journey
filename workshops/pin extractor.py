def pin_extractor(poem):
    secret_code = ''
    lines = poem.split('\n')
    for line_index, line in enumerate(lines):
        print(line_index, line)
        words = line.split()
# In the last line of the loop, update the print call so that it prints the word inside the words list at index line_index.
        print(str(len(words[line_index])))
        if line_index < len(words):
            secret_code += str(len(words[line_index]))
        else:
            secret_code += '0'
    return secret_code


poem = '''Stars and the moon
shine in the sky
white and 
until the end of the night'''

print(pin_extractor(poem))
