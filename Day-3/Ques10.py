# Create a function that reads a large file line by line efficiently using a generator, and processes it in chunks.

def gen_file(file_name):
    with open(file_name, 'r') as file:
        line = file.readline()

        while(line):
            yield line
            line = file.readline()

        

for i in gen_file('demo.txt'):
    print(i, end ='')

# gen_file("demo.txt")