#this is a python program to read the whole file and run through line by line from whole file and then run through word by word in the line and later store the word and count of that word in the file in a dictionary so that we can find the word with the most count in the whole file.
name = input('enter file name: ')
try:
    handle = open(name, 'r')  # Ensure file exists and can be read
except FileNotFoundError:
    print(f"File {name} not found.")
    exit()

count= {}
for line in handle:
    words=line.split()
    for word in words:
        count[word]=count.get(word,0)+1

bigcount=0
bigword=None
for word,count in count.items():
    if count>bigcount:
        bigword = word 
        bigcount= count
print(bigcount,bigword)