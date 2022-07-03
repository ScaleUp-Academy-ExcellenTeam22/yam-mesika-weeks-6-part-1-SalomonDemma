def words_length(sentence: str) -> list:
    """
    A function that receives a sentence and returns the lengths of its words,
    in order of the sentence.
    Notice that punctuations are parts of the words length.
    :param sentence: A string sentence.
    :return: A list of the word's length.
    """
    return [len(word) for word in sentence.split()]


if __name__ == '__main__':
    an_example_sentence = 'Toto, I\'ve a feeling we\'re not in Kansas anymore'
    print(words_length(an_example_sentence))
