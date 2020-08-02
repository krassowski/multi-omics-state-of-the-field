from pandas import Series
from pytest import raises
from helpers.text_processing import matches_n_consecutive_words, prefix_remover


def test_matches_n_consecutive_words():
    # at the beginning
    assert matches_n_consecutive_words(
        'lorem ipsum dolor',
        {'lorem ipsum', 'sit amet'},
        2
    ) == ['lorem ipsum']

    # in the middle
    assert matches_n_consecutive_words(
        'X lorem ipsum X',
        {'lorem ipsum', 'sit amet'},
        2
    ) == ['lorem ipsum']

    # at the end
    assert matches_n_consecutive_words(
        'X lorem ipsum',
        {'lorem ipsum', 'sit amet'},
        2
    ) == ['lorem ipsum']

    # not present
    assert matches_n_consecutive_words(
        'XloremX XipsumX dolor',
        {'lorem ipsum', 'sit amet'},
        2
    ) == []


def test_prefix_remover():
    remove_test_prefix = prefix_remover('test_')
    result = Series(['test_1', 'test_2']).apply(remove_test_prefix)
    assert list(result) == ['1', '2']

    with raises(ValueError, match="Prefix 'test_' missing in 'te_3'"):
        Series(['test_1', 'test_2', 'te_3']).apply(remove_test_prefix)
