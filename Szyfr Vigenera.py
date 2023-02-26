CAPITAL = range(65, 91)

while True:
    mode = input("Wpisz S by SZYFROWAĆ\nWpisz D by DESZYFROWAĆ\nWpisz Z by ZAMKNĄĆ program\n> ")

    while mode[0] not in ["S","D","Z"]: mode = input("Wprowadź poprawny znak.\n> ")
    if mode[0] == "Z": break

    inputText = input("Wprowadź tekst:\n> ")
    key = input("Wprowadź klucz:\n> ")
    while not key.isalpha(): key = input("Klucz musi być zawierać jedynie poprawne znaki alfabetu. Spróbuj ponownie:\n> ")
    
    longKey = key
    while len(inputText) > len(longKey): longKey += key

    def encryption(text, key):
        encrText = str()
        for i in range(len(text)):
            if ord(text[i].upper()) in CAPITAL:
                textCharValue = ord(text[i].upper()) - 65
                keyCharValue = ord(key[i].upper()) - 65
                encrCharValue = ((textCharValue + keyCharValue) % 26) + 65

                encrChar = chr(encrCharValue)
                if text[i].islower(): encrChar = encrChar.lower()
                encrText += encrChar
            else: encrText += text[i]

        return encrText

    def decryption(text, key):
        decrText = str()
        for i in range(len(text)):
            if ord(text[i].upper()) in CAPITAL:
                textCharValue = ord(text[i].upper()) - 65
                keyCharValue = ord(key[i].upper()) - 65
                decrCharValue = ((textCharValue - keyCharValue) % 26)
                if decrCharValue < 0: decrCharValue += 26
                decrCharValue += 65

                decrChar = chr(decrCharValue)
                if text[i].islower(): decrChar = decrChar.lower()
                decrText += decrChar
            else: decrText += text[i]
        return decrText

    if mode[0] == "S": print(encryption(inputText, longKey))
    elif mode[0] == "D": print(decryption(inputText, longKey))
        



