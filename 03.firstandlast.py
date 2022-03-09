# ▹ Dla podanej przez użytkownika liście liczb całkowitych sprawdź czy pierwszy i ostatni element są takie same.
user_list = input('Podaj listę')
counter = len(user_list)
first = user_list[0]
last = user_list[counter-1]

print(user_list[0] == user_list[-1])