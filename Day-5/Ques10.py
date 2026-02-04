# Create a generator pipeline to process large CSV data: read → filter → transform → aggregate, all memory-efficient.
import csv

def read_csv(file_name):
    with open(file_name, mode ='r')as file:
        # for row in csv.DictReader(file):
        #     yield row 
        yield from csv.DictReader(file)
        
            
def filterLine(rows):
    for row in rows:
        if(int(row['age'] )> 18):
            yield row

def transform(rows):
    for row in rows:
        row['salary'] = int(row['salary']) + 10000
        yield row

def aggregate(rows):
    maxSalary = -1
    for row in rows:
        maxSalary = max(maxSalary, row['salary'])
    print(maxSalary)

    
if __name__ == "__main__":
    row = read_csv("output.csv")
    filtered=filterLine(row)
    transformed=transform(filtered)
    maxSalary = aggregate(transformed)



