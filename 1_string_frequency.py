'''Question 1: -
Write a program that takes a string as input, and counts the frequency of each word in the string, there might be repeated characters in the string. Your task is to find the highest frequency and returns the length of the
highest-frequency word.
'''
#  let's import Counter class from the collections module.
from collections import Counter

# First we create a function that takes a string as an input
def count_frequency(string):
    words = string.split() # We can use split function to Splits the input string into individual words
    word_counts = Counter(words) # Create a counter object, which counts the frequency of each word in the words list.
    highest_frequency = max(word_counts.values()) # max function will find a highest frequency
    
    # Using the get method on the word_counts dictionary to get the highest-frequency word 
    highest_frequency_word = max(word_counts, key=word_counts.get) 
    # Then we calculate and return the length of the highest-frequency word using the len function.
    return len(highest_frequency_word)

# User input
input_string = input("Enter a string: ")
result = count_frequency(input_string)
print(f"Length of the highest-frequency word is {result}")

'''
Test Case 1:
string = "apple apple banana banana cherry cherry cherry cherry"
Output: 6

Explanation: In this case, the string consists of three words: "apple", "banana", and "cherry". The word "cherry" appears the most number of times (4 times), followed by "apple" and "banana" (both appearing twice). The length of the highest-frequency word is 6, which corresponds to "cherry".

Test Case 2:
string = "hello world hello world hello world"
Output: 5

Explanation: The input string contains two words: "hello" and "world". Both words occur an equal number of times (3 times). The length of the highest-frequency word is 5, which corresponds to both "hello" and "world".

In both cases, the program correctly identifies the highest-frequency word and returns its length. It handles repeated words and counts their frequencies accurately.
'''