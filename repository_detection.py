slash_or_end = r'(?:/\b|/$|\s|\.$|\)|$)'

source_code_platforms = {
    # code repository platforms
    'github': r'(github\.com/\S+/\S+)',
    'gitlab': r'(gitlab\.com/\S+/\S+)',
    'sourceforge': r'(sourceforge\.net/\S+)',
    'bitbucket': r'(bitbucket\.org/\S+)',
    '.git': r'(\S+:\S+\.git\S*)',
    'cran': rf'cran\.r-project\.org/(?:web/packages/|package=)(\S+){slash_or_end}',
    'pypi': rf'pypi\.python\.org/pypi/(\S+){slash_or_end}',
}

mixed_publication_platforms = {
    # publication platforms
    'zenodo': rf'doi\.org/10.5281/(zenodo\.\d+?){slash_or_end}',
    'bioconductor':  rf'bioconductor.org/packages/(\S+){slash_or_end}',
    'osf': r'osf.io/(\S+){slash_or_end}',
}

data_only_platforms = {
    # unlikely that anyone stores code there, but just to be certain
    'dryad': rf'datadryad.org/(\S+){slash_or_end}'
}


all_platforms = {
    **source_code_platforms,
    **mixed_publication_platforms,
    **data_only_platforms
}