text = input("Enter a string: ")

if len(text) == 0:
    print("Compressed string:")
else:
    compressed = ""
    current_char = text[0]
    count = 1

    for i in range(1, len(text)):
        if text[i] == current_char:
            count += 1
        else:
            compressed += current_char + str(count)
            current_char = text[i]
            count = 1

    compressed += current_char + str(count)

    if len(compressed) < len(text):
        print("Compressed string:", compressed)
    else:
        print("Original string:", text)
