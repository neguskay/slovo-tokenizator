import os

from nltk import tokenize
from src.utils.models import WordMetadata


def split_sent_into_words(sentence):
    if sentence is not None:
        words = sentence.split()
        # print("lolo :: ", words)

        cleaned_words = []
        # Clean each word.
        # Remove ',' '.'
        for w in words:
            # Convert to lower to allow easy comparison
            new_w = clean_word(w=w)

            if new_w is not None:
                cleaned_words.append(new_w)

            else:
                pass

        print("old", words)
        print("new", cleaned_words)
        # Return a list of cleaned words
        return cleaned_words

    else:
        return None


def clean_word(w):
    # Careful use of lower()
    # Depending on use case, you might want to remove
    w = w.lower()

    if "." in w:
        print('dot')
        w = w.replace(".", "")

    if "," in w:
        print('comma')
        w = w.replace(",", "")

    if ";" in w:
        print('semi-co')
        w = w.replace(";", "")

    if ":" in w:
        print('semi-co')
        w = w.replace(":", "")

    if w == "-":
        print("hypen (-) not word")
        return None

    # print("new :: ", w)
    return w


# def count_word_occurrence(words_list):


def get_final_matrix(file):
    final_matrix, sentences = generate_hash_tag_matrix(get_tokenized_unsorted_sentences_from_file(file_to_read=file))

    return final_matrix, sentences


def get_tokenized_unsorted_sentences_from_file(file_to_read):
    # Open the file
    # open_file = open(file_to_read, 'r')

    raw_sentences = file_to_read.read().decode('utf-8')

    # Tokenize sentences with nltk
    list_of_sentences = tokenize.sent_tokenize(raw_sentences)

    return list_of_sentences


def generate_hash_tag_matrix(list_of_sentences):
    final_matrix = {}
    unsorted_words = []

    for sentence_index, sentence in enumerate(list_of_sentences):
        words = split_sent_into_words(sentence=sentence)

        for word_index, word in enumerate(words):
            # TO-DO: Add 1 to index to offset
            word_meta = WordMetadata(word, sentence_index, word_index)

            # Retrieve/check is word in matrix
            if word in final_matrix:
                existing_word_matrix = final_matrix[word]
                sentence_captured = False

                # Check if sentence number is captured
                for exist_word in existing_word_matrix:
                    if exist_word.sent_num == word_meta.sent_num:
                        sentence_captured = True

                # Only add sentence number if we do not already have it for that word
                if sentence_captured is not True:
                    final_matrix[word].append(word_meta)

            else:
                final_matrix[word] = [word_meta]

        unsorted_words.extend(words)
        print("unsorted len :: ", len(unsorted_words))
        print("sorted matrix :: ", len(final_matrix), "wordsssssss:: ", final_matrix)

    return final_matrix, list_of_sentences
