from re import escape

from pandas import DataFrame


def matches_n_consecutive_words(text: str, database: set, consecutive_n: int):
    """Check whether a phrase (one or more words separated by whitespace characters)

    from given database (set of phrases) is present in the provided text quickly.
    Return the first matched phrase.
    """
    words = text.split()
    for span_size in range(1, consecutive_n + 1):
        for start_position in range(0, len(words)):
            if start_position + span_size <= len(words):
                substring = ' '.join(words[start_position:start_position + span_size])
                if substring in database:
                    return substring
    return None


def highlight_first(text: str, keyword: str, margin: int = 50):
    pos = text.index(keyword)
    return text[max(0, pos - margin):min(pos + margin, len(text))]


def check_usage(term, data: DataFrame, column: str):
    # \b = a word break
    return data[data[column].str.contains(fr'\b{escape(term)}\b')][column].apply(highlight_first, keyword=term)
