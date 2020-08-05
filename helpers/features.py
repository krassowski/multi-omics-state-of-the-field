from typing import Iterable

from pandas import DataFrame, Series


def eval_features_frame(data: DataFrame, prefix='mentioned_'):
    """Parses stringified lists and sets of features in columns of `data`."""
    return (
        data
        [data.columns[data.columns.str.startswith(prefix)]]
        .applymap(eval)
    )


def number_of_articles_mentioning_feature(
    data_py: DataFrame, features: Iterable[str],
    exclude: Iterable[str] = None
):
    """Counts number of articles mentioning features of kind given by `features`.

    Args:
        data_py: features data frame evaluated by `eval_features_frame`
        features: names of feature types (column infixes) to count
        exclude: feature to exclude
    """
    if not exclude:
        exclude = []

    result = (
        Series(
            data_py[list('mentioned_' + Series(features) + '_set')]
            .stack()
            .apply(list)
            .sum()
        )
        .value_counts()
        .drop(exclude)
        .to_frame('count')
        .rename_axis(index='term')
        .reset_index()
        .rename_axis(index='rank')
        .assign(kind=','.join(features))
    )
    result['proportion_of_features'] = result['count'] / sum(result['count'])
    result['proportion_of_articles'] = result['count'] / len(data_py)
    return result
