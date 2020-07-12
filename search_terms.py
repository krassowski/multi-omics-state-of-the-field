search_in = '[Text Words]'  # needed as otherwise we were getting articles with {'Affiliation': 'Panomics, Inc., 2003 East Bayshore Road, Redwood City, CA 94063, USA}


def gernerate_term_variations(prefix: str, suffix: str):
    return ' OR '.join([
        '("' + prefix + separator + suffix + ('s' if plural else '') + f'"{search_in})'
        for plural in [False, True]
        for separator in ['-', '', ' ']
    ])


def generate_compound_terms(prefix: str, suffix: str, context: str):
    return ' OR '.join([
        '(("' + prefix + separator + suffix + ('s' if plural else '') + f'"{search_in}) AND (' + context + ('s' if plural_context else '') + f'{search_in}))'
        for plural in [False, True]
        for separator in ['-', '', ' ']
        for plural_context in [False, True]
    ])


primary_terms = {
    f'{term}-omics': gernerate_term_variations(term, 'omic')
    for term in ['multi', 'pan', 'trans', 'poly', 'cross']
}


secondary_terms = {
    f'multi-{term} omics': generate_compound_terms('multi', term, 'omic')
    for term in ['table', 'source', 'view', 'modal', 'block']
}


def pluralize(simple_term: str):
    return ' OR '.join([
        f'"{simple_term}{plural_suffix}"{search_in}'
        for plural_suffix in ['', 's']
    ])


descriptive_terms = {
    'integrative omics': pluralize('integrative omic'),
    'integrated omics': pluralize('integrated omic')
}