#!/usr/bin/env python3
import wordcloud
import string
from matplotlib import pyplot as plt


def calculate_frequencies(file_contents):
    """
    Process the text, remove punctuation, ignore case and words that
    do not contain all alphabets, count the frequencies, and ignore
    irrelevant words.
    """

    # Here is a list of punctuations and irrelevent words
    punctuations = string.punctuation
    irrelevent_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]

    for char in punctuations:
        file_contents = file_contents.replace(char, "")

    file_contents = file_contents.lower()

    words = [word for word in file_contents.split() if word not in irrelevent_words]

    words_dict = {}
    for word in words:
        if word not in words_dict:
            words_dict[word] = 1
        else:
            words_dict[word] += 1

    return words_dict


def main():
    """
    Generate a 'word cloud' from a input text.
    """

    fhand = open("./romeo_and_juliet.txt", "r")
    file_contents = fhand.read()
    words_dict = calculate_frequencies(file_contents)

    # Generate word cloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(words_dict)
    myimage = cloud.to_array()

    plt.imshow(myimage, interpolation = 'nearest')
    plt.axis('off')
    plt.show()


if __name__ == "__main__":
    main()
