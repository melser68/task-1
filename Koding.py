message = input("Введите сообщение: ")
offset = int(input("Введите сдвиг: "))
coded_message = ""
encoded_message = ''
#Кодуємо повідомлення
for ch in message:
    
    if ord(ch) >= 65 and ord(ch) <= 90:
        cript_1 = ord(ch) - ord('A')
        cript_2 = (cript_1 + offset) % 26
        rez_cript = chr(cript_2 + ord('A'))
        coded_message += rez_cript
    elif ord(ch) >= 97 and ord(ch) <= 122:
        cript_1 = ord(ch) - ord('a')
        cript_2 = (cript_1 + offset) % 26
        rez_cript = chr(cript_2 + ord('a'))
        coded_message += rez_cript
    else:
        coded_message += ch
        
        
print(coded_message , 'Закодоване повідомлення')

#Розкодовуємо повідомлення
for enc in coded_message:
    
    if ord(enc) >= 65 and ord(enc) <= 90:
        decript_1 = ord(enc) - ord('A')
        decript_1 = ord(enc) - ord('A')
        decript_2 = (decript_1 - offset) % 26
        if decript_2 < 0:
            decript_2 = (offset - decript_1) % 26
        decript_rez = chr(decript_2 + ord('A'))
        encoded_message += decript_rez
    elif ord(enc) >= 97 and ord(enc) <= 122:
        decript_1 = ord(enc) - ord('a')
        decript_2 = (decript_1 - offset) % 26 
        if decript_2 < 0:
            decript_2 = (offset - decript_1) % 26        
        decript_rez = chr(decript_2 + ord('a'))
        encoded_message += decript_rez
    else:
        encoded_message += enc
        

print('Розкодоване повідомлення ', encoded_message)
