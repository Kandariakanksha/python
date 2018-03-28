alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 3
newMessage = ''
message = input('please enter a character:')

for character in message:
    if character in alphabet:
        position = alphabet.find(character)
        newPosition = (position + key) % 26
        newCharacter = alphabet[newPosition]
        # print('the new character is :', newCharacter)
        newMessage += newCharacter
else:
    newMessage += newCharacter

print('new meassage is :', newMessage)