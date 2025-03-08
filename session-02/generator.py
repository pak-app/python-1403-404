import os

# name_folder = 'ghasem'
# folders_name = ['modules', 'scripts']
# files_name = ['test1.txt', 'test2.txt']

def make(config):
    
    if not os.path.isdir(f'./{config['dirName']}'):
        os.mkdir(f'./{config['dirName']}')
    
    for _file in config['files']:
        
        with open(f'./{config['dirName']}/{_file}', 'a') as file:
            file.close()
    
    
    for folder in config['directories']:
        print(type(folder))
        if not os.path.isdir(f'./{config['dirName']}/{folder['dirName']}'):
            os.mkdir(f'./{config['dirName']}/{folder['dirName']}/')
            


config = {
    "dirName": "ghasem",
    "files": [
        'test1.txt',
        'test2.txt'
    ],
    "directories": [
        {
            "dirName": "modules",
            "files": [
                "test3.txt",
                "test4.txt"
            ],
            "directories": [
                "scripts",
                "env"
            ]
        }
    ]
}



make(config)

# if not os.path.isdir(f'./{config['dirName']}'):
#     os.mkdir(f'./{config['dirName']}')


# for folder in config['directories']:
#     if not os.path.isdir(f'./{config['dirName']}/{folder}'):
#         os.mkdir(f'./{config['dirName']}/{folder}/')

# for _file in config['files']:
    
#     with open(f'./{config['dirName']}/{_file}', 'a') as file:
#         file.close()
