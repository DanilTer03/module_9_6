def all_variants(text):
    length = len(text)
    for char in text:
        yield char
    for substring in range(2, length + 1):
        for start in range(length - substring + 1):
            yield text[start:start + substring]

a = all_variants("abc")
for i in a:
    print(i)
