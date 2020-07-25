from re import findall

from pandas import Series
from omics import get_ome_regexp, get_omics_regexp

ome_re = get_ome_regexp()
omics_re = get_omics_regexp()


def test_ome_re():
    assert findall(ome_re, 'genome') == ['genome']
    assert findall(ome_re, '(genome') == ['genome']
    assert findall(ome_re, 'genome proteome') == ['genome', 'proteome']
    assert findall(ome_re, 'whole-exome') == ['whole-exome']
    assert findall(ome_re, 'we highlight genome-proteome interactions') == ['genome', 'proteome']
    assert findall(ome_re, 'microbiome, proteome, metabolome.') == ['microbiome', 'proteome', 'metabolome']
    assert findall(ome_re, 'www.mycancergenome.org') == []
    assert findall(ome_re, 'cancergenome.nih.gov') == []
    assert findall(ome_re, 'cancergenome.nih/gov') == []

def test_omics_re():

    assert findall(omics_re, 'omic') == []
    assert findall(omics_re, 'genomics') == ['genomic']
    assert findall(omics_re, ' genomics') == ['genomic']
    assert findall(omics_re, 'genomics ') == ['genomic']
    assert findall(omics_re, ' genomics ') == ['genomic']

    assert findall(omics_re, 'prote-omic') == ['prote-omic']
    assert findall(omics_re, 'prote-omics') == ['prote-omic']

    # we do not want to count post-genomics as a reference to genomics
    # as such a reference is likely to occur in some proteomic papers
    assert findall(omics_re, 'post-genomics') == ['post-genomic']

    assert findall(omics_re, 'transcriptomic proteomic') == ['transcriptomic', 'proteomic']
    assert findall(omics_re, 'transcriptomic-proteomic') == ['transcriptomic', 'proteomic']

    assert findall(omics_re, 'transcriptomic proteomic') == ['transcriptomic', 'proteomic']
    assert list(Series(['transcriptomic proteomic']).str.extractall(omics_re)[0]) == ['transcriptomic', 'proteomic']