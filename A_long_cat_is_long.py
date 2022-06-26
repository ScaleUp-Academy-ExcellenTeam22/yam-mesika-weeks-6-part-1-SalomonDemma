def count_words(text: str) -> dict:
    """
    A function that receives text, and returns a dictionary of its word lengths.
    :param text: A text.
    :return: A dictionary of the word lengths in the text.
    """
    # cleaning the text from non alfa letters
    words = ''.join(filter(lambda word: str(word).isalpha() or str(word).isspace(), text))

    return {word: len(word) for word in words.split()}


if __name__ == "__main__":
    pass
