# 1▹ Stwórz krotkę zawierającą dane twojego pupila (rodzaj zwierzecia, rasa, jak się wabi).
# Następnie rozpakuj tę krotkę na pojedyńcze zmienne.
# Wykorzystaj zmienne do wyświetlenia f-stringa, tak by mogło powstać zdanie np.
# “Mój pies, rasy border collie wabi się Dyzio”.

my_pet = ('kot', 'pers', 'Rysiu')
(pet, race, name) = my_pet
print(f'Moj {pet} rasy {race} wabi sie  {name}')
