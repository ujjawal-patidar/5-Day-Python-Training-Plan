# opening a file
# with open("demo.txt", 'w') as file:
#     file.write("Hey this is a new File demo.txt  ohh really")

# with open("demo.txt", 'a') as file:
#     file.write("first line")
#     file.write("\nSecond line")
#     file.write("\nThird line")
    

# with open("demo.txt", 'a+') as file:
#     # file.write("\nHey this is a new File demo.txt  ohh really")
#     file.seek(0)
#     print(file.read())
#     file.seek(2)
#     print("----------")
#     print(file.readline())
#     file.seek(0)
#     print("----------")
#     print(file.readlines())


# with open('new_file1.txt', 'w') as file:
#     file.write('This is the first line.\n')
#     file.write('This is the second line.\n')

# # Example of appending to the same file:
# with open('new_file2.txt', 'a') as file:
#     file.writelines(['This line was appended.\n', 'So was this one.\n'])




# Basic Modes
# r (Read): Default. Opens for reading only. Error if the file is missing.
# w (Write): Opens for writing. Overwrites (truncates) existing content or creates a new file.
# a (Append): Opens for writing at the end. Preserves old data; creates file if missing.
# x (Exclusive): Creates a new file; fails if the file already exists. 
# Update Modes (Read + Write) 
# r+: Read/Write. Pointer starts at the beginning; file must exist.
# w+: Read/Write. Overwrites existing file or creates a new one.
# a+: Read/Append. Preserves data; writes always happen at the end. 
# Format Modifiers
# t: Text mode (default).
# b: Binary mode (for images, PDFs, etc.). 





import csv

data1 = [['Name', 'Age'], ['John', '30'], ['Jane', '25']]
data2 = [{'Name': 'John', 'Age': 30, 'gender' : "male"}, {'Name': 'Jane', 'Age': 25, 'gender' : "male"}]
fieldnames = ['Name', 'Age', 'gender']


# with open('output.csv', mode='w') as file:
#     # writer1 = csv.writer(file)
#     # writer1.writerows(data1) # Use writerow() for single rows

#     writer2 = csv.DictWriter(file, fieldnames=fieldnames)
#     writer2.writeheader()
#     writer2.writerows(data2)


# with open('output.csv', mode='r') as file:

    # reader2 = csv.DictReader(file)
    # for row in reader2:
    #     print(row)
    
    # reader2 = csv.reader(file)
    # for row in reader2:
    #     print(row)




import json


# person_data = {
#     "name": "Bob",
#     "age": 30,
#     "city": "New India",
#     "isEmployed": True
# }

# with open('output.json', 'w') as file:
#     json.dump(person_data, file, indent=4)
# print("Data written to output.json successfully.")





try:
    with open('output.json', 'r') as file:
        data = json.load(file)
    print("Data loaded successfully:", data)
except:
    print("Error occured")

