# 2▹ Pobierz od użytkownika 10 liczb, wyświetl tylko te, które są nieparzyste.

print('Wprowadz 10 liczb')
lst = []

for i in range(0, 10):
    user_numbers = int(input())
    lst.append(user_numbers)

print('Lista liczb to: ', lst)

for num in lst:
    if num % 2 != 0:
        print('Liczby nieparzyste to:')
        print(num)


