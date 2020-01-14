import nltk
import os


from nltk import tokenize
from utils import split_sent_into_words
from utils.classes import WordMetadata, WordReaderGui


final_matrix = {}

file_paths = {
    1: "/Users/sofosu-ottopah/PycharmProjects/HashTags/testdocs/doc1.txt",
    2: "/Users/sofosu-ottopah/PycharmProjects/HashTags/testdocs/doc2.txt",
    3: "/Users/sofosu-ottopah/PycharmProjects/HashTags/testdocs/doc3.txt",
    4: "/Users/sofosu-ottopah/PycharmProjects/HashTags/testdocs/doc4.txt",
    5: "/Users/sofosu-ottopah/PycharmProjects/HashTags/testdocs/doc5.txt",
    6: "/Users/sofosu-ottopah/PycharmProjects/HashTags/testdocs/doc6.txt",
}

print("hello")

# Get the GUI
gui = WordReaderGui()
gui.mainloop()

unsorted_words = []

test = open(file_paths[1], 'r')

test_sen = test.read()

# nltk.download('punkt')

list_of_sen = tokenize.sent_tokenize(test_sen)


print(list_of_sen)

print(len(list_of_sen))

print(os.path.basename(file_paths[1]))

for sen_index, sen in enumerate(list_of_sen):
    words = split_sent_into_words(sentence=sen)

    for w_index, w in enumerate(words):
        # Add 1 to index to offset
        w_meta = WordMetadata(w, sen_index, w_index)

        if w in final_matrix:
            final_matrix[w].append(w_meta)

        else:
            final_matrix[w] = [w_meta]

    unsorted_words.extend(words)

print("unsorted :: ", len(unsorted_words))

print(len(final_matrix))
print(final_matrix)
print(final_matrix["let"][0].sent_num, "hello:: ", final_matrix["let"][0].sent_pos)
