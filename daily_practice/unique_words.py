from collections import Counter
import re 
import pandas as pd 

feedback_list = ["The product is great, but delivery was slow.",
    "Excellent product quality! Fast delivery.",
    "Great product and fast delivery. Recommended!"]
all_feedback = " ".join(feedback_list)
words = re.findall(r'\b\w+\b', all_feedback.lower())
words_count = Counter(words)

for word, count in words_count.items():
    print(f'{word}: {count}')


# if we need to use pandas for larger dataset for fast operation for same task
df = pd.DataFrame(words,columns=['word'])
words_counts = df['word'].value_counts().reset_index()
words_counts.columns = ['word','frequency']
print(words_counts)
