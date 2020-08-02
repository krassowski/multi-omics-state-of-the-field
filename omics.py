from re import escape
from typing import Dict

from pandas import DataFrame, Series


separators = {'/', '"', "'", '(', ')', ',', ';', ':'}
final_dot_not_url_part = '\.(?:$|\s)'
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
            rf'(?:\s|$|{separators_re}|{final_dot_not_url_part}|-)'
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
            rf'(?:\s|$|{separators_re}|{final_dot_not_url_part}|-)'
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


omics_by_entity = {
    'genes': {
        'genomics',
        'whole-genomics',
        'exomics',
        'whole-exomics',
        # associations
        'immunogenomics'
    },
    'transcripts': {
        'transcriptomics',
        'whole-transcriptomics',
        'mirnomics',
        'translatomics',  # the "final day" in life of a transcript
    },
    'proteins & peptides': {
        'proteomics',
        # proteogenomics is basicaly protein/peptite identification
        # using genomic data, see https://doi.org/10.1038/nmeth.3144
        'proteogenomics',
        'peptidomics',
        # secretomics - study of all secreted proteins
        'secretomics',
        # degradomics is the study of proteases, substrates & inhibitors
        # using genomic & proteomic data, see https://doi.org/10.1038/nrm858
        'degradomics',
    },
    # both microbes, viruses AND animals!
    'clades (meta-* & pan-*)': {
        # for the sake of methods comparisons, the meta-*omic data are so different
        # (being a mix of thousands of organisms) that it warrants considering
        # those meta-Xomic as separate from Xomics (e.g. metagenomics as separate
        # from genomics)
        'metagenomics',
        'metatranscriptomics',
        'metaproteomics',
        'meta-omics',
        'microbiomics',  # used as a synonym for metagenomics, but there are other uses too
        'mycobiomics',
        'viromics',   # = viral metagenomics (but sometimes also viral genomics...)
        'pan-genomics',  # genes of all strains in a species/clade;
                         # used for microbiome but also for plants and human https://doi.org/10.1038/s41576-020-0210-7
    },
    'epigenetic modifications': {
        'epigenomics',
        'methylomics'
    },
    'protein modifications': {
        'glycoproteomics',
        'phosphoproteomics',
        'kinomics'
    },
    # drugs, toxins, diet & interactions
    'exogenous factors': {
        # metabolomic
        'exposomics',
        'pharmacometabolomics',
        # genomic
        'pharmacogenomics',
        'nutrigenomics',
        'toxicogenomics',
        'foodomics'
    },
    'endogenous molecules': {
        'metabonomics',
        'lipidomics',
        'metabolomics',
        'glycomics',
        'fluxomics',
        'ionomics'
    },
    'clinical data': {
        'radiogenomics',
        'radiomics',
        'phenomics'
    }
}


omics_by_entity_group = {
    'proteins, peptides & modifications': {
        *omics_by_entity['proteins & peptides'],
        *omics_by_entity['protein modifications']
    },
    'metabolites & other molecules': {
        *omics_by_entity['endogenous molecules'],
        'exposomics',
        'pharmacometabolomics',
    },
    'genes, epigenetics & genetic associations': {
        *omics_by_entity['genes'],
        *omics_by_entity['epigenetic modifications'],
        'pharmacogenomics',
        'nutrigenomics',
        'radiogenomics',
        'toxicogenomics'
    },
    'clades (meta-* & pan-*)': omics_by_entity['clades (meta-* & pan-*)'],
    'transcripts': omics_by_entity['transcripts'],
    #'clinical data': ,
    'other': {
        *omics_by_entity['clinical data'],
        'foodomics',
        'interactomics',
        'immunomics'
    },
}
