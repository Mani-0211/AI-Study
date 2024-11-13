read_content = open("data/notes.txt", "r")

content = read_content.read()

read_content.close()

print("full content:")
print(content)

read_character = open("data/notes.txt", "r")

characters = read_character.read(5)

read_character.close()

print("first five letters:")
print(characters)