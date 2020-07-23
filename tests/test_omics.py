from re import findall

from pandas import Series
from omics import get_ome_regexp, get_omics_regexp

ome_re = get_ome_regexp()
omics_re = get_omics_regexp()


def test_ome_re():
    assert findall(ome_re, 'genome') == ['genome']
    assert findall(ome_re, '(genome') == ['genome']
    assert findall(ome_re, 'genome proteome') == ['genome', 'proteome']
    assert findall(ome_re, 'whole-exome') == ['whole-exome', 'exome']


def test_omics_re():

    assert findall(omics_re, 'omic') == []
    assert findall(omics_re, 'genomics') == ['genomic']
    assert findall(omics_re, ' genomics') == ['genomic']
    assert findall(omics_re, 'genomics ') == ['genomic']
    assert findall(omics_re, ' genomics ') == ['genomic']

    assert findall(omics_re, 'prote-omic') == ['prote-omic']
    assert findall(omics_re, 'prote-omics') == ['prote-omic']

    assert findall(omics_re, 'radio-genomics') == ['radio-genomic', 'genomic']

    assert findall(omics_re, 'transcriptomic proteomic') == ['transcriptomic', 'proteomic']
    assert findall(omics_re, 'transcriptomic-proteomic') == ['transcriptomic', 'proteomic']

    assert findall(omics_re, 'transcriptomic proteomic') == ['transcriptomic', 'proteomic']
    assert list(Series(['transcriptomic proteomic']).str.extractall(omics_re)[0]) == ['transcriptomic', 'proteomic']