from helpers.text_processing import matches_n_consecutive_words


def test_matches_n_consecutive_words():
    # at the beginning
    assert matches_n_consecutive_words(
        'lorem ipsum dolor',
        {'lorem ipsum', 'sit amet'},
        2
    ) == 'lorem ipsum'

    # in the middle
    assert matches_n_consecutive_words(
        'X lorem ipsum X',
        {'lorem ipsum', 'sit amet'},
        2
    ) == 'lorem ipsum'

    # at the end
    assert matches_n_consecutive_words(
        'X lorem ipsum',
        {'lorem ipsum', 'sit amet'},
        2
    ) == 'lorem ipsum'

    # not present
    assert matches_n_consecutive_words(
        'XloremX XipsumX dolor',
        {'lorem ipsum', 'sit amet'},
        2
    ) is None
