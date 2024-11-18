#Работа со словарями
my_dict = {'Andrey': 1950, 'Boris': 2001, 'Sasha': 1999}
print(my_dict)
print(my_dict['Sasha'])
print(my_dict.get('Gosha')) # Метод «get»
# print(my_dict.get('Gosha', 'нет нужного ключа')) # указываем значение по умолчанию, которое будет возвращено вместо «None»
my_dict['Grisha'] = 2010
my_dict['Pyotr'] = 1976
# my_dict['Harlam'] = [1975, 2005] # значений могут использоваться изменяемые типы данных
print(my_dict)
# print(my_dict.keys()) # Метод «keys»
# print(my_dict.values()) # Метод «values»
# print(my_dict.items()) # Метод «items»
# my_dict.update({'Grisha': 2001, 'Pyotr': 1955}) # Метод «update»
# print(my_dict)
# del my_dict ['Andrey'] # оператор `del` для удаления
# print(my_dict)
deleted = my_dict.pop('Boris') # Метод «pop»
print(deleted)
print(my_dict, '\n') # \n для отступа строки между работы со словарями и множествами
#Работа с множествами
my_set = {1, 2, 'три', 1.0, 2.0, 3, 4,'пять' , 5 }
print(my_set)
my_set.add(7.0)
my_set.add(6)
print(my_set)
# my_set.discard(1)
# print(my_set) # метод «discard»
my_set.remove('три')
print(my_set) # метод «remove»
