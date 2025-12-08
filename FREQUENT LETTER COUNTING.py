import random

random_words = ["mississippi", "hello", "strawberry", "banana", "apple"]

a = random.choice(random_words)
print("Selected word:", a)

max_count = 0
most_frequent_letter = ""

for i in a:
    count = a.count(i)
    if count > max_count:
        max_count = count
        most_frequent_letter = i

print("Most frequent letter:", most_frequent_letter)
print("Frequency:", max_count)
