# Word Counter
def count_words(sentence):
    # Split the sentence into words using spaces
    words = sentence.split()
    
    # Count the number of words
    word_count = len(words)
    
    return word_count

# Example usage
sentence = input("Enter a sentence: ")
print(f"Number of words in the sentence: {count_words(sentence)}")
