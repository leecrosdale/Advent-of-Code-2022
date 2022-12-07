filename = './day7/test.txt'

def run():
    current_directory = ''
    files = []
    directory_paths = []

    with open(filename) as fh:
        for line in fh:
            line = line.strip('\n')

            print(line)

            if '$ cd' in line:

                command = line.split('$ cd ').pop()

                if command == '..':
                    # print("Moving back a directory")
                    current_directory = directory_paths.pop()
                else:
                    directory_paths.append(command)
                    current_directory = command

                # files = []

                print(f"Changing Directory to {current_directory}")
                print(f"- {current_directory} (dir)")

            elif ' ls' in line:
                print(f"Listing Files in directory")
                pass
            else:
                if 'dir' not in line:
                    file = line.split(' ')
                    size = int(file[0])
                    print(f"- {file[1]} (file, size={file[0]})")
                    files[current_directory].append(size)
                else:
                    dir = line.split(' ')
                    print(f"- {dir[1]} (dir)")

    print(f"Max: {sum(files)}")
    print(f"Files: {files}")
    print(directory_paths)