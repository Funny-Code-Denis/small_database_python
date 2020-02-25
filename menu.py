import DATA_BASE
import time
import os
List = []
path = 'C:\\Users\\Пользователь\\Desktop\\PDF\\BIG_DATA'
while True:
	choise = input('\
1.Display data\n\
2.Change data\n\
3.Create new record\n\
4.Remove record\n\
5.Display documentation\n\
6.Exit\n')
	if choise == '1':
		with open(path + '\\' + 'name.txt') as file:
			while True:
				line = file.readline()
				if len(line) == 0:
					break
				if '\n' in line:
					line = line[:-1]
				print(line)
		name_open_dir = input('Enter name: ')
		os.system('cls')
		DATA_BASE.output_txt(path, name_open_dir)
		os.system('pause>nul')
		os.system('cls')
	elif choise == '2':
		DATA_BASE.output_file(path, 'name.txt', List)
		iteration = 1
		for list_element in List:
			print(iteration, end = '. ')
			print(list_element)
			iteration += 1
		choise_dir = input('Choise directory: ')
		if choise_dir in List:
			change_file = BIG_DATA.change(path, choise_dir)
			print(change_file)
			os.system('pause>nul')
			os.system('cls')
		else:
			print('Directory not found')
			os.system('pause>nul')
			os.system('cls')
		del List[:]
	elif choise == '3':
		name_new_dir = input('Enter name for create new directory: ')
		DATA_BASE.new_directory(path, name_new_dir, List)
	elif choise == '4':
		DATA_BASE.output_file(path, 'name.txt', List)
		iteration = 1
		for list_element in List:
			print(iteration, list_element)
			iteration += 1
		choise_dir = input('Choise director: ')
		iteration = 0
		for element in List:
			if element == choise_dir:
				del List[iteration]
			iteration += 1
		list.sort(List)
		file = open(path + '\\' + 'name.txt', 'w')
		for element in List:
			element += '\n'
			file.write(element)
		file.close()
		DATA_BASE.delete(path, choise_dir)
		del List[:]
		print('Directory was remove')
		os.system('pause>nul')	
	elif choise == '5':
		print(DATA_BASE.__doc__)
		os.system('pause>nul')
		os.system('cls')
	else:
		break
os.system('cls')