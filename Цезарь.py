# алфавит
alphabet ='абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

# реализация шифра Цезаря
def caesar(message, shift, encode=True):
    global alphabet
    # зашифрованное или дешифрованное сообщение
    result = ''
    # для каждого символа исходного сообщения
    for c in message:
        # определение номера символа в алфавите
        position = alphabet.find(c)
        
        # определение нового номера в случае шифрования
        if encode:
            new_position = (position + shift) % len(alphabet)
        # определение нового номера в случае дешифрования 
        else:
            new_position = (position - shift) % len(alphabet)

        # добавление нового символа в сообщение-результат
        result += alphabet[new_position]
    return result

# сообщение
message = input("Введите сообщение: ")
# шаг сдвига
shift = int(input("Введите шаг сдвига: "))
# тип операции
encode = input("Введите 1 для шифровки, любой другой текст для расшифровки: ") == '1'
# вывод результата
print("Результат: ", caesar(message, shift, encode))
