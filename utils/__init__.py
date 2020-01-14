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
