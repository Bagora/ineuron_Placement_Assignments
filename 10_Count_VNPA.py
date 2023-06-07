import nltk

#Download the necessary resources
#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')

# Function to count parts of speech
def count_parts_of_speech(text):
    # Tokenize the text into sentences
    sentences = nltk.sent_tokenize(text)

    # Initialize counts dictionary
    counts = {
        'nouns': 0,
        'pronouns': 0,
        'verbs': 0,
        'adjectives': 0
    }

    # Perform part-of-speech tagging on each sentence
    for sentence in sentences:
        tagged_words = nltk.pos_tag(nltk.word_tokenize(sentence))

        # Count the occurrences of each part of speech
        for word, tag in tagged_words:
            if tag.startswith('NN'):
                counts['nouns'] += 1
            elif tag.startswith('PRP'):
                counts['pronouns'] += 1
            elif tag.startswith('VB'):
                counts['verbs'] += 1
            elif tag.startswith('JJ'):
                counts['adjectives'] += 1

    return counts

# Test the function
text = "The quick brown fox jumps over the lazy dog. The dog sees a bone and runs towards it. The fox watches the dog from a distance and starts running too. They both chase after the bone together."
print(count_parts_of_speech(text))

# Test the function
text = "The sun is shining brightly."
print(count_parts_of_speech(text))

# Test the function
text = "She sings beautifully and dances gracefully."
print(count_parts_of_speech(text))

# Test the function
text = "The big dog barks loudly."
print(count_parts_of_speech(text))

# Test the function
text = "I enjoy reading books and playing sports."
print(count_parts_of_speech(text))