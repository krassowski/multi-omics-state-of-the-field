from pandas import Series


def value_counts(values: Series):
    """Value_counts with predictable sort of values that have equal count.

    Useful at reducing diffs between consecutive runs of notebooks where value_counts is used.
    """
    name = values.name or 0

    return (
        values.value_counts()
        .reset_index()
        .sort_values([name, 'index'], ascending=[False, True])
        .set_index('index')
        [name]
    )
