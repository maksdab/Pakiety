def read_large_file(file_name):
    with open(file_name, 'r') as file:
        for line in file:
            yield line.rstrip()

file_name = 'large_file.txt'
lines_generator = read_large_file(file_name)
for line in lines_generator:
    print(line)

