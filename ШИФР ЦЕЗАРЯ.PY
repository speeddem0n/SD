def tally(text):
    zdarova = {}
    for letter in text:
        if letter in zdarova:
            zdarova.update({letter:zdarova.get(letter)+1})
        else:
            zdarova.update({letter:1})
    for key in sorted(zdarova.keys()):
        print (key, '=', zdarova[key],end=". ") 
    print('')
alphabet ="абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
encript = input("Введите текст: ")
key = int(input("Введите ключ шифрования(1-30): "))
encript = encript.lower()
desencripted = ""
encripted = ""
for letter in encript:
    position = alphabet.find(letter)
    newPosition = position + key
    if letter in alphabet:
        encripted = encripted + alphabet[newPosition]
    else:
        encripted = encripted + letter
print("зашифрованный текст: ", encripted)
for letter in encripted:
    position = alphabet.find(letter)
    newPosition = position - key
    if letter in alphabet:
        desencripted += alphabet[newPosition]
    else:
        desencripted += letter
print("разшифрованный текст: ",desencripted)
print("колл-во символов в расшифрованном тексте:")
tally(encript)
print("колл-во символов в зашифрованном тексте:")
tally(encripted)
