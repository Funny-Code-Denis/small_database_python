
'''Console program for working with a database
Devoloper: Sosnin Denis
Verion 1.5'''

import time
import os

#Create new directory
def new_directory(path_to_dir, name_new_dir, List):
	new_dir = path_to_dir + '\\' + name_new_dir
	
	try:
		os.mkdir(new_dir)
	except OSError:
		print('The directory is not created, perthaps the directory woth the same name already exists')
		return
	else:
		print('Directory was create')

	#add directory name to file
	f = open(path_to_dir + '\\' +'name.txt')
	while True:
		reading_line = f.readline()
		if len(reading_line) == 0:
			break
		if '\n' in reading_line:
			reading_line = reading_line[:-1]
		List.append(reading_line)
	f.close()
	List.append(name_new_dir)
	f = open(path_to_dir + '\\' +'name.txt', 'w')
	for elemnts in List:
		elemnts += '\n'
		f.write(elemnts)
	f.close()
	#clear list
	del List[:]
	new_directory_file(path_to_dir, name_new_dir)
#file creation and filling database
def new_directory_file(path_to_dir, name_new_dir):
	new_dir = path_to_dir + '\\' + name_new_dir
	with open(new_dir + '\\' + 'FIO.txt', 'tw') as file:
		name_human = input('Enter name: ')
		file.write(name_human)
	with open(new_dir + '\\' + 'address.txt', 'tw') as file:
		address_human = input('Enter address: ')
		file.write(address_human)
	with open(new_dir + '\\' + 'job.txt', 'tw') as file:
		job_human = input('Enter place work/study: ')
		file.write(job_human)
	with open(new_dir + '\\' + 'pay.txt', 'tw') as file:
		pay_human = input('Enter pay: ')
		file.write(pay_human)
	with open(new_dir + '\\' + 'hobby.txt', 'tw') as file:
		hobby_human = input('Enter hobby: ')
		file.write(hobby_human)
#output from directory
def output_txt(path, name_open_dir):
	open_dir = path + '\\' + name_open_dir + '\\'
	with open(open_dir + 'FIO.txt') as f:
		print('Name:', end = '\t')
		while True:
			line = f.readline()
			if len(line) == 0:
				break
			print(line)
	with open(open_dir + 'address.txt') as f:
		print('Adress:', end = '\t')
		while True:
			line = f.readline()
			if len(line) == 0:
				break
			print(line)
	with open(open_dir + 'job.txt') as f:
		print('Place work/study:', end = '\t')
		while True:
			line = f.readline()
			if len(line) == 0:
				break
			print(line)
	with open(open_dir + 'pay.txt') as f:
		print('Pay:', end = '\t')
		while True:
			line = f.readline()
			if len(line) == 0:
				break
			print(line)
	with open(open_dir + 'hobby.txt') as f:
		print('Hobby:', end = '\t')
		while True:
			line = f.readline()
			if len(line) == 0:
				break
			print(line)
#write from file to list
def output_file(path, name_file, List):
	#with open(path + '\\' + name_file, encoding = 'utf-8') as file:
	file = open(path + '\\' + name_file)
	while True:
		reading_line = file.readline()
		if len(reading_line) == 0:
			break
		if '\n' in reading_line:
			reading_line = reading_line[:-1]
		List.append(reading_line)
	file.close()
	return List
#function remove directory
def delete(path, name_dir):
	os.chdir(path + '\\' + name_dir)
	directory = ('FIO.txt', 'address.txt', 'job.txt', 'pay.txt', 'hobby.txt')
	number_file = 0
	for iteration in range(0, len(directory)):
		os.remove(directory[number_file])
		number_file += 1
	os.chdir(path)
	os.rmdir(name_dir)
#change file in directory
def change(path, choise_dir):
	os.chdir(path + '\\' + choise_dir)
	directory = ('FIO.txt', 'address.txt', 'job.txt', 'pay.txt', 'hobby.txt')
	iteration = 1
	for file_static in directory:
		print(iteration, end = '. ')
		print(file_static)
	choise_file = input('Choise file: ')
	if choise_file in directory:
		List = []
		choise_file1 = choise_dir + '\\' + choise_file
		output_file(path, choise_file1, List)
		print('File contains: ', List)
		change_word = input('Enter changes: ')
		with open(path + '\\' + choise_dir + '\\' + choise_file, 'w') as file:
			file.write(change_word)
		ishod = 'File ' + choise_file + ' was change'
		return ishod
	else:
		return 'File not found'