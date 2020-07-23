from re import escape
from typing import Dict

from pandas import DataFrame, Series


separators = {'/', '"', "'", '(', ')'}
separators_re = '|'.join([escape(s) for s in separators])


def get_ome_regexp() -> str:
    return (
        # use look-ahead to allow for overlaps
        '(?='
            rf'(?:^|\s|{separators_re}|ome-)'
            '('
                r'(?:\w+)ome'
                '|'
                r'(?:(?:\w+-\w*)|\w+)ome'
            ')'
            # also, match plural form
            '(?:s)?'
            rf'(?:\s|$|{separators_re}|-)'
        ')'
    )


def get_omics_regexp() -> str:
    return (
        # use look-ahead to allow for overlaps
        '(?='
            rf'(?:^|\s|{separators_re}|omic-)'
            # match '*-omic', '*-*omic', '*omic'
            '('
                # handle both *omic-*omic and *-*omic
                r'(?:\w+)omic'
                '|'
                r'(?:(?:\w+-\w*)|\w+)omic'
            ')'
            # match both *omic and omics, but capture only "omic" part
            '(?:s)?'
            rf'(?:\s|$|{separators_re}|-)'
        ')'
    )


def add_entities_to_features(
    entity_omic_mapping: Dict,
    entity_type: str,
    features: DataFrame,
    omics_terms: Dict
):
    frame = []
    for entity, omics in entity_omic_mapping.items():
        terms = sorted({
            term
            for omic in omics
            for term in omics_terms[omic]
        })
        frame.append({entity_type: entity, 'terms': terms})
        features[entity_type + '_' + entity] = (
            features['mentions_' + Series(terms)]
            .any(axis=1)
        )
    return DataFrame(frame)
