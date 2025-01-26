                             #Efficient memory management is crucial when working with large files in Python. Here are some strategies:
#Using File Streams:Instead of reading the entire file into memory, process it line by line or in chunks:
# Reading a large file line by line
with open("large_file.txt", "r") as file:
    for line in file:
        process(line)  # Replace with your processing logic

#Using Generators
#Generators yield data one piece at a time, avoiding memory-intensive lists:
def read_large_file(file_path):
    with open(file_path, "r") as file:
        for line in file:
            yield line.strip()

for line in read_large_file("large_file.txt"):
    process(line)  # Replace with your processing logic


#Chunk Processing
#For binary or CSV files, read and process in chunks:
import pandas as pd
# Process a large CSV in chunks
for chunk in pd.read_csv("large_file.csv", chunksize=10000):
    process(chunk)  # Replace with your processing logic
