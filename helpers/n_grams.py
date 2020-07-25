from pandas import Series
from sklearn.feature_extraction.text import CountVectorizer


def find_longest_common_n_grams(data, min_words, max_words, min_count, min_frequency):

    if not len(data):
        return []

    vectorizer = CountVectorizer(ngram_range=(min_words, max_words), analyzer='word')
    counts = Series(
        vectorizer.fit_transform(data).sum(0).tolist()[0],
        index=vectorizer.get_feature_names(),
        name='counts'
    )
    frequent = counts[(counts >= 3) & (counts > min_frequency * len(data))]
    hits = Series(frequent.index)

    return [
        hit
        for hit in hits
        if not ((hits.str.startswith(hit) | hits.str.endswith(hit)) & (hits != hit)).any()
    ]
