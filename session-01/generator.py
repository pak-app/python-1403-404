import os

name_folder = 'ghasem'
folders_name = ['modules', 'scripts']
files_name = ['test1.txt', 'test2.txt']

if not os.path.isdir(f'./{name_folder}'):
    os.mkdir(f'./{name_folder}')


for folder in folders_name:
    if not os.path.isdir(f'./{name_folder}/{folder}'):
        os.mkdir(f'./{name_folder}/{folder}/')

for _file in files_name:
    
    with open(f'./{name_folder}/{_file}', 'a') as file:
        
        file.close()
