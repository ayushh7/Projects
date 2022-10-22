text=['h','e','l','l','o']
print(text)
vowels="aeiou"
newText=[x.upper() for x in text if x not in vowels]
print(newText)
