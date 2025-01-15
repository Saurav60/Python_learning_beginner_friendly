from collections import Counter
def count_char(file_path):
    with open('file_path', 'r') as file:
        text = file.read()
        frequency = Counter(text)
        for char,count in frequency.items():
            return char, count
        