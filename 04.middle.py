#4▹ Pobierz od użytkownika parzystą listę elementów. Sprawdź czy 2 środkowe elementy są takie same.

print('Podaj parzystą liczbę elementów listy : ')
array = []

n2 = 'Ile elementów bedzie miała twoja lista?'
print(n2)



for i in n2:
    n = int(input())
    print('--------------------------')
    if n % 2 != 0:
        print('Ta liczba nie jest parzysta. Podaj parzystą liczbę elementów listy.')
        n = int(input())
        print('-----------------------')
    for f in range(0, n):
            user_list = input()
            array.append(user_list)
    print('Twoja lista', array)
    middle_index = (n-1)//2
    second_index = middle_index + 1
    if array[middle_index] == array[second_index]:
        print('Dwa środkowe elementy są takie same')
    else:
        print('Dwa środkowe elementy nie są takie same')







