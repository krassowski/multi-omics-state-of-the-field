from re import findall


def get_between_headers(md_list, start, end):
    return md_list[md_list.index(start):md_list.index(end)]


def match_dois(lines):
    return findall(r'doi.org/(.*?)\)\W', '\n'.join(lines))


def match_pubmed(lines):
    return findall(r'pubmed/(\d+)', '\n'.join(lines))


def match_pubmed_central(lines):
    return findall(r'pmc/articles/(PMC\d+)/', '\n'.join(lines))


def extract_references(text):
    return {
        'doi': match_dois(text),
        'pubmed': match_pubmed(text),
        'pubmed_central': match_pubmed_central(text)
    }
