#Longest Word In The List

num_words = int(input("Enter the number of words: "))

words = [input(f"Enter word {i + 1}: ") for i in range(num_words)]

longest_word = max(words, key=len)
print(f"The word with the longest length is: {longest_word}")
