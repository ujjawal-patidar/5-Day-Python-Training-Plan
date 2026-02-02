# Create a function to write a list of dictionaries to a CSV file with headers.
import csv
l = [
    {
        "name" : "Ujjawal",
        "age" : 20
    },
    {
        "name" : "Anant",
        "age" : 17
    },
    {
        "name" : "aaditya",
        "age" : 21
    }
]

feilnames = ["name", "age"]

with open("output.csv", mode = 'w') as file:
    writer = csv.DictWriter(file, fieldnames=feilnames)
    writer.writeheader()
    writer.writerows(l)